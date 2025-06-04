---
doku: officers-chess
---
# Introduction

**This is a working document! Things may change, be moved, or be incomplete!**

# Game Pieces

## Units

Units are a single combatant that a player controls on the battlefield. Players will control a small group of Units (referred to in the rules as their Army) while playing. 

| Properties        | Description                                                                                                                                                                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **HP**            | Units range from 14 to 22 point of HP, or health points. A unit that loses all it's HP is defeated, and possibly killed.                                                                                                                                      |
| **Movement**      | Unpromoted units have a movement of 4, and promoted units have a movement of 5 tiles. Some tags can increase or decrease a unit's Movement.                                                                                                                  |
| **Inventory**     | Units can carry up to 3 Items on them. Items are Weapons, Accessories, or Consumables that a Unit can start a battle with.                                                                                                                                    |
| **Class**         | Each Unit has a single Class which provides it's Ratings, it's Weapon Proficiencies, and it's Tags. Classes are either Base or Promoted, promoted classes are stronger classes that units can grow into.                                                      |
| **Proficiencies** | A list of the Weapon Types a Unit can use. A Unit cannot equip a weapon not on the list, or a weapon that is a Level higher than rating listed in brackets. Ratings with a + can be increased in the Roleplaying rules. This is provided by the Unit's Class. |
| **Tags**          | Classes may provide a Unit with tags that given them unique mechanics, defined in the Tags section.                                                                                                                                                           |

### Core Stats

Ratings describe how good a Unit is at certain things. Ratings are on a letter scale, with `E` being the worst and `A` being the best. (Some tables with go above or below this scale, but no Class can provide a default higher or lower than these values.) There are 6 Ratings a Unit gets from their Class, detailed in this table:

| Rating         | Description                                                                                                                                                                                                                        |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Strength**   | Strength represents the units physical strength. Strength contributes to Damage dealt by the Unit.                                                                                                                                 |
| **Magic**      | Magic represents the Unit's proficiency with the Arcane arts. Magic contributes to the Damage dealt by magical attacks made by the Unit.                                                                                           |
| **Dexterity**  | Dexterity represents a Unit's combat talent. Dexterity is used to determine if a Unit hits with an attack. A Unit must roll less than equal to it's Dexterity value to hit in combat.                                              |
| **Speed**      | Speed represents a Unit's swiftness in combat. Speed is used to determine which Unit gets to make a Follow Up attack and how evasive the unit is. Speed is reduced by the weight of the Unit's Weapon/Accessories (labeled Avoid). |
| **Defense**    | Defense is a unit's physical resistance. It reduces the amount of Martial Damage the unit takes.                                                                                                                                   |
| **Resistance** | Resistance is a units magical defense. It reduces the amount of Damage taken from Magic attacks.                                                                                                                                   |

### Combat Stats

These are derived statistics that come from classes, weapons, and sometimes even the Terrain. On Foundry these values can be found on the weapon entry. 

| Stat        | Description                                                                                                                            |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Agility** | Agility is used when determining when who gets to follow up and contributes to Evasion. Agility is `Speed + Weight` of the current weapon  |
| **Avoid** | Avoid is `Agility + Terrain Bonuses` if the unit has any. A unit attacking this unit has it's Hit reduced by this unit's Evasion. |
| **Hit**     | Hit is calculated as `70 + Dex + Weapon Hit - Target's Evasion`. This is the number a unit must roll under to hit with a given weapon.   | 

## Items

Units can carry multiple types of item in their Inventory. Weapons allow a Unit to fight enemies or assist allied Units. Accessories are Items that provide a benefit to the Unit as long as the Unit carries them in their Inventory. Consumables are Items that can be used in some way for a limited number of times. 

### Weapons

Weapons are required for Units to attack. A Unit may only equip one Weapon at a time, and will use it's equipped weapon when attacking or being attacked. Weapons have the following attributes.

