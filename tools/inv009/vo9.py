# INV-009 voice (same settings as INV-006): Kokoro onyx50/michael50, speed 0.92, one WAV per part, -16 LUFS, row start times -> segs6.json
import sys, os, re, json, runpy
import numpy as np, soundfile as sf, pyloudnorm as pyln
from kokoro_onnx import Kokoro
R = [r for _,_,rs in runpy.run_path(sys.argv[1])["PARTS"] for r in rs]; OUT = sys.argv[2]; PARTS = set(sys.argv[3:])
MOD = os.environ.get('KOKMODELS','/tmp/claude-0/kok/models'); SR = 24000
k = Kokoro(MOD + '/kokoro-v1.0.onnx', MOD + '/voices-v1.0.bin')
FIX = [(r'\bTSMC\b','T S M C'),(r'\bCSIS\b','see-sis'),(r'\bODNI\b','O D N I'),(r'\bAPEC\b','ay-peck'),(r'\bCIA\b','C I A'),(r'\bAI\b','A I'),(r'\bGDP\b','G D P'),(r'\bG20\b','G twenty'),(r'Kaohsiung','Gow-shyoong'),(r'Taichung','Tie-chung'),(r'Keelung','Kee-loong'),(r'Xi Jinping','Shee Jin-ping'),(r'\bXi\b','Shee'),(r'Shenzhen','Shen-jen'),(r'Aquilino','Ah-kwi-lee-no'),(r'Nvidia','En-vidia'),(r'iPhone','eye-phone'),(r'COVID','Covid'),(r'\bOAPEC\b','oh-ay-peck'),(r'\bOPEC\b','oh-peck'),(r'\bNBER\b','N B E R'),(r'\bBLS\b','B L S'),(r'Faisal','Fy-sal'),(r'\bILO\b','I L O'),(r'\bICS\b','I C S'),(r'\bITF\b','I T F'),(r'\bIBF\b','I B F'),(r'\bUNCTAD\b','unk-tad'),(r'\bADNOC\b','ad-nock'),(r'\bIRGC\b','I R G C'),(r'\bMLC\b','M L C'),(r'Mussafah','Moo-sah-fah'),(r'Dominguez','Doh-ming-gez'),(r'Araghchi','Arak-chee'),(r'Gandhar Nahim Ajij','Gun-dar Na-heem Ah-jeej'),(r'Jusufi','Joo-soo-fee'),(r'Hapag-Lloyd','Hah-pahg Loyd'),(r'Maersk','Mursk'),(r'\bEU\b','E U'),(r'\bUK\b','U K'),(r'\bUS\b','U S'),(r'\bIEA\b','I E A'),(r'\bIEEFA\b','I E E F A'),(r'\bIMO\b','I M O'),(r'\bEDF\b','E D F'),(r'\bVAT\b','V A T'),(r'\bLNG\b','L N G'),(r'Ofgem','Ofjem')]
def say(s):
    for a,b in FIX: s=re.sub(a,b,s)
    return s.strip()
def trim(x,thr=0.008):
    i=np.where(np.abs(x)>thr)[0]; return x if len(i)==0 else x[max(0,i[0]-int(.03*SR)):i[-1]+int(.12*SR)]
def fade(x,n=int(.01*SR)):
    x=x.copy(); r=np.linspace(0,1,n); x[:n]*=r; x[-n:]*=r[::-1]; return x
st = 0.5*k.get_voice_style('am_onyx') + 0.5*k.get_voice_style('am_michael')
def part_of(code): return code.split('-')[0]
order=[]; groups={}
for r in R:
    p=part_of(r[0]); 
    if p not in groups: order.append(p); groups[p]=[]
    groups[p].append(r)
segs={}
for p in order:
    if PARTS and p not in PARTS: continue
    chunks=[np.zeros(int(.25*SR),np.float32)]; starts=[]
    for r in groups[p]:
        starts.append([r[0], sum(len(c) for c in chunks)/SR])
        for s_ in [x for x in re.split(r'(?<=[.!?])\s+', r[1]) if x.strip()]:
            a,_=k.create(say(s_), voice=st, speed=0.92, lang='en-us')
            chunks += [fade(trim(np.asarray(a,np.float32))), np.zeros(int(.28*SR),np.float32)]
        chunks.append(np.zeros(int((1.6 if (r[0].endswith('-01') and r[0][0]=='P') else .8)*SR),np.float32))
    y=np.concatenate(chunks); m=pyln.Meter(SR)
    y=pyln.normalize.loudness(y, m.integrated_loudness(y.astype('float64')), -16.0)
    y=np.clip(y,-0.89,0.89).astype(np.float32)
    sf.write(os.path.join(OUT,f'INV-009-{p}.wav'), y, SR)
    segs[p]={'dur':len(y)/SR,'starts':starts}; print(p, f'{len(y)/SR:.1f}s', flush=True)
    jp=os.path.join(OUT,'segs9.json'); old=json.load(open(jp)) if os.path.exists(jp) else {'segs':{}}
    old['segs'].update(segs); old['order']=order; json.dump(old, open(jp,'w'), indent=1)
print("VO DONE")
