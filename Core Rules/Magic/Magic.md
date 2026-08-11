# Magic

Magic is the ability to impose a supernatural will on reality. The specific tradition — wavebinding, glyphweaving, or whatever form magic takes in a given campaign setting — is defined by that setting's magic system. The mechanics here apply universally.

## Access

A character cannot cast spells unless something explicitly grants access to magical abilities: a lineage trait, an unlocked supernatural lineage, or a campaign setting rule. Access grants the ability to invest in the [Spellcasting](../Skills/Universal/Combat/Spellcasting%20Skill.md) skill tree. Spellcasting skills improve Spellcasting attack Opposition Checks and spell damage, and raise how much AP a caster can commit to a single cast.

## Learning Spells

Spells are not automatically known. A character with Spellcasting access can only cast spells they have specifically learned. Learning a spell requires encountering it in the world — through a spellbook, scroll, mentor, or other narrative source — and spending time studying it.

**Starting spells.** A new caster begins play knowing a small number of spells (typically 2–3), chosen in consultation with the Narrator and reflecting what's narratively available in the setting.

Any spell that costs AP to cast actively resists being learned. To learn one, the caster makes a Spellcasting Defense Opposition Check — built the same way as the [Spellcasting attack pool](../Core%20Mechanics/Dice%20Pools.md), applied here to withstand the spell's raw shape rather than to strike a target — against a difficulty based on the spell's Casting Time:

**Difficulty = 5 + (Casting Time × 1.5), rounded up.**

| Casting Time (AP) | Difficulty |
| :---: | :---: |
| 0 | No check required |
| 1 | 7 |
| 2 | 8 |
| 3 | 10 |
| 4 | 11 |
| 5 | 13 |
| 6 | 14 |
| 7 | 16 |
| 8 | 17 |
| 9 | 19 |
| 10 | 20 |
| 11 | 22 |
| 12 | 23 |

A spell with a Casting Time of 0 AP does not resist being learned at all — the character only needs to encounter it and spend the time studying it.

On a success, the spell is added to the character's repertoire. On a failure, the character may try again after at least 24 hours have passed.

**Attempting a spell without learning it.** A caster who attempts to cast a spell they have not learned triggers a Predation manifestation immediately, regardless of the current Predation Clock. Whether the spell produces its intended effect is the Narrator's call.

## Casting a Spell

