# INV-024 voice: Kokoro bm_george 0.5 + bm_lewis 0.5 (deep British documentary blend, chosen 2026-11-18 at Hammad's request),
# speed 0.9, en-gb, one WAV per part, -16 LUFS. Writes segs24.json: row starts, sentence spans and {cue} word times (part-relative s).
# usage: python3 vo11.py <script.py> <out_dir> [PART ...]
import sys, os, re, json, runpy
import numpy as np, soundfile as sf, pyloudnorm as pyln
from kokoro_onnx import Kokoro
PARTS_ = runpy.run_path(sys.argv[1])["PARTS"]; R = [r for _,_,rs in PARTS_ for r in rs]; OUT = sys.argv[2]; WANT = set(sys.argv[3:])
MOD = os.environ.get('KOKMODELS','/tmp/claude-0/kok/models'); SR = 24000
VOICE = {"bm_george":0.5, "bm_lewis":0.5}; SPEED = 0.9; LANG = "en-gb"
k = Kokoro(MOD + '/kokoro-v1.0.onnx', MOD + '/voices-v1.0.bin')
FIX = [(r'\bIRGC\b','I R G C'),(r'\bLNG\b','L N G'),(r'\bUS\b','U S'),(r'\bUN\b','U N'),(r'\bVAT\b','V A T'),(r'S&P','S and P'),
 (r'Hormuz','Hor-mooz'),(r'Ajr','Ahj-er'),(r'Sahand','Sah-hand'),(r'Sabalan','Sah-bah-lahn'),(r'Qatar','Kuh-tar'),(r"Qatar's","Kuh-tar's"),
 (r'\burea\b','yoo-ree-uh'),(r'Vincennes','Vin-senz'),(r'Bridgeton','Bridge-ton'),(r'rials','ree-ahls'),(r'Brent','Brent'),(r'Princeton','Prince-ton'),
 (r'six-five-five','six five five'),(r'Ajr\.','Ahj-er.'),(r'Khamenei','Kha-meh-nay'),(r'Mojtaba','Moj-tah-bah'),(r'Kharg','Karg'),(r'Touska','Toos-kah'),(r'Islamabad','Is-lahm-ah-bahd'),(r'Khomeini','Kho-may-nee'),(r'Volcker','Vol-ker'),(r'OPEC','Oh-pek'),(r'WTI','W T I'),(r'S&Ls','S and Ls'),(r'Qeshm','Keshm'),(r'Laffan','Lah-fahn'),(r'Tanura','Tah-noo-rah'),(r'ADNOC','Ad-nock'),(r'Houthis','Hoo-theez'),(r'Shaybah','Shay-bah'),(r'Jubail','Joo-bail'),(r'Jebel Ali','Jeb-el Ah-lee'),(r'Ali Al Salem','Ah-lee al Sah-lem'),(r'Riyadh','Ree-yahd'),(r'IATA','eye-ah-tah'),(r'ING','I N G'),(r'Pars','Parss'),(r'Bahraini','Bah-ray-nee'),(r'Bahrain','Bah-rain')]
def say(s):
    for a,b in FIX: s=re.sub(a,b,s)
    return s.strip()
def trim(x,thr=0.008):
    i=np.where(np.abs(x)>thr)[0]; return x if len(i)==0 else x[max(0,i[0]-int(.03*SR)):i[-1]+int(.12*SR)]
def fade(x,n=int(.01*SR)):
    x=x.copy(); r=np.linspace(0,1,n); x[:n]*=r; x[-n:]*=r[::-1]; return x
st = sum(w*k.get_voice_style(v) for v,w in VOICE.items())
groups={}; order=[]
for r in R:
    p=r[0].split('-')[0]
    if p not in groups: order.append(p); groups[p]=[]
    groups[p].append(r)
jp=os.path.join(OUT,'segs24.json'); data=json.load(open(jp)) if os.path.exists(jp) else {'segs':{}}
for p in order:
    if WANT and p not in WANT: continue
    chunks=[np.zeros(int(.25*SR),np.float32)]; starts=[]; sents={}; cues={}
    pos=lambda: sum(len(c) for c in chunks)/SR
    for r in groups[p]:
        code=r[0]; starts.append([code, pos()]); sents[code]=[]; cues[code]=[]
        for s_ in [x for x in re.split(r'(?<=[.!?])\s+', r[1]) if x.strip()]:
            plain=s_.replace('{','').replace('}','')
            a,_=k.create(say(plain), voice=st, speed=SPEED, lang=LANG); a=fade(trim(np.asarray(a,np.float32)))
            t0=pos(); dur=len(a)/SR; sents[code].append([round(t0,3), round(t0+dur,3)])
            # cue word time ~ proportional to character offset in the sentence (Kokoro pace is near-uniform)
            off=0; L=max(1,len(plain))
            for m in re.finditer(r'\{([^}]*)\}', s_):
                ci=m.start()-2*sum(1 for _ in re.finditer(r'\{[^}]*\}', s_[:m.start()]))
                cues[code].append(round(t0+0.06+dur*ci/L,3))
            chunks += [a, np.zeros(int(.30*SR),np.float32)]
        chunks.append(np.zeros(int((1.6 if (code.endswith('-01') and code[0] in 'PW') else .75)*SR),np.float32))
    y=np.concatenate(chunks); m=pyln.Meter(SR)
    y=pyln.normalize.loudness(y, m.integrated_loudness(y.astype('float64')), -16.0); y=np.clip(y,-0.89,0.89).astype(np.float32)
    sf.write(os.path.join(OUT,f'INV-024-{p}.wav'), y, SR)
    data['segs'][p]={'dur':len(y)/SR,'starts':starts,'sents':sents,'cues':cues}; data['order']=order
    json.dump(data, open(jp,'w'), indent=1); print(p, f'{len(y)/SR:.1f}s', flush=True)
print("VO DONE")
