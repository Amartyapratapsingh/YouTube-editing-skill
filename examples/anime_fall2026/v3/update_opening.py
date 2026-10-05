from pathlib import Path
import urllib.request,json
r=Path(__file__).resolve().parent
p=json.loads((r/'plan.json').read_text(encoding='utf-8'))
live=json.load(urllib.request.urlopen('http://localhost:7777/api/project'))
(r/'project_before_v3.json').write_text(json.dumps(live,ensure_ascii=False,indent=2),encoding='utf-8')
live['clips']=[c for c in live['clips'] if not(c['track']=='V1' and c['start']<48.1)]
for i,s in enumerate(p['shots']):
 if s['start']>=48.1:break
 live['clips'].append(dict(id=f'v3_intro_{i}',mediaId=s['mediaId'],kind='video',track='V1',start=s['start'],duration=s['duration'],**{'in':s['source']},name='Opening trailer montage',props=dict(volume=0,fit='cover',cropB=12,contrast=102.5,saturation=102.5)))
for c in live['clips']:
 if c['id']=='v2_frame':c.update(start=0,duration=p['outro_start'])
live['name']='Rekvon — Romance Anime V3 — Trailer Opening'
live['revision']=live.get('revision',0)+1
body=json.dumps(live,ensure_ascii=False,indent=2)
(r.parent/'project_v3.json').write_text(body,encoding='utf-8')
print(urllib.request.urlopen(urllib.request.Request('http://localhost:7777/api/project',data=body.encode(),headers={'Content-Type':'application/json'},method='PUT')).read().decode())
