# INV-006 sound: VO + in-house music bed + sparing kit SFX, -16 LUFS. usage: python3 mix6.py <parts_dir> <sfx_dir> <out.wav>
import sys, json, glob, os, numpy as np, soundfile as sf, pyloudnorm as pyln, subprocess
PD, SFXD, OUT = sys.argv[1:4]; SR=48000
ORDER=os.environ.get("ORDER","CO,P1,BR,P2,P3,P4,P5,RC").split(",")
def load(p):
    x,sr=sf.read(p,dtype='float32',always_2d=True); x=x.mean(1)
    if sr!=SR:
        n=int(len(x)*SR/sr); x=np.interp(np.linspace(0,len(x)-1,n),np.arange(len(x)),x).astype(np.float32)
    return x
def vdur(part):
    fs=sorted(glob.glob(f"{PD}/{part}-[0-9][0-9].mp4")); t=0.0
    for f in fs: t+=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout)
    return t
offs={}; t=0.0; shots=[]
for p in ORDER:
    offs[p]=t; js=json.load(open(f"{PD}/{p}-shots.json"))
    for s in js["shots"]: shots.append(dict(s, T=t+s["t"], part=p))
    t+=js["dur"]
TOTAL=t; N=int(TOTAL*SR)+SR
vo=np.zeros(N,np.float32)
for p in ORDER:
    x=load(f"{PD}/{p}.wav"); a=int(offs[p]*SR); vo[a:a+len(x)]+=x[:N-a]
# ---------- music bed (in-house synth) ----------
rng=np.random.default_rng(6)
def note(f): return 440.0*2**((f-69)/12)
def lp(x, a):  # one-pole low-pass
    y=np.empty_like(x); acc=0.0
    for i in range(0,len(x),4096):
        seg_=x[i:i+4096]; out=np.empty_like(seg_)
        for j,v in enumerate(seg_): acc+=a*(v-acc); out[j]=acc
        y[i:i+4096]=out
    return y
CH=[[50,53,57],[46,50,53],[41,45,48],[48,52,55]]  # Dm Bb F C (midi)
CL=8.0
tt=np.arange(N)/SR
music=np.zeros(N,np.float32)
nchord=int(TOTAL/CL)+2
env_unit=np.minimum(1,np.minimum(np.arange(int(CL*SR))/(2.5*SR),(int(CL*SR)-np.arange(int(CL*SR)))/(2.5*SR)))*0.9+0.1
for k in range(nchord):
    a=int(k*CL*SR); L=min(int(CL*SR*1.3),N-a)
    if L<=0: break
    ts=np.arange(L)/SR; env=np.minimum(1,ts/2.5)*np.exp(-np.maximum(0,ts-CL)/1.2)
    chord=CH[k%4]; sig=np.zeros(L,np.float32)
    for m in chord:
        for det in (-0.12,0.0,0.11):
            f=note(m+det/1.0); sig+=np.sin(2*np.pi*f*ts+rng.random()*6)*0.10+0.03*np.sin(4*np.pi*f*ts)
    sig+=0.22*np.sin(2*np.pi*note(chord[0]-12)*ts)  # soft bass
    music[a:a+L]+=sig*env
# felt-piano motif every 2 chords: D5 F5 E5 A4
mot=[74,77,76,69]
for k in range(0,nchord,2):
    for j,m in enumerate(mot):
        a=int((k*CL+j*1.5+0.5)*SR); L=min(int(3.5*SR),N-a)
        if L<=0: continue
        ts=np.arange(L)/SR; f=note(m)
        s=(np.sin(2*np.pi*f*ts)+0.35*np.sin(4*np.pi*f*ts)+0.12*np.sin(6*np.pi*f*ts))*np.exp(-ts*1.6)*np.minimum(1,ts/0.01)
        music[a:a+L]+=0.18*s.astype(np.float32)
