# YouTube Editing Skill

A reusable Codex skill for narration-led YouTube editing and publishing assets, based on a FableCut editing workflow.

## Included workflow

- Preserve supplied Hindi narration and create English subtitles.
- Mute source-video audio and keep narration continuous across picture cuts.
- Prepare landscape 1080p exports, with honest disclosure when footage is upscaled.
- Continue existing FableCut timelines with backups and verified media counts.
- Check synchronization, subtitle readability, media integrity and export settings.
- Write English titles, descriptions, chapter timestamps, keywords and hashtags.
- Create six distinct thumbnail concepts when a selection stage is requested, then refine the chosen design.
- Diagnose editor audio stutter and YouTube upload/processing delays.

These are user defaults, not fixed requirements for every project. Explicit instructions override them. The skill does not authorize public posting, paid purchases, or unrelated account changes.

## Install

Copy this repository's `SKILL.md`, `agents/`, and `references/` into a folder named `youtube-editing` under your Codex skills directory, normally `~/.codex/skills/`.

Then invoke:

> Use $youtube-editing to continue my video project, preserve my narration, add English subtitles, and prepare a verified 1080p export.

## Files

- `SKILL.md`: entry point, user preferences and task routing.
- `agents/openai.yaml`: skill display metadata and default prompt.
- `references/editing-and-export.md`: FableCut, rendering, audio and verification guidance.
- `references/packaging-and-thumbnails.md`: upload copy and thumbnail design workflow.
- `references/upload-troubleshooting.md`: local file checks and YouTube processing diagnosis.

## Requirements

This repository contains skill instructions and project-specific editing source examples; it does not bundle FableCut, media, model weights or editing software. The executing agent needs suitable editor/browser tools and, when local rendering is used, a trusted FFmpeg installation. Image generation is needed only for generated thumbnail artwork. The skill checks available capabilities before selecting a route.

## Anime and narration workflow

The established service URLs and their roles are documented in [Websites and tools](references/websites-and-tools.md), including Rekvon, FableCut, Grok, Reddit, X, YouTube and YTDown.

The skill now includes natural Devanagari Hindi script preparation, Rekvon narration, trailer-only hooks, source-matched countdown footage, scoped revisions, and English upload metadata. See `references/anime-and-narration.md`. The full anime editing source snapshot and timing plans are in `examples/anime_fall2026`; read its dependency notes before running any stage.
