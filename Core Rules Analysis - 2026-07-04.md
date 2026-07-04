# Core Rules Analysis — 2026-07-04

## Summary

| Severity | Open | Resolved | Total |
| :------- | ---: | -------: | ----: |
| 🔴 Critical | 0 | 2 | 2 |
| 🟡 Significant | 0 | 7 | 7 |
| 🟠 Minor | 0 | 8 | 8 |
| **Total** | **0** | **17** | **17** |

Issues marked ~~like this~~ were corrected automatically on 2026-07-04. Issues without strikethrough require a design decision before they can be fixed.

---

## 🔴 Critical Issues

---

### ~~CR-01 — Consciousness Check triggers after stabilization are contradictory~~

**Files:** `Characters/Dying.md`, `Characters/Stabilization.md`, `Glossary/Glossary.md`, `Characters/Health.md`, `Encounters/Conditions.md`, `Encounters/Combat.md`, `Glossary/Glossary.md`, `Equipment/Gear.md`  
**Principle:** 7 — Rules Do Exactly What They Say  
**Status:** ✅ Resolved — Mike revised Dying.md and Stabilization.md directly, establishing the canonical model: Wounded begins Bleeding Out; if not stabilized, Bleeding Out can drop a character into Dying; Consciousness Checks are triggered by the Dying condition (three triggers: entering Dying, taking damage while Dying, losing Health from Bleeding Out while Dying); stabilization ends Bleeding Out and therefore ends all Consciousness Checks (Stabilization.md §11). All downstream documents updated to match:
- `Characters/Health.md` §4: "Consciousness Checks on incoming damage" expanded to list all three triggers.
- `Encounters/Conditions.md` "Bleeding Out" Effect: reframed — Bleeding Out that drops a character into Dying causes entry into the Dying condition; if already Dying, a CC is triggered. Ends clause now includes "healing above the wounded threshold."
- `Encounters/Conditions.md` "Vulnerable" Trigger: "Forced Awakening" removed — Stabilization.md §Forced Awakening lists only Prone and Hindered, not Vulnerable.
- `Encounters/Combat.md` §Opening: "Element of Surprise" → "Surprise"; §5 → §4 (stale reference from MN-07, missed in the earlier pass).
- `Encounters/Combat.md` "Dying and Death": CC trigger description expanded to all three triggers.
- `Glossary/Glossary.md` "bleeding out": revised framing — CC is triggered by the Dying condition when the character loses Health from Bleeding Out; the old note about CC being triggered "independently of Bleeding Out" removed.
- `Glossary/Glossary.md` "forced awakening": Vulnerable removed from imposed conditions.
- `Equipment/Gear.md` Smelling Salts: Vulnerable removed from imposed conditions.

---

### ~~CR-02 — Opposition Checks.md "Intense Concentration" section contradicts the rest of the system~~

**Files:** `Encounters/Opposition Checks.md`, `Encounters/Concentration.md`, `Encounters/Conditions.md`, `Glossary/Glossary.md`  
**Principle:** 4 — Get Out of the Way; 7 — Rules Do Exactly What They Say  
**Status:** ✅ Resolved — removed "cannot initiate physical actions" line from Opposition Checks.md.

Opposition Checks.md contained a section on Intense Concentration that included the line: the character "cannot initiate physical actions until the concentration ends."

This contradicted every other authoritative source in the system:
- `Concentration.md` §4.1: "A participant may take actions while concentrating unless the effect specifies otherwise."
- `Concentration.md` §3.3: "Intense Concentration does not restrict movement."
- `Glossary/Glossary.md` "intense concentration" entry: "Intense Concentration does not restrict movement."
- `Glossary/Glossary.md` "vulnerable" entry: no action restriction listed.
- CLAUDE.md design decision (confirmed): "Movement is not restricted."

The Vulnerable condition — which Intense Concentration applies — only removes Reflex from defense rolls. It does not prohibit actions.

---

## 🟡 Significant Issues

---

### ~~SG-01 — Panther damage is 1d8 in Shapeshifter.md, violating the CLAUDE.md design decision~~

**Files:** `Lineages/Shapeshifter.md`  
**Principle:** 7 — Rules Do Exactly What They Say  
**Status:** ✅ Resolved — Panther claws and bite corrected to 1d10 each.

CLAUDE.md (Session 21) explicitly states: "Medium forms: 1d8 (light, e.g. Otter), 1d10 (standard, e.g. Panther)." The Animal Forms table had Panther at 1d8/1d8, identical to Otter. Corrected to match the design decision and the established pattern of Wolf (1d10) and Wild Boar (1d10).

---

### ~~SG-02 — Smelling Salts in Gear.md contradicts the Forced Awakening rules~~

**Files:** `Equipment/Gear.md`, `Characters/Stabilization.md`, `Glossary/Glossary.md`  
**Principle:** 7 — Rules Do Exactly What They Say  
**Status:** ✅ Resolved — Smelling Salts entry in Gear.md rewritten to match Stabilization.md §Forced Awakening (Healing II prerequisite, 1 AP, once per patient per incident, Prone + Hindered + Vulnerable imposed). The "chemical action" paragraph above the table updated to note that smelling salts carry additional restrictions.

