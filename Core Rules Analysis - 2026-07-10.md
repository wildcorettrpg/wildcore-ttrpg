# Core Rules Analysis — 2026-07-10

## Summary

| Severity | Count |
| :------- | ----: |
| 🔴 Critical | 1 |
| 🟡 Significant | 2 |
| 🟠 Minor | 13 |
| **Total** | **16** |

Auto-fixed in this session: 9 (C-01, MN-01 through MN-05, MN-09, MN-10, MN-13).  
Resolved post-session: 6 (SG-01, SG-02, MN-06, MN-08, MN-11, MN-12).  
Awaiting Mike's call: 1 (MN-07).

---

## Issues

### 🔴 Critical

#### C-01 — Magic.md §"The Sight Spells" contradicts Traits.md ✅ Auto-fixed

**File:** `Core Rules/Encounters/Magic.md` lines 130–138  
**Principle:** 7 — Rules Do Exactly What They Say  

The section states "Characters who are not God-touched may learn any of the three [Sight spells] through normal Spellcasting investment." This is directly contradicted by `Characters/Traits.md` (canonical since Session 24), which classifies Far Sight, Long Sight, and True Sight as God-touched cross-lineage traits — innate perceptions that cannot be purchased, learned, or trained. The section was replaced with a cross-reference to Traits.md.

---

### 🟡 Significant

#### SG-01 — Rasgard's Rage stuns targets who succeed their defense ✅ Resolved

**File:** `Core Rules/Spells/Level 6 Spells.md`  
**Principle:** 7 — Rules Do Exactly What They Say  

Intentional by design. A successful defense Opposition Check does not guarantee the target escapes unharmed — the spell defines its own outcomes for both success and failure. Rasgard's Rage's "Stunned 1 round on success" is correct: the concussive blast staggers everyone in the cone regardless of how well they brace. This rule was added to `Encounters/Magic.md` §Spell Attacks and `Encounters/Opposition Checks.md` §Attacks and Defense, and documented in Design Decisions. Rasgard's Rage category also corrected from "Offense, Crowd Control" → "Crowd Control" (MN-08).

#### SG-02 — Balathor's Creation: "stacking" Bleeding Out is undefined ✅ Resolved

**File:** `Core Rules/Spells/Level 8 Spells.md`  
**Principle:** 7 — Rules Do Exactly What They Say  

The Bolg description states: "If any attack should get past armor mitigation, the target immediately enters the Bleeding Out condition. Multiple successful hits stack the Bleeding Out condition on the target."

Resolved by defining stacking in `Conditions.md` §Bleeding Out: each additional stack adds 1 Health/round (2 stacks = 2/round, etc.). Each stack is tracked and removed independently — Stabilization removes one stack. Healing above the wounded threshold removes all stacks.

---

### 🟠 Minor

#### MN-01 — Dwarf.md duplicate Languages section ✅ Auto-fixed

**File:** `Core Rules/Lineages/Dwarf.md`  

Languages are listed in the header block (line 7: `**Languages**: Common, Dwarven`) and repeated as a standalone `## Languages` section at the bottom. The bottom section was removed.

#### MN-02 — Dwarf.md Fearless description incomplete ✅ Auto-fixed

**File:** `Core Rules/Lineages/Dwarf.md`  
**Principle:** 7 — Rules Do Exactly What They Say  

The `### Fearless` trait block says "Dwarves are immune to fear effects." The Opposition Check Modifiers section and `Characters/Traits.md` both add "Automatic success on Willpower Opposition Checks to resist fear." The trait description was missing this mechanic. Updated to match Traits.md.

#### MN-03 — Faerie.md: incorrect Difficult Terrain modifier label ✅ Auto-fixed

**File:** `Core Rules/Lineages/Faerie.md` §Opposition Check Modifiers  
**Principle:** 7 — Rules Do Exactly What They Say  

The modifier reads "Ignores Difficult Terrain opposition checks." There are no Opposition Checks triggered by Difficult Terrain — Difficult Terrain halves movement speed. The Lightborne Step trait body text correctly says "ignore movement penalties from Difficult Terrain." The modifier summary was updated to match.

#### MN-04 — Faerie.md: Ethereal Form healing comparison is wrong ✅ Auto-fixed

**File:** `Core Rules/Lineages/Faerie.md` §Ethereal Form  

The text reads "heals at 2 Health per hour of rest instead of 1." The base recovery rate per `Recovery.md` is 1 Health per **four** hours — not 1 per hour. "Instead of 1" implies the baseline is 1/hour, which is incorrect. The rate is actually eight times base, not double. Updated to: "heals at 2 Health per hour of rest (compared to the base rate of 1 Health per four hours)."

#### MN-05 — Shapeshifter.md references retired Weapon proficiency tree ✅ Auto-fixed

