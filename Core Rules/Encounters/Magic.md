# Magic

Magic is the ability to impose a supernatural will on reality. The specific tradition — wavebinding, glyphweaving, or whatever form magic takes in a given campaign setting — is defined by that setting's magic system. The mechanics here apply universally.

## Access

A character cannot cast spells unless something explicitly grants access to magical abilities: a lineage trait, an unlocked supernatural lineage, or a campaign setting rule. Access grants the ability to invest in the [Spellcasting](../Skills/Universal/Combat/Spellcasting%20Skill.md) skill tree. Spellcasting skills unlock spell levels and improve Spellcasting attack Opposition Checks and spell damage.

## Learning Spells

Spells are not automatically known. A character with Spellcasting access can only cast spells they have specifically learned. Learning a spell requires encountering it in the world — through a spellbook, scroll, mentor, or other narrative source — and spending time studying it.

**Starting spells.** A new caster begins play knowing all Level 0 spells (cantrips) and one spell from each spell level their Spellcasting tier unlocks. Starting spells are chosen in consultation with the Narrator and should reflect what is narratively available in the setting.

To learn a spell, the character makes a Research Opposition Check against a difficulty based on the spell's level:

| Spell Level | Difficulty |
| :---: | :--- |
| 1–2 | Challenging |
| 3–4 | Dangerous |
| 5–9 | Extreme |

On a success, the spell is added to the character's repertoire. On a failure, the character may try again after at least 24 hours have passed.

A character may learn a spell at any level, even one above their current Spellcasting tier. They cannot cast it until they unlock the appropriate tier, but they may study and prepare it in advance.

**Attempting a spell without learning it.** A caster who attempts to cast a spell they have not learned triggers a Predation manifestation immediately, regardless of the current Predation Difficulty. Whether the spell produces its intended effect is the Narrator's call.

## Casting a Spell

Casting a spell costs **1 AP**. The caster selects a spell they have access to (based on their Spellcasting tier), pays the Health cost immediately, and applies the effect. If the spell requires an attack Opposition Check, the caster makes one before the effect is applied.

