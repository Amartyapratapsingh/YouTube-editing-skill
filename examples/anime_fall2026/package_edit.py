from pathlib import Path
import json
R=Path(__file__).resolve().parent
p=json.loads((R/'edit_plan.json').read_text())
def clock(t):return f'{int(t)//60:02}:{int(t)%60:02}'
chapters=['00:00 Hook and early-season watchlist']+[clock(a)+' '+str(rank)+'. '+title.replace('\n',' ')+' — '+kind.title() for a,b,rank,title,kind,*_ in p['chapters']]+['06:49 Choose your romance mood','07:06 Your number one pick']
credits=[]
for f in sorted((R/'media').glob('*.info.json')):
 j=json.loads(f.read_text(encoding='utf-8'))
 credits.append({'title':j['title'],'channel':j['channel'],'url':'https://www.youtube.com/watch?v='+j['id'],'file':'media/'+j['id']+'.mp4','width':j['width'],'height':j['height'],'duration':j['duration']})
(R/'research/trailer_sources.json').write_text(json.dumps(credits,ensure_ascii=False,indent=2),encoding='utf-8')
refs=[
'https://about.netflix.com/en/news/romance-anime-lineup-october',
'https://www.crunchyroll.com/news/latest/2026/9/18/firefly-wedding-anime-opening-theme-song-previewed-in-new-trailer',
'https://www.crunchyroll.com/news/latest/2026/9/14/hi-im-a-witch-and-my-crush-wants-me-to-make-a-love-potion-anime-october-5-release-date-trailer-visual-theme-songs',
'https://www.crunchyroll.com/news/latest/2026/9/2/from-far-away-anime-key-visual-theme-songs-trailer-additional-cast',
'https://prtimes.jp/main/html/rd/p/000000017.000113351.html',
'https://www.reddit.com/r/romanceanime/comments/1wd2l1q/romance_anime_you_guys_are_most_exited_for/',
'https://www.reddit.com/r/Animesuggest/comments/1v5j8x8/any_good_romance_coming_out_this_fall/',
'https://www.reddit.com/r/anime/comments/1wdbyp5/tv_anime_chitose_is_in_the_ramune_bottle_2nd_cour/',
'https://www.reddit.com/r/shoujo/comments/1wxm58r/from_far_away_ep1_delivered_i_have_hope_for_this/',
]
(R/'research/research_sources.txt').write_text('Research cutoff: 5 October 2026\nEditorial early-season watchlist, not a Reddit poll, score ranking, or completed-season review.\nGrok used for leads; trailer title and channel metadata checked independently.\n\n'+'\n'.join(refs),encoding='utf-8')
text='''TITLE
Top 10 Romance Anime to Watch This Fall 2026 | Cute Crushes to Red Flags!

DESCRIPTION
This Fall's romance anime go from sweet school crushes to dangerous marriage proposals. Here are Rekvon's 10 early-season romance picks for Fall 2026, with spoiler-free premises, sequel guidance, and a little Hinglish humor.

This is an editorial watchlist based on announced stories, official trailers and early fan discussion as of October 5, 2026. It is not a final season review. The list includes new series, sequels, a returning cour and My Happy Marriage special episodes. Release dates and streaming availability can vary by region.

Which is your number one: wholesome romance or fictional red flags?

CHAPTERS
'''+ '\n'.join(chapters)+'''

OFFICIAL TRAILER CREDITS
'''+ '\n'.join(c['title']+' — '+c['channel']+'\n'+c['url'] for c in credits)+'''

HASHTAGS
#RomanceAnime #Fall2026Anime #AnimeRecommendations #Rekvon

TAGS
romance anime 2026, fall 2026 anime, top 10 romance anime, romance anime recommendations, new romance anime, anime in Hindi, Hinglish anime, Blue Box season 2, Firefly Wedding, My Happy Marriage specials, Ranma season 3, The Ramparts of Ice, From Far Away anime, The Salty Koharu, Chitose Is in the Ramune Bottle, love potion anime, Rekvon
'''
(R/'upload_details.txt').write_text(text,encoding='utf-8')
(R/'chapters.txt').write_text('\n'.join(chapters),encoding='utf-8')
def srt(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(R/'highlights_en.srt').write_text('\n\n'.join(f"{i+1}\n{srt(c['start'])} --> {srt(c['end'])}\n{c['text']}" for i,c in enumerate(sorted(p['cues'],key=lambda c:c['start']))),encoding='utf-8')
(R/'README.txt').write_text('''REKVON / FALL 2026 ROMANCE ANIME

Delivery: exports/Rekvon_Fall2026_Romance_Top10_review_v1.mp4
Editable FableCut snapshot: project_review_v1.json
Live working timeline: project.json (opened at http://localhost:7777)
Narration: media/narration.wav (Rekvon Aditya Premium, Hinglish)
Script: script_hinglish.txt
English highlights: highlights_en.srt / highlights.ass (selective titles, not a full transcript)
Publishing copy: upload_details.txt
Research and official trailer credits: research/

Keep the entire media folder beside the project. Its /media paths resolve through FableCut.
To reopen later, run the installed FableCut server with FABLECUT_DATA_DIR pointing to this folder.

The MP4 was rendered locally with FFmpeg using the same picture-cut plan and narration as the FableCut timeline. Text rendering is ASS in the MP4 and native editable text in FableCut; font metrics can differ slightly. Trailer soundtracks were not downloaded or mixed. Source trailers are 1080p. Reframing crops their lower edge and enlarges the retained image slightly to reduce baked-in trailer captions; this does not recover detail.

REVIEW STATUS
Two automated transcription passes and audio-level checks were performed. Proper names and a few title announcements were inconsistently recognized; full listening verification has not been completed. Please review pronunciation and delivery before publishing. Research is an early-season editorial watchlist, not a claim to have reviewed completed seasons.
''',encoding='utf-8')
print('Saved credits, chapters, publishing copy and reopen notes.')
