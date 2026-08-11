# Damage

## Damage Basics

When an attack or supernatural effect hits, the attacker rolls damage. Damage reduces the target's Health after armor mitigation is applied. Damage cannot reduce a character's Health below 0.

## Base Damage

Every weapon has a base damage die defined by its category in [Weapons](../Equipment/Weapons.md). Every spell has a base damage value defined in its description. Base damage is expressed as a die or fixed value (e.g., 1d6, 2d6) and reflects the nature of the weapon or spell, not the attacker's attributes.

## Attribute Damage Bonus

A character's relevant attribute increases their damage beyond the base value. The relevant attribute is **Strength** for melee attacks, **Strength** for ranged attacks, and **Willpower** for spell attacks. A character gains **1 bonus damage die for every 3 points** in the relevant attribute. Bonus damage dice use the same die as the weapon or spell's base damage. If the relevant attribute does not meet the threshold for a bonus die, no bonus die is added. Only one attribute damage bonus applies to any single attack.

## Skill Damage Bonuses

Certain skills may grant additional damage dice or flat damage bonuses, as defined in each skill's description. Skill damage bonuses stack with attribute damage bonuses unless a rule states otherwise.

## Damage Application

After rolling all damage dice, total the result. Apply armor mitigation to the total, if applicable — see [Armor Mitigation](#armor-mitigation) below. Apply any remaining damage to the target's Health. If total damage after mitigation is 0 or less, the target takes no damage.

## Damage and Conditions

Some attacks inflict conditions in addition to damage. Conditions are applied after damage is resolved unless the attack specifies otherwise. A condition is applied regardless of whether the attack deals damage, unless the condition's source specifies it requires damage to trigger.

## Armor Mitigation

Armor provides flat damage mitigation applied to every hit unless a rule states otherwise. Armor does not modify hit chance — it only reduces damage after a hit lands. Mitigation sources stack unless a rule specifies a cap or exception. Sources include worn armor, natural armor, temporary effects, and abilities or traits.

## Damage Types

All damage in WildCore has a type. Damage type determines whether armor mitigates and, for spells, how a target may defend. See [Spell Defense](../Magic/Magic.md#spell-defense) for defense rules by type.

| Damage Type     | Description                                                                                  | Armor Mitigates? |
| :-------------- | :------------------------------------------------------------------------------------------- | :--------------- |
| Slashing        | Blades, edges, claws                                                                         | Yes              |
| Piercing        | Points, arrows, fangs                                                                        | Yes              |
| Bludgeoning     | Impact, crushing force, unarmed strikes                                                      | Yes              |
| Fire            | Flame, heat, combustion                                                                      | Yes              |
| Cold            | Frost, ice, freezing temperature                                                             | Yes              |
| Lightning       | Electrical discharge                                                                         | Yes              |
| Acid            | Corrosive liquid or vapor                                                                    | Yes              |
| Elemental Force | Kinetic impact, compressed air, concussive wave | Yes              |
| Magical Force   | Conjured weapons, raw supernatural energy                                                    | No               |
| Poison          | Venom, toxin — delivered separately; see [Poisons](../Conditions%20and%20Hazards/Poisons.md)          | No               |

Magic weapons bypass armor regardless of their damage type. A spell states **(unmitigated)** in its Damage line when armor does not apply.

Specific rules always override the general table. An individual spell or ability may specify that its damage bypasses armor regardless of what the table shows for that damage type — the specific rule takes precedence.

## What Armor Protects Against

The default is that armor mitigates. It does not mitigate when a rule explicitly says otherwise.

**Mitigated:** mundane weapons (slashing, piercing, and bludgeoning); natural attacks (claws, teeth, unarmed strikes); elemental spell damage (fire, cold, lightning, acid, and Elemental Force). Armor reduces how much physical force or elemental energy reaches the body beneath.

**Not mitigated:** magic weapons bypass armor entirely regardless of damage type; Magical Force (conjured weapons and raw supernatural energy) bypasses armor — there is nothing physical to block; magical creature abilities that are explicitly supernatural (not breath weapons, which are elemental) bypass armor; environmental hazards including toxic atmosphere and poison bypass armor. A spell indicates **(unmitigated)** in its Damage line when armor does not apply.

## Natural Armor

Natural armor functions identically to worn armor — it applies flat mitigation to every hit and is always active unless suppressed by a specific effect. Large or resilient creatures may have high natural armor values.

## Armor and Health

Armor reduces incoming damage before Health is lost. High armor reduces the need for high Health pools. Health represents biological endurance, not avoidance.