Some spells require sustained effort — see [Concentration Spells](#concentration-spells).

## Spell Attacks

When a spell targets an unwilling creature, the caster makes a Spellcasting attack Opposition Check. The caster's dice pool comes from Spellcasting skills that explicitly grant dice to the roll, plus a flat bonus from Willpower and any applicable flat skill bonuses. The target responds with a defensive Opposition Check.

**Attacker:** Spellcasting dice pool + Willpower  
**Defender:** see [Spell Defense](#spell-defense) below

If the caster's total exceeds the defender's total, the spell hits. On a hit, apply the spell's effect.

A successful defense Opposition Check does not automatically mean the target escapes unharmed. The spell's description defines what happens on a successful defense. If the spell specifies no outcome for a successful defense, the target is assumed to emerge unaffected.

Spells that do not target an unwilling creature — healing, utility, and buff spells — require no attack Opposition Check. Their effects apply automatically.

## Spell Defense

How a target resists a spell depends on the spell's type, as stated in the spell's description.

**Elemental spells** (fire, lightning, cold, acid, and similar effects that produce a real physical phenomenon) can only be Dodged. Parry and Block cannot deflect magic. Standard Dodge rules apply, including the −2 restricted-space penalty and −4 prone penalty. A defender who cannot or chooses not to Dodge takes the hit automatically. **Armor mitigates elemental spell damage normally** — fire burns through what it touches, and armor reduces how much of that heat reaches the body beneath.

**Magical spells** (force, conjured weapons, and effects that are purely supernatural rather than a physical phenomenon) can only be Dodged. Armor provides no mitigation against these effects — there is nothing physical to block. A defender who cannot or chooses not to Dodge takes the full damage. Spells that bypass armor will state **(unmitigated)** in their Damage line.

**Mind-affecting spells** (charm, compulsion, illusion, fear, and similar) are resisted with the defender's dice pool + Willpower. No physical defense can counter a spell that targets the mind; Parry and Block are unavailable. A defender who cannot make a Willpower check (Stunned, Unconscious, [Incapacitated](Conditions.md), or similar) takes the hit automatically.

A defender who cannot make any defensive Opposition Check — because they are [Vulnerable](Conditions.md), unable to act or react, or lack the AP to pay for a defensive Reaction — takes the hit automatically. Armor mitigation still applies normally.

## Health Cost

Casting a spell costs the caster **Health equal to the spell's level** (a 3rd-level spell costs 3 Health, a 9th-level spell costs 9 Health, a Level 0 spell costs 0 Health). This cost is paid immediately when the spell is cast. It is a literal physical toll — casting a spell hurts.

This cost is **never reduced** by any Spellcasting tier or any other skill or ability. Investing further in Spellcasting unlocks higher-level spells and improves attack Opposition Checks and spell damage, but never makes casting cheaper. The Health cost is the permanent price of admission for magic, regardless of investment.

## Creature Spellcasting

A creature's magic is physiological — inherent to its nature, not a trained skill. **Creatures do not pay the per-spell Health cost** that player characters and humanoid NPCs pay. A creature's Spellcasting tier still governs which spell levels it can access, but casting never costs it Health.

Humanoid NPCs are built on the same framework as player characters and pay the same Health cost when they cast.

The [Predation Difficulty](#predation-difficulty) system applies to all casters — creature or otherwise — whenever a Level 1+ spell is cast.

## Predation Difficulty

Every spell of Level 1 or higher sends ripples through the magical field — and in some settings, something in those depths may notice. Level 0 spells are too shallow to reach anything dangerous, no matter how many are cast.

**Tracking.** At the start of each encounter, the Narrator privately sets the Predation Difficulty to **25**. The Predation Difficulty is shared — every caster on the battlefield, friend and foe alike, draws from the same pool. Players do not track the Predation Difficulty.

**Casting.** Each time a Level 1+ spell is cast, subtract that spell's level from the Predation Difficulty.

If a spell is overcharged, subtract its overcharged Health cost (see [Spell Overcharging](#spell-overcharging)) from the Predation Difficulty instead of the spell's normal level.

**Concentration.** Maintaining a concentration spell is channeling — the caster continues to draw on the magical field to sustain the effect. At the start of each of the caster's turns, subtract 1 from the Predation Difficulty for each concentration spell they are maintaining. Each maintained spell is a separate subtraction. A caster maintaining two concentration spells subtracts 2.

**Manifestation.** When the Predation Difficulty reaches 0, a hostile manifestation occurs — the Narrator determines what it is, where it appears, and who it targets. From that point forward, every draw on the magical field triggers an additional manifestation immediately: each cast of a Level 1+ spell, and each concentration spell maintained at the start of a caster's turn.

The campaign setting defines what specifically answers the call (e.g., Anar's Magesea predators). If the active campaign setting has no such mechanism, the Narrator may rule that the Predation Difficulty system does not apply.

## Spell Overcharging

A caster may choose to overcharge a spell at the moment of casting, pushing more power through it than it was designed to carry. All numerical aspects of the spell are doubled — range, number of targets, duration, radius, damage, and any other quantified value in the spell's description — at a higher Health cost.

**Health cost.** An overcharged spell costs 1.5× the spell's level in Health, rounded up. Overcharging a Level 0 spell costs 1 Health.

| Spell Level | Normal Cost | Overcharged Cost |
| :---: | :---: | :---: |
| 0 | 0 | 1 |
| 1 | 1 | 2 |
| 2 | 2 | 3 |
| 3 | 3 | 5 |
| 4 | 4 | 6 |
| 5 | 5 | 8 |
| 6 | 6 | 9 |
| 7 | 7 | 11 |
| 8 | 8 | 12 |
| 9 | 9 | 14 |

**Predation.** Overcharging a Level 1+ spell subtracts its overcharged Health cost from the Predation Difficulty instead of the spell's normal level. Overcharging a Level 0 spell does not affect the Predation Difficulty.

## Concentration Spells

Some spells require ongoing effort to maintain. A spell with a Duration of *Concentration* costs **1 AP per round**, paid at the start of the caster's turn, to sustain its effect. If the caster does not pay or cannot pay the AP cost, the spell ends.

See [Concentration](Concentration.md) for full rules — Concentration Checks, Intense Concentration, and stacking limits.

## How to Read a Spell Entry

Each spell in the catalog uses the following fields:

- **Level** — which Spellcasting tier unlocks this spell.
- **Category** — the spell's functional type: Offense, Defense, Crowd Control, Healing, or Utility. A spell may have more than one category.
- **Casting Time** — the AP cost to cast the spell. Most spells cost 1 AP.
- **Casting Cost** — Health paid when the spell is cast.
- **Range** — maximum distance to the target. *Line of sight* means the caster must be able to see the target directly.
- **Target** — what or who the spell affects.
- **Damage** — the damage the spell deals on a hit, including damage type. Spells with no Damage line deal no damage directly. The tag **(unmitigated)** means armor provides no mitigation against this damage.
- **Duration** — how long the spell lasts. *Instantaneous* means the effect occurs and ends immediately. *Concentration* means the caster must maintain the spell each round — see [Concentration](Concentration.md).
- **Defense** — how the target resists an attack spell. See [Spell Defense](#spell-defense). Spells with no Defense line do not allow a resistance roll.


## The Sight Abilities

Far Sight, Long Sight, and True Sight are cross-lineage traits, not spells. They are innate perceptions — present from birth, requiring no Spellcasting investment, costing no Health, and contributing nothing to the Predation Difficulty. They cannot be learned, purchased, or trained.

Characters who possess one of these abilities are **God-touched**. See [Traits](../Characters/Traits.md#god-touched) for full rules on God-touched characters and the three Sight abilities.


## Available Spells

The spell catalog lists available spells by level. See [Spells](../Spells/Spells.md).

Campaign settings may add spells to any level. Spells listed in the Core Rules catalog are available in any setting unless a campaign setting explicitly restricts them.
                                                                                                                                                                             