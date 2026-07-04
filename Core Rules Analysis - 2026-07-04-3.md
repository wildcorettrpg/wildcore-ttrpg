# Core Rules Analysis — 2026-07-04-3

## Summary

| Severity | Open | Resolved | Total |
| :------- | ---: | -------: | ----: |
| 🔴 Critical | 0 | 0 | 0 |
| 🟡 Significant | 0 | 1 | 1 |
| 🟠 Minor | 1 | 8 | 9 |
| **Total** | **1** | **9** | **10** |

Auto-fixable issues are marked ~~like this~~ when resolved. Issues requiring Mike's decision are marked ◆.

---

## 🟡 Significant Issues

---

### ~~SG-01 — Kin: Voracious Mind trait text contradicts the Opposition Check Modifiers~~

**File:** `Core Rules/Lineages/Kin.md`  
**Principle:** 7 — Rules Do Exactly What They Say  
**Auto-fix:** No — requires Mike's decision on which numbers are correct.

The Voracious Mind trait says: "+4 on Knowledge and Investigation Opposition Checks."

The Opposition Check Modifiers section says:
- "+2 on Investigation Opposition Checks (see Voracious Mind)."
- "+4 on Research Opposition Checks (see Voracious Mind)."

"Knowledge" is not a defined skill in Velocity — Research is the closest match. But the trait text "+4 on Knowledge AND Investigation" cannot reconcile with the Modifiers section's "+2 on Investigation, +4 on Research": if "Knowledge" = Research (giving +4), the "+4 on Investigation broadly" becomes "+2 on Investigation broadly," which the trait text doesn't say.

**Options for Mike:**

A. **Trait text is authoritative:** Kin get +4 to all Investigation Opposition Checks (a strong, broad bonus). Update the Modifiers section to: "+4 on all Investigation Opposition Checks (Forensics, Research, Supernatural Detection)." Remove the separate Research line.

B. **Modifiers section is authoritative:** Kin get +2 on general Investigation and a separate +4 on Research. Update the trait text to: "+2 on Investigation Opposition Checks and +4 on Research Opposition Checks." Replace "Knowledge" with "Research."

C. **Split bonus:** Kin get +4 on Research specifically and +2 on all other Investigation checks (Forensics, Supernatural Detection). This is what the Modifiers imply. Update the trait text to match option B.

Option B/C is mechanically the same; the difference is whether the +4 stacks on top of the +2 when making a Research check (giving a character with both Investigation I and Voracious Mind +1+2+4=+7 on Research) or replaces it.

**Status:** ✅ Resolved — Mike updated the trait text to "+2 on Investigation Opposition Checks, and +4 on Research Opposition Checks," matching the Modifiers section exactly.

---

## 🟠 Minor Issues

---

### ~~MN-01 — Unconscious condition omits Prone; Movement.md states Unconscious = Prone~~

**Files:** `Encounters/Conditions.md`, `Encounters/Movement.md`  
**Principle:** 7 — Rules Do Exactly What They Say  
**Auto-fix:** ✅

`Movement.md` §Movement and Conditions item 4 states: "**Unconscious:** The participant is prone and cannot move at all — Unconscious's own restrictions are stricter than Incapacitated's and control."

The Unconscious entry in `Conditions.md` says the character "is Incapacitated" but never states they are Prone or that they cannot move. A player reading Conditions.md alone would see Incapacitated (which allows crawling) and miss the stricter Unconscious movement restriction entirely.

**Fix:** Add explicit Prone and no-movement language to the Unconscious condition in Conditions.md.

**Status:** ✅ Resolved — Unconscious condition updated.

---

### ~~MN-02 — "Standard treatment difficulty" is undefined~~

**Files:** `Skills/Universal/Survival/Healing.md`, `Characters/Recovery.md`  
**Principle:** 7 — Rules Do Exactly What They Say  
**Auto-fix:** ✅

Healing.md Note 4 reads: "The Opposition Check difficulty is the **standard treatment difficulty** + 4." Healing X references the same term. Recovery.md §3 reproduces it: "On a successful Opposition Check (standard difficulty +4)."

No document defines what "standard treatment difficulty" is. The term is used twice with no referent. A Narrator hitting this mid-session has nothing to work from.

**Fix:** Replace "standard treatment difficulty" with "a Narrator-assigned difficulty based on the severity of the patient's injuries (typically Challenging, 8–13, for Wounded characters; Dangerous, 14–16, for Dying characters — see the [Opposition Check Difficulty Table](../Tables/Opposition Check Difficulty Table.md))." Apply the same language to Recovery.md §3.