| Property        | Description                                                                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Weapon Type** | The Type of the Weapon. Each Class can only use certain types of Weapon.                                                                         |
| **Level**       | A Unit can only use this weapon if it has proficiency in the type of Weapon at or above this Rating.                                             | 
| **Damage Type** | Weapons do either Martial or Magic damage when used. Which type determines which of the Target's stats reduces the Damage taken from the weapon. |
| **Might (Mt)**  | Might is effectiveness of the weapon in combat. It is added to a Unit's strength to calculate Damage.                                            |
| **Weight (Wt)** | Weight reduces a unit's Agility while wielding the weapon, and by proxy their Evasion. Weight is either 0, -5, or -10.                           |
| **Hit**         | A Weapon's hit is typically a penalty to a Unit's Hit when using the weapon. It's a multiple of 5 and typically negative.                        |
| **Tags**        | Weapons can provide a Unit with tags that give them unique mechanics, defined in the Tags section.                                               |
| **Range**       | Weapons will list a range in number of tiles. Some weapons have fixed number, others have a range.                                               |

## Accessories

## Consumables

# Gameplay

## Rounds 

Game play takes place in rounds. In a round, every unit on the map moves once. All units on a side are not activated at the same time. Players begin and activate one unit each that is under their control. Once they have moved those units, the GM will move three enemy units. This alternates until all units have moves and the round ends.

## Combat Turns 

When a Unit is activated, it begins a Combat Turn. On a Combat Turn, a Unit can: 
- Move, 
- use an Action (Attack, Staff, Special Action)
- and take any number of Free Actions.

### Move

All units can move up to their Movement during their turn. The **Fast(X)** and **Slow(X)** tags increase and decrease this amount respectively. Movement is also affected by the Terrain of each tile. 

The Terrain Table lists different types of tiles a unit can encounter on the Map. 

| Column  | Description                                                                                                                                                     |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Move**    | The amount of Movement required to enter this tile.                                                                                                             |
| **DR**      | When standing on this tile, add this value to a Unit's Damage Reduction when it's attacked.                                                                     |
| **Avo**     | When standing on this tile, add this value to a Unit's Avo when determining the target number to hit this Unit. This does NOT apply when determining follow up! |
| **Vein**    | Terrain with "Yes" can be created via the **Vein** Tag. Terrain modified via **Vein** remains modified until the end of the round.                              |
| **Special** | Notes or additional mechanics related to the Tile.                                                                                                              | 

Tile types not listed cost 1 move to enter. These tiles include Plains, Sand, Buildings, Ruins, Floors, Stairs, Bridges, and Village Gates

#### Terrain Table

| Tile Terrain    | Move | DR  | Avo | Vein? | Special                                                    |
| --------------- | ---- | --- | --- | ----- | ---------------------------------------------------------- |
| Mountain        | 2    | +1  | -   |       |                                                            |
| Woods           | 2    | -   | +5  |       |                                                            |
| Woods           | 2    | -   | +5  |       |                                                            |
| Pillar          | 2    | -   | +5  |       |                                                            |
| Thicket         | 2    | -   | +5  |       |                                                            |
| Fog             | 2    | -   | +5  | Yes   |                                                            |
| Fort            | 2    | +2  | +5  |       | At start of turn on this tile, **Heal(10)**                |
| Protection Tile | 1    | +2  | +5  |       | At start of turn on this tile, **Heal(10)**                |
| Heal Tile       | 1    | -   | -   | Yes   | At start of turn on this tile, **Heal(10)**                |
| Gate/Door       | -    | -   | -   |       | Deal 15 Damage to destroy and make Floor, or use **Pick**. |
| Water           | 1    | -   | -5  | Yes   |                                                            |
| Stone Pillars   | 2    | +2  | -   | Yes   |                                                            |
| Vines           | 2    | -   | -   | Yes   |                                                            |
| Flames          | 1    | -   | -   | Yes   | At start of turn on this tile, take 5 Damage **Piercing**. |
| Ice             | -    | -   | -   | Yes   | Deal 15 Damage to destroy                                  |

### Actions

#### Attack 