# simple reverb: decaying noise IR via FFT convolution in blocks
ir_len=int(2.2*SR); ir=(rng.standard_normal(ir_len)*np.exp(-np.arange(ir_len)/(0.55*SR))).astype(np.float32); ir/=np.sqrt((ir**2).sum())
from numpy.fft import rfft, irfft
nfft=1<<int(np.ceil(np.log2(ir_len+SR*20))); IR=rfft(ir,nfft); wet=np.zeros(N+ir_len,np.float32); B=nfft-ir_len
for i in range(0,N,B):
    blk=music[i:i+B]; y=irfft(rfft(blk,nfft)*IR,nfft)[:len(blk)+ir_len]; wet[i:i+len(y)]+=y[:len(wet)-i]
music=0.55*music+0.45*wet[:N]
# musical events: stop before each PART card, swell back
gain=np.ones(N,np.float32)
for s in shots:
    if s["code"].endswith("-01") and s["code"][0]=="P" and s["kind"]=="gfx" and s["t"]<0.5:
        a=int((s["T"]-0.9)*SR); b=int((s["T"]+1.6)*SR); c=int((s["T"]+4.0)*SR)
        gain[max(0,a):b]=0.0; gain[b:c]=np.linspace(0,1,max(0,c-b))[:len(gain[b:c])]
gain=np.convolve(gain,np.ones(2400)/2400,mode="same").astype(np.float32)
music*=gain
# duck music a little under voice
envv=np.sqrt(np.convolve(vo**2,np.ones(SR//5)/(SR//5),mode="same")); duck=1-0.35*np.clip(envv/0.05,0,1)
music*=duck.astype(np.float32)
meter=pyln.Meter(SR)
music=pyln.normalize.loudness(music.astype('float64'), meter.integrated_loudness(music.astype('float64')), -31.0).astype(np.float32)
# ---------- SFX: only where needed ----------
def sfx(name): return load(glob.glob(f"{SFXD}/**/{name}.wav",recursive=True)[0])
S={k:sfx(k) for k in ["reverse_cymbal_01","sub_drop_01","land_card_01","whoosh_deep_01","tick_fine_01","counter_roll_01","sub_drop_808_01"]}
fx=np.zeros(N,np.float32); last=-99
def put(name, t, g, end_at=False):
    x=S[name]*g; a=int((t-(len(x)/SR if end_at else 0))*SR)
    if a<0: x=x[-a:]; a=0
    fx[a:a+len(x)]+=x[:N-a]
for s in shots:
    T=s["T"]; code=s["code"]; vis=s["visual"].lower(); sf_=(s.get("sfx") or "").lower()
    if code.endswith("-01") and code[0]=="P" and s["kind"]=="gfx" and s["t"]<0.5:
        put("reverse_cymbal_01",T,0.10,end_at=True); put("sub_drop_01",T,0.22); last=T; continue
    if s["kind"]!="gfx" or T-last<18: continue
    if "card-number" in vis or "counter" in sf_: put("counter_roll_01",T+0.1,0.045); put("land_card_01",T+1.3,0.08); last=T
    elif ("map" in vis) and "whoosh" in sf_: put("whoosh_deep_01",T,0.06); last=T
    elif "receipt" in vis: put("tick_fine_01",T+0.8,0.05); last=T
    elif "sub hit" in sf_ or "stamp" in sf_: put("sub_drop_808_01",T+0.2,0.12); last=T
mix=vo+music+fx
L=meter.integrated_loudness(mix.astype('float64')); mix=pyln.normalize.loudness(mix.astype("float64"),L,-15.0)
mix=np.tanh(mix/0.95)*0.95*0.94
sf.write(OUT, mix[:int(TOTAL*SR)].astype(np.float32), SR)
print("mix", round(TOTAL,1), "s; LUFS", round(meter.integrated_loudness(mix[:int(TOTAL*SR)]),1), "music LUFS -31")