**Status:** ✅ Resolved.

---

### ~~MN-03 — Poisons.md Note 3 contradicts Drow Poison's timing~~

**File:** `Encounters/Poisons.md`  
**Principle:** 7 — Rules Do Exactly What They Say  
**Auto-fix:** ✅

Note 3 states: "Special conditions listed in the Notes column (Unconscious, Incapacitated, Blind) **apply immediately on exposure** and last until the poison ends, unless a specific removal condition is stated."

Drow Poison says: "**On the first failed check**, the character is also Unconscious; they wake if they take damage or are forcibly roused."

Drow Poison explicitly defers Unconscious until a check is failed — not immediately on exposure. Note 3's blanket "immediately on exposure" directly contradicts this.

**Fix:** Update Note 3 to: "Special conditions listed in the Notes column apply as stated in each entry. When no trigger is specified, the condition applies immediately on exposure and lasts until the poison ends."

**Status:** ✅ Resolved.

---

### ~~MN-04 — Movement.md §Engagement contradicts the Glossary's Opportunity Attack definition~~

**File:** `Encounters/Movement.md`  
**Principle:** 7 — Rules Do Exactly What They Say  
**Auto-fix:** ✅

`Movement.md` §Engagement, item 3: "Moving out of melee range **may trigger a reaction if an opponent has an ability that allows it**."

The Glossary's "opportunity attack" entry defines it as: "A **Reaction** triggered when an opponent moves out of melee range. The triggering character may immediately make a melee attack against the departing opponent." — no special ability required, available to any character with AP.

The Movement.md language implies opportunity attacks are ability-gated; the Glossary says they are universal Reactions available to everyone. These directly contradict each other.

**Fix:** Update Movement.md §Engagement item 3 to: "Moving out of melee range may trigger an Opportunity Attack from any opponent who has AP available — see **opportunity attack** in the Glossary."

**Status:** ✅ Resolved.

---

### ~~MN-05 — Shapeshifter Keen Senses grants no stated bonus in the trait text; +2 appears only in Modifiers~~

**File:** `Core Rules/Lineages/Shapeshifter.md`  
**Principle:** 7 — Rules Do Exactly What They Say  
**Auto-fix:** ✅

Keen Senses reads: "A Shapeshifter's inner animal sharpens every sense they carry in human form. Within 30 ft., their sight, hearing, smell, taste, and touch exceed what any purely human person can perceive."

No mechanical bonus is stated. The Opposition Check Modifiers section lists "+2 on all perception-based Opposition Checks relying on the physical senses within 30 ft." but provides no link back to the trait that grants it.

**Fix:** Add "+2 to perception-based Opposition Checks within 30 ft." to the Keen Senses trait text.

**Status:** ✅ Resolved.

---

### ~~MN-06 — Faerie.md Lightborne Step has a broken relative link~~

**File:** `Core Rules/Lineages/Faerie.md`  
**Principle:** 7 (completeness — broken cross-reference)  
**Auto-fix:** ✅

Lightborne Step links to `../Movement.md#difficult-terrain`. From `Core Rules/Lineages/`, this resolves to `Core Rules/Movement.md` — a file that does not exist. The correct path is `../Encounters/Movement.md#difficult-terrain`.

**Fix:** Update the link in Lightborne Step to `../Encounters/Movement.md#difficult-terrain`.

**Status:** ✅ Resolved.

---

### ~~MN-07 — Faerie "+2 on Opposition Checks to detect or resist deception" has no trait source~~

**File:** `Core Rules/Lineages/Faerie.md`  
**Principle:** 7 — Rules Do Exactly What They Say  
**Auto-fix:** No — requires Mike's decision.

The Opposition Check Modifiers section includes: "+2 on Opposition Checks to detect or resist deception, lies, or manipulation." None of Faerie's five traits (Luminous, Incapable of Deception, Sense Truth, Ethereal Form, Lightborne Step) grants this bonus. It is an orphaned modifier with no mechanical source.

Sense Truth (passive detection of sincere vs. deliberate statements) could plausibly be the source, but the trait text grants no numerical bonus — it's an always-on qualitative ability.

**Options for Mike:**

A. **Add +2 to Sense Truth:** "Within 10 ft., Faeries know whether what a speaker is saying is sincere. +2 to Opposition Checks to detect or resist deception, lies, or manipulation."

