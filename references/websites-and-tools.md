# Websites and tools used for Rekvon videos

These are the user's established services. Reuse an existing signed-in tab when available. Check the current page before acting; saved URLs and interfaces can change.

| Purpose | Website / URL | How it is used |
| --- | --- | --- |
| Hindi narration | Rekvon — https://rekvon.in/app/ (home: https://rekvon.in/) | Generate audio from the approved Devanagari Hindi script. Select Hindi and the approved voice, download the finished audio, and measure it before editing. |
| Video editing | FableCut — http://localhost:7777/ | Existing local editor for arranging footage, continuous narration, title reveals, images and subtitles. This address works only while the user's local FableCut server is running; it is not a public hosted service. |
| Research assistant | Grok — https://grok.com/ | Ask focused research questions and collect leads. Check factual claims against official announcements; a Grok answer is not primary evidence. |
| Community research | Reddit — https://www.reddit.com/ | Find audience reactions, suggestions and discussions. Distinguish opinions and rumours from verified announcements. |
| Public posts and announcements | X — https://x.com/ | Review public creator, studio and publisher posts; prefer original announcements over reposts. |
| Official trailers and videos | YouTube — https://www.youtube.com/ | Locate and verify the exact trailer, title, source channel and footage. Save source URLs with the project. |
| YouTube video downloader | YTDown — https://app.ytdown.to/en38/ (observed working tab) | Submit the selected YouTube video URL and download the intended clip. The locale/version path may change; inspect the user's existing tab before navigating or submitting. |
| Publishing and upload checks | YouTube Studio — https://studio.youtube.com/ | Prepare or inspect video details, processing status and upload assets when requested. Editing alone does not authorize publishing. |
| Skill and editing source | GitHub — https://github.com/Amartyapratapsingh/YouTube-editing-skill | Maintain the reusable skill, reference instructions and editing code. Push updates when the user requests repository changes. |

## Practical handoffs

- Research in Grok, Reddit and public X posts, verify against primary sources, then write the requested script. Use the approved script for Rekvon narration, obtain verified source footage, and assemble it in FableCut.
- Rekvon's observed Studio provided audio generation; the video timeline belongs in FableCut unless the user explicitly selects another editor.
- Use an actually available FableCut MCP connection when present. Otherwise use its supported browser or documented local project/API workflow and describe that route accurately. A localhost page alone does not prove MCP is connected.
- Let the user complete sign-in when required. Never save passwords, cookies or authentication tokens in this skill or GitHub. Follow current browser confirmation requirements for terms, permission prompts and downloads; past permission for a particular download is not blanket consent to future agreements.
- Verify the selected download's title, duration, resolution and playable contents. Avoid advertising download buttons, installers and unrelated redirects. If a source cannot be obtained through the authorized route, use supplied media or request the specific missing clip.
- The original source URL and channel remain the footage credit, not the downloader. Download availability does not itself establish reuse permission.
- Local FFmpeg exports are also used where appropriate. State when the export was rendered locally rather than through FableCut's browser compositor.
