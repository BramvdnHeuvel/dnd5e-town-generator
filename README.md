# The dnd5e town generator

This repository contains a program that allows you to look up humongous cities in a "memory free" manner.

## How does it work?

The dnd5e-town-generator makes use of what's called pseudo-randomness.
Pseudo-randomness is given a determined seed, which will always reproduce the same "random" values.

We are using this property to regenerate the town.
This means that the program is way more memory-friendly, but requires quite a bit more CPU-time,
as the town needs to be regenerated every time.

The reason why that's efficient, is the assumption that a Dungeon Master will only look up data
at a human's speed - not at a computer's. This means that they'll look up people at a relatively
low speed.