**File:** `Core Rules/Lineages/Shapeshifter.md` §Animal Forms  

The text reads: "The Weapon proficiency trees do not apply; natural weapons require no proficiency and impose no untrained penalty." The Weapon proficiency tree was retired in Session 14 (replaced by the multi-attack cumulative −2 penalty system). Referencing it is stale even if the second clause is correct. Removed the stale first clause; the correct behavior is preserved in "natural weapons require no proficiency and impose no untrained penalty."

#### MN-06 — Healing I / Conditions.md: tourniquet not listed as a way to end Bleeding Out ✅ Resolved

**File:** `Core Rules/Skills/Universal/Survival/Healing Skill.md` and `Core Rules/Encounters/Conditions.md`  

Resolved by updating the Bleeding Out **Ends** line to read "stabilized by a healer" — making explicit that Stabilization requires a healer (i.e., someone with Healing skills). Healing I's tourniquet is the mechanism of stabilization, not a separate shortcut around it. The two descriptions are now consistent.

#### MN-07 — Attribute Pairings Table Footnote 1 conflates spell categories ⚠️ Awaiting Mike's call

**File:** `Core Rules/Tables/Attribute Pairings for Opposition Checks Table.md`  

Footnote 1 lists "force" alongside elemental spells (fire, lightning, cold) under the "Physical / elemental spell" row. `Magic.md` §Spell Defense treats these as distinct categories: elemental spells (armor mitigates) vs. magical/force spells (armor does not mitigate, tagged `(unmitigated)`). Both types use Dodge as the defense mechanic, so the Attribute Pairings table is functionally correct — but "force" under "Physical / elemental" is a category error since force specifically bypasses armor.

Suggested: move "force" to its own row or footnote, or add a note: "Force spells use Dodge only (same as elemental) but see Magic.md §Spell Defense for armor mitigation differences."

Leaving for Mike's call since the defense mechanic (Dodge only) is correct and this is categorization/clarity.

#### MN-08 — Rasgard's Rage: "Offense" category but no damage dealt ✅ Resolved

**File:** `Core Rules/Spells/Level 6 Spells.md`, `Core Rules/Spells/Spells.md`, `Core Rules/Spells/Spells.csv`  

Category changed to "Crowd Control" only in `Level 6 Spells.md`, `Spells.md` Type Coverage table, and `Spells.csv`. Resolved alongside SG-01.

#### MN-09 — Glossary "spell overcharging" entry links to stale file ✅ Auto-fixed

**File:** `Glossary/Glossary.md`  

The spell overcharging entry links to `../Core%20Rules/Skills/Universal/Combat/Magic%20Attack.md#spell-overcharging`. The skill tree file was renamed from "Magic Attack" to "Spellcasting" in Session 23. The spell overcharging rules canonically live in `Magic.md` §Spell Overcharging. Link updated.

#### MN-10 — Nunor's Trident missing Target field ✅ Auto-fixed

**File:** `Core Rules/Spells/Level 9 Spells.md`  

Nunor's Trident is the only spell in the catalog missing a **Target** field in the header block. All other spells include one. Added: `**Target:** Self (what answers is Nunor's decision)`.

#### MN-11 — Example of Play: Sela casts "force bolt" — no such spell in catalog ✅ Resolved

**File:** `Core Rules/Example of Play.md`  

Updated to Elemental Bolt III. Sela's stat block raised to Spellcasting IV (may cast 3rd-level spells); Health cost updated to 3; all "force bolt" references replaced with "Elemental Bolt III" or "elemental bolt"; the design note paragraph updated to reflect the 3 PD drain of a 3rd-level cast.

#### MN-12 — Example of Play: Mira's Arcane Echo description doesn't match Traits.md ✅ Resolved

**File:** `Core Rules/Example of Play.md`, `Starter Kit/Characters/Mira.md`  

The +2 bonus was stale — Elf.md §Opposition Check Modifiers has no Arcane Echo-based bonus. Updated in both files: Arcane Echo description corrected to "grants access to Spellcasting skills; Spellcasting I unlocked for free." Mira's Opposition Check Modifiers updated to match Elf.md (Research +2, Supernatural +2, Intimidation +4 — removing the nonexistent Spellcasting/magical defense +2). Magical defense Key Roll removed from Mira.md.

#### MN-13 — Example of Play contains horizontal rules ✅ Auto-fixed

**File:** `Core Rules/Example of Play.md`  

Six `---` horizontal rule lines in the document. Project formatting rule: "Never add horizontal rules (`---`) to any document. If horizontal rules are found in existing documents, remove them." All six were removed and sections are now separated by blank lines only.

---

## Files Read

All `.md` files under `Core Rules/` were read, plus `Glossary/Glossary.md`. Total: approximately 90 files.

`Spells/_test.md` contained no rules content (test data only).

