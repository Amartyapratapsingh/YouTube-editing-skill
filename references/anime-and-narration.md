# Anime lists and Hindi narration

## Research and script

- Respect the requested season and year. For an early-season list, frame recommendations as a watchlist based on announced premises and trailers, not completed-season reviews or an audience poll.
- Reddit, Grok and public X discussions provide leads and audience reactions. Verify release, sequel and special-episode claims against primary announcements. Never pad a top ten with unverified seasonal entries.
- Write natural spoken Hindi in Devanagari for this user's generated anime narration. Familiar English words may be written phonetically where that improves delivery. Avoid literal translations and broken Hindi. Keep upload copy and display titles in English.
- Build a curiosity hook, concise introduction, distinct reasons to watch each entry, light situational humour and a closing viewer question. Mention prerequisite seasons where relevant; avoid spoilers.
- If the user requests script review first, deliver the script before voice generation. Approval followed by “start editing” authorizes the approved production; do not request approval again for routine steps.

## Rekvon audio

- Use the user's selected Rekvon service and existing sign-in through available browser tools. Hindi mode with the approved Devanagari script is the accepted route. Aditya Premium at speed 1.0 was used for this production, not a universal voice requirement.
- Measure the generated recording and build the timeline around it. A requested visual revision alone does not authorize rewriting or regenerating accepted narration.
- Review names, sentence joins and the ending. Automated ASR alignment can interpolate uncertain words; do not describe it as verified word-perfect timing or listening.

## Accepted visual treatment

- For the anime opening, combine strong moments from the selected trailers while narration plays. No invented introductory text, anime-name slides or typography-only hook. Brief name/rank reveals belong at the corresponding countdown entry.
- During each entry, use that anime's footage. Match the visible action to the spoken idea: badminton must show badminton, basketball must show basketball. Inspect real source frames; nearby timestamps can cross an internal trailer cut.
- Mix emotional reactions, interactions, wide shots and action according to the sentence. Hold meaningful moments; avoid repetitive fixed-length cuts, tiny leftover flashes and promotional end cards.
- In gaming/news edits, when the subject is absent from gameplay, show the relevant sourced image at that spoken moment. The accepted treatment is an image with restrained motion over blurred gameplay, returning to gameplay afterward. Use news transition cards when requested.
- Use restrained grading. Caption treatment depends on the current request: brief gold emphasis for selected moments, no added opening text for this anime edit, or green/red word highlighting when full captions are requested. Do not apply an older caption preference over the current brief.

## Revisions and handoff

- Preserve the accepted narration, countdown, timing and previous export when changing only the opening. Re-read the live project and patch the relevant clips instead of replacing unrelated user changes.
- Check that every entry uses its matching source, opening text is absent when requested, narration is continuous, source audio is muted, and there are no timeline gaps. Sample the rendered output around changes and decode the final file.
- Supply the versioned MP4 and its absolute file location. Describe local FFmpeg export accurately and distinguish export verification from a full listening review.
- Code under `examples/anime_fall2026` records a completed project. It contains project-specific timestamps and local dependencies; inspect and adapt it before execution. Scripts that update localhost edit the live FableCut project.
