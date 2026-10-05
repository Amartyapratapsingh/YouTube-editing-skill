from pathlib import Path
import json,re,math,urllib.request
R=Path(__file__).resolve().parent;ROOT=R.parent
A=json.loads((R/'alignment.json').read_text(encoding='utf-8'));fps=30
def q(t):return round(t*fps)/fps
paras=A['paragraphs'];duration=math.ceil((A['duration']+1)*fps)/fps
ids=['dXeAqvXkSUM','8RHh2AyKRfY','CeUZpSuOuS4','7fXK-8PHGL0','dLRKywRu3iM','8XgKVzuLmJw','nvWCcqdBycQ','sWvfeHOkAOU','kLfQNqd_NA0','n0ugKku1fzc']
titles=['My Happy Marriage','Chitose Is in the\nRamune Bottle','Ranma 1/2','Super Timid Noble Girl','From Far Away','The Salty Koharu Has\na Soft Spot for Me','Hello, I am a Witch','The Ramparts of Ice','Firefly Wedding','Blue Box']
kinds=['SPECIAL EPISODES','PART 2','SEASON 3','NEW SERIES','NEW SERIES','NEW SERIES','NEW SERIES','SEASON 2','DARK ROMANCE','SEASON 2']
# Each row follows the entry's spoken paragraphs: reveal, premise, relationship, recommendation.
# Source windows were inspected in the contact sheets. Avoid distributor end screens and graphic shots.
banks=[
 [[(24,3)],[(26,5),(17,4),(2,3)],[(20,4),(25,5),(16,4)],[(28,3),(23,4),(10,4),(17,4)]],
 [[(63,4)],[(45,5),(17,5),(63,4)],[(45,4),(64,5),(72,5)],[(98,5),(62,5),(27,5)]],
 [[(74,3)],[(73,4),(24,5),(39,4)],[(74,5),(1,3),(47,4)],[(73,4),(54,4),(64,4)]],
 [[(42,3)],[(6,5),(23,4),(73,4)],[(42,4),(31,5),(76,4)],[(74,5),(34,5),(82,5)]],
 [[(62,3)],[(24,6),(60,4)],[(61,4),(15,5),(30,4)],[(24,5),(50,4),(76,5),(65,5)]],
 [[(25,4)],[(14,5),(65,5),(25,5)],[(2,4),(38,4),(76,5)],[(25,4),(86,5),(35,4)]],
 [[(31,3)],[(7,5),(36,5),(25,4)],[(12,5),(54,5)],[(31,5),(37,4),(18,5)]],
 [[(14,4)],[(14,5),(59,5)],[(44,5),(51,5),(29,5)],[(36,5),(58,5),(4,4)]],
 [[(31,2.2)],[(4,5),(15,4),(22,4)],[(30,5),(7,4)],[(22,4),(31,4),(4,5),(16,4),(29,4)]],
 [[(58,3.2)],[(58,5),(69,5)],[(72,2),(74,3),(88,5),(33,4)],[(90,5),(22,5),(58,4),(46,3)]]
]
shots=[];chapters=[];cues=[]
def addshot(start,end,mid,source,reason,zoom=1):
 start=q(start);end=q(end)
 if end<=start:return
 shots.append(dict(start=start,duration=end-start,mediaId=mid,source=source,zoom=zoom,reason=reason))
def cue(a,b,text,size=72,x=960,y=820,color='gold'):
 cues.append(dict(start=q(a),end=q(b),text=text,size=size,x=x,y=y,color=color))
