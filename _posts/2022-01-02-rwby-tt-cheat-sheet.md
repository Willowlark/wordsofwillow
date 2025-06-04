---
doku: brewery
postdate: 2022-01-02
categories:
  - RWBYTTRPG
  - Resources
tags:
  - resources
  - rwbyttrpg
  - rwby
description: A RWBY TTRPG cheat sheet for key mechanics.
---
# Mechanics

## Skill Checks

- All skill checks begin on `2d10`. 
- These first two d10 are special.
	- When both are 10, you get a natural 20. Natural 20's automatically succeed.
	- When both are 1, you get a natural 2. Natural 2's automatically fail.

## Rule of Cool

- Rule of Cool is shared by the whole party. 
- Rule of Cool is awarded after you succeed at something cool. Some inspiration:
	- Two characters working in tandem. 
	- Clever role-play.
	- Using enemies against each other. 
	- Lateral thinking. 
	- Three-dimensional movement.
	- Doing things according to character desires even if they complicate things for the player.
• Making a particularly cringe-worthy pun or one liner.
- Rule of Cool is added to all **Skill Checks** (This includes Accuracy) and **Damage Rolls**. 
- When you roll a natural 20, automatically get a Rule of Cool and apply it to that roll.
- When you roll a natural 2, lose a Rule of Cool.

# Combat
1. Roll Initiative, take the highest from the allies, if higher than highest enemy `Speed` stat, Allies act first. 
	- `WIL+PER` When attacking firest
	- `AGI+PER` When engaged by someone else
