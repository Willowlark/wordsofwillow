---
doku: officers-chess
---
# Terrain Table

| Tile Terrain    | Move | DR  | Avo | Vein? | Special                                                    |
| --------------- | ---- | --- | --- | ----- | ---------------------------------------------------------- |
| Mountain        | 2    | +1  | -   |       |                                                            |
| Woods           | 2    | -   | +1  |       |                                                            |
| Woods           | 2    | -   | +1  |       |                                                            |
| Pillar          | 2    | -   | +1  |       |                                                            |
| Thicket         | 2    | -   | +1  |       |                                                            |
| Fog             | 2    | -   | +1  | Yes   |                                                            |
| Fort            | 2    | +2  | +1  |       | At start of turn on this tile, **Heal(10)**                |
| Protection Tile | 1    | +2  | +1  |       | At start of turn on this tile, **Heal(10)**                |
| Heal Tile       | 1    | -   | -   | Yes   | At start of turn on this tile, **Heal(10)**                |
| Gate/Door       | -    | -   | -   |       | Deal 15 Damage to destroy and make Floor, or use **Pick**. |
| Water           | 1    | -   | -1  | Yes   |                                                            |
| Stone Pillars   | 2    | +2  | -   | Yes   |                                                            |
| Vines           | 2    | -   | -   | Yes   |                                                            |
| Flames          | 1    | -   | -   | Yes   | At start of turn on this tile, take 5 Damage **Piercing**. |
| Ice             | -    | -   | -   | Yes   | Deal 15 Damage to destroy                                  |

# Rating Reference


| Rating                      | F   | D   | E   | C   | B   | A   | S   |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- |
| Base Damage (Str/Mag)       | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| Hit/Agility Bonus (Dex/Spd) | -5  | 0   | 5   | 10  | 15  | 20  | 25  |
| Damage Reduction (Def/Res)  | 0   | 1   | 2   | 3   | 4   | 5   | 6   |

# Follow Up Reference

| Rating         | F   | E   | D   | C    | B       | A          | S             |
| -------------- | --- | --- | --- | ---- | ------- | ---------- | ------------- |
| Follows Up on: | -   | -   | F   | F, E | F, E, D | F, E, D, C | F, E, D, C, B |

# Weapon Triangle

| Weapon | Effective Against    |
| ------ | -------------------- |
| Swords | Axes                 | 
| Lances | Swords               |
| Axes   | Lances               |
| Arts   | Tomes, Daggers, Bows |