B. **Remove the orphaned modifier:** Delete the "+2 on Opposition Checks to detect or resist deception" line from the Modifiers section.

**Status:** ✅ Resolved — Mike added the bonus to Sense Truth with a range split: "+2 on Opposition Checks to detect or resist deception... Automatic success when within 10 feet." Modifiers section updated to match both tiers.

---

### ~~MN-08 — Movement Modes Table contains internal session-history notes~~

**File:** `Core Rules/Tables/Movement Modes Table.md`  
**Principle:** N/A — publication quality  
**Auto-fix:** ✅

Notes 2 and 3 in this table document decisions made in prior sessions (removing "Weakened," removing Concentration penalties), presented as gameplay content:

> Note 2: **"Weakened"** has been removed from the Swimming rows...
> Note 3: **Resolved 2026-06-21:** this table previously listed Concentration penalties...

These are session-history tracking notes, not gameplay rules. They belong in CLAUDE.md, not a published Core Rules reference table.

Note 1 (Vulnerable definition) and Note 4 (table is a reference, not a new rule) are legitimate gameplay notes and should be kept.

**Fix:** Remove Notes 2 and 3. Renumber remaining notes: current Note 4 ("This table is a reference...") becomes Note 2.

**Status:** ✅ Resolved.

---

### ~~MN-09 — Turn Structure.md "Martial Actions / Supernatural Actions" disconnected from "Standard Actions" umbrella~~

**File:** `Encounters/Turn Structure.md`  
**Principle:** 7 — Rules Do Exactly What They Say (cohesiveness)  
**Auto-fix:** ✅

Turn Structure.md §Action Types lists "Martial Actions" and "Supernatural Actions" as top-level action categories with no mention that both are subtypes of Standard Actions. Combat.md §Action Points calls the same category "Standard actions (attacks, abilities, maneuvers)." The Glossary correctly defines both "martial action" and "supernatural action" as subtypes of Standard Actions — but Turn Structure.md presents them as if they are the primary categories, leaving readers who don't cross-reference the Glossary without the full picture.

**Fix:** Add "(a Standard Action)" after "Martial Actions" and "Supernatural Actions" in the Action Types list, linking to the Glossary entries.

**Status:** ✅ Resolved.

---

## CLAUDE.md Maintenance Items

The following items are not Core Rules correctness issues but are stale entries in CLAUDE.md that should be updated to match the current state of the rules:

1. **Light Shield and Heavy Shield skill trees are missing from the Universal Skill Trees inventory.** Both are full 5-skill trees, fully defined in `Skills/Universal/Combat/Light Shield.md` and `Heavy Shield.md`, listed in `Skills/Skills.md`, and referenced in `Equipment/Armor.md`. The CLAUDE.md inventory under "Universal Skill Trees" does not mention them.

2. **Healer's Bag description is stale.** CLAUDE.md still describes it as "10 charges, 1d6 + Willpower per charge" — the design was revised to a slot-based container (5 slots, 5 items per slot) with no charges. The healing amounts now depend on which items are inside the bag. `Healing.md`, `Gear.md`, and `Recovery.md` all reflect the new model.

These were already flagged in the -2 report's "Intentional Design Decisions" section. Both are auto-fixed in this pass.

---

## Intentional Design Decisions — Not Flagged

- d20 terminology (spell levels, weapon categories, opportunity attacks) — intentional compatibility goal
- Social attribute numbers larger than combat numbers — cinema-first, relationship-driven design
- Armor mitigates damage only — core design principle
- No critical hits, no fumbles — Narrator handles exceptional outcomes narratively
- Attacks cost 1 AP with cumulative −2 multi-attack penalty — intentional
- Base AP 3 per turn, maximum 5 — intentional
- Magic Attack V granting +1d10 to Consciousness Checks — intentional (learned resilience)
- Weapon damage one die tier above d20 SRD baseline — intentional
- Vitality is not creation-assignable — intentional
- Light Shield V and Heavy Shield V sharing the name "Shield Bash" with different effects — intentional; each tree's flavor and fiction differs (deflection vs. brute force)
- Both Elf (Arcane Echo) and Kin (Innate Magic) granting Magic Attack I for free — intentional; two different lore paths to the same mechanical grant
- Faerie cannot receive a ≥1 Health/round Bleeding Out tick in Ethereal Form because they can't be physically harmed in that form — this is consistent, not a gap; the condition is applied by the Wounded trigger and the fiction resolves naturally

---

*Report generated by Core Rules Analysis skill. Session 23 — 2026-07-04.*
