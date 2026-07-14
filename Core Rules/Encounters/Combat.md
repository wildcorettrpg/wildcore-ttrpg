# Combat

## What Combat Is

Combat is a structured scene resolved through Opposition Checks. There are no guaranteed hits, no passive defenses, and no separate hit-point-attrition subsystem. Every offensive and defensive action is a contested roll — attacker versus defender — and the outcome of each exchange is always uncertain until the dice land.

Combat begins when the Narrator determines that timing, danger, or opposition requires structured turns. Everything between that moment and the resolution of the conflict follows the rules in this section and its referenced documents.

## Structure of a Combat Encounter

A combat encounter proceeds in three phases. 

In the **Opening**, the Narrator privately determines which side acts first (see [Turn Order](Turn%20Order.md) §3); if Surprise applies, a surprise round occurs before the first standard round (see [Turn Order](Turn%20Order.md) §4). 

During **Rounds**, one side completes all of its turns before the other side begins; within a side, players choose their own acting order at the start of each round, and rounds continue until the encounter ends. 

In **Resolution**, the encounter ends when all hostile characters are defeated, incapacitated, or withdrawn; one side surrenders or ceases hostilities; or the Narrator determines the conflict has resolved (see [Encounter Structure](Encounter%20Structure.md)).

## Action Points

Each character receives **3 AP** at the start of their turn. Unspent AP do not carry over. For base AP, maximum AP, costs by action type, and which skills grant additional AP, see [Action Points](Action%20Points.md).

## Making an Attack

All attacks are Opposition Checks (see [Opposition Checks](../Core%20Mechanics/Opposition%20Checks.md)).

**Assembling the attack roll:** the attacker's [dice pool](../Core%20Mechanics/Dice%20Pools.md) comes from skills that explicitly grant attack dice, plus a flat bonus from the relevant attribute. Melee attacks use **Strength**, ranged attacks use **Strength**, and magical attacks use **Willpower**.

**The defender responds** with their own [dice pool](../Core%20Mechanics/Dice%20Pools.md) and attribute bonus, choosing one defensive option. Against melee or ranged attacks, the defender may choose **Dodge** ([Dodge pool](../Core%20Mechanics/Dice%20Pools.md)), **Parry** ([Parry pool](../Core%20Mechanics/Dice%20Pools.md)), or **Block** ([Block pool](../Core%20Mechanics/Dice%20Pools.md)). Against spells — fire, lightning, cold, force, and similar — only **Dodge** is available; Parry and Block cannot deflect magic. Against mind-affecting spells — charm, compulsion, illusion, fear, and similar — the defender makes a **Willpower Opposition Check** ([Willpower pool](../Core%20Mechanics/Dice%20Pools.md)); no physical defense can counter a spell aimed at the mind, so Dodge, Parry, and Block are unavailable.

**Resolving the exchange:** if the attacker's total exceeds the defender's total, the attack hits. If the totals are equal, the exchange is a stalemate — neither side gains the upper hand; narrate accordingly. If the defender's total exceeds the attacker's total, the attack fails. If the defender cannot make a defensive roll at all — because they are [Vulnerable](../Conditions%20and%20Hazards/Conditions.md#vulnerable), [Stunned](../Conditions%20and%20Hazards/Conditions.md#stunned), [Unconscious](../Conditions%20and%20Hazards/Conditions.md#unconscious), [Incapacitated](../Conditions%20and%20Hazards/Conditions.md#incapacitated), or out of AP for a Reaction — the attack hits automatically; armor mitigation still applies.

See [Actions](Actions.md) for the full attack resolution rules, including defender restrictions and simultaneous-attack tiebreaking.

## Damage

On a hit, the attacker rolls for damage immediately. **Base damage** is determined by the specific weapon — see [Weapons](../Equipment/Weapons.md) for each weapon's die; unarmed attacks have no base die, so damage is Strength bonus only. **Attribute bonus damage** adds +1 die (the same size as the weapon die) per 3 points of Strength for melee and ranged attacks, or per 3 points of Willpower for magical attacks. **Skill bonus damage** is added as explicitly granted by applicable skills. Finally, **armor mitigation** lets the defender subtract their armor's mitigation value from the total; mitigation applies after all damage dice are summed. Armor mitigates physical damage and elemental spell damage (fire, cold, lightning, acid). Purely magical effects — force, conjured weapons, and effects that are supernatural rather than physical — bypass armor entirely. Each spell's Damage line indicates **(unmitigated)** when armor does not apply.

See [Damage](Damage.md) for the full damage rules. See [Armor](../Equipment/Armor.md) for mitigation values by armor category.

## Spellcasting in Combat

Casting a spell costs the caster Health equal to the spell's level (Level 0 costs nothing; a 9th-level spell costs 9 Health). This cost is never reduced by skill investment. Every spell of Level 1 or higher may draw supernatural attention — see [Predation Clock](../Magic/Magic.md#predation-clock) for how this is tracked and what it risks. Level 0 spells never draw attention.

Elemental spell damage (fire, cold, lightning, acid) is mitigated by armor normally. Purely magical effects — force, conjured weapons, and effects marked **(unmitigated)** in their Damage line — bypass armor entirely. See [Magic](../Magic/Magic.md) for spell attack and defense rules, and [Spellcasting](../Skills/Universal/Combat/Spellcasting%20Skill.md) for the skill tree.

## Conditions

Combat regularly imposes conditions on characters — [Prone](../Conditions%20and%20Hazards/Conditions.md#prone), [Hindered](../Conditions%20and%20Hazards/Conditions.md#hindered), [Stunned](../Conditions%20and%20Hazards/Conditions.md#stunned), [Bleeding Out](../Conditions%20and%20Hazards/Conditions.md#bleeding-out), [Frightened](../Conditions%20and%20Hazards/Conditions.md#frightened), and others. Each condition has specific mechanical effects and defined removal triggers. See [Conditions](../Conditions%20and%20Hazards/Conditions.md) for the full list.

## [Bleeding Out](../Conditions%20and%20Hazards/Conditions.md#bleeding-out) and Death

The Narrator may apply **[Bleeding Out](../Conditions%20and%20Hazards/Conditions.md#bleeding-out)** when a character suffers a significant wound — or any attack, ability, or effect that explicitly causes it. A character who is [Bleeding Out](../Conditions%20and%20Hazards/Conditions.md#bleeding-out) loses 1 Health per round at the end of their turn. When any source of damage or Health loss drops a character to **7 Health or below**, they must make a **Consciousness Check**. Reaching 0 Health means death.

See [Consciousness Checks](Consciousness%20Checks.md), [Dying](../Conditions%20and%20Hazards/Dying.md), [Stabilization](../Conditions%20and%20Hazards/Stabilization.md), and [Death](../Conditions%20and%20Hazards/Death.md).
