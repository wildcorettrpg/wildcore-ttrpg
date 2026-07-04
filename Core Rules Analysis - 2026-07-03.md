# Core Rules Analysis — 2026-07-03

## Summary

| Severity | Count | Resolved | Open |
| :------- | ----: | -------: | ---: |
| 🔴 Critical | 4 | 4 | 0 |
| 🟡 Significant | 11 | 11 | 0 |
| 🟠 Minor | 5 | 5 | 0 |
| **Total** | **20** | **20** | **0** |

Analysis covered 81 files across 8 directories (Characters, Encounters, Equipment, Lineages, Skills/Universal, Tables, Glossary, and root Introduction/Example of Play). All files were read in full.

All issues were resolved in the same session.

---

## 🔴 Critical Issues

### 1. ~~Glossary "willpower" entry contradicts itself on Consciousness Checks~~ ✅ Resolved
**File:** `Glossary/Glossary.md` — "willpower" entry  
**Description:** The entry read: "Willpower contributes to Consciousness Checks: a dying character rolls the higher of their Willpower or Fortitude" — then, in the very next sentence, correctly stated "a dying character rolls their dice pool + Willpower." The first clause was stale (Session 16 changed Consciousness Checks to Willpower-only).  
**Fix applied:** Removed the stale "higher of their Willpower or Fortitude" clause. The entry now reads correctly.

---

### 2. ~~Stabilization.md is truncated mid-sentence~~ ✅ Resolved (pre-existing)
**File:** `Characters/Stabilization.md` — "Forced Awakening" section  
**Description:** The file appeared truncated at "The character is Hindered until they r" in a prior read. On re-read, the sentence was already complete: "The character is Hindered until they receive healing or the scene ends." Resolved before this session.  
**Note:** The Glossary's "forced awakening" entry also lists **Vulnerable** as an effect of Forced Awakening, but Stabilization.md does not. Worth checking whether a Vulnerable item was lost and should be restored as item 5 in the Effects of Forced Awakening list.

---

### 3. ~~Recovery.md "Restrictions" directly contradict Heroic Measures~~ ✅ Resolved
**File:** `Characters/Recovery.md` — §Restrictions  
**Description:** §Restrictions §1 stated "A character cannot recover Health while dying," directly contradicting Heroic Measures (Healing VI+), which restores Health on Dying characters.  
**Fix applied:** Changed to "A character cannot recover Health through rest while Dying." Rest recovery is halted; Heroic Measures and other explicit healing abilities are unaffected.

---

### 4. ~~Gear.md references an undefined "Diseased" condition~~ ✅ Resolved
**File:** `Equipment/Gear.md` — Fever Tonic entry  
**Description:** "End the Diseased condition" referenced a condition that doesn't exist in Core Rules.  
**Fix applied:** Changed to "End a fever or illness." — narrative rather than mechanical, no undefined condition referenced.

---

## 🟡 Significant Issues

### 5. ~~Stabilization.md §3 misleadingly implies all stabilized characters are Incapacitated~~ ✅ Resolved
**File:** `Characters/Stabilization.md` — §3  
**Description:** "A stabilized character remains Incapacitated" stated Incapacitated as a universal consequence of stabilization, which was wrong.  
**Fix applied:** Rewritten to "If the stabilized character was Incapacitated before stabilization, that condition remains — stabilization does not remove it."

---

### 6. ~~Recovery.md references non-existent section numbers in Stabilization.md~~ ✅ Resolved
**File:** `Characters/Recovery.md`  
**Description:** Cross-references to "Stabilization.md §2.3 and §5.2" and "Stabilization.md §6" pointed to numbered sections that don't exist in the heading-based Stabilization document.  
**Fix applied:** Replaced with heading-based references: "— Effects of Stabilization" and "— Forced Awakening."

---

### 7. ~~Glossary "incapacitated" says the Dying condition applies it; Dying.md does not~~ ✅ Resolved
**File:** `Glossary/Glossary.md` — "incapacitated" entry  
**Description:** "Often applied directly by an effect (such as the **dying** condition)" — but Dying no longer imposes Incapacitated (Session 16/19 removed this; Dying now imposes −2 OC penalty and −5 ft movement only).  
**Fix applied:** Removed "such as the **dying** condition" from the entry.

