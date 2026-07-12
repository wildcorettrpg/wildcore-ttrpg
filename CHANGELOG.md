# Changelog

Notable changes to Velocity — rules, content, and the website — recorded here as they're committed. Newest entries first, grouped by date and area.

This is the public-facing summary. It doesn't need session-by-session design rationale (why a decision was made, alternatives considered) — just what changed, in plain terms a player, Narrator, or site visitor would care about.

## 2026-07-12

**Rules — Lineages**
- **Race and Lineage are now two distinct systems.** A character's **race** is their birth ancestry (Human, Dwarf, Elf, Faerie, Kin, Kith, Shapeshifter) — fixed at creation, carries traits and flaws, no skill tree. A character's **lineage** is a supernatural transformation acquired through play (Vampire, Werewolf, Angel, Demon, Fae-Touched) — narratively triggered, unlocks a 10-skill progression tree. The two systems are independent and a character may have both.
- **Shapeshifter confirmed as a Race**, not a Lineage. Shapeshifters are a born people; wild shape manifests at puberty.
- **Five Lineage skill trees added to Core Rules:** Angel, Demon, Fae-Touched, Vampire, and Werewolf. Each is a 10-skill tree (training tier I–V, mastery tier VI–X) with a defined acquisition trigger. Located in `Core Rules/Skills/Lineages/`.
- **Lineage overview pages added** (`Core Rules/Lineages/`) describing what each lineage is, how it is acquired, what it grants, and what it costs. These are separate from the mechanical skill trees.
- **Silver suppresses vampire Blood Healing** until removed. A vampire cannot use Blood Healing to close a silver wound while any silver remains in it.
- **Silver and wolfsbane both suppress werewolf accelerated healing.** Silver suppresses only the silver wounds; wolfsbane (while the character is exposed) suppresses all wound healing.
- **Wolfsbane added to the Named Poisons table** (Ingested / Injury, Potent, 25 gp). On non-lycanthropes it acts as a standard Potent poison; on werewolves it suppresses accelerated healing for the duration.
- **Weapon Coatings added to Weapons.md.** Silver paste and wolfsbane can be applied to bladed weapons and arrowheads (1 AP, 3 doses per application, 25 gp per dose). Silver paste delivers the full silver-weapon effect without the weapon being made of silver; a coated iron blade still triggers the iron/steel bonus against Faerie and Fae-Touched.
- **Iron and steel deal +1 damage die** against the Faerie race and Fae-Touched lineage (explicit automatic rule).
- **Silver deals +1 damage die** against Vampire and Werewolf lineages (explicit automatic rule).

