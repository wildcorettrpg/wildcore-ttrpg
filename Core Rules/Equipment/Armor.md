# Armor

For armor mitigation rules — how mitigation works, what armor protects against, and natural armor — see [Damage](../Encounters/Damage.md) §Armor Mitigation.

## Armor Types

1. Worn armor is grouped into three categories — Light, Medium, and Heavy — each with its own skill tree (see [Light Armor](../Skills/Universal/Combat/Light%20Armor%20Skill.md), [Medium Armor](../Skills/Universal/Combat/Medium%20Armor%20Skill.md), [Heavy Armor](../Skills/Universal/Combat/Heavy%20Armor%20Skill.md)).
2. Each armor item provides its own flat mitigation value. Trained mitigation applies when the character has at least tier I in the matching skill tree; untrained mitigation applies when they do not. A character wearing no armor receives no mitigation at all.
3. Wearing armor without the matching skill training imposes the following untrained wear penalties by category:
    1. **Light**: No additional penalties. The mitigation reduction (trained vs. untrained column) is the only cost.
    2. **Medium**: −2 to Stealth Opposition Checks.
    3. **Heavy**: −2 to Reflex-based Opposition Checks, −5 ft per AP spent on movement, and −4 to Stealth Opposition Checks.
4. These penalties are removed by investing in the matching armor skill tree. See each tree for which skill removes which penalty.
5. Sizes follow [Inventory](Inventory.md) §2. Costs are ported from d20 source material in gold pieces (gp) and have no effect on inventory slots — see [Currency](Currency.md) for the currency note.

| Category | Item            | Size   |     Cost | Mitigation (trained) | Mitigation (untrained) |
| :------- | :-------------- | :----- | -------: | -------------------: | ---------------------: |
| Heavy    | Chain mail      | Large  |   150 gp |                   14 |                      7 |
| Medium   | Chain shirt     | Medium |    50 gp |                   10 |                      5 |
| Medium   | Hide armor      | Large  |    15 gp |                    8 |                      4 |
| Light    | Leather armor   | Medium |    10 gp |                    3 |                      2 |
| Light    | Padded armor    | Medium |     5 gp |                    2 |                      1 |
| Heavy    | Plate armor     | Large  | 1,500 gp |                   18 |                      9 |
| Medium   | Scale mail      | Large  |    50 gp |                   12 |                      6 |
| Heavy    | Splint armor    | Large  |   200 gp |                   16 |                      8 |
| Light    | Studded leather | Medium |    25 gp |                    5 |                      3 |

6. The mitigation values above are a first draft intended for playtesting, in keeping with [Weapons](Weapons.md)'s draft status. They're expected to be tuned once tested against WildCore's damage dice scale (base die + attribute/skill bonus dice).

## Shields

Shields are worn items separate from body armor. A character may wear both simultaneously; their effects stack.

Two shield types exist, each with its own training path:

- **Light shields** (wood, steel, and bucklers) provide a bonus to Block Opposition Checks rather than flat mitigation.
- **Heavy shields** (wood, steel, and tower shields) provide flat damage mitigation, applied in addition to any worn armor.

A buckler is the exception among light shields: it straps to the forearm rather than being gripped, allowing the same arm to carry a one-handed weapon or item. All other light shields require the off-hand to grip.

The tower shield imposes additional penalties when used without Heavy Shield training: −2 to Reflex-based Opposition Checks and −2 to Stealth Opposition Checks. These are removed by the [Heavy Shield](../Skills/Universal/Combat/Heavy%20Shield%20Skill.md) skill tree. No other shield imposes additional untrained penalties beyond using the lower benefit value.

| Type | Item | Size | Cost | Benefit (trained) | Benefit (untrained) |
| :--- | :--- | :--- | ---: | :--- | :--- |
| Light | Buckler | Small | 5 gp | +3 to Block Opposition Checks | +1 to Block Opposition Checks |
| Heavy | Heavy shield, steel | Medium | 20 gp | 5 mitigation | 2 mitigation |
| Heavy | Heavy shield, wood | Medium | 7 gp | 3 mitigation | 1 mitigation |
| Light | Light shield, steel | Small | 15 gp | +3 to Block Opposition Checks | +1 to Block Opposition Checks |
| Light | Light shield, wood | Small | 3 gp | +2 to Block Opposition Checks | +1 to Block Opposition Checks |
| Heavy | Tower shield | Large | 30 gp | 6 mitigation | 3 mitigation; −2 Reflex, −2 Stealth |

See [Light Shield](../Skills/Universal/Combat/Light%20Shield%20Skill.md) and [Heavy Shield](../Skills/Universal/Combat/Heavy%20Shield%20Skill.md) for training options. Values are a first draft intended for playtesting alongside the armor table above.
