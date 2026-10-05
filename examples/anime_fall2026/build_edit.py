from pathlib import Path
import json,subprocess,wave,math,shutil,urllib.request
R=Path(__file__).resolve().parent
fps=30
with wave.open(str(R/'media/narration.wav')) as w: duration=w.getnframes()/w.getframerate()
end=math.ceil((duration+1)*fps)/fps
chapters=[
 (43.8,78.3,10,'My Happy Marriage','SPECIAL EPISODES','dXeAqvXkSUM',[2,10,17,23,26,12,19,28]),
 (78.3,119.0,9,'Chitose Is in the\nRamune Bottle','PART 2','8RHh2AyKRfY',[44,18,63,72,28,49,57,98,67]),
 (119.0,157.0,8,'Ranma 1/2','SEASON 3','CeUZpSuOuS4',[72,24,39,47,54,58,65,75]),
 (157.0,190.5,7,'Super Timid\nNoble Girl','NEW SERIES','7fXK-8PHGL0',[31,5,23,42,73,82,51,105]),
 (190.5,226.5,6,'From Far Away','NEW SERIES','dLRKywRu3iM',[60,73,15,24,30,44,51,66]),
 (226.5,266.5,5,'The Salty Koharu','NEW SERIES','8XgKVzuLmJw',[24,13,2,35,65,76,87,43,18]),
 (266.5,299.5,4,'Hello, I am a Witch','NEW SERIES','nvWCcqdBycQ',[31,37,7,12,18,26,54,34]),
 (299.5,331.7,3,'The Ramparts of Ice','SEASON 2','sWvfeHOkAOU',[14,44,51,29,36,58,4,21]),
 (331.7,370.4,2,'Firefly Wedding','NEW SERIES / DARK ROMANCE','kLfQNqd_NA0',[20,3,15,25,31,39,7,18,28]),
 (370.4,409.2,1,'Blue Box','SEASON 2','n0ugKku1fzc',[55,46,68,33,23,89,10,61,94]),
]
shots=[]
def shot(t,d,mid,src,zoom=1):
 t=round(t*fps)/fps; d=round(d*fps)/fps
 shots.append(dict(start=t,duration=d,mediaId=mid,source=src,zoom=zoom))
intro=[('nvWCcqdBycQ',32,4),('nvWCcqdBycQ',38,3),('nvWCcqdBycQ',13,2.2),('kLfQNqd_NA0',21,3),('kLfQNqd_NA0',32,2.4),('8XgKVzuLmJw',25,3.4),('n0ugKku1fzc',59,3),('CeUZpSuOuS4',74,3),('dLRKywRu3iM',25,3),('8RHh2AyKRfY',64,4),('sWvfeHOkAOU',51,4),('dXeAqvXkSUM',24,4),('8XgKVzuLmJw',65,4.8)]
t=0
for mid,src,d in intro: shot(t,d,mid,src);t+=d
for a,b,rank,title,kind,mid,srcs in chapters:
 t=a; i=0
 while t<b-0.02:
  d=min([4.2,4.8,4.0,5.0][i%4],b-t)
  shot(t,d,mid,srcs[i%len(srcs)],1.025 if i%3==1 else 1);t+=d;i+=1
outro=[('8XgKVzuLmJw',24,3.4),('nvWCcqdBycQ',54,3),('CeUZpSuOuS4',73,3),('kLfQNqd_NA0',31,3),('n0ugKku1fzc',59,4.7),('8RHh2AyKRfY',64,5),('8XgKVzuLmJw',87,5),('n0ugKku1fzc',89,5),('dXeAqvXkSUM',24,4)]
t=409.2
for mid,src,d in outro:
 d=min(d,end-t)
 if d>0:shot(t,d,mid,src);t+=d
if t<end:shot(t,end-t,'8XgKVzuLmJw',26)
# Short, editorial English titles, deliberately not continuous subtitles.
cues=[]
def cue(a,b,text,size=76,x=960,y=825,color='gold'):
 cues.append(dict(start=a,end=b,text=text,size=size,x=x,y=y,color=color))
cue(.4,5.0,'LOVE POTION?',96)
cue(5.3,8.8,'FOR SOMEONE ELSE?!',92)
cue(9.3,14.1,'MARRY AN ASSASSIN?',92)
cue(18.8,24.2,'10 ROMANCE PICKS',104,960,230)
cue(27.4,35.8,'FALL 2026\nEARLY-SEASON WATCHLIST',72,960,750)
for a,b,rank,title,kind,mid,srcs in chapters:
 cue(a+.15,a+4.0,f'#{rank:02d}  {title.upper()}',76,960,760)
 cue(a+.3,a+4.0,kind,36,960,940,'white')
 cue(a+4.0,b-.2,f'#{rank:02d}  '+title.replace('\n',' '),34,420,80,'white')