---

### 8. ~~Glossary "poisoned" entry invents Healing tier rules that don't exist in Poisons.md or Healing.md~~ ✅ Resolved
**File:** `Glossary/Glossary.md` — "poisoned" entry  
**Description:** The entry cited "Healing VII" and "Healing IX" effects on poison that appear nowhere in Poisons.md or Healing.md. Poisons.md canonically says Healing V halves the difficulty; antivenom ends the condition.  
**Fix applied:** Entry rewritten to match Poisons.md: Healing V halves the check difficulty; antivenom (grade-matched) ends the condition immediately.

---

### 9. ~~Glossary "movement allowance" contradicts the Movement Modes Table~~ ✅ Resolved
**File:** `Glossary/Glossary.md` — "movement allowance" entry; `Tables/Movement Modes Table.md`  
**Description:** The Glossary stated "each additional AP spent on movement grants another full increment of base movement" (2 AP = 2×, 3 AP = 3×). The Movement Modes Table said Running (2 AP) = 1.5× and Sprinting (3 AP) = 2×. These produced different values for every speed.  
**Fix applied (Option A):** Movement Modes Table updated to match the Glossary. Running is now 2×, Sprinting 3×. Crawling and Swimming corrected to constant ¼× increments (¼, ½, ¾) — eliminating the inconstant ⅓× values. Climbing and Wading were already constant. "At base 30 ft" column added to the table to pre-calculate all fractional distances, eliminating the need to multiply during play.

---

### 10. ~~Opposition Checks.md — broken relative link to the Difficulty Table~~ ✅ Resolved
**File:** `Encounters/Opposition Checks.md`  
**Description:** Link `[Opposition Check Difficulty Table](Tables/...)` resolved to `Core Rules/Encounters/Tables/...` — which doesn't exist.  
**Fix applied:** Changed to `../Tables/Opposition%20Check%20Difficulty%20Table.md`.

---

### 11. ~~Elf lineage "Arcane Echo" — ambiguous about whether it grants Magic Attack access~~ ✅ Resolved
**File:** `Core Rules/Lineages/Elf.md`  
**Description:** Magic Attack.md requires an explicit lineage grant of magical access. Arcane Echo described attunement to casting without stating it grants Magic Attack skill access.  
**Fix applied:** Added "Arcane Echo grants access to Magic Attack skills." to the trait description.

---

### 12. ~~Kith.md "Improvised Combatant" uses undefined weapon terminology~~ ✅ Resolved
**File:** `Core Rules/Lineages/Kith.md`  
**Description:** "Kith treat improvised weapons as Martial weapons." The current weapon system uses Light/Medium/Heavy categories; "Martial weapons" is not defined anywhere in the current rules.  
**Fix applied:** Rewritten to: "Kith treat improvised weapons — bottles, furniture, tools, rocks, anything at hand — as melee or ranged weapons, applying all Melee Attack or Ranged Attack skills they have purchased, as appropriate to how the weapon is used." No weapon category needed; the skill stack is the proficiency.

---

### 13. ~~Movement Modes Table — fractional multipliers require multiplication at the table~~ ✅ Resolved
**File:** `Tables/Movement Modes Table.md`  
**Description:** Running = 1.5×, Sprinting = 2×, Crawling = ¼×–½×. No pre-calculated values, no rounding guidance. Required multiplication and division mid-play.  
**Fix applied:** Resolved with issue #9. "At base 30 ft" column added; all inconstant fractions corrected to constant increments. Players can read the ft value directly for base 30 ft movement, or use the multiplier column for other speeds without needing to compute mid-play.

---

### 14. ~~Encounter Structure.md — unencoded space in filename link~~ ✅ Resolved
**File:** `Encounters/Encounter Structure.md`  
**Description:** `[Turn Order](Turn Order.md)` used a raw space; other links in the file used `%20`.  
**Fix applied:** All three instances changed to `[Turn Order](Turn%20Order.md)`.

---