**Rules — Structure**
- **"Predation Difficulty" renamed to "Predation Clock."** The mechanic is a countdown timer, not a target number — the old name implied a difficulty to beat rather than a clock that runs down.
- **Predation Clock manifestation targeting clarified:** manifestations now target the caster whose action triggered the clock reaching zero. The Narrator still determines what manifests and where.
- **Concentration** basics corrected: the introductory text no longer claims Concentration is "not an action." Maintaining Concentration costs 1 AP per round.
- **Conditions** intro fixed: removed circular "Conditions are conditions..." phrasing.
- **Dice Pools** — new dedicated document explaining what a dice pool is and how to build one, covering both attack pools and damage pools with worked examples. All "dice pool" references across the Core Rules now link to it.
- **Intense Concentration removed.** Concentration no longer grants the Narrator discretion to impose [Vulnerable](Core%20Rules/Conditions%20and%20Hazards/Conditions.md#vulnerable) on a concentrating character. If a specific spell or ability imposes [Vulnerable](Core%20Rules/Conditions%20and%20Hazards/Conditions.md#vulnerable), it says so in its own description. Removed from `Concentration.md`, `Opposition Checks.md`, `Conditions.md`, and the Glossary.
- **All condition mentions across the Core Rules are now linked** to their entries in `Conditions.md`.
- **Encounters chapter split into four chapters.** `Core Rules/Encounters/` contained unrelated content. Files redistributed:
  - **Core Mechanics** (new) — Opposition Checks, Dice Pools
  - **Magic** (new) — Magic, Concentration
  - **Conditions and Hazards** (new) — Conditions, Environmental Hazards, Poisons, Dying, Death, Stabilization, Recovery
  - **Encounters** (retained) — Encounter Structure, Turn Order, Turn Structure, Action Points, Actions, Free Actions, Reactions, Combat, Damage, Consciousness Checks, Movement
- **Characters chapter narrowed to character creation.** Dying, Death, Stabilization, and Recovery moved to Conditions and Hazards — they are play-state rules, not character creation content. Characters now covers: Attributes, Health, Skill Points, Traits, Modifiers, Effective Level, Starting Equipment.

**Rules — Vampire Lineage**
- **Blood Healing redesigned** as a per-round Health transfer. Initiating costs 1 AP; each sustained round costs 1 AP. At Vampire III (Blood Healing), **8 Health transfers per round** from the target to the vampire — the target loses it, the vampire gains it. Target must be willing or [Incapacitated]. At Vampire X (Apex Predator), the rate increases to **16 Health per round** and the vampire may feed from any creature regardless of condition. No once-per-scene limit.

**Rules — Spells**
- **Spells.md** now includes a complete alphabetical spell index (all 53 spells with Level and Category, each linked to its spell entry).

**Rules — Stabilization**
- **Forced Awakening clarified:** a character forced back to consciousness while still at 7 Health or below resumes making Consciousness Checks each time their Health drops further. Forced Awakening restores consciousness; it does not secure it.

**Rules — Dice Pools**
- **Named Pool Types** defined in `Core Mechanics/Dice Pools.md`: Spellcasting attack pool (Willpower), Melee attack pool (Strength), Ranged attack pool (Strength), Dodge/Parry/Block pools (Reflex), Willpower pool. Verbose "dice pool + Attribute" phrasing replaced with pool names throughout the Core Rules.

**Website**
- **Anchor navigation fixed.** Links to section headings now scroll correctly — the target heading is no longer hidden behind the fixed playtest banner. Fix: `scroll-margin-top` set on all headings in `#reader-content` using the banner and topbar CSS variables.

## 2026-07-11

**Rules**
- **Dying system redesigned.** The Wounded and Dying conditions and their per-character threshold calculations are removed. In their place: a single fixed threshold — when a character's Health falls to 7 or below from any source, they make a Consciousness Check (dice pool + Willpower vs. the damage value that triggered it). Failing = [Unconscious](Core%20Rules/Conditions%20and%20Hazards/Conditions.md#unconscious). The threshold is the same for all characters regardless of Maximum Health.
- **[Bleeding Out](Core%20Rules/Conditions%20and%20Hazards/Conditions.md#bleeding-out) is now a Narrator-applied condition**, not an automatic threshold trigger. Any attack, ability, or effect can cause it. 1 Health per round, stacks independently, ends when stabilized.
- **"Vitality" renamed to "Health."** Health is now a two-value tracked stat: Maximum Health (ceiling) and Current Health (fluctuating). The Vitality skill tree is renamed the Health skill tree (Health I–X).
- **Kithkin Blood** (Kith and Kin flaw) now triggers while [Bleeding Out](Core%20Rules/Conditions%20and%20Hazards/Conditions.md#bleeding-out) instead of while Wounded.
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
  - Lightning Arc locks a single target in a sustained arc of electricity for as long as the caster maintains Concentration. On hit: 2d6 lightning damage and the target is [Electrified](Core%20Rules/Conditions%20and%20Hazards/Conditions.md#electrified) and [Immobilized](Core%20Rules/Conditions%20and%20Hazards/Conditions.md#immobilized) until the arc ends. Additional 2d6 per damage instance if the target is wearing metal or in contact with water. Anyone who touches an [Electrified](Core%20Rules/Conditions%20and%20Hazards/Conditions.md#electrified) target takes 2d6 and is thrown back 5 feet.
  - Lightning Storm strikes a primary target plus up to 1d8 additional enemies within 120 feet. 6d6 lightning to the primary, 3d6 to each secondary. Cannot be dodged. All targets [Electrified](Core%20Rules/Conditions%20and%20Hazards/Conditions.md#electrified) for the duration of Concentration, taking repeated automatic damage each round.
- Added two new conditions: **[Electrified](Core%20Rules/Conditions%20and%20Hazards/Conditions.md#electrified)** and **[Immobilized](Core%20Rules/Conditions%20and%20Hazards/Conditions.md#immobilized)**.
  - [Electrified](Core%20Rules/Conditions%20and%20Hazards/Conditions.md#electrified): imposes [Immobilized](Core%20Rules/Conditions%20and%20Hazards/Conditions.md#immobilized), ignites nearby flammables, conducts damage to anyone who makes physical contact, and makes stealth impossible.
  - [Immobilized](Core%20Rules/Conditions%20and%20Hazards/Conditions.md#immobilized): cannot take actions, Reactions, or move voluntarily; auto-fails checks that require voluntary movement.
- **Predation Clock redesigned.** Now a pure countdown rather than a die roll. Starts at 25 each encounter. When a Level 1+ spell is cast, subtract its level. When a concentration spell is maintained, subtract 1 per maintained spell per round. When PD reaches 0, a manifestation occurs — and every subsequent draw on the magical field triggers another immediately. The PD is shared across all casters on the battlefield, friends and enemies alike.

## 2026-07-07

**Website**
- Spell header blocks now render as formatted lists instead of collapsing into a single line of text. Each field (Level, Category, Range, etc.) displays as its own line.

**Rules**
- Added a **Spells** section to Core Rules: ten files, one per spell level, covering Level 0 through Level 9.
- Each spell entry now includes a **Damage** field where applicable, showing dice, damage type, and any special notes.
- **Armor mitigation rule clarified for spells:** Elemental spell damage (fire, cold, lightning, acid) is mitigated by armor. Purely magical effects — force, conjured weapons — bypass armor entirely and are tagged `(unmitigated)` in the spell's Damage field. The default is that armor mitigates unless a spell says otherwise. Updated Magic.md, Combat.md, and Damage.md to reflect this.
- **Balathor's Creation** (Level 8): Bolg stat block updated. Each Bolg has 15 Vitality, 9 damage mitigation from