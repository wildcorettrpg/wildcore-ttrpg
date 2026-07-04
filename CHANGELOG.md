# Changelog

Notable changes to Velocity — rules, content, and the website — recorded here as they're committed. Newest entries first, grouped by date and area.

This is the public-facing summary. It doesn't need session-by-session design rationale (why a decision was made, alternatives considered) — just what changed, in plain terms a player, Narrator, or site visitor would care about.

## 2026-07-03

**Website**
- Fixed a bug in the site builder where trait and flaw descriptions on lineage pages were silently dropped if no blank line appeared between the `###` heading and the paragraph below it. All lineage pages now display their full descriptions.

**Rules**
- **Shapeshifter** now has a full Animal Forms section: 15 forms (Bat through Wolf), each with its own size, movement, and natural weapon damage. Natural weapon damage follows the same one-tier-above-5e-SRD scale as standard weapons. Multi-Strike can use any natural weapons the form has — player's call per activation.
- **Kith Improvised Combatant** rewritten: Kith apply all purchased Melee Attack or Ranged Attack skills to improvised weapons, removing the reference to undefined weapon categories.
- **Kin Voracious Mind** now has a mechanical effect: +4 on Knowledge and Investigation Opposition Checks.
- **Faerie Ethereal Form** healing rate clarified: 2 Health per hour of rest (instead of 1); doubles Health restored by potions and Healing skills.
- **Elf Arcane Echo** now explicitly grants access to Magic Attack skills.
- **Movement Modes Table** corrected to match the Glossary's movement model: Running is now 2× base movement (was 1.5×) and Sprinting 3× (was 2×). Crawling and Swimming normalized to constant ¼× increments. A pre-calculated "at base 30 ft" column added to eliminate multiplication at the table.
- Various Glossary corrections: the Willpower entry no longer references the retired "higher of Willpower or Fortitude" rule for Consciousness Checks; the Incapacitated entry no longer incorrectly lists Dying as a cause; the Poisoned entry now correctly reflects the rules in Poisons.md.
- Recovery clarified: the restriction on recovering Health while Dying applies to rest only — it does not block Heroic Measures or other explicit healing.
- Stabilization clarified: stabilization ends Bleeding Out only. If a character was Incapacitated before being stabilized, that condition remains; stabilization does not remove it.

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
