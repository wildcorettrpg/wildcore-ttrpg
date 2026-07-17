---
name: core-rules-analysis
description: Run a Core Rules Analysis for the Velocity TTRPG project. Use this skill whenever the user says "run a Core Rules Analysis", "analyze the Core Rules", "check the Core Rules for issues", "do a rules review", or wants a systematic review of the Velocity TTRPG rules for correctness, completeness, cohesiveness, or design principle violations. Trigger even if the user phrases it casually ("give the core rules a pass", "check for issues in the rules", "what's wrong with the rules"). This skill reads all Core Rules files, compares them against the Eight Core Principles in the Design Philosophy, and produces a timestamped markdown report saved to the workspace root.
---

# Core Rules Analysis

This skill performs a systematic review of the Velocity TTRPG Core Rules and produces a timestamped markdown report. Run it whenever the user asks for a Core Rules Analysis.

This is an analysis-only skill. Do not auto-fix any issues found. Do not modify any files. Report findings only.

---

## Step 1 — Orient Yourself

Before reading anything, read `C:\Velocity TTRPG\CLAUDE.md`. It records:
- Resolved issues (do not re-flag these)
- Deliberate design decisions (do not flag these as violations)
- Session history and known deferred items

Then read the Eight Core Principles. They live in `C:\Velocity TTRPG - Coming Soon\Design Philosophy\Core Principles.md` if the Coming Soon folder is connected. If it is not, fall back to the "The Founding Eight" section in CLAUDE.md — the full list is reproduced there.

---

## Step 2 — Inventory and Read Core Rules Files