A Unit can attack a Target if the Target is within the Range of the Unit's equipped weapon. The attack process is as follows:

##### Hitting Targets

- First, **confirm the Target is in range** of the Attacker's Weapon.
- Next, **Calculate the Hit Target number for the Weapon**.
    - Hit is `70 + Dex + Weapon's Hit`. Dex ratings are converted to to a numeric bonus per the below table.
    - Subtract the target's Avoid. Avoid is `Speed + Weapon Weight`. Speed is converted to a numeric value per the same table as Dex.
    - Tags on the Classes of either combatant or Tags on their Equipped weapons, such as the **Inaccurate(X)** tag. 
- The Target Number is **Hit - Avoid**. The attackers rolls 1d100 which must be equal or less than the target number to hit.
-   A Critical Hit is scored when the result is 10 or less. This range is modified by Tags such as **Lucky(X)**.

| Rating      | F   | E   | D   | B   | C   | A   | S   |
| ----------- | --- | --- | --- | --- | --- | --- | --- |
| Dex / Speed | -5  | 0   | 5   | 10  | 15  | 20  | 25  | 

##### Dealing Damage

- First, **Get the Base Damage**. Base Damage for Martial weapons is listed under Str, and Base Damage for Magic weapons is listed under Mag.
- Next, **Apply add any Damage modifiers that apply.**
    - On a Critical hit, double the Damage. This should be applied last.
    - The [Terrain Table]({% link _obsidian/officers-chess/Rulebook.md %}) modifies the Defense and Resistance of a Unit standing on certain tiles.
    - Tags on the Classes of either combatant or Tags on their Equipped weapons, such as the **Effective(X)** tag. 
- Then, **The defender applies Damage Reduction**. Damage Reduction for Martial weapons is listed under Def, and Damage Reduction for Magic weapons is listed under Res. 
    - Damage Reduction can from Tags as well.
- **The Defender reduces their HP by the Damage Total - Damage Reduction.**
    - If the Defender's HP is reduced to 0 after taking damage, the Target is Routed. 
        - An Routed unit is removed from the map and unable to return to the battle. 
        - Some victory conditions may require you to track how many Units have been routed on either side.
    - If the attacker had advantage from the [The Weapon Triangle]({% link _obsidian/officers-chess/Rulebook.md %}), the enemy unit will gain the [Broken Status.]({% link _obsidian/officers-chess/Rulebook.md %})

| Rating           | F   | D   | E   | C   | B   | A   | S   |
| ---------------- | --- | --- | --- | --- | --- | --- | --- |
| Base Damage      | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
| Damage Reduction | 0   | 1   | 2   | 3   | 4   | 5   | 6   |

##### Counter Attack and Follow Up

