# Core Rules Analysis — 2026-07-10-2

## Summary

| Severity | Count |
| :------- | ----: |
| 🟡 Significant | 2 |
| 🟠 Minor | 10 |
| **Total** | **12** |

Auto-fixed in this session: 3 (MN-04, MN-05, MN-08).  
Carry-forward from prior analysis: 1 (MN-10 / previously MN-07 in 2026-07-10 report, awaiting Mike's call).  
Awaiting Mike's call: 9 (SG-01, SG-02, MN-01, MN-02, MN-03, MN-06, MN-07, MN-09, MN-10).

---

## Issues

### 🟡 Significant

#### SG-01 — Social attribute has one skill tree file; CLAUDE.md documents two ⚠️ Awaiting Mike's call

**Files:** `Core Rules/Skills/Universal/Attributes/Social.md`, `Skills/Skills.md`, `Skills/Universal/Attributes/Attributes.md`  
**Principle:** 7 — Rules Do Exactly What They Say

CLAUDE.md Design Decisions (Session 12) documents the Social attribute as built via **two separate branches — Dominance and Empathy** — each a 10-skill tree granting identical `+Social` bonuses (I–V: +1, VI: +2), differing in flavor text and capstone effects:

- **Dominance X:** "+1d10 to Domination Opposition Checks"
- **Empathy X:** "+1d10 to Empathy Opposition Checks"

What exists in the repo is a **single `Social.md`** file with a unified 10-skill tree whose Tier X capstone is "+1d10 to Opposition Checks involving commanding a scene." Neither `Dominance.md` nor `Empathy.md` exists. `Skills/Skills.md` and `Attributes/Attributes.md` list only `Social.md`.

The split capstone effects (Domination vs. Empathy) are mechanically meaningful: players choosing to invest in Dominance vs. Empathy would gain different tier-X capabilities. That distinction is currently lost. The "commanding a scene" capstone in Social.md does not match either documented capstone.

Options:
1. Create `Dominance.md` and `Empathy.md` as the two documented branches, each with their own capstone, and remove or demote `Social.md` to a parent node entry. Update `Skills/Skills.md` and `Attributes/Attributes.md` to list both.
2. Formally consolidate to a single Social tree and update CLAUDE.md to reflect that Dominance/Empathy are flavor names only (no distinct mechanical branches). In that case, the tier X capstone needs to be specified — "+1d10 to Domination Opposition Checks" or "+1d10 to Empathy Opposition Checks" can't both apply from a single tree tier.

#### SG-02 — Tree of Life (Level 7): "half the Healing Pool" requires division during play ⚠️ Awaiting Mike's call

**File:** `Core Rules/Spells/Level 7 Spells.md`  
**Principle:** 6 — Ruthlessly Eliminate Unnecessary Math

The Tree of Life spell sets a **Healing Pool** equal to the caster's Willpower + 7. On the round it appears, allies recover "Health equal to half the Healing Pool (rounded down)." This requires division at the table — a violation of Principle 6.

The subsequent rounds are fine (4 Health per round, 4 subtracted from pool — pure subtraction). Only the opening burst requires the halving.

Suggested fix: replace "half the Healing Pool" with a pre-calculated expression. Since Willpower ranges from 0 to ~9 at high investment, the burst could be replaced with a flat value (e.g., "4 Health on the first round, same as subsequent rounds") or a fixed die (e.g., "1d6 + Willpower" as a burst). Alternatively, remove the burst entirely and have the tree heal 4 per round from round one.

Mike's call on which approach preserves the spell's design intent.

---

### 🟠 Minor

#### MN-01 — Human Eye for Value: trait body (+4) conflicts with OC Modifiers (+2) ⚠️ Awaiting Mike's call

**Files:** `Core Rules/Characters/Traits.md`, `Core Rules/Lineages/Human.md`  
**Principle:** 7 — Rules Do Exactly What They Say

`Traits.md` §Human lists:

> **Eye for Value** — +4 to find and assess the value of treasure; +2 on Investigation and Negotiation checks when trading.

`Human.md` §Eye for Value trait body:

> +4 to find and assess the value of treasure.

`Human.md` §Opposition Check Modifiers:

> +2 on Investigation Opposition Checks when searching for or assessing valuables.  
> +2 on Negotiation Opposition Checks when trading or establishing prices.

The `Example of Play` character sheet (Cael) confirms the +2 versions.

The "+4 to find and assess" in the trait body and Traits.md does not reconcile with the "+2 on Investigation Opposition Checks when assessing valuables" in Human.md's OC Modifiers. One of the following is true:

- The bonus is +2 (OC Modifiers and Example of Play are correct; trait body is wrong)
- The bonus is split: +4 to a non-OC "find" action (noticing treasure exists) and +2 to Investigation OC when formally assessing it — but this split is not documented anywhere

Mike's call on which value is correct. If +2 is canonical, update `Traits.md` body and `Human.md` §Eye for Value to say "+2 on Investigation Opposition Checks when searching for or assessing valuables."

#### MN-02 — Faerie opening description implies baseline Difficult Terrain immunity ⚠️ Awaiting Mike's call

**File:** `Core Rules/Lineages/Faerie.md`  
**Principle:** 7 — Rules Do Exactly What They Say

The opening description paragraph reads:

> "Generally, faeries float above the ground and do not suffer movement penalties from difficult terrain."

The Difficult Terrain immunity is granted by the **Lightborne Step** trait — it is not a baseline Faerie property, it is a named trait with additional effects (+4 Stealth while moving). "Generally" is ambiguous enough that a reader could conclude all Faeries always hover without purchasing or having Lightborne Step.

Suggested fix: add a parenthetical or subordinate clause linking the statement to the trait: *"...their Lightborne Step making them immune to terrain penalties and near-silent in motion."* Or reframe the sentence as a description of what Lightborne Step produces rather than a general statement about the lineage.

Mike's call on preferred phrasing.

#### MN-03 — Faerie "Incapable of Deception": Anar-specific lore in Core Rules ⚠️ Awaiting Mike's call

**File:** `Core Rules/Lineages/Faerie.md`  
**Principle:** 1 — Narrative First (setting-agnostic Core Rules should not encode setting lore)

The Incapable of Deception trait description states:

> "This makes Faerie testimony legally and culturally unimpeachable **throughout Anar**."

Core Rules are setting-agnostic. The legal and cultural standing of Faeries in Anar is Anar-specific lore — it does not belong in the Core Rules lineage file. The equivalent content belongs in `The Lost Realms of Anar/Lineages/Faerie.md` or Anar's Player's Guide.

Suggested fix: remove "throughout Anar" and rephrase as a general consequence of the trait: *"In settings where this trait is known, Faerie testimony is often considered unimpeachable — a Faerie cannot say what is not true."* Mike's call on exact phrasing, or the sentence can simply be removed and left to campaign setting volumes.

#### MN-04 — Forced Awakening: "healing" vs. "medical treatment" ✅ Auto-fixed

**Files:** `Core Rules/Characters/Stabilization.md`, `Glossary/Glossary.md`, `Core Rules/Equipment/Gear.md`  
**Principle:** 7 — Rules Do Exactly What They Say

`Stabilization.md` §Forced Awakening states the patient is "Prone and Hindered until they receive **healing** or the scene ends." The `Glossary` "forced awakening" entry and `Gear.md` §Smelling Salts both say "**medical treatment** or the scene ends." Two documents used one term; one used another.

`Stabilization.md` updated to read "medical treatment" to match the Glossary and Gear.md.

#### MN-05 — Balathor's Wrath (Level 7): successful defense "half damage" not pre-calculated ✅ Auto-fixed

**File:** `Core Rules/Spells/Level 7 Spells.md`  
**Principle:** 6 — Ruthlessly Eliminate Unnecessary Math

On a successful defense, the text reads "they take half damage" — requiring the player to halve the 2d10 roll. `Televard's Fury` (Level 8) correctly handles this pattern with a parenthetical: *"they take half damage (2d12 fire damage)."* Half of 2d10 = 1d10.

Updated to: "On a successful defense, they take half damage (1d10 fire damage)." Now consistent with Televard's Fury's format and requires no division.

#### MN-06 — Nunor's Blessing (Level 3): "all fire-based attacks deal half damage" requires division ⚠️ Awaiting Mike's call

**File:** `Core Rules/Spells/Level 3 Spells.md`  
**Principle:** 6 — Ruthlessly Eliminate Unnecessary Math

The storm effect states: "All fire-based attacks against creatures within the storm deal half damage." This requires dividing each fire attack's damage roll in half during play — a Principle 6 violation. Unlike Balathor's Wrath (which deals a fixed dice expression that halves cleanly), fire attacks vary by weapon, skill, and attribute — no pre-calculated value can be given.

Options:
1. Replace "half damage" with a flat mitigation: "fire-based attacks deal 4 fewer damage" (or another flat value)
2. Replace "half damage" with "deal their minimum damage (no dice rolled)" — simpler but changes the effect's flavor
3. Remove the half-damage clause and replace it with a condition: targets within the storm are Protected from fire (fire attacks require a second Dodge or always fail)
4. Leave it as a Narrator ruling (round down to the nearest die) — but this still involves division

Mike's call on redesign.

#### MN-07 — Luniel's Blessing (Level 4): "double damage" requires multiplication ⚠️ Awaiting Mike's call

**File:** `Core Rules/Spells/Level 4 Spells.md`  
**Principle:** 6 — Ruthlessly Eliminate Unnecessary Math

The summoned creature's vulnerability reads: "attacks of either type deal double damage to it." Doubling requires multiplication — a Principle 6 violation.

Options:
1. Pre-calculate by doubling each die expression on the animal form's stat block and listing them explicitly in the spell
2. Replace "double damage" with "+1d12 additional damage of the same type" (approximate, but avoids math)
3. Replace with "the maximum damage of the attack, without rolling" — a Principle-6-clean approximation
4. Replace with "attacks bypass armor mitigation and deal an additional die of damage"

Mike's call on redesign. Note this also involves the animal form stat blocks, which vary by creature.

#### MN-08 — Ordred's Hammer (Level 3): missing Defense field ✅ Auto-fixed

**File:** `Core Rules/Spells/Level 3 Spells.md`  
**Principle:** 7 — Rules Do Exactly What They Say

Every spell in the catalog that can be attacked-against has a **Defense** field in its header block. Ordred's Hammer, which auto-hits without an Opposition Check, had no Defense field — leaving a blank where Narrators and players would expect one. The spell body describes the auto-hit behavior correctly, but the header was incomplete.

Added `**Defense:** None (strikes automatically — no attack Opposition Check)` to the spell header block.

#### MN-09 — Luniel's Blessing (Level 4): "half the caster's current Vitality" requires division ⚠️ Awaiting Mike's call

**File:** `Core Rules/Spells/Level 4 Spells.md`  
**Principle:** 6 — Ruthlessly Eliminate Unnecessary Math

The summoned creature's Vitality is set as "half the caster's current Vitality score, rounded down." This requires division at the table during what may be an intense combat moment (the caster just spent 4 Health to summon a creature).

Suggested fix: Replace the halved-Vitality formula with a fixed value or an expression using only addition. Options:
1. Fixed value: "The creature has Vitality equal to the caster's Willpower score plus 10" (approximate, avoids division)
2. Fixed flat: "The creature has 12 Vitality" (simplest; loses the "scales with caster" flavor)
3. Pre-tabulated: Add a note to the spell: "If the caster's Vitality is 25 (base), the creature has 12. If 45, it has 22. If 65, it has 32." Avoids in-play math.

Mike's call on which approach preserves intent.

#### MN-10 — Attribute Pairings Table: "force" listed under "Physical/elemental spell" ⚠️ Awaiting Mike's call (carry-forward from 2026-07-10 analysis)

**File:** `Core Rules/Tables/Attribute Pairings for Opposition Checks Table.md`  
**Principle:** 7 — Rules Do Exactly What They Say

Footnote 1 lists "force" alongside elemental damage types under the "Physical / elemental spell" row. `Magic.md` §Spell Defense treats these as distinct: elemental spells are mitigated by armor; force/conjured-weapon spells (e.g., Ordred's Hammer) are tagged `(unmitigated)` and bypass armor entirely. Both types use Dodge as the defense mechanic, so the table is functionally correct for resolving checks — but "force" under "Physical / elemental" is a category error since force specifically bypasses armor where elemental does not.

Suggested: add a note to the footnote clarifying that force spells use the same defense mechanic but differ in armor mitigation (see `Magic.md` §Spell Defense), or move "force" to its own row with a cross-reference.

---

## Files Read

All `.md` files under `Core Rules/` were read, plus `Glossary/Glossary.md`. Total: approximately 95 files, including all 10 spell level files.
