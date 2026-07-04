# Changelog

Notable changes to Velocity — rules, content, and the website — recorded here as they're committed. Newest entries first, grouped by date and area.

This is the public-facing summary. It doesn't need session-by-session design rationale (why a decision was made, alternatives considered) — just what changed, in plain terms a player, Narrator, or site visitor would care about.

## 2026-07-02

**Website**
- Fixed the Report Issue modal and flags being completely unresponsive across the entire site. The modal's JavaScript was being regenerated inline on every page from within the site builder's own template, which was silently corrupting escaped characters and breaking the script everywhere. It now lives in its own file instead.
- Fixed per-item Report Issue flags in bullet and numbered lists leaving a stray blank line when the flag wrapped onto its own line.
- The reader pane now resizes fluidly with the browser window, within a sensible minimum and maximum reading width, instead of sitting at a fixed size.
- Fixed hand-authored HTML tables (e.g. the Party Effective Level Calculation table) rendering as literal text instead of a table.
- Added automatic notification to Bing and other search engines whenever the site is updated, so new and changed pages get discovered faster.
- Site assets (stylesheet, scripts) now update immediately for visitors after a deploy, instead of potentially being served from a stale browser cache.

**Rules**
- Split the old single "dying" threshold into two stages: **Wounded** (half of max Vitality) and **Dying** (a quarter of max Vitality). Bleeding Out now begins at Wounded rather than Dying, creating urgency earlier.
- Renamed **Situational Awareness** to **Perception** and moved it from the Investigation skill branch to Survival, where it no longer requires another skill as a prerequisite.
- Reworded some Investigation skill descriptions to fit the setting better.
- Added a Health Thresholds by Vitality reference table.
- Updated the Starter Kit adventure to match the above.