Casting a spell costs AP equal to its Casting Time, paid at the moment of casting. Most spells cost 1 AP. A spell with a Casting Time of 0 AP is cast as a [Free Action](../Encounters/Free%20Actions.md) instead, at no AP cost — see [Potency and Charging](#potency-and-charging). The caster selects a spell they have learned, applies its effect, and subtracts from the Predation Clock (see below). If the spell requires an attack Opposition Check, the caster makes one before the effect is applied.

Some spells require sustained effort to maintain after they take effect — see [Concentration Spells](#concentration-spells). A caster may spend additional AP to charge a spell, or spend Health to overclock it — see [Potency and Charging](#potency-and-charging) and [Overclocking](#overclocking). Some spells cost more AP than a caster can spend in a single turn — see [Multi-Round Casting](#multi-round-casting).

## Spell Attacks

When a spell targets an unwilling creature, the caster makes a Spellcasting attack Opposition Check. The caster assembles a [Spellcasting attack pool](../Core%20Mechanics/Dice%20Pools.md) and the target responds with a defensive Opposition Check.

**Attacker:** [Spellcasting attack pool](../Core%20Mechanics/Dice%20Pools.md)  
**Defender:** see [Spell Defense](#spell-defense) below

If the caster's total exceeds the defender's total, the spell hits. On a hit, apply the spell's effect.

A successful defense Opposition Check does not automatically mean the target escapes unharmed. The spell's description defines what happens on a successful defense. If the spell specifies no outcome for a successful defense, the target is assumed to emerge unaffected.

Spells that do not target an unwilling creature — healing, utility, and buff spells — require no attack Opposition Check. Their effects apply automatically.

## Spell Defense

How a target resists a spell depends on the spell's type, as stated in the spell's description.

**Elemental spells** (fire, lightning, cold, acid, Elemental Force, and similar effects that produce a real physical phenomenon) can only be Dodged. Parry and Block cannot deflect magic. Standard Dodge rules apply, including the −2 restricted-space penalty and −4 prone penalty. A defender who cannot or chooses not to Dodge takes the hit automatically. **Armor mitigates elemental spell damage normally** — fire burns through what it touches, and armor reduces how much of that energy reaches the body beneath. Individual spells and abilities may specify that their elemental damage is unmitigated — when they do, the specific rule takes precedence over this default.

**Magical Force spells** (conjured weapons and effects comprised of raw supernatural energy) can only be Dodged. Armor provides no mitigation — there is nothing physical to block. A defender who cannot or chooses not to Dodge takes the full damage. Spells that deal Magical Force damage state **(unmitigated)** in their Damage line.

**Mind-affecting spells** (charm, compulsion, illusion, fear, and similar) are resisted with the defender's [Willpower pool](../Core%20Mechanics/Dice%20Pools.md). No physical defense can counter a spell that targets the mind; Parry and Block are unavailable. A defender who cannot make a Willpower check ([Stunned](../Conditions%20and%20Hazards/Conditions.md#stunned), [Unconscious](../Conditions%20and%20Hazards/Conditions.md#unconscious), [Incapacitated](../Conditions%20and%20Hazards/Conditions.md#incapacitated), or similar) takes the hit automatically.

A defender who cannot make any defensive Opposition Check — because they are [Vulnerable](../Conditions%20and%20Hazards/Conditions.md#vulnerable), unable to act or react, or lack the AP to pay for a defensive Reaction — takes the hit automatically. Armor mitigation still applies normally.

## Concentration Spells

Some spells require ongoing effort to maintain *after* they take effect. A spell with a Duration of *Concentration* costs **1 AP per round**, paid at the start of the caster's turn, to sustain its effect. If the caster does not pay or cannot pay the AP cost, the spell ends.

See [Concentration](Concentration.md) for full rules — Concentration Checks and stacking limits.

## Potency and Charging

A spell's description lists its numerical values — damage dice, healing dice, range, radius, duration, targets, declared amounts — at their base value, produced by casting the spell for exactly its base Casting Time and no more.

A caster may **charge** a spell by committing more AP to it than its base Casting Time. Charging is declared as a whole-number multiplier: casting at ×2 costs twice the spell's base Casting Time in AP, ×3 costs three times its base Casting Time, and so on. The declared multiplier applies to every numerical value in the spell's description. A spell with a 3 AP base Casting Time charged to ×2 costs 6 AP and doubles its effects; charged to ×3 it costs 9 AP and triples them.

There is no separate cap on charging beyond the AP economy itself. Base AP is 3 per turn, maximum 5 with skill investment (see [Action Points](../Encounters/Action%20Points.md)). If the AP a declared multiplier requires exceeds what the caster can spend in a single turn, the cast spills into [Multi-Round Casting](#multi-round-casting) — overcharging a spell should take longer, the same as any other cast too large to finish in one turn.

Bonus dice granted by attributes or skills (such as Willpower's bonus spell damage) are added after charging is applied — they are not themselves multiplied.

A spell with a Casting Time of 0 AP cannot be charged or overclocked. It always produces its base effect, cast as a Free Action, and never affects the Predation Clock.

## Overclocking

Casting normally trades power for time honestly — a heavily charged spell costs AP the caster could have spent moving, defending, or acting again, and a spell too large to finish in one turn costs the rounds it takes to complete. Overclocking breaks that trade. A caster may spend Health to reduce how much AP a cast still owes, finishing faster than it should take and keeping AP in hand — or finishing this round instead of needing another.

It is quietly, or not so quietly, considered reckless. Rasgard is said to have told generations of students there are almost always safer ways to accomplish something than magic — and overclocking is very much what he meant.

**Cost.** At the moment of casting — or, for a spell already in progress, on any round of its casting — the caster may declare a number of AP to shave off the amount still owed, down to a minimum of 1 AP paid that round. Each AP shaved costs Health and drains the Predation Clock, per the table below, **in addition to** the normal Predation subtraction for the AP actually spent.

| AP Shaved | Health Cost | Predation Penalty |
|:---:|:---:|:---:|
| 1 | 3 | −2 |
| 2 | 7 | −4 |
| 3 | 12 | −6 |
| 4 | 18 | −8 |
| 5 | 25 | −10 |
| 6 | 33 | −12 |
| 7 | 42 | −14 |
| 8 | 52 | −16 |
| 9 | 63 | −18 |

**Example.** A caster charges a spell to 3 AP (×3 effect), then overclocks it down to 1 AP — shaving 2. That costs 7 Health. The Predation Clock takes the normal −1 for the AP actually spent, plus the −4 penalty: **−5 total**, against a Clock that started the encounter at 25.

A caster may declare a shave larger than their current Health can pay. They pay everything they have — Current Health drops to 0.

This cost is never reduced by any Spellcasting tier or other skill or ability. Mastery does not make overclocking safer — it only makes a caster more capable of surviving having done it.

## Multi-Round Casting

Any cast — base or charged — whose total committed AP exceeds what the caster can spend in a single turn cannot be finished in one turn under ordinary circumstances. This can happen two ways: a small number of especially powerful spells simply have a base Casting Time greater than a caster's available AP, or a caster charges an otherwise-affordable spell to a multiplier whose AP cost outgrows their turn. Both are handled identically.

A spell like this is cast as a Concentration effect. Beginning the round the caster starts casting it, they commit AP toward the cast's total committed AP each of their turns — however much they choose to spend, up to what remains. Full Concentration rules apply throughout (see [Concentration](Concentration.md)): taking damage forces a Concentration Check, and failing it ends the casting immediately — the spell fizzles, nothing is refunded, and no effect occurs. Becoming [Stunned](../Conditions%20and%20Hazards/Conditions.md#stunned), [Unconscious](../Conditions%20and%20Hazards/Conditions.md#unconscious), or otherwise incapacitated ends it the same way. A caster cannot begin a second spell this way, or maintain any other Concentration effect, while one is already in progress.

Each round the caster commits AP toward the spell, the Predation Clock drains by that round's amount (see [Predation Clock](#predation-clock)) — a working this size announces itself for as long as it takes to finish.

When the caster's cumulative AP committed reaches the cast's full total — the spell's base Casting Time, or the higher AP cost of a declared charging multiplier — the effect resolves immediately, at the potency declared when casting began, and Concentration ends.

A caster may overclock the remaining balance on any round to finish early, at the same Health and Predation cost as overclocking a single-round spell (see [Overclocking](#overclocking)).

## Predation Clock

Every spell cast sends ripples through the magical field — and in some settings, something in those depths may notice.

**Tracking.** At the start of each encounter, the Narrator privately sets the Predation Clock to **25**. The Predation Clock is shared — every caster on the battlefield, friend and foe alike, draws from the same pool. Players do not track the Predation Clock.

**Casting.** Each time AP is spent casting a spell, subtract that amount from the Predation Clock. For an ordinary cast, this is the total AP spent at once (base plus any charging). For a spell cast across multiple rounds (see [Multi-Round Casting](#multi-round-casting)), this is the amount committed that round, subtracted each round it's worked on.

**Overclocking.** Overclocking a spell subtracts an additional penalty on top of the AP-based subtraction above — see [Overclocking](#overclocking).

**Concentration.** Maintaining a concentration spell *after* it has taken effect is channeling — the caster continues to draw on the magical field to sustain it. At the start of each of the caster's turns, subtract 1 from the Predation Clock for each concentration spell they are maintaining. Each maintained spell is a separate subtraction. A caster maintaining two concentration spells subtracts 2.

**Manifestation.** When the Predation Clock reaches 0, a hostile manifestation occurs — the Narrator determines what it is and where it appears. The manifestation targets the caster whose action triggered it. From that point forward, every draw on the magical field triggers an additional manifestation immediately: each spell cast, each round of AP committed to a multi-round cast, and each concentration spell maintained at the start of a caster's turn.

The campaign setting defines what specifically answers the call (e.g., Anar's Magesea predators). If the active campaign setting has no such mechanism, the Narrator may rule that the Predation Clock system does not apply.

## How to Read a Spell Entry

Each spell in the catalog uses the following fields:

- **Category** — the spell's functional type: Offense, Defense, Crowd Control, Healing, or Utility. A spell may have more than one category.
- **Casting Time** — the AP cost to cast the spell, before charging. Most spells cost 1 AP. A spell costing 0 AP is Minor — the simplest, most mundane spells in the catalog — and is cast as a Free Action; it cannot be charged or overclocked and never affects the Predation Clock. A spell costing more AP than the caster can spend in a single turn is cast across multiple rounds — see [Multi-Round Casting](#multi-round-casting).
- **Range** — maximum distance to the target. *Line of sight* means the caster must be able to see the target directly.
- **Target** — what or who the spell affects.
- **Damage** — the damage the spell deals on a hit at base (uncharged) potency, including damage type. Spells with no Damage line deal no damage directly. The tag **(unmitigated)** means armor provides no mitigation against this damage.
- **Duration** — how long the spell lasts, at base potency. *Instantaneous* means the effect occurs and ends immediately. *Concentration* means the caster must maintain the spell each round — see [Concentration Spells](#concentration-spells).
- **Defense** — how the target resists an attack spell. See [Spell Defense](#spell-defense). Spells with no Defense line do not allow a resistance roll.

All listed numerical values scale with charging — see [Potency and Charging](#potency-and-charging).

## The Sight Abilities

Far Sight, Long Sight, and True Sight are cross-race traits, not spells. They are innate perceptions — present from birth, requiring no Spellcasting investment, costing no AP, and contributing nothing to the Predation Clock. They cannot be learned, purchased, or trained.

Characters who possess one of these abilities are **God-touched**. See [Racial Traits](../Characters/Racial%20Traits.md#god-touched) for full rules on God-touched characters and the three Sight abilities.

## Available Spells

The spell catalog lists available spells by category. See [Spells](../Spells/Spells.md).

Campaign settings may add spells to the catalog. Spells listed in the Core Rules catalog are available in any setting unless a campaign setting explicitly restricts them.
