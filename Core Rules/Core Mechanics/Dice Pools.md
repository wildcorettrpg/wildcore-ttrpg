# Dice Pools

A dice pool is the set of dice a character assembles for a given roll. Velocity uses two distinct types: **attack pools** for Opposition Checks, and **damage pools** for resolving damage after a hit lands. They are built from different ingredients and serve different purposes.

## Named Pool Types

For the most common check types, the relevant attribute is fixed. These pools are referred to by name throughout the rules — the name carries the attribute, so it does not need to be restated at each use.

| Pool Name | Dice From | Attribute Added |
| :-------- | :-------- | :-------------- |
| Melee attack pool | Melee Attack skills | Strength |
| Ranged attack pool | Ranged Attack skills | Strength |
| Spellcasting attack pool | Spellcasting skills | Willpower |
| Dodge pool | Defense (Dodge) skills | Reflex |
| Parry pool | Defense (Parry) skills | Reflex |
| Block pool | Defense (Block) skills | Reflex |
| Willpower pool | Any applicable skills | Willpower |

When a spell or rule refers to a named pool, assemble it using the steps in [Attack Pools](#attack-pools) below with the attribute listed here.

## Attack Pools

Attack pools are used for Opposition Checks — any contested roll that determines whether an action succeeds or fails. Melee attacks, spell attacks, defensive rolls, social contests, skill checks, and Consciousness Checks all use attack pools.

**Base die.** Every attack pool starts with 1d10, always present regardless of skills or attributes.

**Additional dice.** A small number of skills explicitly grant additional dice to an attack pool. Most skills grant flat bonuses instead. A skill's description states which it provides — if it doesn't say it grants a die, it doesn't. Strength and Willpower each grant 1 bonus attack die for every 3 points in the attribute — this applies automatically without any skill purchase.

**Flat bonuses.** Flat bonuses from applicable skills are added to the rolled total after all dice are rolled. The relevant attribute is also added as a flat bonus.

**Assembly:**

1. Start with 1d10.
2. Add 1d10 for each skill that explicitly grants an attack die for this type of check.
3. Roll all dice and sum the results.
4. Add flat bonuses from applicable skills.
5. Add the relevant attribute.

## Damage Pools

Damage pools determine how much damage a successful attack deals. They are not Opposition Checks — the attacker rolls alone and applies the result.

**Base die.** The base damage die comes from the weapon or ability being used. Weapon damage dice range from 1d6 (light weapons) to 3d6 (the heaviest weapons). There is no universal 1d10 base for damage.

**Additional dice.** Skills and attributes can grant bonus damage dice. Unless specified otherwise, bonus damage dice match the weapon's die type. Strength and Willpower each grant 1 bonus damage die for every 3 points in the attribute — this applies automatically without any skill purchase.

**Flat bonuses.** Flat bonuses from applicable skills are added after rolling. The relevant attribute is also added as a flat bonus, the same as in an attack pool.

**Assembly:**

1. Start with the weapon's base damage die.
2. Add one bonus die (of the weapon's type) for each skill or attribute effect that grants a bonus damage die.
3. Roll all dice and sum the results.
4. Add flat bonuses from applicable skills.
5. Add the relevant attribute.

## Example 1: Attack Roll

Ryn has invested in Melee Attack through tier VIII and wields a mace (a medium weapon). Her Strength is 3.

Her skills and attributes relevant to this attack roll:

- Melee Attack V: +2 flat to melee attack rolls with medium weapons.
- Melee Attack VIII: +1d10 to all melee attack rolls.
- Strength 3: +1 bonus attack die (1 per 3 points of Strength); +3 flat to attack.

Building her attack pool:

1. Start with 1d10.
2. Melee Attack VIII adds 1d10. Pool is now 2d10.
3. Strength 3 adds 1d10. Pool is now 3d10.
4. Roll 3d10: results are 7, 4, and 5. Running total: 16.
5. Melee Attack V adds +2 flat. Running total: 18.
6. Strength 3 adds +3 flat. Final
total: **15 damage**.

Armor mitigation is applied to this total before Health is reduced.
