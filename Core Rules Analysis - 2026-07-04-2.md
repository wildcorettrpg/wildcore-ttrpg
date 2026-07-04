# Core Rules Analysis — 2026-07-04-2

## Summary

| Severity | Open | Resolved | Total |
| :------- | ---: | -------: | ----: |
| 🔴 Critical | 0 | 2 | 2 |
| 🟡 Significant | 0 | 4 | 4 |
| 🟠 Minor | 0 | 10 | 10 |
| **Total** | **0** | **16** | **16** |

Auto-fixable issues were corrected automatically and are marked ~~like this~~. Issues requiring Mike's decision remain open and are marked ◆.

---

## 🔴 Critical Issues

---

### ~~CR-01 — Dying.md §25 internally contradicts §30's three-trigger CC model~~

**File:** `Characters/Dying.md`  
**Principle:** 7 — Rules Do Exactly What They Say  
**Auto-fix:** ◻

Dying.md contains two statements about when Consciousness Checks are made. They directly contradict each other.

**§25** (Dying section, item 5): "A dying character must make a Consciousness Check **each round** to remain conscious."

**§30** (Consciousness Checks section): "A character who is not unconscious must attempt a Consciousness Check when any of the following occur: (1) They enter the Dying condition. (2) They are Dying and take damage. (3) They are Dying and lose Health from Bleeding Out."

The "each round" language is wrong under the established model. A Dying character who has been stabilized (no longer Bleeding Out) and takes no damage in a round makes zero CCs per §30 — but §25 says they must make one regardless. Multiple hits in a round can also trigger multiple CCs, which "each round" doesn't capture.

**Status:** ✅ Resolved — §25 rewritten to: "A dying character must make a Consciousness Check when they enter the Dying condition, when they take damage, or when they lose Health from Bleeding Out — see Consciousness Checks, below."

---

### ~~CR-02 — Magic Attack.md "Combat threshold" contradicts the established design decision~~

**File:** `Skills/Universal/Combat/Magic Attack.md`  
**Principle:** 3 — The Narrator Directs; 5 — Eschew Systems Complexity  

**Status:** ✅ Resolved — The "Combat threshold" subsection was replaced with a **Predation Difficulty** system. Predation Difficulty starts at 25 at the beginning of each encounter. Each time a Level 1+ spell is cast, subtract that spell's level from the difficulty, then the Narrator rolls 1d10. If the roll meets or exceeds the current difficulty, a hostile manifestation appears. Level 0 spells never affect the Predation Difficulty. Overcharging a Level 1+ spell subtracts twice its level. The Narrator tracks this privately — players do not. `Magic Attack.md` §Note 4 and §Spell Overcharging updated; `CLAUDE.md` updated to correct the stale "no tracked counter" language.

---

## 🟡 Significant Issues

---

### ~~SG-01 — Elf's Immortal Vitality contradicts the "no creation lineage modifies core attributes" rule~~

**Files:** `Lineages/Elf.md`, `Characters/Attributes.md`, `Glossary/Glossary.md`  
**Principle:** 7 — Rules Do Exactly What They Say  

**Status:** ✅ Resolved — Mike removed the prohibition entirely. `Attributes.md` §Lineage and Attributes, `Glossary.md` "lineage" entry, and `CLAUDE.md` (Core Mechanics summary + Design Decisions) updated: lineages may now apply attribute bonuses or penalties at creation; the only remaining constraint is that no attribute may exceed 3 at character creation, regardless of lineage. Elf's Immortal Vitality (+20 Vitality) is no longer contradictory.

---

### ~~SG-02 — Dwarf Opposition Check Modifier is inconsistent with Fearless~~

**File:** `Lineages/Dwarf.md`  
**Principle:** 7 — Rules Do Exactly What They Say  

**Status:** ✅ Resolved — Mike updated `Dwarf.md`. The modifier now reads "Automatic success on Willpower Opposition Checks to resist fear," correctly expressing immunity within the OC framework. The unsourced mind-control resistance modifier was removed.

---

### ~~SG-03 — Kith has an orphaned "+2 when using improvised weapons" modifier~~

**File:** `Lineages/Kith.md`  
**Principle:** 7 — Rules Do Exactly What They Say  

