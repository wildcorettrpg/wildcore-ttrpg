# Actions

Actions represent discrete activities a character may perform during their turn. Each action has an AP cost as listed in its description unless it is a Free Action. A character may take actions in any order during their turn as long as they have sufficient [Action Points](Action%20Points.md) (AP).

## Action Categories

Every action falls into one of four categories. **Free Actions** are simple activities that don't cost AP unless a rule states otherwise. **Standard Actions** are any actions that cost AP, including physical, supernatural, social, or tactical maneuvers. **Reactions** are actions taken outside the character's turn when their trigger occurs, and cost AP as listed. **Movement** is purchased with AP and follows the rules in the Movement chapter.

## Common Standard Actions

- Making a melee attack
- Making a ranged attack
- Using a supernatural ability
- Shoving, grappling, or attempting to restrain a target
- Disengaging from an adjacent opponent
- Aiming a ranged weapon
- Reloading a weapon

## Action Points

All actions, movement, Concentration maintenance, and Reactions are paid for with Action Points (AP). See [Action Points](Action%20Points.md) for base AP, the maximum, what each action type costs, and which skills grant additional AP.

## Attacks and Strikes

An attack is a single action taken by a character. A strike is an individual hit roll made as part of an attack — a single attack may contain one or more strikes. The number of strikes in an attack does not change the AP cost of the attack.

Multi-strike actions are attacks that include multiple strikes as part of one fluid motion and cost **1 AP** unless they explicitly consume multiple actions. Each strike in a multi-strike action requires a separate attack Opposition Check and a separate damage roll. A multi-strike action must be explicitly granted by a skill, ability, or stat block entry — a character may not declare an ordinary attack a multi-strike action.

## Multi-Action Maneuvers

Some actions require more time, commitment, or setup than a standard attack. These actions consume multiple actions and therefore cost **2 AP** or **3 AP**. A multi-action maneuver represents extended effort, not multiple strikes. When a character uses a multi-action maneuver, they expend the corresponding number of AP from their AP for the round.

## Concentration

Concentration is not an action, but it is the only mechanic that can drain AP each round without being one. See [Concentration](../Magic/Concentration.md) for full rules on AP costs, Concentration Checks, and the types of effects Concentration maintains.

## Attack Cost and Multiple Attacks

Each attack costs **1 AP**. Each attack beyond the first made in the same turn imposes a cumulative **−2 penalty** to that attack's Opposition Check: the first attack is unpenalized, the second is at −2, the third at −4, and so on. This penalty applies to all attacks in a turn, including bonus attacks granted by skills or abilities.

## Attack Resolution

### Attack Roll

**Size Disparity (Auto-Hit)**: When a combatant attacks a target two or more [size categories](../Tables/Size%20Categories%20Table.md) larger than themselves with a melee weapon, no attack [Opposition Check](../Core%20Mechanics/Opposition%20Checks.md) is required — the attack automatically hits. The attacker still rolls a damage pool normally. One size category difference has no effect on the attack roll. This rule applies to melee only; ranged attacks and spellcasting always require an attack Opposition Check regardless of size.

All attacks are resolved as Opposition Checks. Every character rolls a minimum of 1d10. Skills that explicitly grant dice add to this base. The attacker adds the relevant [Attribute](../Characters/Attributes.md) and any flat bonuses from applicable [skills](../Skills/Skills.md). The defender responds with an Opposition Check of their own.

The relevant attack attribute is **Strength** for melee attacks, **Strength** for ranged attacks (bows, thrown weapons, crossbows, and similar), and **Willpower** for spell attacks — see [Magic](../Magic/Magic.md) for full spell attack and defense rules.

### Defense Roll

Stunned, Immobilized, Unconscious, and Restrained characters are unable to defend themselves for the duration of the effect using dodge, parry, or block.

For all other characters, the defender's response depends on the type of attack. For melee and ranged attacks, the defender makes an Opposition Check using one of the following options:

**Dodge:** [dice pool](../Core%20Mechanics/Dice%20Pools.md) from Dodge skills + **Reflex**. The defender rolls clear, twists, or steps out of the path of the attack. Always available. When the defender has no open space to step into — cornered, completely surrounded, or within 5 feet of the attacker with no open ground — Dodge takes a **−2 penalty**. A prone character may still Dodge but takes the **−4 prone penalty**.

When the defender is two or more [size categories](../Tables/Size%20Categories%20Table.md) smaller than the attacker, they gain **+2 to their Dodge pool** against that melee attack. This bonus does not apply to Parry or Block, and does not apply against ranged attacks or spells.

**Parry:** [dice pool](../Core%20Mechanics/Dice%20Pools.md) from Parry skills + **Reflex**.

**Block:** [dice pool](../Core%20Mechanics/Dice%20Pools.md) from Block skills + **Reflex**.

For all rules above, Vulnerable characters lose their Reflex bonus.

For spells, see [Magic](../Magic/Magic.md) for how spell defense works.

### Final Resolution 

If the attacker's total is greater than the defender's total, the attack hits. If the defender cannot make a defensive Opposition Check at all — because they are [Vulnerable](../Conditions%20and%20Hazards/Conditions.md#vulnerable) (see [Conditions](../Conditions%20and%20Hazards/Conditions.md)), unable to act or react ([Stunned](../Conditions%20and%20Hazards/Conditions.md#stunned), [Unconscious](../Conditions%20and%20Hazards/Conditions.md#unconscious), [Incapacitated](../Conditions%20and%20Hazards/Conditions.md#incapacitated), or similar), lack the [AP](Action%20Points.md) to pay for a defensive Reaction (see [Reactions](Reactions.md)), or have no Dodge/Parry/Block/Willpower-resistance option available for any other reason — no defensive roll is made and the attack automatically hits. Armor mitigation still applies normally. On a hit, the attacker immediately rolls for damage and applies the result.

### Multiple Attackers

When multiple attacks occur simultaneously, the character with the higher **Reflex** score goes first. If still tied, the players involved decide who goes first; if they can't agree, the Narrator decides.

