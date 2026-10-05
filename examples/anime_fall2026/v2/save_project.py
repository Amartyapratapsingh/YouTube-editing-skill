from pathlib import Path
import json,urllib.request,datetime
R=Path(__file__).resolve().parent;ROOT=R.parent;P=json.loads((R/'plan.json').read_text(encoding='utf-8'))
live=json.load(urllib.request.urlopen('http://localhost:7777/api/project'))
(R/('backup_'+datetime.datetime.now().strftime('%H%M%S')+'.json')).write_text(json.dumps(live,indent=2),encoding='utf-8')
media=[m for m in live['media'] if m['id'] in {s['mediaId'] for s in P['shots']}]
for mid,d in [('intro_v2',P['chapters'][0]['start']),('outro_v2',P['duration']-P['outro_start'])]:
 if not any(m['id']==mid for m in media):media.append(dict(id=mid,name=mid.replace('_',' ').title(),kind='video',src=f'/media/{mid}.mp4',duration=d,width=1920,height=1080))
media.append(dict(id='narration_v2',name='Approved Devanagari Hindi narration',kind='audio',src='/media/narration_v2.wav',duration=P['narration_duration']))
media.append(dict(id='frame',name='Cinema frame',kind='svg',src='/media/cinema_frame.svg',duration=P['duration'],width=1920,height=1080))
(ROOT/'media/rank_panel_v2.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080"><rect x="90" y="650" width="1740" height="290" fill="#121014" fill-opacity="0.79"/></svg>')
media.append(dict(id='rank_panel',name='Rank reveal panel',kind='svg',src='/media/rank_panel_v2.svg',duration=6,width=1920,height=1080))
clips=[]
for i,s in enumerate(P['shots']):
 native=s['mediaId'] in ['intro_v2','outro_v2'];props=dict(volume=0,fit='cover')
 if not native:props.update(cropB=12,contrast=102.5,saturation=102.5)
 c=dict(id=f'v2_{i:03}',mediaId=s['mediaId'],kind='video',track='V1',start=s['start'],duration=s['duration'],**{'in':s['source']},name=s['reason'][:80],props=props)
 if not native and s['zoom']>1:c['keyframes']={'scale':[{'t':0,'v':1},{'t':s['duration'],'v':s['zoom'],'ease':'linear'}]}
 clips.append(c)
clips.append(dict(id='v2_voice',mediaId='narration_v2',kind='audio',track='A1',start=0,duration=P['narration_duration'],**{'in':0},name='Continuous Hindi narration',props=dict(volume=1,pan=0)))
clips.append(dict(id='v2_frame',mediaId='frame',kind='svg',track='V2',start=P['chapters'][0]['start'],duration=P['outro_start']-P['chapters'][0]['start'],**{'in':0},name='Cinema frame',props=dict(fit='contain')))
for i,ch in enumerate(P['chapters']):clips.append(dict(id=f'panel_{i}',mediaId='rank_panel',kind='svg',track='V3',start=ch['start']+.1,duration=5.7,**{'in':0},name='Rank reveal',props=dict(fit='contain'),transitionIn=dict(type='fade',duration=.18),transitionOut=dict(type='fade',duration=.18)))
for i,c in enumerate(P['cues']):
 clips.append(dict(id=f'v2_text_{i}',mediaId=None,kind='text',track='V4',start=c['start'],duration=c['end']-c['start'],**{'in':0},name=c['text'].replace('\n',' / '),props=dict(text=c['text'],font='Arial',fontSize=c['size'],bold=True,color='#ffffff' if c['color']=='white' else '#ffda7b',x=c['x']-960,y=c['y']-540,boxW=1700 if c['x']==960 else 1400 if c['x']>500 else 230,boxH=240,boxFit=True,strokeWidth=3,strokeColor='#121014'),transitionIn=dict(type='fade',duration=.18),transitionOut=dict(type='fade',duration=.18)))
project=dict(name='Rekvon — Romance Anime V2 — Hindi Narration',width=1920,height=1080,fps=30,revision=live.get('revision',0)+1,panSchema=1,background='#121014',tracks=[dict(id=f'V{i}',kind='video') for i in [4,3,2,1]]+[dict(id='A1',kind='audio')],media=media,clips=clips,markers=[dict(t=c['start'],label=f"#{c['rank']} "+c['title'].replace('\n',' ')) for c in P['chapters']],encodeProfile='hq')
body=json.dumps(project,ensure_ascii=False,indent=2)
(ROOT/'project_v2.json').write_text(body,encoding='utf-8')
print(urllib.request.urlopen(urllib.request.Request('http://localhost:7777/api/project',data=body.encode(),headers={'Content-Type':'application/json'},method='PUT')).read().decode())
