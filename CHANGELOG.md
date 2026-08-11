# Changelog

Notable changes to WildCore — rules, content, and the website — recorded here as they're committed. Newest entries first, grouped by date and area.

This is the public-facing summary. It doesn't need session-by-session design rationale (why a decision was made, alternatives considered) — just what changed, in plain terms a player, Narrator, or site visitor would care about.

## 2026-08-11

Session 33: Magic system redesign — AP-based casting replaces spell levels; Spells catalog restructured to one file per spell

### Rules changes
- **Magic** — spell levels removed. Casting Time (in AP) replaces spell level as the core unit of a spell's cost, and the flat per-level Health cost is gone. Three new systems: **Potency and Charging** (a caster may commit AP beyond a spell's base Casting Time as a whole-number multiplier — ×2 costs twice the base Casting Time and doubles every numerical value in the spell, ×3 costs three times and triples them, and so on), **Overclocking** (spend Health to shave AP off a cast, at an escalating Health cost and Predation Clock penalty), and **Multi-Round Casting** (any cast — base or charged — whose total AP exceeds what the caster can spend in one turn is cast as a Concentration effect spread across multiple rounds, so a heavily charged spell takes proportionally longer rather than getting cheaper to overcharge). **Learning Spells** reworked: a spell now actively resists being learned via a Spellcasting Defense Opposition Check, with difficulty scaled to the spell's Casting Time, replacing the old flat Research check against spell level. **Predation Clock** now drains by AP spent casting (plus an Overclocking penalty when used) instead of by spell level.
- **Spellcasting skill tree** — removed "may cast Level N spells" language from every tier; spell access is no longer level-gated. Spellcasting IV now grants +2 to Concentration Checks (previously an empty tier). Mastery Tier split into two independent branches: **Mastery Tier: Combat** (the existing VI–X progression) and a new **Mastery Tier: Overclocking** (five new skills, Overclocking I–V, prerequisite Spellcasting V) that mitigates Overclocking's risks — bonus to Consciousness Checks from Overclocking, a once-per-session Predation waiver, a once-per-encounter Concentration Check reroll, immunity to Bleeding Out from Overclocking Health loss, and a once-per-session floor of 1 Health instead of dropping to 0.
- **Tree of Life** — Casting Time reduced from 7 AP to 3 AP; Healing Pool, initial burst, and per-round recovery reduced to match. Full power is recoverable by charging the spell.

### Spells catalog restructure
- Replaced the 10 `Level 0–9 Spells.md` files with 46 individual spell files (one per spell), matching the Creatures and Races convention. The old Level-based files are preserved in `.backup/Spells/`.
- `Spells.md` rebuilt: the category grid and the alphabetical list now show AP cost instead of spell level and link directly to each spell's own file.
- Elemental Bolt collapsed from nine separate tiered spells (Elemental Bolt I–IX) into a single spell that scales with charging.
- Every 0 AP ("Minor") spell now explicitly states it cannot be charged or overclocked and is cast as a Free Action.

### Assets
- Added `Logo/` folder: WildCore logo in PNG and SVG, standard and transparent variants.
- Added `Licensing/Compatible with WildCore Badge.png`; removed the outdated `Compatible with Velocty Badge.png`.

### Fixes
- `Licensing` — corrected the license acronym from the old **VOL**/**VOL-DL** to **WOL**/**WOL-DL** throughout all five renamed license documents; only the filenames and the word "WildCore" had been updated previously, leaving the acronym stale in the body text.
- `Spellcasting Skill.md` — Spellcasting X's prerequisite corrected to Spellcasting IX (was duplicated from Overclocking I's prerequisite during the Mastery Tier split).

---

## 2026-08-09

Session 32: Dice Pools rewrite; game rename cleanup; licensing folder cleared

### Rules changes
- **Dice Pools** — assembly steps in both Attack Pools and Damage Pools reframed as a character-sheet task, not a roll-time procedure. Sections renamed "Building your pool (do this on your character sheet, not during play)"; the roll step is removed from the procedure; a "Record" step added at the end. Added a "During play" one-liner to each section: grab your recorded pool, roll, add flat, done. Examples restructured into explicit "Building (character sheet)" and "At the table" stages.