2. Allies and Enemies act as a group on their turn, each gets three actions that can be taken in any order. **Up to Two Actions** can be Major. 
	1. Allies
		- **Major Actions**
			1. Attack an enemy (See [Attacks](#attacks) table) 
				- Optionally, Capacity Boost (Spend 1 Capcity, +1 Accuracy)
				- If Accuracy roll 5 or more greater than threshold, apply [Defense Thresholds](#defense-thresholds).
				- If Accuracy roll of Attack > Target's Defense Threshold, Deal Damage.
			2. Use Semblance (Non combat use) 
				- Semblance Infusion (Spend 2 Cap to add Element dust effect)
			3. Reload (Restore **DIS+1** Capacity)
			4. **Two Actions** Charge Attack (Attack, spend 1-3 Capacity, add Capacity spent to Accuracy and Damage)
		- **Minor Actions**
			1. Move 1 range increment closer/further from someone
			2. Make a Skill check
				- Capacity Boost (Spend 1 Capcity, +1 to Skill Check)
			3. Grapple target
				- `STR+PER` versus target's `Speed`. On a Success with RoC:
				- Equal to target's Threat: Target held in place
				- Less than target's Threat: Move with Target when it moves
				- Greater than target's Threat: Allows you to - 
					- Move Target with you as major action
					- Throw with `STR+END` versus Defense Threshold.
	2. Enemies
		1. Move 1 range increment closer/further from someone
		2. Make an Attack
			1. Target choses a Defense Roll (see [Defending](#defending))
			2. If roll < than attackers `Attack` Attribute, deal Damage listed in block.
		3. Use a special ability on stat block

# Attack Resolution

## Attacks

| Attack              | Accuracy                 | Range       | Damage  | Capacity | Special       |
| ------------------- | ------------------------ | ----------- | ------- |:--------:| ------------- |
| Melee Weapon        | Melee Weapon Style       | Adjacent    | 1d6+STR |          |               |
| Ranged Weapon       | Ranged Weapon Style      | Long Range  | 1d6     |    -1    |               |
| Thrown Melee Weapon | Melee Weapon Style       | Close Range | 1d6     |          | Lose Weapon   |
| Semblance           | `WIL+Relevant Attribute` | Close       | WIL     |          | Requires Aura |
| Unarmed             | `STR+END`                | Adjacent    | STR     |          |               |
| Dust Phial          | `DIS + Color Dependent`  | Close       | DIS     |    -2    |               |

### Defense Thresholds

When an Accuracy Roll is a certain amount higher than the Defense Threshold of the Target being attacked, the attack gains additional effects. The following list shows the effects under how many points are required to achieve them. Chose one from each tier that applies. IE, if the accuracy roll is 15 over, chose a +5, +10, and +15.

Optionally, you can take a lower tier bonus instead of a higher tier (a +5 rather than a +10).

- **5 Points Over**
	- Critical Damage (Can select multiple times, add damage listed in Stat Block)
	- Stagger Target
	- Confuse Target
- **10 Points Over**
	- Maximize Damage (All d6s rolled for Damage are 6s)
	- Cripple Target
	- Collateral Damage (Any enemy with equal or less Defense that's adjacent to the Target takes all Damage and Effects from this attack as well.)
- **15 Points Over** 
	- Cleave Target
	- Stun Target
- **20 Points Over**
	- Dispatch Target (Reduce Target's health to 0.)

# Tables

## Defending

| Name      | Roll      | On Success                                                             | Description                    |
|:--------- | --------- | ---------------------------------------------------------------------- | ------------------------------ |
| Parry     | `STR+PER` | Deal 3 points of damage to Attacker                                    | Physically parrying the blow   |
| Dodge     | `AGI+PER` | Move 1 Range increment OR do one minor action that doesn't need a roll |                                |
| Resist    | `END+PER` | **On Failure**, can take 1 HP instead of damage to Aura                | Tanking the hit                |
| Semblance | `WIL+PER` | **Before Roll** Can Empower for 1 Aura, **Requires** 1+ Aura           | Use Semblance to avoid injury. |
| Dust      | `DIS+PER` | Can Capacity Boost the check (1 Capacity, +1), **Cost** -1 Dust        | Use Dust                       |

## Range

| Increment | Feet Away | Movements Away |
|:--------- | --------- | -------------- |
| Adjacent  | 5 Feet    | 0              |
| Close     | 30 Feet   | 1              |
| Medium    | 45 Feet   | 2              |
| Long      | 60 Feet   | 3              |
| Distant   | 75+       | Multiple       |

## Status Effects

| Name      | Effect                                                                                     |
|:--------- | ------------------------------------------------------------------------------------------ |
| Blinded   | Decreate Attack Threshold by 5 and have disadvantage on attacks next Action Sequence       |
| Cleaved   | Decrease all Defense Thresholds by 5                                                       |
| Confused  | Decrease Target's Specal Threshold by 5 for and cannot use semblance next Action Sequence. |
| Cripped   | Decrease Attack Threshold by 5.                                                            |
| Held      | Target cannot make a move action next Action Sequence.                                     |
| Helpless  | Cannot take any actions rest of Scene. (Unconscious)                                       |
| Stunned   | Cannot take any actions next Action Sequence                                               |
| Staggered | Reduce Target's `Speed` by 5 for and lose one action during next Action Sequence           |
| Weaken    | Until hit, Defense threshold reduced by 5. Disadvantage on attacks next Action Sequence    |
| Cover     | Increase Defense against Ranged Attacks by 5                                               |
| Disarmed  | Reduce Attack Threshold by 5, minor action to pick up weapon                               |

## Skills

| X   | STR        | AGI             | END         | WIL             | PER        | DIS       |
|:--- | ---------- | --------------- | ----------- | --------------- | ---------- | --------- |
| STR | X          | Jump            | Lift        | Intimidate      | Grapple    | Break     |
| AGI | Jump       | X               | Climb       | Sleight of Hand | Dodge      | Stealth   |
| END | Life       | Climb           | X           | Performance     | Resistance | Resolve   |
| WIL | Intimidate | Sleight of Hand | Performance | X               | Influence  | Hacking   |
| PER | Grapple    | Dodge           | Resistance  | Influence       | X          | Detection |
| DIS | Break      | Stealth         | Resolve     | Hacking         | Detection  | X         |

## Dust 
- Red Dust - Fire
	- **Incindiary** +1 to each Damage Die
	- **Explosive** Collateral Damage Threshold reduced to +5, adjacent enemies exploded to close range to target.
	- `END+DIS`
- Yellow Dust - Earth
	- **Fissure** Stagger targets
	- **Armor Piercing**  ignore cover, one adjacent enemy with <= Defense takes 1d6 Damage
	- `STR+DIS`
- Green Dust - Wind
	- **Featherweight** Thrown Melee weapon Range to Medium, returns to hand
	- **Horizon** No distance limit
	- `AGI+DIS`
- Blue Dust - Water
	- **Lash** Melee weapon attacks can be made at close range
	- **Whirlpool** Confuse targets
	- `AGI+DIS`
- Orange Dust - Lightning
	- **Arc** one adjacent enemy with <= Defense takes 1d6 Damage
	- **Stun** Stagger targets
	- `WIL+DIS`
- Violet Dust - Force 
	- **Kinetic** Push target one range increment further away
	- **Concussion** Move 1 Range increment away from target
	- `STR+DIS`
- Brown Dust - Acid
	- **Rust** Weaken target
	- **Bleed**  +1 to each Damage Die
	- `END+DIS`
- Pink Dust - Sonic
	- **Scream** Confuse targets
	- **Echo** Sound of weapons comes from impact, not source 
	- `PER+DIS`
- White Dust - Ice
	- **Freeze** Target is Held
	- **Chill** Target  Reduce damage of Target's next successful attack by 2, min 1.
	- `WIL+DIS`
- Black Dust - Light
	- **Star** Blind targets
	- **Barrier** Attacker gains cover status until they move or next action sequence
	- `PER+DIS`
- Amethyst Dust - Mind
	- **Charm** target focuses attacker, can only attack them and becomes unaware of medium+ range threats during their next action sequence
	- **Nullifier** Target cannot make special attacks until next action sequence
	- `WIL+DIS`
- Emerald Dust - Life
	- **Growth** Target is Held
	- **Bramble** Any creature that moves in area within close range of target next action sequence takes 1d6 damage
	- `AGI+DIS`
- Silver Dust - Time
	- **Rewind** Target moves back to it's position last action sequence
	- **Pause** Target stunned, but cannot be interacted while stunned.
	- `PER+DIS`
- Gold Dust - Space
	- **Neutron** - All enemies in close range with < Defense Threshold are pulled adjacent
	- **Warp** Open portal between character and target, either swap with target or move adjacent to.
	- `STR+DIS`