---

### ~~SG-03 — Combat.md node document is missing Light Shield and Heavy Shield from its Branches list~~

**Files:** `Skills/Universal/Combat/Combat.md`, `Skills/Skills.md`  
**Principle:** 7 — Rules Do Exactly What They Say  
**Status:** ✅ Resolved — Light Shield (9) and Heavy Shield (10) added to the Branches list in Combat.md.

---

### ~~SG-04 — Elf lineage references undefined skill check types~~

**Files:** `Lineages/Elf.md`  
**Principle:** 7 — Rules Do Exactly What They Say  
**Status:** ✅ Resolved — Elf.md was updated (by Mike, outside this analysis session) to replace the undefined "History and Lore" and "Cosmology" check types with defined categories: Research Opposition Checks, Supernatural Opposition Checks, and Intimidation Opposition Checks. All three map to existing skill trees.

---

### ~~SG-05 — Multiple lineages have Opposition Check Modifiers with no granting trait~~

**Files:** `Lineages/Dwarf.md`, `Lineages/Kith.md`, `Lineages/Kin.md`, `Lineages/Shapeshifter.md`, `Lineages/Faerie.md`  
**Principle:** 7 — Rules Do Exactly What They Say

Across five lineages, modifiers appear in the Opposition Check Modifiers section that are not granted by, or even implied by, any listed trait:

| Lineage | Orphaned Modifier | Traits Listed |
| :------ | :---------------- | :------------ |
| Dwarf | +2 Athletics | Fearless, Low Center of Gravity |
| Dwarf | +2 Fortitude | Fearless, Low Center of Gravity |
| Kith | +2 Fortitude | Improvised Combatant, Terrain Mastery, Wallcrawler |
| Kin | +2 Research | Voracious Mind (+4 Knowledge/Investigation), Innate Magic |
| Kin | +2 Social | Voracious Mind, Innate Magic |
| Shapeshifter | +2 Fortitude | Keen Senses, Low-Light Vision, Mindspeech, Multi-Strike |
| Faerie | +2 to move silently | Luminous, Incapable of Deception, Sense Truth, Ethereal Form |
| Faerie | +2 to resist magical effects | (same) |

A modifier with no named granting trait has no rules basis — the player cannot tell where it comes from, whether it stacks with skill bonuses, or why the lineage has it.

Note: Kith's "+2 on attack Opposition Checks when exploiting terrain features" is correctly tied to Terrain Mastery. Kin's "+2 Magic Attack" is justifiable from Innate Magic's "exceptional aptitude" language. Those are not flagged.

**Resolution needed:** For each orphaned modifier, either (a) add a trait that grants it, (b) incorporate it into an existing trait's description, or (c) remove it if it's narratively unjustified.

**Status:** ✅ Resolved — all five lineages updated. Kith and Faerie were already clean. Dwarf modifiers now exactly mirror trait/flaw text. Shapeshifter gained an "Inner Animal" trait explicitly granting the Fortitude bonus; Low-Light Vision now states its Perception modifier inline. Kin gained a "Gregarious Nature" trait granting the +2 Social bonus; Innate Magic now explicitly states its +2 Magic Attack bonus. All modifiers across all five lineages are traceable to a named trait or flaw.

---

### ~~SG-06 — Serrated arrows impose Bleeding Out independently of the Wounded condition~~

**Files:** `Equipment/Weapons.md`  
**Principle:** 7 — Rules Do Exactly What They Say

Weapons.md Special Ammunition section: Arrows, serrated — "On a hit, the target gains the Bleeding Out condition."

The Glossary defines Bleeding Out as "The ongoing Health loss suffered by a **Wounded** character." The Wounded condition section in Dying.md establishes that Bleeding Out begins when a character enters Wounded. The system's entire Bleeding Out → Stabilization chain assumes the character is at or below their Wounded threshold.

Serrated arrows allow a character to be Bleeding Out at full Health. This creates undefined interactions:
- Does a healthy character (not Wounded or Dying) make Consciousness Checks from the Bleeding Out damage?
- Does stabilization end the serrated-arrow Bleeding Out, or only the Wounded-triggered one?
- Can a character be stabilized against serrated-arrow Bleeding Out if they never entered Wounded?

This may be intentional (serrated arrows are supposed to cause bleeding independently), but if so the rules need to address how Bleeding Out from this source interacts with the Wounded/Dying/Stabilization chain.

**Resolution needed:** Either (a) clarify in Weapons.md (or a separate section) how serrated-arrow Bleeding Out interacts with Wounded, Dying, and Stabilization, or (b) change the effect to trigger only when the target is already at or below their Wounded threshold.

