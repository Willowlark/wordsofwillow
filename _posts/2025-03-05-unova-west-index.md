---
postdate: 2025-03-05
categories:
- Pokerole
- Modules
doku: UnovaWildWest
tags: rpgs modules pokerole
---
# Pokerole: Unova's Wild West!

This is a module set in the past of the Pokemon world, meant to invoke the feel of Pokemon: Legends Arceus. Unlike PLA, this game takes place in the Wild West! The module should cover one long session or two-three shorter ones, depending on how much the players explore. Key details include

- The module assumes guns aren't a thing, mostly because it's meant to emulate anime/PLA tone.
- Trainers are not common and most people consider them dangerous. 
- Trainers can have **up to two Pokemon** with them at the start of the game, and both can be up to **Amateur rank**. 
- Trainers can be targeted by Pokemon at any time, they are considered to always be in the fray. (They do not need to be included in Initiative if they don't intend to do more than order their Mon about) 

> Player Introduction
> Your character is a rarity in the Wild West, a Pokemon trainer. You've found a request, a telegram that was sent out to every corner of the country that was pinned to train bulletin boards everywhere. The request, which you've chosen to answer, reads as follows: 
> 
> > Help Request in Littlebank Town STOP
> > Wild pkmn attacking Town STOP
> > Looking for Pkmn trainers to drive them off STOP
> > Contact Mayor Sherman Sheppard Upon arrival STOP
> > Cash Reward STOP 
{: .prompt-tip }
# For the Storyteller

**[Click here for the module text itself.]({% link _obsidian/UnovaWildWest/Unova West Plot.md %})**

> A Note on Formatting
> In the module, you'll find various formatting styles. Callout blocks like these can be imagined as sidebars. *Italic text* can be read as GM notes and tips. `Code blocks` contain rolls the players will need to make, in the format of `attribute+skill`. If the code block has a `x#` at the end, that means the minimum number of successes is that number, not one. 
{: .prompt-tip }

There are two maps for this module. The first is of [Littlebank]({% link _obsidian/UnovaWildWest/Littlebank.md %}) Town, a small frontier town that has called for aid. The second is of the [Frontier]({% link _obsidian/UnovaWildWest/Frontier.md %}) surrounding it, made up as if it was a hand drawn map. The map of Littlebank isn't really necessary, but the Frontier map should be available as a handout. 

## Story Summary

The request was send out by [Sherman Sheppard]({% link _obsidian/UnovaWildWest/Sherman Sheppard.md %}), the mayor of [Littlebank]({% link _obsidian/UnovaWildWest/Littlebank.md %}). Lycanroc have been attacking the town, it's fields, and their wagons. People are scared and Mayor Sheppard is a beloved leader whose calling in strangers to help out of his own pocket. The PCs will see an attack on the town when they arrive and Sheppard will send them into the frontier to find the Lycanroc den. 

The twist, once the party navigate the frontier to find the Lycanroc, is that Mayor Sheppard's railroad expansion is preventing the Lycanroc from resting, making them angry and upset. The expected finale is the party return to town and confront Sheppard, who has been hiding the fact he has a Pokemon this whole time. 

| NPCs                 | Sex | Pokemon                                             | Notes                                         |
| -------------------- | --- | --------------------------------------------------- | --------------------------------------------- |
| [Sherman Sheppard]({% link _obsidian/UnovaWildWest/Sherman Sheppard.md %}) | M   | [Sheppard's Magmortor]({% link _obsidian/UnovaWildWest/Sheppard's Magmortor.md %}), [Sheppard's Electivire]({% link _obsidian/UnovaWildWest/Sheppard's Electivire.md %}) | The Mayor of Littlebank and a Railroad baron. |
| [Wilson Downs]({% link _obsidian/UnovaWildWest/Wilson Downs.md %})     | M   | [Wilson's Machamp]({% link _obsidian/UnovaWildWest/Wilson's Machamp.md %})                                | The Mayor's right hand man.                   |
| [Sophia Walter]({% link _obsidian/UnovaWildWest/Sophia Walter.md %})    | F   |                                                     | The Mayor's secretary.                        |

The story is broken up into a few sections. It begins with the party arriving in Littlebank and **finding Mayor Sheppard**. They'll meet with him and be able to ask about the telegram and job they're being asked to do. 

The second section starts when their interview with Sheppard is interrupted by **Lycanroc attack** on a man returning to town. The PCs are expected to drive the Lycanroc off. 

The third section is a **series of encounters** that occur on the routes through the [Frontier]({% link _obsidian/UnovaWildWest/Frontier.md %}) as the party searches for the Lycanroc's den. On 

- [Braxien Bluff]({% link _obsidian/UnovaWildWest/Braxien Bluff.md %}) has some Braxien and a Delphox surround the PCs, but they're willing to negotiate to let the trainers pass. This is the the X in southwest. 
- [Hippowden Hollow]({% link _obsidian/UnovaWildWest/Hippowden Hollow.md %}) involves the players rescuing a man from a Hippowden's sandy den. This is the western X.
- [Manectric Meadows]({% link _obsidian/UnovaWildWest/Manectric Meadows.md %}) has the players being hunted by a group of Manectric while traveling through open fields. This is the center most X.
- [Phanpy Peaks]({% link _obsidian/UnovaWildWest/Phanpy Peaks.md %}) puts the players traveling through a series of valleys and Phanpy chase after them, rolling from the peaks. This is the eastern X.

The fourth section is the **Lycanroc Den**, where the players will not only find the Lycanroc, but the railroad construction site where [Wilson Downs]({% link _obsidian/UnovaWildWest/Wilson Downs.md %}) is in charge. 

The final section of the story is (presumably) the return to Littlebank where the party confronts Wilson and Sheppard in a mexican stand off pokemon battle. 

```mermaid
graph TD

1((Town))
2[Arrive in Town]
3[Attack While Mayor Explains the Problem]
3.5((Frontier))
4[Braxien Bluff]
5[Hoppowden Hollow]
10[Manectric Meadows]
11[Phanpy Peaks]
12[Lycanroc Den]
5.5((Town))
6[Return to Confront Mayor shootout style]
1 --> 2 --> 3 --> 3.5
3.5 --> 4 --> 5 --> 12 
3.5 --> 10 --> 12 
3.5 --> 11 --> 12 
12 --> 5.5 --> 6
```