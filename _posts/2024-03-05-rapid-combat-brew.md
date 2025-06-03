---
doku: brewery
dokuflags: ''
postdate: 2024-03-05
categories: [Pokerole, Brews]
tags: homebrew pokerole rpgs
---
# Rapid Combat: a Pokerole Combat Brew

## Narrative Notes

This home brew aims to make Pokerole playable without Multiple Actions. The reasoning for this is rooted in watching the anime: every combat exchange goes something like this: "Pikachu use attack!" followed by "Dodge it!" or "Block it with attack!". Pokerole already captures this in it's evade and clash mechanics, which means most of the work is done here! 

Why this hack exists is Pokerole rules as written limits the number of times you can use a move, evade, and clash in a combat round. While this adds a tactical layer to action conservation, but it adds more decisions to the combat flow and can make uneven fights impossible due to action imbalance. 
## Mechanics

These are the changes you'll make the default Pokerole combat system in order to play with one action turns. Some of these are directly related to removing multiple actions, some are recommendations to smooth the transition. if you don't like one, don't use it! That's your choice as a GM.

- There are no longer *Rounds*. Moves that reference a number of rounds should be treated as referencing multiple Turns. 
    - Whenever *Damage* is dealt "*at the end of the round*", such as for the **Hail** weather condition or from a **Burn**, that damage is dealt as "One die of Damage at the end of their turn" instead. The Pokemon will roll a single die and only suffer damage on a success. 
    - Whenever a move has a *Duration of X Rounds*, the duration of that move becomes the same number of turns for the user of the move. EX: Hail will last for four turns of the user, starting from the turn after Hail is executed. With Hail used on as Turn 1, the opponent's first turn of Hail will be turn 2, then turn 4, 6, and 8 while the user's Hail turns will be 3, 5, 7, and 9. 
    - Whenever an effect references *next, last, or this Round*, the effect will apply on the last turn, current turn, or next turn depending on the effect. Examples: 
        - **Venom Drench**: If an affected foe is poisoned or becomes poisoned ~~in the same Round you used this Move~~ *before the end of your next turn*, then Reduce its Strength, Special, and Dexterity.
        - **Uproar** ~~For the rest of the Round~~, *Until the end of your next turn,* no Pokemon can fall asleep. If a Pokemon was asleep it wakes up. Sound Based Move.
        - **Retaliate**: If an ally fainted during ~~this or the last Round~~ *since your last turn*, add 3 Extra Dice to the Damage Pool. This effect can only be used once per Ally.
        - **Rage Powder**: Priority 2. During ~~this Round~~ *until your next turn*, all damage moves from any foe must target the User.
        - **Mat Block**: Shield. Reduce 3 Dice from the foe's Damage Pool. This Move only works the first ~~Round~~ *turn* the User has been out.
        - Some moves, such as **Future Sight** or **Double Team**, might work better with individually modified rules. Double Team might be better as a "+2 to the User's Evasion rolls until they suffer damage" and Future Sight might be "After 3 turns, this attack deals Damage." While specific takes can be added, my goal here is not to rewrite a chunk of moves in this document. Use your judgement, or ping in the Pokerole Discord for ideas.
- Whenever you are *attacked*, you may choose to Evade, Clash, or use another Reaction freely. These are always available to you. 
- Whenever you *attack*, all of your moves are always available. 
- When spending *Will Points* in combat, they may be spent after the attacker has rolled their attack AND after the Target has reacted. Both sides may spend as many Will Points as they have available to try and exceed or meet their opponent respectively. Each Will Point spend adds one success to the Pokemon's roll, there are no additional dice rolls or rerolls. Will Points can cause the Pokemon to exceed their normal maximum for a dice pool (IE, 5 successes on 4 dice). 
- When you use *Successive Actions*, you may make sequential attacks until the opponent successfully reactions to your attack, or until you use a maximum of 5 attacks in a row. 
- When you *Switch Pokemon* without a Switcher Move, you must do so on one of your turns and the action of Switching uses up your turn. 