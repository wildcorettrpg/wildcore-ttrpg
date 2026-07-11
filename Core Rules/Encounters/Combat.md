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

Each character receives **3 AP** at the start of their turn — spent on attacks, movement, Concentration, and Reactions. Unspent AP do not carry over. For the full breakdown of costs by action type, see [Actions](Actions.md).

## Making an Attack

All attacks are Opposition Checks (see [Opposition Checks](Opposition%20Checks.md)).

**Assembling the attack roll:** the attacker's dice pool comes from skills that explicitly grant attack dice, plus a flat bonus from the relevant attribute. Melee attacks use **Strength**, ranged attacks use **Strength**, and magical attacks use **Willpower**.

**The defender responds** with their own dice pool and attribute bonus, choosing one defensive option. Against melee or ranged attacks, the defender may choose **Dodge** (dice pool + Reflex), **Parry** (dice pool + Reflex), or **Block** (dice pool + Reflex). Against spells — fire, lightning, cold, force, and similar — only **Dodge** is available; Parry and Block cannot deflect magic. Against mind-affecting spells — charm, compulsion, illusion, fear, and similar — the defender makes a **Willpower Opposition Check** (dice pool + Willpower); no physical defense can counter a spell aimed at the mind, so Dodge, Parry, and Block are unavailable.

**Resolving the exchange:** if the attacker's total exceeds the defender's total, the attack hits. If the totals are equal, the exchange is a stalemate — neither side gains the upper hand; narrate accordingly. If the defender's total exceeds the attacker's total, the attack fails. If the defender cannot make a defensive roll at all — because they are Vulnerable, Stunned, Unconscious, Incapacitated, or out of AP for a Reaction — the attack hits automatically; armor mitigation still applies.

See [Actions](Actions.md) for the full attack resolution rules, including defender restrictions and simultaneous-attack tiebreaking.

## Damage

On a hit, the attacker rolls for damage immediately. **Base damage** is determined by the specific weapon — see [Weapons](../Equipment/Weapons.md) for each weapon's die; unarmed attacks have no base die, so damage is Strength bonus only. **Attribute bonus damage** adds +1 die (the same size as the weapon die) per 3 points of Strength for melee and ranged attacks, or per 3 points of Willpower for magical attacks. **Skill bonus damage** is added as explicitly granted by applicable skills. Finally, **armor mitigation** lets the defender subtract their armor's mitigation value from the total; mitigation applies after all damage dice are summed. Armor mitigates physical damage and elemental spell damage (fire, cold, lightning, acid). Purely magical effects — force, conjured weapons, and effects that are supernatural rather than physical — bypass armor entirely. Each spell's Damage line indicates **(unmitigated)** when armor does not apply.

See [Damage](Damage.md) for the full damage rules. See [Armor](../Equipment/Armor.md) for mitigation values by armor category.

## Spellcasting in Combat

Casting a spell costs the caster Health equal to the spell's level (Level 0 costs nothing; a 9th-level spell costs 9 Health). This cost is never reduced by skill investment. Every spell of Level 1 or higher may draw supernatural attention — see [Predation Difficulty](Magic.md#predation-difficulty) for how this is tracked and what it risks. Level 0 spells never draw attention.

Elemental spell damage (fire, cold, lightning, acid) is mitigated by armor normally. Purely magical effects — force, conjured weapons, and effects marked **(unmitigated)** in their Damage line — bypass armor entirely. See [Magic](Magic.md) for spell attack and defense rules, and [Spellcasting](../Skills/Universal/Combat/Spellcasting%20Skill.md) for the skill tree.

## Conditions

Combat regularly imposes conditions on characters — Dying, Prone, Hindered, Stunned, Bleeding Out, Frightened, and others. Each condition has specific mechanical effects and defined removal triggers. See [Conditions](Conditions.md) for the full list.

## Dying and Death

When a character's Health falls to or below their **wounded threshold** (half their Vitality, rounded up — 13 Health at base Vitality 25), they enter the Wounded condition and begin Bleeding Out. When Health falls further to or below their **dying threshold** (one quarter of their Vitality, rounded up — 7 Health at base Vitality 25), they enter the Dying condition: −2 on all Opposition Checks, movement reduced by 5 ft, Consciousness Checks when they enter the Dying condition, take damage, or lose Health from Bleeding Out. Reaching 0 Health means death.

See [Dying](../Characters/Dying.md), [Stabilization](../Characters/Stabilization.md), and [Death](../Characters/Death.md).