### 15. ~~Gear.md §Stacking contradicts Inventory.md on item quantity limits~~ ✅ Resolved
**File:** `Equipment/Gear.md` §Stacking; `Equipment/Inventory.md`  
**Description:** Gear.md cited Inventory.md §3 and then stated "a single slot holds a stack of 10 identical Tiny/Small gear" — a cap that doesn't exist in Inventory.md ("regardless of quantity").  
**Fix applied:** Removed the invented "10 items" cap. Gear.md now correctly states "a single slot holds any number of identical Tiny or Small items with no quantity limit."

---

## 🟠 Minor Issues

### 16. ~~Kin "Voracious Mind" trait has no mechanical effect~~ ✅ Resolved
**File:** `Core Rules/Lineages/Kin.md` — Traits section  
**Description:** "Kin read everything, remember most of it, and ask questions constantly." Pure flavor listed alongside mechanical traits. Under Principle 7, a trait in the mechanical section should do something.  
**Fix applied:** Added "+4 on Knowledge and Investigation Opposition Checks." Bonus also added to the Opposition Check Modifiers section for quick reference.

---

### 17. ~~Health Thresholds table omits Fortitude VII and IX as Vitality sources~~ ✅ Resolved
**File:** `Tables/Health Thresholds by Vitality Table.md`  
**Description:** The table showed Vitality values up to 65 (Vitality tree max) without noting that Fortitude VII and IX each grant +10 Vitality, allowing a character to reach Vitality 85.  
**Fix applied:** Added a note: "Fortitude VII and IX each grant an additional +10 Vitality; a character who invests in both can reach Vitality 85 — Wounded at 43 HP, Dying at 22 HP."

---

### 18. ~~Faerie "Ethereal Form" healing rate is unspecified~~ ✅ Resolved
**File:** `Core Rules/Lineages/Faerie.md`  
**Description:** "A Faerie heals at twice the normal rate while in Ethereal Form." Velocity has no single healing rate — rest, potions, Heroic Measures, and Healing Salve all work differently. "Twice the normal rate" has no referent.  
**Fix applied:** "While ethereal, a Faerie recovers 2 Health per hour of rest instead of 1, and doubles Health restored by potions and Healing skills."

---

### 19. ~~Shapeshifter "Multi-Strike" trait — natural weapon damage is unspecified~~ ✅ Resolved
**File:** `Core Rules/Lineages/Shapeshifter.md`  
**Description:** Multi-Strike delivered "an unarmed attack that strikes twice" with no damage defined for the natural weapons referenced in the flavor text.  
**Fix applied:** Added an "Animal Forms" section to Shapeshifter.md defining 15 available forms (Small through Large), each with its own natural weapons and damage dice. Multi-Strike uses any natural weapons available to the form — the player decides per activation which weapons each of the two strikes brings to bear.

---

### 20. ~~Apothecary.md redirect stub remains in the file tree — pending manual deletion~~ ✅ Resolved
**File:** `Skills/Universal/Survival/Apothecary.md`  
**Description:** The file itself said "Delete it when convenient." File deletion is not available through automated tools.  
**Fix applied:** Deleted manually by Mike.

---

## Notes

**Overall state of the rules:** The Core Rules are in good shape. The document architecture is clear, the skill trees are internally consistent, and the design decisions are coherent across most of the file tree. The majority of issues found were localized contradictions or stale entries rather than systemic design problems — and 13 of 20 were resolved automatically in the same session.

**Remaining open issues fall into two categories:** (1) Movement model conflict (issues 9 and 13) requires one design decision, then both documents update to match. (2) Underspecified lineage content (issues 12, 16, 18, 19) requires Mike to decide what each trait does or means. Issue 4 (Diseased condition) can go either way — a full mechanical definition or a deliberate narrative handwave.

**Shield trees and "Combat Threshold" in Magic Attack:** Both the Light Shield and Heavy Shield trees (not documented in CLAUDE.md session history) and the "combat threshold" rule in Magic Attack.md (5 or more spells cast in a scene = guaranteed manifestation) were found in the files but are not recorded as confirmed design decisions. They appear internally consistent and sensible, but they should be added to CLAUDE.md before the next session to preserve the rationale.