for a,b,txt in [(48,53,'SPECIALS • NOT SEASON 3'),(103.2,110,'MIXED EARLY REACTIONS'),(138,143.5,'COMMUNICATION + PLUMBING'),(162.8,167.2,'THAT TITLE NEEDS A BREATH'),(199.6,205,'A DANGEROUS PROPHECY'),(253.2,258.8,'EVERYONE: SEEN\nYOU: REPLY'),(274.5,279,'CRUSH OR PHARMACY?'),(325.8,329,'EMOTIONAL FREEZER'),(334,339,'DARK ROMANCE'),(362.8,367,'FICTIONAL RED FLAGS'),(378.8,385,'BADMINTON × BASKETBALL'),(391,394.4,'TEXTING IS ALREADY HARD')]:cue(a,b,txt,70)
cue(426.3,431.5,'WHO IS YOUR #1?',96,960,750)
cue(437,444.6,'REKVON\nMORE ANIME WATCHLISTS',90,960,730)
def stamp(t):
 h=int(t//3600);m=int(t%3600//60);s=t%60
 return f'{h}:{m:02d}:{s:05.2f}'
ass='''[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
ScaledBorderAndShadow: yes
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,76,&H005ED8FF,&H005ED8FF,&H00141012,&H90000000,-1,0,0,0,100,100,0,0,1,4,3,5,90,90,90,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
for c in cues:
 color='&H00FFFFFF&' if c['color']=='white' else '&H005ED8FF&'
 txt=c['text'].replace('\n','\\N')
 ass+=f"Dialogue: 0,{stamp(c['start'])},{stamp(c['end'])},Default,,0,0,0,,{{\\pos({c['x']},{c['y']})\\fs{c['size']}\\c{color}\\fad(140,120)}}{txt}\n"
(R/'highlights.ass').write_text(ass,encoding='utf-8')
(R/'edit_plan.json').write_text(json.dumps(dict(duration=end,shots=shots,cues=cues,chapters=chapters),indent=2),encoding='utf-8')
media=[]
for p in (R/'media').glob('*.info.json'):
 j=json.loads(p.read_text(encoding='utf-8'))
 media.append(dict(id=j['id'],name=j['title'],kind='video',src='/media/'+j['id']+'.mp4',duration=j['duration'],width=j['width'],height=j['height']))
media.append(dict(id='narration',name='Rekvon Hinglish narration',kind='audio',src='/media/narration.wav',duration=duration))
clips=[]
for i,s in enumerate(shots):
 clips.append(dict(id=f'v_{i:03}',mediaId=s['mediaId'],kind='video',track='V1',start=s['start'],duration=s['duration'],**{'in':s['source']},name=f'Shot {i+1}',props=dict(volume=0,fit='cover',cropB=12,scale=s['zoom'],contrast=102.5,saturation=102.5)))
clips.append(dict(id='voice',mediaId='narration',kind='audio',track='A1',start=0,duration=duration,**{'in':0},name='Continuous Hinglish narration',props=dict(volume=1,pan=0)))
for i,c in enumerate(cues):
 clips.append(dict(id=f't_{i:03}',mediaId=None,kind='text',track='V2',start=c['start'],duration=c['end']-c['start'],**{'in':0},name=c['text'].replace('\n',' / '),props=dict(text=c['text'],font='Arial',fontSize=c['size'],bold=True,color='#ffffff' if c['color']=='white' else '#ffd85e',x=c['x']-960,y=c['y']-540,boxW=1700 if c['size']>36 else 770,boxH=260,boxFit=True,strokeWidth=4,strokeColor='#121014',textShadow='3px 3px 3px #000000'),transitionIn=dict(type='fade',duration=.14),transitionOut=dict(type='fade',duration=.12)))
old=json.load(urllib.request.urlopen('http://localhost:7777/api/project'))
(R/'project_before_anime.json').write_text(json.dumps(old,indent=2),encoding='utf-8')
project=dict(name='Rekvon — Top 10 Fall 2026 Romance Anime — Review Cut',width=1920,height=1080,fps=fps,revision=old.get('revision',0)+1,panSchema=1,background='#121014',tracks=[dict(id='V2',kind='video'),dict(id='V1',kind='video'),dict(id='A1',kind='audio')],media=media,clips=clips,markers=[dict(t=a,label=f'#{rank} '+title.replace('\n',' ')) for a,b,rank,title,*_ in chapters],encodeProfile='hq')
(R/'project_review_v1.json').write_text(json.dumps(project,indent=2),encoding='utf-8')
req=urllib.request.Request('http://localhost:7777/api/project',data=json.dumps(project).encode(),headers={'Content-Type':'application/json'},method='PUT')
print(urllib.request.urlopen(req).read().decode())
print('Shots',len(shots),'titles',len(cues),'duration',end)