**Status:** ✅ Resolved — Mike added the +2 bonus explicitly to the Improvised Combatant trait. The modifier is now properly sourced.

---

### ~~SG-04 — Elf.md has two contradictory language entries~~

**File:** `Lineages/Elf.md`  
**Principle:** 7 — Rules Do Exactly What They Say  

**Status:** ✅ Resolved — Mike removed the duplicate Languages section at the bottom of the file. The single canonical entry in the header block remains: "Common, Old Anaric."

---

## 🟠 Minor Issues

---

### ~~MN-01 — Dying.md §12 has a duplicate word~~

**File:** `Characters/Dying.md`  
**Status:** ✅ Resolved — extra "character" removed.

---

### ~~MN-02 — Dying.md §23 has a grammatical error~~

**File:** `Characters/Dying.md`  
**Status:** ✅ Resolved — "is remains" corrected to "remains."

---

### ~~MN-03 — Dying.md §35 uses wrong term "Consciousness Opposition Check"~~

**File:** `Characters/Dying.md`  
**Status:** ✅ Resolved — "Consciousness Opposition Check" corrected to "Consciousness Check."

---

### ~~MN-04 — Attributes.md §12 Fortitude description is incomplete~~

**File:** `Characters/Attributes.md`  
**Status:** ✅ Resolved — "disease" and "exhaustion" added to the Fortitude description in §12.

---

### ~~MN-05 — Human.md lists Kithkin as a starting language~~

**File:** `Lineages/Human.md`  
**Status:** ✅ Resolved — Kithkin removed. Human languages entry now reads "Common."

---

### ~~MN-06 — Faerie.md has two typos in the Lightborne Step trait~~

**File:** `Lineages/Faerie.md`  
**Status:** ✅ Resolved — "tot" corrected to "to"; anchor corrected from `#difficult-terain` to `#difficult-terrain`.

---

### ~~MN-07 — Faerie Ethereal Form's +2 resistance modifier is not stated in the trait text~~

**File:** `Lineages/Faerie.md`  
**Status:** ✅ Resolved — vague "more resistant to magical attacks" replaced with "+2 to Opposition Checks to resist magical effects."

---

### ~~MN-08 — Environmental Hazards.md uses "disadvantage" — undefined in Velocity~~

**File:** `Encounters/Environmental Hazards.md`  
**Status:** ✅ Resolved — "disadvantage" replaced with "a −2 penalty on the Fortitude check."

---

### ~~MN-09 — Glossary "natural armor" links to a nonexistent section~~

**File:** `Glossary/Glossary.md`  
**Status:** ✅ Resolved — broken `#natural-armor` anchor removed; entry now links to `Armor.md`.

---

### ~~MN-10 — Concentration.md uses lowercase "opposition check"~~

**File:** `Encounters/Concentration.md`  
**Status:** ✅ Resolved — "opposition check" capitalized to "Opposition Check."

---

## Intentional Design Decisions — Not Flagged

The following items were noted and confirmed as intentional per CLAUDE.md:

- d20 terminology (spell levels, weapon categories, range values, "opportunity attack") — intentional compatibility goal
- Social numbers larger than combat numbers — cinema-first, relationship-driven design
- Armor mitigates damage only, does not affect hit chance — core design principle
- No critical hits, no fumbles — Narrator handles exceptional outcomes narratively
- Attacks cost 1 AP each with cumulative −2 multi-attack penalty — intentional
- Base AP 3 per turn, maximum 5 — intentional
- Magic Attack V granting +1d10 to Consciousness Checks — intentional "learned resilience"
- Weapon damage one die tier above d20 SRD baseline — intentional
- Vitality is not creation-assignable — intentional
- Strength VII/IX add damage dice to melee only, not ranged — intentional melee specialization
- Human Eye for Value "+4 to find and assess valuables" vs. "+2 Investigation, +2 Negotiation" in Modifiers — same bonus stated at two levels of specificity; not a contradiction
- Healer's Bag redesigned from "10 charges, 1d6+Willpower per charge" to "expanded inventory slots" — CLAUDE.md reflects the prior design; Healing.md, Gear.md, and Recovery.md are internally consistent under the new model. CLAUDE.md should be updated in a future session.

---

*Report generated by Core Rules Analysis skill. Session 22 — 2026-07-04.*