### File cleanup
- Licensing folder: renamed all five VOL documents from `Velocity*` to `WildCore*` (Open License v1.0, Dual-License Variant, Plain-English Summary, Creator FAQ, Publisher's Guide)
- Renamed "Velocity" → "WildCore" throughout: `README.md`, `Core Rules/Introduction.md`, `Starter Kit/Introduction.md`, `Starter Kit/Narrator's Guide/Narrator Quick Reference.md`, `Starter Kit/Narrator's Guide/Overview.md`, `Starter Kit/Characters/Paivel.md`, `TODO.md`
- TODO.md: removed resolved and struck-through items

---

## 2026-08-08

Session 31: Core Rules Analysis resolution pass — all 16 issues from the 2026-08-02 analysis resolved

### Rules changes
- **Elf — Fell Presence** (renamed from "Intimidating Presence"): the trait now applies to all Social Opposition Checks made in person, not just Intimidation. The bonus (+4) is unchanged.
- **Strength VII and IX** now explicitly grant +1 additional damage die to ranged damage rolls as well as melee, matching the design intent. Previously the tier descriptions said "melee" only while the skill description said "both."
- **Forced Awakening** now correctly imposes [Vulnerable] alongside Prone and Hindered. A character woken by smelling salts in a fight is prone, hindered, and vulnerable until treated or the scene ends.
- **Actions** — added Incapacitated to the list of conditions that prevent a character from using Dodge, Parry, or Block.
- **Health.md** — clarified that characters who make no Health Archetype declaration use the Average Archetype (25 Maximum Health), not an undefined "standard baseline."

### Consistency and link fixes
- `Racial Traits.md` converted to a link index pointing to each race file; eliminates the duplication that caused trait descriptions to drift out of sync
- `Glossary.md` — health entry updated to reference Health Archetypes (20/25/30); forced awakening entry updated to include Vulnerable
- `Werewolf Lineage.md` Note 4 — "Blood Healing" corrected to "Lycan Healing"
- `Magic.md` — removed "(cantrips)" parenthetical; Level 0 spells throughout
- `Health Skill.md` — fixed broken anchor (#health-archetypes.md → #health-archetypes)
- Creatures index: The Fae added; Source column standardized to "Core Rules" for all current entries
- The Fae stat block: Size row added
- Various internal link corrections across Opposition Checks, Turn Structure, and Magic

---

## 2026-08-02

Session 30: reference library, file reorg, rules clarifications, CI fixes

### File reorganization
- Moved `Glossary/Glossary.md` → `Core Rules/Glossary.md` (Glossary is now a Core Rules chapter)
- Renamed `Characters/Traits.md` → `Characters/Racial Traits.md`
- Fixed longstanding typo: `Attribute Parings for Opposition Checks Table.md` → `Attribute Pairings for Opposition Checks Table.md`
- Updated all internal links across Core Rules to reflect the above moves

### Health Archetypes propagation
- `Characters/Attributes.md`: Maximum Health now references Archetypes (20/25/30) instead of flat 25; links updated
- `Tables/Character Attributes Table.md`: Max Health row reflects Archetypes; added Reflex tiebreaker note
- `Skills/Universal/Attributes/Health Skill.md`: description updated to reference Archetypes and link to Health.md

### Rules clarifications (Actions.md)
- Added explicit rule: Stunned, Immobilized, Unconscious, and Restrained characters cannot use Dodge, Parry, or Block
- Removed "restrained" from Dodge's constraint list (Restrained already blocks all defense entirely)
- Added rule: Vulnerable characters lose their Reflex bonus on defense rolls
- Fixed link casing: `action points.md` → `Action Points.md`

### Conditions
- Mute: replaced d20 "verbal components" language with "spells requiring the caster to speak"
- Restrained: clarified that other conditions (Blind, Mute) may apply additionally to a Restrained character
- Recovery.md: fixed heading render bug `[Unconscious]ness` → `Unconscious`; minor wording fix

### Spells
- Level 0: removed duplicate Nunor's Spring entry; fixed heading level (H4 → H3)
- Level 3: removed Nunor's Blessing and Rasgard's Flying Bridge

### Equipment
- Gear.md: reformatted General Gear table for alignment; removed Spell Component Pouch

### CI/CD
- `build-and-deploy.yml`: added missing Deploy to GitHub Pages step and IndexNow URL submission step


## 2026-07-17

**Rules — Characters**
- **Health Archetypes added** (`Characters/Health.md`). At character creation, players may declare a Health Archetype reflecting their character's natural constitution. **Frail** — 20 Maximum Health, +1 SP at creation; the entire Health skill tree is locked until the first SP is earned through play (may not purchase Health I at creation). **Average** — 25 Maximum Health; no declaration required. **Robust** — 30 Maximum Health; costs 1 SP from the starting pool. Replaces the previous flat 25 Maximum Health baseline for all characters.

**Rules — Encounters**
- **AP timing now consistent across all documents.** `Action Points.md` §1 and `Turn Structure.md` updated to state that unspent AP are lost "when the round ends" (once all characters have taken their turns), not "at the end of the turn." This aligns with the Reactions system, which requires AP to persist through other participants' turns within the same round.
- **Dodge removed from the Standard Actions list** in `Actions.md`. Dodge is a Reaction triggered by an incoming attack — a participant cannot declare it proactively on their own turn.

**Rules — Lineages / Races**
- **Fae-Touched III Lightborne Step** updated in `Fae-Touched Lineage.md` to resolve a naming conflict with the Faerie race trait of the same name (which grants a +4 Stealth bonus that the Fae-Touched version did not include).
- **Werewolf Lineage Note 3** corrected: "Blood Healing (Werewolf VII)" changed to "Lycan Healing (Werewolf VII)."

**Spells**
- **Nunor's Spring** (Level 0) restored — was absent from `Level 0 Spells.md` after the prior restoration pass.
- **Nunor's Blessing** (Level 3) and **Rasgard's Flying Bridge** (Level 3) restored — both were absent from `Level 3 Spells.md` after the prior restoration pass.

**Fixes**
- `Characters/Traits.md` — "cross-lineage" corrected to "cross-race" in the God-touched trait introduction.
- `Races/Faerie Race.md` — OC Modifiers table now includes the Ethereal Form daily −4 penalty (applies the following day if Ethereal Form is not assumed during the prior day).
- `Glossary/Glossary.md` — Dead link to revival rules removed from the **dead/death** entry. Revival via spell is a deferred design decision not yet defined in Core Rules.

---

## 2026-07-15

**Rules — Combat (Size Disparity)**
- **Size Categories Table added** (`Core Rules/Tables/Size Categories Table.md`). Six size categories — Tiny, Small, Medium, Large, Huge, Gargantuan — with race assignments. Dwarf, Kin, and Kith are Small; Human, Elf, Faerie, and Shapeshifter (humanoid form) are Medium. Shapeshifter animal form sizes are defined in the Shapeshifter race file.
- **Auto-hit rule for size disparity added** to `Actions.md`. When a combatant attacks a melee target two or more size categories larger than themselves, no attack Opposition Check is required — the attack automatically hits. Damage is still rolled normally. One category difference has no effect. Ranged attacks and spellcasting are excluded.
- **Dodge bonus for size disparity added** to `Actions.md`. When a defender is two or more size categories smaller than a melee attacker, they gain +2 to their Dodge pool against that attack. Does not apply to Parry or Block, and does not apply against ranged attacks or spells.
- **§Attack Resolution restructured** into four named subsections: Attack Roll, Defense Roll, Final Resolution, and Multiple Attackers.

**Rules — Action Points**
- **Reaction AP clarified** in `Action Points.md`. A character holding AP in reserve for a Reaction does not voluntarily end their turn — their turn remains open until the reserved AP is spent or they choose to close it. Unspent AP are lost when the round ends (all characters have taken their turns), not when an individual character stops acting.

**Spells**
- **All ten spell files restored** (Level 0–9). Every file was truncated mid-sentence. Content restored to complete state across the full catalog.

**Creatures — Shapeshifter Animal Forms**
- **15 animal form creature entries added** to the Creatures chapter: Bat, Bear, Crocodile, Eagle, Fox, Hawk, Mountain Lion, Otter, Owl, Panther, Raven, Serpent, Stag, Wild Boar, and Wolf. Each entry includes a full stat block (Health, Natural Armor, Size, Movement), Strength score, and attack table. Description and Behavior sections are placeholders pending prose pass.
- **Health** derived from SRD equivalent HP + 10 flat, ensuring no animal goes down in a single hit at baseline.
- **Natural Armor** assigned by hide toughness: Crocodile 8, Wild Boar 6, Bear 4, Stag 2, all others 0.
- **Strength** assigned by physical power: Bear 3, Mountain Lion/Panther/Crocodile 2, Stag/Wild Boar/Wolf 1, all others 0. Bear's Strength 3 grants a bonus attack and damage die on every strike.
- **Multi-Strike** granted to all creatures with claws or talons: Bear, Eagle, Fox, Hawk, Mountain Lion, Otter, Owl, Panther, Raven.
- **Crocodile** has a special follow-on ability: **Deathroll** (1 AP after a successful Bite) — opposed Strength check; on failure the target is Restrained and, if near water, dragged beneath the surface.
- **Serpent** is a Large constrictor with a special follow-on ability: **Constrict** (1 AP after a successful Bite) — Strength OC vs. difficulty 12; on failure the target is Restrained and takes 1d8 crushing damage each round until they break free.
- **Owl** carries a note: silent flight — no Stealth penalty for movement while airborne.
- **Creatures.md** index updated to include all 15 new entries alongside Bolg.

**Fixes**
- `Core Mechanics/Dice Pools.md` — Example 1 corrected: final total was labelled "15 damage" (wrong number, wrong label, wrong context). Correct final attack total is 21. Example 2 was truncated from the file; restored and updated with a worked armor mitigation note using Hide Armor.
- `Characters/Traits.md` — Arcane Echo entry now includes the +2 bonus on Supernatural Detection Opposition Checks, matching the Elf race file.
- `Skills/Universal/Survival/Healing Skill.md` — Healing I now cross-references `Stabilization.md` for the stabilization procedure; prior wording implied the tourniquet worked automatically with no roll required.
- `Skills/Lineages/Werewolf Lineage.md` — Werewolf X now correctly references "Lycan Healing (Werewolf VII)" instead of "Blood Healing (Werewolf VII)."

---

## 2026-07-14

**Rules — Damage**
- **Specific overrides general** documented in `Encounters/Damage.md` and `Magic/Magic.md`. The Damage Types table is the general rule — individual spells and abilities may specify that their damage bypasses armor regardless of damage type, and the specific rule always takes precedence over the table. This makes Hellfire Touch's fire damage being unmitigated by armor a legitimate documented exception rather than a one-off inconsistency.

**Rules — Lineages**
- **Werewolf VII renamed from "Blood Healing" to "Lycan Healing"** to eliminate name collision with Vampire III (also "Blood Healing"). The mechanics are opposite — Werewolf VII spends own Health to burst-heal; Vampire III drains target Health — and the identical name caused table confusion.

**Spells**
- **Rasgard's Bolts** added (Level 2, Offense). Variable AP cost (1–5 AP); each AP fires one bolt dealing 1d8 Magical Force (unmitigated). Auto-hit — no attack OC, no defense. Predation Clock subtracts total Health cost paid rather than the spell's base level. Bolts may be split freely among targets in range.
- **Spell description restorations:** Malavard's Ward (Level 0), Whisper Walk (Level 1), and Tuvien's Echo (Level 2) were truncated in the file and never complete in git history. Content reconstructed: Malavard's Ward now states that speaking the correct password dispels the ward and permits normal use; Whisper Walk now states that any action that would break Stealth dispels the spell; Tuvien's Echo now includes Narrator guidance on what the echo shows.

**Creatures — New Chapter**
- **Creatures chapter added** to Core Rules, appearing last in the site navigation. Contains a landing page (`Creatures.md`) with an alphabetical creature index, and one file per creature.
- **Bolg** added as the first Core Rules creature entry. Stat block: 15 Health, Natural Armor 9, Movement 60 ft., Scent 60 ft. (immune to Blind for tracking). Attributes: Strength 2. Attack: unarmed Multi-Strike (1 AP) — one bite OC (2d4) and two claw OCs (1d6 each), resolved independently, no cumulative multi-attack penalty within the Multi-Strike. Each successful strike applies one stack of Bleeding Out. Defenders may Dodge, Parry, or Block each strike.
- **Balathor's Creation** (Level 8) updated to reference the Bolg creature entry rather than embedding the full stat block inline.

---

## 2026-07-13

**Rules — Damage**
- **Force damage split into two distinct types.** Elemental Force (kinetic impact, compressed air, concussive wave) is physical — armor mitigates it normally. Magical Force (conjured weapons, raw supernatural energy) is purely supernatural — armor does not apply. A new Damage Types table in `Encounters/Damage.md` lists all damage types with their mitigation status.
- **Ordred's Hammer** reclassified from Bludgeoning to Magical Force — it is a conjured weapon of pure supernatural energy, not a physical impact.

**Rules — Conditions**
- **Restrained** added as a new condition. A Restrained character is physically bound — shackled, cuffed, held, pinned — and cannot act of their own volition. They cannot take actions, Reactions, or move voluntarily, and cannot make attack, Dodge, Parry, or Block Opposition Checks. Armor mitigation still applies to attacks against a Restrained character. Breaking free requires a Strength Opposition Check against a Narrator-assigned difficulty.

**Rules — Action Points**
- **5 AP per turn maximum** now explicitly noted in Blood Surge (Vampire VIII) and Reflex VII, making the cap visible at all points where bonus AP can be granted.

---

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
  - *  - **Core Mechanics** (new) — Opposition Checks, Dice Pools
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

---

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

---

## 2026-07-10

**Rules**
- Added two new spells: **Lightning Arc** (Level 5) and **Lightning Storm** (Level 9).
  - Lightning Arc locks a single target in a sustained arc of electricity for as long as the caster maintains Concentration. On hit: 2d6 lightning damage and the target is Electrified and Immobilized until the arc ends. Additional 2d6 per damage instance if the target is wearing metal or in contact with water. Anyone who touches an Electrified target takes 2d6 and is thrown back 5 feet.
  - Lightning Storm strikes a primary target plus up to 1d8 additional enemies within 120 feet. 6d6 lightning to the primary, 3d6 to each secondary. Cannot be dodged. All targets Electrified for the duration of Concentration, taking repeated automatic damage each round.
- Added two new conditions: **Electrified** and **Immobilized**.
  - Electrified: imposes Immobilized, ignites nearby flammables, conducts damage to anyone who makes physical contact, and makes stealth impossible.
  - Immobilized: cannot take actions, Reactions, or move voluntarily; auto-fails checks that require voluntary movement.
- **Predation Clock redesigned.** Now a pure countdown rather than a die roll. Starts at 25 each encounter. When a Level 1+ spell is cast, subtract its level. When a concentration spell is maintained, subtract 1 per maintained spell per round. When the clock reaches 0, a manifestation occurs — and every subsequent draw on the magical field triggers another immediately. The clock is shared across all casters on the battlefield, friends and enemies alike.

---

## 2026-07-07

**Website**
- Spell header blocks now render as formatted lists instead of collapsing into a single line of text. Each field (Level, Category, Range, etc.) displays as its own line.

**Rules**
- Added a **Spells** section to Core Rules: ten files, one per spell level, covering Level 0 through Level 9.
- Each spell entry now includes a **Damage** field where applicable, showing dice, damage type, and any special notes.
- **Armor mitigation rule clarified for spells:** Elemental spell damage (fire, cold, lightning, acid) is mitigated by armor. Purely magical effects — force, conjured weapons — bypass armor entirely and are tagged `(unmitigated)` in the spell's Damage field. The default is that armor mitigates unless a spell says otherwise.
- **Balathor's Creation** (Level 8): Bolg stat block added. Each Bolg has 15 Health, Natural Armor 9, Movement 60 ft., and Scent 60 ft. Attack: Multi-Strike (1 AP) — one bite (2d4) and two claws (1d6 each), resolved independently. Each successful strike applies one stack of Bleeding Out.