- After an Attack, **The Defender performs a Counter Attack if able.**
    - The unit's currently equipped weapon must be able to hit it's Attacker for it to counter. 
    - A unit cannot switch weapons, it must use the one it last used, even if that weapon cannot counter attack.
    - Counter Attacks follow the [Rulebook#Attack]({% link _obsidian/officers-chess/Rulebook.md %}) processes, but swap Attacker and Defender.
- After Counter Attack, **Determine if a Unit can Follow Up.**
    - A Follow Up is a second attack (made in the same process) a Unit gets to make after the Counter Attack.
    - **A Unit can only follow up if it's Avo (Speed - Weapon Weight) is 2 Ratings higher than it's opponent.**
    - A follow up does not occur if neither Unit meets the Avo condition.

| Rating         | F   | E   | D   | C    | B       | A          | S             |
| -------------- | --- | --- | --- | ---- | ------- | ---------- | ------------- |
| Follows Up on: | -   | -    | F   | F, E | F, E, D | F, E, D, C | F, E, D, C, B |

**Special note: Staves cannot counter attack or follow up. Staves also do not need to roll to hit when targeting an allied unit, they always hit.** 

##### The Weapon Triangle

| Weapon | Effective Against    |
| ------ | -------------------- |
| Swords | Axes                 |
| Lances | Swords               |
| Axes   | Lances               |
| Arts   | Tomes, Daggers, Bows |

When a unit attacks with advantage on the Weapon Triangle and deals damage, the [Break Status Effect]({% link _obsidian/officers-chess/Rulebook.md %}) is applied to the target. They immediately lose their ability to counter attack in the current combat, and cannot counter attack in the next one they're involved in. 

The break status cures itself after a combat where the unit started broken or if the unit is activated to take a turn. A broken unit cannot be further broken, it must cure the status before it can be broken again. 

#### Use a Staff

Staves always have at least two tags. The first is **Consumable(X)** which lists how many times the Staff may be used in a given battle. The second will be a [Special Action Tags]({% link _obsidian/officers-chess/Rulebook.md %}) that covers what happens when you use the Staff. 

Staff actions that target allies (such as **Heal(X)**) do not require a roll to hit, they automatically succeed. When targeting an enemy unit, roll to as per an attack action. The effect of the Tag takes place if the unit hits. Enemies may never counter attack a staff action, even if it otherwise would be able to. However, Staff Actions never follow up.

#### Use a Special Action

Some tags give a Unit access to Special Actions, they can take on their turn. These actions don't require an accuracy roll when the Target is an allied Unit. Find out more in [Special Action Tags]({% link _obsidian/officers-chess/Rulebook.md %}). Using these actions functions identically to a Staff. 

### Free Actions 

Free actions can be taken at anytime on a Unit's turn.

- **Equip** Change which Weapon or Accessory the unit has equipped from it's Inventory.
- **Discard** Remove an item from the Unit's Inventory permanently. This item is lost for the rest of the battle.
- **Trade** When a unit is adjacent to an allied unit, it can Trade any number of items between their Inventories. A Unit can only Trade with one Unit in a single Combat Turn. 

# Tags 

Tags are keyword that represent features of a Class, Weapon, Accessory, or Consumable. These keywords can be referenced by other Tags, can provide the Unit with it special rules or other mechanical benefits. Tags on a Weapon or Accessory only apply while that Weapon or Accessory is equipped. 

*Tags are grouped by the most likely place you'll find them (Classes, Weapons, etc) but can be provided anywhere as needed.*

## Class Tags

| Tag          | Description                                                                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Armor**    | This unit cannot be Broken.                                                                                                                          |
| **Backup**   | If an allied unit attacks a unit this unit could attack, that ally deals 3 extra damage. This only applies once per combat.                          |
| **Canto**    | After taking it's action, this unit can move up to 2 tiles before ending it's turn. (Terrain still applies.)                                         |
| **Cavalry**  | This unit gains one additional tile of movement.                                                                                                     |
| **Covert**   | Double Terrain bonuses for this unit.                                                                                                                |
| **Dragon**   |                                                                                                                                                      |
| **Flying**   | Unit ignores all Terrain Bonus and Penalties.                                                                                                        |
| **Mystical** | This unit ignore terrain bonuses when attacking.                                                                                                     |
| **Qi Adept** | When this unit is at full health, it may choose to take the first attack made against an allied unit adjacent to it. This attack's damage is halved. | 
| **Slow(X)**  | Unit can move X less tiles in a turn.                                                                                                                |

## Weapon Tags

| Tag                   | Description                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **AoE**               | Hits all targets in range.                                                                                                                  |
| **Bonus(Rating+X)**   | Increase the listed Rating by X.                                                                                                            |
| **Brave**             | Attack an additional time any time this weapon is used during an Attack action. (This applies to both the Attack, and potential Follow Up.) |
| **Complex**           | When using this weapon the unit will never get a Follow Up attack, even if it is faster.                                                    |
| **Consumable(X)**     | The item can be used X times before it is removed from the unit's inventory for the rest of the battle.                                     |
| **Cursed(Rating-X)**  | When this weapon is equipped, reduce Rating by X.                                                                                           |
| **Deadly(X)**         | Unit scores a critical hit when their roll to Hit is less than X. This effect stacks if a Class and Weapon both provide it.                 |
| **Drain**             | Recover HP equal to half of the damage dealt.                                                                                               |
| **Effective(tag)**    | Attacks against units with the noted tag do 5 extra Damage.                                                                                 |
| **Enchanted**         | Attacks with this Weapon are considered Magic attacks rather than Martial.                                                                  |
| **Exclusive(Class)**  | Can only be used by the tagged Class.                                                                                                       |
| **Heavy**             | In combat, this unit may not follow up, and always attacks second. If this unit hits, move the enemy back one tile.                         | 
| **Homing**            | This weapon always hits. It cannot score critical hits.                                                                                     |
| **Inaccurate(X)**     | When using this weapon, reduce the Unit's Dexterity Rating by X.                                                                            |
| **Inflict(Rating-X)** | Target unit has their Rating reduced by X until end of their turn. This effect does not stack.                                              |
| **Inverted**          | Reverse the Weapon Triangle when using this weapon.                                                                                         |
| **Nimble(X)**         | Reduce the crit range of enemies attacking this unit by X                                                                                   |
| **Piercing**          | Treat a Target's Defense or Resistance as E when using this Weapon.                                                                         |
| **Status(Effect)**    | On hit, apply the Effect tag to Target.                                                                                                     |
## Special Action Tags

Special Action tags each give a Unit access to a Special Action they can use, as defined in [Rulebook#Use a Special Action]({% link _obsidian/officers-chess/Rulebook.md %}). 

*Special actions typical come as a benefit of a given Class or are granted by using a Staff.*

| **Tag**           | Description                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------- |
| **Dance**         | Targets an adjacent allied unit that has already been activated this round. That unit can be activated again. |
| **Entrap**        | Move target enemy to an adjacent tile.                                                                        |
| **Freeze**        | Target cannot move on it's next turn. It may take any other actions.                                          |
| **Heal(X)**       | Heal the Target for X+Mag Damage.                                                                             | 
| **Rescue**        | Move Target to a tile adjacent to User.                                                                       |
| **Restore**       | Remove any Status Effect tags from Unit.                                                                      |
| **Rewarp**        | Move the user to an unoccupied tile within range.                                                             |
| **Torch(X)**      | Reveal X tiles around the User in Fog of War.                                                                 |
| **Vein(Terrain)** | Change the terrain of an unoccupied tile within range to the listed type for one round.                       |
| **Warp**          | Move target adjacent allied unit to an unoccupied tile within range.                                                   |

## Status Effects

Certain Tags (such as **Effect(Tag)**) can temporarily bestow a Tag onto another Unit. These Status Effect tags are typically given in battle rather than found on a Unit at the start of the battle. Each includes a way that the Tag will be removed from the Unit.

| **Tag**      | Description                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------- |
| **Barrier**  | Unit gains **Bonus(Res+1**) until end of next round.                                                    |
| **Broken**    | Unit cannot counter attack in the next combat it's involved in. Activating the unit clears this effect. |
| **Poisoned** | All attacks against the Unit deal an additional 1 point of damage.                                      |
| **Silenced** | Unit cannot use Tomes or Staves. Effect lasts one activation of the unit.                |

## Scenario Tags

Scenario Tags are tags that should only be used if the scenario calls for them. These tags are often applied at the start of the game to a number of a Player's Units and enable their Units to take a Special Action needed for the Scenario.

| **Tag**      | Description                                                                                                                                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Fleeing**  | This unit can take the Escape action on certain tiles. A unit that takes the escape action is removed from the board. This unit is not counted as Routed. This action can only be taken on predefined tiles. |
| **Leader**   | This unit can use the Seize action on specified tiles. A unit Seizing a tile ends the battle. This action can only be taken on predefined tiles.                                                             |
| **Raider** | This Unit can use the Raze Action on specified tiles. A unit Razing a tile turns the tile into a Ruins tile and removes all special effects of that tile. This action can only be taken on predefined tiles. |