**File discovery:** Use bash to list all `.md` files under `C:\Velocity TTRPG\Core Rules\` recursively. This gives you the inventory of what exists. Use bash for directory traversal only.

**File reading:** Use the Read tool for all file content — not bash. The Read tool reads files directly and is reliable. Bash pipes (`cat`, `tail`, `wc -l`) can produce truncated or stale output through the workspace mount and must not be used to read or verify file content.

Read every file. Do not skim. The analysis is only as good as the reading.

Read files in this order, matching the current chapter structure:

1. `Characters/` — Attributes, Health, Skill Points, Traits, Modifiers, Effective Level, Starting Equipment
2. `Conditions and Hazards/` — Conditions, Environmental Hazards, Poisons, Dying, Death, Stabilization, Recovery
3. `Core Mechanics/` — Opposition Checks, Dice Pools
4. `Encounters/` — Encounter Structure, Turn Order, Turn Structure, Action Points, Actions, Free Actions, Reactions, Combat, Damage, Consciousness Checks, Movement
5. `Equipment/` — Armor, Weapons, Gear, Currency, Inventory
6. `Magic/` — Magic, Concentration
7. `Races/` — One file per race (Human, Dwarf, Elf, Faerie, Kin, Kith, Shapeshifter)
8. `Skills/Skills.md` and all files under `Skills/Universal/` and `Skills/Lineages/`
9. `Spells/` — Spells.md index, Level 0 through Level 9 Spells.md, Spells.csv
10. `Tables/` — all reference tables
11. `Creatures/` — Creatures.md index and individual creature files
12. `Introduction.md`, `Example of Play.md`
13. `Glossary/Glossary.md`

### Truncation verification protocol

The workspace mount can serve stale data. Before flagging any file as truncated or incomplete:

1. Read the file using the Read tool. Note the final lines returned.
2. If the file appears to end mid-sentence, mid-link, or mid-block: read it again using the Read tool with an `offset` set near the end of the file (e.g., if the file returned 90 lines, re-read with `offset: 80` to confirm what the file actually ends with).
3. If the Read tool confirms the file ends incompletely, flag it as a suspected truncation and include the exact final characters as evidence. Mark it as requiring manual verification in Obsidian before treating it as a confirmed finding.
4. Do not report a file as truncated until the user confirms it. The Read tool is more reliable than bash, but manual inspection in Obsidian is the authoritative check.

Never report a file as truncated based on bash output alone.

---

## Step 3 — Analyze for Issues

For each file and across files, evaluate the following. Take notes as you go.

### Correctness
- Does the rule describe something that works as stated?
- Are there internal contradictions within the file?
- Do cross-references point to files or sections that actually exist?
- Is terminology used consistently with the Glossary?
- Do numbers, dice, and formulas add up correctly?

### Completeness
- Does the rule mention mechanics it doesn't define?
- Are there gaps a player or Narrator would hit during actual play?
- Are there placeholder or stub sections that haven't been filled?
- Are there skills or abilities that reference items, conditions, or rules that don't exist elsewhere?
- Are all Markdown links valid? For every `[text](path.md)` or `[text](path.md#anchor)` link in the file, verify that the target file exists (resolve relative to the linking file's location) and, for anchored links, that the heading exists in that file. A link that resolves to a missing file or missing heading is a broken reference.
- Are standard terms linked on first use? The first occurrence of any condition (Bleeding Out, Dying, Wounded, Hindered, Unconscious, Prone, Stunned, Poisoned, Frightened, Nauseated, Vulnerable, Incapacitated, Mute, Blind, Deaf), mechanic (Opposition Check, Consciousness Check, Concentration, Stabilization, Effective Level), or named rule (Healer's Bag, Master Healer's Satchel, Bottomless Coinpurse) in a file should be linked to either the Glossary entry or the canonical definition in Core Rules — whichever is more specific. Subsequent uses within the same file do not need to be re-linked. Flag as Minor when a term is used without a link on its first appearance in a file.

### Cohesiveness
- Does this rule contradict rules in other files?
- Is terminology consistent across documents (e.g., same condition called different names)?
- Is the same mechanic defined in two places with different details?

### Core Principles Compliance
For every issue found, note which of the Eight Core Principles it violates, if any:

1. **Narrative First** — Every rule must serve the story. Friction without narrative purpose fails this.
2. **The Players Are the Stars** — Rules must not push player characters into the background.
3. **The Narrator Directs** — Rules provide tools; they must not override Narrator judgment.
4. **Get Out of the Way** — No rule should restrict what players may attempt.
5. **Eschew Systems Complexity** — No new subsystem when an existing one handles the problem.
6. **Ruthlessly Eliminate Unnecessary Math** — No multiplication, division, or sustained arithmetic during play. Exception: half damage and double damage are explicitly permitted and must not be flagged as violations.
7. **Rules Do Exactly What They Say** — No implied abilities, no universal inferences, no emergent effects.
8. **Horizontal Progression** — Characters grow in breadth, not power.

---

## Step 4 — Assign Severity

- 🔴 **Critical** — Breaks gameplay, undefined required mechanic, directly contradicts another rule, clear principle violation
- 🟡 **Significant** — Causes confusion, missing expected rule, terminology inconsistency that affects rulings, partial principle violation
- 🟠 **Minor** — Stale cross-reference, cosmetic terminology drift, missing link, style inconsistency with no gameplay impact

**Do not flag the following as issues — they are intentional design decisions documented in CLAUDE.md:**
- d20 terminology (weapon categories, spell levels, range values) — intentional compatibility
- Social attribute numbers being larger than combat numbers — intentional
- Armor mitigates damage only, does not affect hit chance — intentional
- No levels, no classes, no critical hits — intentional
- Bleeding Out as a standalone condition (not exclusively tied to Wounded) — intentional
- Reach property = 10 ft; default melee = 5 ft — intentional
- Long-range penalty is −2 — intentional
- Spellcasting V granting +1d10 to Consciousness Checks — intentional (learned resilience)
- Weapon damage one die tier above d20 SRD baseline — intentional
- Attacks cost 1 AP each with cumulative −2 multi-attack penalty — intentional
- Base AP 3 per turn, maximum 5 — intentional
- Half damage, double damage, and half [stat value] — permitted under Principle 6 exception
- Race/Lineage as two distinct systems — intentional
- Base races have no skill trees — intentional
- Social is a single unified 10-skill tree (not Dominance/Empathy branches) — intentional, final
- Anar-specific references in Core Rules — intentional (Anar is the default setting)

---

## Step 5 — Write the Report

Determine today's date. Save the report to:
```
C:\Velocity TTRPG\.analysis\Core Rules Analysis - YYYY-MM-DD.md
```
If a file with that date already exists, append `-2`, `-3`, etc. The `.analysis\` folder is excluded from git via `.gitignore`.

### Report Format

```markdown
# Core Rules Analysis — [DATE]

## Summary

| Severity | Count |
| :------- | ----: |
| 🔴 Critical | N |
| 🟡 Significant | N |
| 🟠 Minor | N |
| **Total** | **N** |

[One sentence framing note]

---

## Critical Issues

### CR-01 — [Title]

**File:** `path/to/file.md`
**Principle:** N (Principle Name)

[Description — quote conflicting text, name files, explain why it matters during play.]

**Resolution:** [What kind of action is needed — design decision, content restoration from git history, Mike's call. Do not provide a fix; describe what is required.]

---

## Significant Issues

### SG-01 — [Title]

**File:** `path/to/file.md`
**Principle:** N (Principle Name)

[Description]

**Resolution:** [What is needed]

---

## Minor Issues

### MN-01 — [Title]

**File:** `path/to/file.md`
**Principle:** N (if applicable)

[Description]

**Resolution:** [What is needed]
```

Issue IDs use the prefix CR-, SG-, or MN- followed by a two-digit number, numbered sequentially within each severity tier. If no issues exist at a given severity level, omit that section from the report entirely.
