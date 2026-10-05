from pathlib import Path
import json,re,difflib,wave
R=Path(__file__).resolve().parent
script=(R.parent/'script_devanagari_v2.txt').read_text(encoding='utf-8')
rows=json.loads((R/'research/narration_segments.json').read_text(encoding='utf-8'))
words=[w for s in rows for w in s['words']]
def norm(w):return re.sub(r'[\s.,!?।:;"“”…—-]','',w).replace('़','').lower()
raw=script.split();a=[norm(w) for w in raw];b=[norm(w['word']) for w in words]
match=difflib.SequenceMatcher(None,a,b,autojunk=False)
times={}
for m in match.get_matching_blocks():
 for k in range(m.size):times[m.a+k]=words[m.b+k]['start']
known=sorted(times)
for i in range(len(a)):
 if i in times:continue
 lo=max([k for k in known if k<i],default=None);hi=min([k for k in known if k>i],default=None)
 if lo is None:times[i]=0
 elif hi is None:times[i]=times[lo]+(i-lo)*.32
 else:times[i]=times[lo]+(times[hi]-times[lo])*(i-lo)/(hi-lo)
with wave.open(str(R.parent/'media/narration_v2.wav')) as f:duration=f.getnframes()/f.getframerate()
paras=[];pos=0
for text in script.strip().split('\n\n'):
 n=len(text.split());start=times[pos];end=times.get(pos+n,duration)
 paras.append(dict(start=round(start,3),end=round(end,3),text=text,word_index=pos));pos+=n
def locate(phrase):
 needle=[norm(x) for x in phrase.split()]
 for i in range(len(a)-len(needle)+1):
  if a[i:i+len(needle)]==needle:return round(times[i],3)
 raise ValueError(phrase)
anchors={s:locate(s) for s in ['दसवें नंबर पर','नौवें नंबर पर','आठवें नंबर पर','सातवें नंबर पर','छठे नंबर पर','पाँचवें नंबर पर','चौथे नंबर पर','तीसरे नंबर पर','दूसरे नंबर पर','और पहले नंबर पर','तो आपकी पसंद क्या है','ताइकी बैडमिंटन','चिनात्सु बास्केटबॉल','अब सोचो','इस बार की रोमांस','आज की लिस्ट','आप देख रहे हैं']}
(R/'alignment.json').write_text(json.dumps(dict(duration=duration,paragraphs=paras,anchors=anchors,matched_fraction=len(known)/len(a),word_times=[times[i] for i in range(len(a))]),ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(anchors,ensure_ascii=False,indent=2));print('Matched',len(known),'/',len(a))