addshot(0,paras[5]['start'],'intro_v2',0,'Original animated hook and introduction')
for ci,mid in enumerate(ids):
 ps=paras[5+ci*4:9+ci*4];a=q(ps[0]['start']);b=q(ps[-1]['end'])
 chapters.append(dict(start=a,end=b,rank=10-ci,title=titles[ci],kind=kinds[ci],mediaId=mid))
 for pi,para in enumerate(ps):
  # Sentence boundaries come from alignment with the actual narration.
  bounds=[q(para['start'])];wi=para['word_index'];textwords=para['text'].split()
  for k,w in enumerate(textwords[:-1]):
   if w.endswith(('।','?','!')):
    t=q(A['word_times'][wi+k+1])
    if t-bounds[-1]>=2.4 and para['end']-t>=2.0:bounds.append(t)
  bounds.append(q(para['end']))
  bank=banks[ci][pi];bi=0
  for ta,tb in zip(bounds,bounds[1:]):
   t=ta
   while t<tb-.01:
    src,maxd=bank[bi%len(bank)];d=min(maxd,tb-t)
    if tb-t-d<1.4 and tb-t<=maxd+.6:d=tb-t
    addshot(t,t+d,mid,src,para['text'],1.018 if bi%3==2 else 1)
    t=q(t+d);bi+=1
 title=titles[ci].upper()
 cue(a+.1,min(a+5.8,b),f'{10-ci:02}',148,245,795)
 cue(a+.1,min(a+5.8,b),title,70,1100,770)
 cue(a+.2,min(a+5.8,b),kinds[ci],32,1100,888,'white')
 if ci==3:
  cue(a+5.9,a+12.5,"EVEN THOUGH I'M A SUPER TIMID NOBLE GIRL,\nI ACCEPTED THE BET FROM MY CUNNING FIANCE",48,960,800)
# Split the sports sentence at the actual spoken terms, then use the corresponding activity.
for phrase,src,endphrase in [('ताइकी बैडमिंटन',71.5,'चिनात्सु बास्केटबॉल'),('चिनात्सु बास्केटबॉल',74,None)]:
 a=q(A['anchors'][phrase]);b=q(A['anchors'][endphrase]) if endphrase else q(paras[42]['end'])
 updated=[]
 for s in shots:
  sa=s['start'];sb=sa+s['duration']
  if sb<=a or sa>=b:updated.append(s);continue
  if sa<a:updated.append(dict(s,duration=a-sa))
  if sb>b:updated.append(dict(s,start=b,duration=sb-b,source=s['source']+b-sa))
 shots=updated;addshot(a,b,ids[-1],src,'Spoken sports name matched to visible sport')
# Mood recap follows the named shows, then a dedicated closing card.
a=paras[-2]['start'];b=paras[-2]['end'];recap=[(ids[5],25),(ids[6],54),(ids[2],74),(ids[8],31)]
for i,(mid,src) in enumerate(recap):addshot(a+(b-a)*i/4,a+(b-a)*(i+1)/4,mid,src,'Mood recap')
addshot(b,duration,'outro_v2',0,'Original closing card')
shots.sort(key=lambda s:s['start'])
plan=dict(duration=duration,narration_duration=A['duration'],chapters=chapters,shots=shots,cues=cues,intro_bounds=[A['anchors'][x] for x in ['अब सोचो','इस बार की रोमांस','आज की लिस्ट','आप देख रहे हैं']],outro_start=q(b))
(R/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
def stamp(t):return f'{int(t)//3600}:{int(t)//60%60:02}:{t%60:05.2f}'
ass='''[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,72,&H007BDAFF,&H007BDAFF,&H00141012,&H90000000,-1,0,0,0,100,100,0,0,1,3,2,5,90,90,90,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
for ch in chapters:
 a=ch['start']+.1;b=a+5.7
 ass+=f'Dialogue: 0,{stamp(a)},{stamp(b)},Default,,0,0,0,,{{\\an7\\pos(90,650)\\p1\\1c&H141012&\\1a&H35&\\bord0\\shad0\\fad(180,180)}}m 0 0 l 1740 0 1740 290 0 290\n'
for c in cues:
 color='&HFFFFFF&' if c['color']=='white' else '&H7BDAFF&';txt=c['text'].replace('\n','\\N')
 ass+=f"Dialogue: 1,{stamp(c['start'])},{stamp(c['end'])},Default,,0,0,0,,{{\\pos({c['x']},{c['y']})\\fs{c['size']}\\c{color}\\fad(180,180)}}{txt}\n"
(R/'highlights.ass').write_text(ass,encoding='utf-8')
print('Prepared',len(shots),'speech-aligned shots; intro',chapters[0]['start'],'seconds')