**Status:** ✅ Resolved — the revised Dying/Bleeding Out model separates Bleeding Out (a health-loss mechanism) from Consciousness Checks (a Dying-condition trigger). A character bleeding out from a serrated arrow at full health loses 1 HP/round but makes no CC until they cross into Dying; all CC triggers are now defined by Dying.md. Stabilization ends Bleeding Out regardless of source; for characters not yet Wounded, bandages (Gear.md) provide an equivalent tool. The root ambiguity is resolved.

---

### ~~SG-07 — Vitality.md Note 2 omits Universal Attribute skills as sources of bonus Vitality~~

**Files:** `Skills/Universal/Attributes/Vitality.md`, `Tables/Health Thresholds by Vitality Table.md`  
**Principle:** 7 — Rules Do Exactly What They Say  
**Status:** ✅ Resolved — Vitality.md Note 2 updated to: "Universal attribute skills (Fortitude VII and IX, +10 Vitality each) and lineage skills may increase Vitality beyond the values achievable through this tree alone."

---

## 🟠 Minor Issues

---

### ~~MN-01 — Base Movement Rates by Lineage Table is stale for Shapeshifter~~

**File:** `Tables/Base Movement Rates by Lineage Table.md`  
**Status:** ✅ Resolved — Shapeshifter row updated to reference `Lineages/Shapeshifter.md` §Animal Forms.

---

### ~~MN-02 — Shield Bash damage notation is ambiguous~~

**Files:** `Skills/Universal/Combat/Light Shield.md`, `Skills/Universal/Combat/Heavy Shield.md`  
**Status:** ✅ Resolved — both Shield Bash entries rewritten to explicitly state "flat Strength bonus (minimum 1)" parallel to unarmed attack language, with a note that the Strength attribute damage bonus (1 die per 3 points, per Damage §3) applies normally on top.

---

### ~~MN-03 — Opposition Checks.md uses wrong relative path for Attribute Pairings table link~~

**File:** `Encounters/Opposition Checks.md`  
**Status:** ✅ Resolved — path corrected to `../Tables/Attribute%20Parings%20for%20Opposition%20Checks%20Table.md`.

---

### ~~MN-04 — Environmental Hazards.md link is malformed and references a non-existent section~~

**File:** `Encounters/Environmental Hazards.md`  
**Status:** ✅ Resolved — space encoded as `%20`; bogus `§4` fragment removed.

---

### ~~MN-05 — Glossary "vitality" entry uses circular language~~

**File:** `Glossary/Glossary.md`  
**Status:** ✅ Resolved — entry rewritten to specify actual mechanisms: Vitality skill tree, Fortitude VII/IX, lineage abilities, or other explicitly stated effects.

---

### ~~MN-06 — Glossary "bleeding out" entry implies it is the only Consciousness Check trigger~~

**File:** `Glossary/Glossary.md`  
**Status:** ✅ Resolved — entry rewritten (twice: first pass added a cross-reference; second pass as part of CR-01 resolution revised the framing to correctly attribute CC to the Dying condition rather than to Bleeding Out as a cause).

---

### ~~MN-07 — Encounter Structure.md and Glossary use "Element of Surprise"; Turn Order.md heading is "Surprise"~~

**Files:** `Encounters/Encounter Structure.md`, `Glossary/Glossary.md`, `Encounters/Turn Order.md`  
**Status:** ✅ Resolved — standardized on "Surprise" throughout: Encounter Structure.md body text updated from "Element of Surprise" to "Surprise" (section reference corrected from §5 to §4); Glossary entry renamed from "element of surprise" to "surprise".

---

### ~~MN-08 — Grammatical error in Glossary "nauseated" entry~~

**File:** `Glossary/Glossary.md`  
**Status:** ✅ Resolved — "an Healing check" corrected to "a Healing check."

---

## Intentional Design Decisions — Not Flagged

The following were noted during the review and confirmed as intentional per CLAUDE.md. They are recorded here to distinguish them from oversights:

- **d20 terminology** (spell levels, weapon categories Simple/Martial/Exotic, range values) — intentional compatibility goal
- **Social numbers are larger than combat numbers** — reflects cinema-first, relationship-driven priorities
- **Armor mitigates damage only, does not affect hit chance** — core design principle
- **No critical hits, no fumbles** — intentional; Narrator handles exceptional outcomes narratively
- **Attacks cost 1 AP with cumulative −2 multi-attack penalty** — intentional; flat attack bonuses offset this
- **Base AP 3 per turn, maximum 5** — intentional
- **Magic Attack V granting +1d10 to Consciousness Checks** — intentional "learned resilience"
- **Weapon damage one die tier above d20 SRD baseline** — intentional
- **Vitality is not creation-assignable** — intentional
- **Strength skill tree (VII/IX) adds damage dice to melee only, not ranged** — intentional melee specialization; Strength attribute bonus already applies to both
- **Human Eye for Value trait says "+4" while modifiers section lists "+2 Investigation, +2 Negotiation"** — these describe the same bonus in two levels of specificity (trait = narrative framing; modifiers = mechanical implementation). Not a contradiction.

---

*Report generated by Core Rules Analysis skill. Session 22 — 2026-07-04.*
