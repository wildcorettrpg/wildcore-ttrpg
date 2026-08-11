Here's the full list, organized by what kind of decision each one is.

**Overclocking table doesn't cover its main use case.** This is the most important gap. The table only goes to 4 AP shaved (Health 18, Predation −8), but the whole reason Overclocking exists now is to compress large multi-round rituals — a 9–12 AP spell overclocked down to something castable in one turn could mean shaving 8–11 AP, well past what the table defines. Either the table needs to extend a lot further, or the cost needs to become a formula instead of a lookup table. Worth running the math on whether overclocking a big ritual down is even survivable for a 20–30 Health character before locking numbers in — that's the scenario the mechanic was built for, and it's never actually been checked.

**Design decisions still genuinely open:**

Whether a "Minor" spell category exists — small utility tricks that never touch the Predation Clock at all. I dropped it from the draft since you never confirmed it, which means as written, every single cast, however trivial, drains at least 1 Predation. That's a real design stance (all magic is meaningfully dangerous, full stop) rather than an oversight, but worth confirming it's the one you want.

Whether Overclocking requires a minimum Spellcasting tier to attempt at all, or is available to a first-session novice exactly as readily as a master. I asked this a few turns back and we moved straight to the AP math without settling it. The "cost is never reduced by tier" rule is already locked in — this is the separate question of access, not cost.

Whether multi-round casting has a minimum AP commitment per round, or a caster can trickle 1 AP per turn indefinitely to keep exposure low each round while stretching a ritual out. The Concentration Check interruption mechanism makes slow pacing somewhat self-limiting in practice (more rounds = more chances to get hit and lose the whole thing), but the document never states that as an intentional design choice.

Whether Willpower's bonus spell damage dice get multiplied by charging, or added afterward unmultiplied. I assumed the latter and wrote the doc that way, but it's my call, not yours.

**Numbers still placeholder, not confirmed final:**

Learning-spell difficulty flattened to a single Challenging check for every spell, replacing the old level-scaled table. Starting spell count set to "typically 2–3." The Overclocking table itself (Health cost and Predation penalty per AP shaved) was explicitly a first pass, never confirmed as final even within its current range.

**Downstream work blocked on Magic.md being locked:**

`Spellcasting Skill.md` — I drafted a tier rewrite for this several turns ago, but it's now stale; it referenced a dice-based overcharge system that no longer exists after the AP-charging redesign. Needs a full new pass once Magic.md is final.

`Spells.md` — the index table is still organized by Level × Category and needs rebuilding by Category alone.

The `Level 0 Spells.md`–`Level 9 Spells.md` files themselves — need reorganizing (by category or some other scheme), every entry needs its Level and Casting Cost fields removed, and every entry needs a real Casting Time (AP) value assigned, including deciding actual AP costs for what used to be the high-level spells. Elemental Bolt specifically needs its nine near-duplicate entries collapsed into one.

**Minor clarity gaps, low priority:** the document doesn't explicitly say a caster can't overclock for more Health than they currently have — this probably just falls out of the existing Health rules (you can't spend what you don't have, and a big overclock can trigger a Consciousness Check or even kill you like any other Health loss) but it's worth a one-line statement for clarity rather than leaving it implied. `Concentration.md` also doesn't currently cross-reference Multi-Round Casting, which would help discoverability even though it's not strictly required.