# Dice Pools

A dice pool is the set of dice a character assembles for a given roll. WildCore uses two distinct types: **attack pools** for Opposition Checks, and **damage pools** for resolving damage after a hit lands. They are built from different ingredients and serve different purposes.

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

**Building your pool (do this on your character sheet, not during play):**

1. Start with 1d10.
2. Add 1d10 for each skill that explicitly grants an attack die for this type of check.
3. Add flat bonuses from applicable skills.
4. Add the relevant attribute as a flat bonus.
5. Record the result: *[X]d10 + [Y]* (e.g., *3d10 + 5*).

**During play:** pick up your recorded dice, roll them, add your recorded flat bonus, and compare. No reassembly required.

## Damage Pools

Damage pools determine how much damage a successful attack deals. They are not Opposition Checks — the attacker rolls alone and applies the result.

**Base die.** The base damage die comes from the weapon or ability being used. Weapon damage dice range from 1d6 (light weapons) to 3d6 (the heaviest weapons). There is no universal 1d10 base for damage.

**Additional dice.** Skills and attributes can grant bonus damage dice. Unless specified otherwise, bonus damage dice match the weapon's die type. Strength and Willpower each grant 1 bonus damage die for every 3 points in the attribute — this applies automatically without any skill purchase.

**Flat bonuses.** Flat bonuses from applicable skills are added after rolling. The relevant attribute is also added as a flat bonus, the same as in an attack pool.

**Building your pool (do this on your character sheet, not during play):**

1. Start with the weapon's base damage die.
2. Add one bonus die (of the weapon's type) for each skill or attribute effect that grants a bonus damage die.
3. Add flat bonuses from applicable skills.
4. Add the relevant attribute as a flat bonus.
5. Record the result: *[X]d[Y] + [Z]* (e.g., *2d8 + 5*).

**During play:** pick up your recorded dice, roll them, add your recorded flat bonus, and apply the result. No reassembly required.

## Example 1: Attack Roll

Ryn has invested in Melee Attack through tier VIII and wields a mace (a medium weapon). Her Strength is 3.

**Building her melee attack pool (character sheet):**

1. Start with 1d10.
2. Melee Attack VIII grants +1d10. Pool is now 2d10.
3. Strength 3 grants +1d10 (1 die per 3 points). Pool is now 3d10.
4. Flat bonuses: Melee Attack V (+2), Strength 3 (+3). Total flat: +5.
5. Record: **3d10 + 5**.

**At the table:** Ryn picks up 3d10 and rolls 7, 4, and 5. Total: 16. She adds her recorded +5. Final total: **21**.

Her opponent rolls their defense pool and compares. Higher total wins.

## Example 2: Damage Roll with Bonus Dice

Ryn hits. Now she rolls damage. Her mace's base damage die is 1d8. Her Strength is 3, which grants 1 bonus damage die.

**Building her melee damage pool (character sheet):**

1. Start with 1d8 (mace base).
2. Strength 3 grants +1d8 (1 die per 3 points). Pool is now 2d8.
3. Flat bonuses: Melee Attack V (+2), Strength 3 (+3). Total flat: +5.
4. Record: **2d8 + 5**.

**At the table:** Ryn picks up 2d8 and rolls 6 and 4. Total: 10. She adds her recorded +5. Final total: **15 damage**.

Armor mitigation is subtracted from this total before Health is reduced. Assume her target wears Hide Armor (8 mitigation). Damage that gets through: 15 − 8 = **7**. Her target loses 7 Health.
