# Changelog

Notable changes to Velocity — rules, content, and the website — recorded here as they're committed. Newest entries first, grouped by date and area.

This is the public-facing summary. It doesn't need session-by-session design rationale (why a decision was made, alternatives considered) — just what changed, in plain terms a player, Narrator, or site visitor would care about.

## 2026-07-11

**Rules**
- **Dying system redesigned.** The Wounded and Dying conditions and their per-character threshold calculations are removed. In their place: a single fixed threshold — when a character's Health falls to 7 or below from any source, they make a Consciousness Check (dice pool + Willpower vs. the damage value that triggered it). Failing = Unconscious. The threshold is the same for all characters regardless of Maximum Health.
- **Bleeding Out is now a Narrator-applied condition**, not an automatic threshold trigger. Any attack, ability, or effect can cause it. 1 Health per round, stacks independently, ends when stabilized.
- **"Vitality" renamed to "Health."** Health is now a two-value tracked stat: Maximum Health (ceiling) and Current Health (fluctuating). The Vitality skill tree is renamed the Health skill tree (Health I–X).
- **Kithkin Blood** (Kith and Kin flaw) now triggers while Bleeding Out instead of while Wounded.
- **Eye for Value** (Human trait) corrected to +4 on Investigation Opposition Checks when assessing valuables.
- **Elf Living Memory** trait added: +2 on Research Opposition Checks. **Arcane Echo** expanded: also grants +2 on Supernatural Opposition Checks when detecting magical creatures.
- **Principle 6 exception documented:** halving and doubling values are explicitly permitted. "Half damage" and "double damage" are universally understood and not flagged as math violations.

**Spells**
- **Radius field added** to all AoE and cone spell stat blocks (Level 0–9) and to Spells.csv. Each area-effect spell now explicitly states its radius (e.g., "30 ft.", "60 ft. cone") in its own stat block field, separate from Range and Target.
- **Tuvien's Bond redesigned** (Level 5). The old equal-split mechanic is replaced by an **Anchor** system: at cast time, one bonded creature designates themselves the Anchor and declares a flat absorption amount. When the other creature takes damage, the Anchor takes the lesser of that amount or the total damage; the remainder goes to the struck creature. Protection is one-directional. The bond now persists until dismissed by a caster — no longer requires Concentration — and remains active across encounters indefinitely.
- **Tree of Life** (Level 7): Radius reduced to 10 ft. (from "line of sight"). Casting Time raised to 3 AP. Healing Pool increased to Willpower + 20. Flat drain design — no division anywhere.
- **Solan's Glory** (Level 3): Description completed (was truncated mid-sentence in source file).

**Website**
- "Cinema-first" replaced with "narrative-first" throughout the site and Starter Kit.

## 2026-07-10

**Rules**
- Added two new spells: **Lightning Arc** (Level 5) and **Lightning Storm** (Level 9).
  - Lightning Arc locks a single target in a sustained arc of electricity for as long as the caster maintains Concentration. On hit: 2d6 lightning damage and the target is Electrified and Immobilized until the arc ends. Additional 2d6 per damage instance if the target is wearing metal or in contact with water. Anyone who touches an Electrified target takes 2d6 and is thrown back 5 feet.
  - Lightning Storm strikes a primary target plus up to 1d8 additional enemies within 120 feet. 6d6 lightning to the primary, 3d6 to each secondary. Cannot be dodged. All targets Electrified for the duration of Concentration, taking repeated automatic damage each round.
- Added two new conditions: **Electrified** and **Immobilized**.
  - Electrified: imposes Immobilized, ignites nearby flammables, conducts damage to anyone who makes physical contact, and makes stealth impossible.
  - Immobilized: cannot take actions, Reactions, or move voluntarily; auto-fails checks that require voluntary movement.
- **Predation Difficulty redesigned.** Now a pure countdown rather than a die roll. Starts at 25 each encounter. When a Level 1+ spell is cast, subtract its level. When a concentration spell is maintained, subtract 1 per maintained spell per round. When PD reaches 0, a manifestation occurs — and every subsequent draw on the magical field triggers another immediately. The PD is shared across all casters on the battlefield, friends and enemies alike.

## 2026-07-07

**Website**
- Spell header blocks now render as formatted lists instead of collapsing into a single line of text. Each field (Level, Category, Range, etc.) displays as its own line.

**Rules**
- Added a **Spells** section to Core Rules: ten files, one per spell level, covering Level 0 through Level 9.
- Each spell entry now includes a **Damage** field where applicable, showing dice, damage type, and any special notes.
- **Armor mitigation rule clarified for spells:** Elemental spell damage (fire, cold, lightning, acid) is mitigated by armor. Purely magical effects — force, conjured weapons — bypass armor entirely and are tagged `(unmitigated)` in the spell's Damage field. The default is that armor mitigates unless a spell says otherwise. Updated Magic.md, Combat.md, and Damage.md to reflect this.
- **Balathor's Creation** (Level 8): Bolg stat block updated. Each Bolg has 15 Vitality, 9 damage mitigation from natural hide, and 60 ft. base movement. They target the healthiest enemy first, not the most wounded. Hits that get past mitigation trigger Bleeding Out; multiple hits stack the condition.
- Renamed the **Magic Attack** skill tree to **Spellcasting** throughout all Core Rules documents.

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
