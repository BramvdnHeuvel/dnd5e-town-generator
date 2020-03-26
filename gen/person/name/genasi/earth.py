import random
from gen.person.name.human import last_name

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

NAMES = ["Adamant", "Agate", "Alabaster", "Amethyst", "Azurite", "Basalt", "Bedrock", "Block", "Boulder", "Brick", "Callous", "Citrine", "Clay", "Cliff", "Cobble", "Cobblestone", "Crag", "Crystal", "Dense", "Diamond", "Emerald", "Flint", "Fossil", "Fossilstone", "Garnet", "Gem", "Geo", "Geode", "Granite", "Gravel", "Grime", "Ground", "Hill", "Hunk", "Ingot", "Jade", "Jewel", "Lapis", "Lazuli", "Limestone", "Lodge", "Lump", "Malachite", "Marble", "Marmoreal", "Mason", "Masonry", "Mineral", "Monolith", "Moonstone", "Mountain", "Nugget", "Obsidian", "Onyx", "Opal", "Ore", "Pebble", "Pellet", "Peridot", "Precious", "Quarry", "Quartz", "Quartzite", "Rock", "Rocky", "Rough", "Rubble", "Ruby", "Rugged", "Sand", "Sandstone", "Sapphire", "Sediment", "Shelf", "Slab", "Slate", "Soapstone", "Solid", "Spinel", "Stone", "Stony", "Sturdy", "Terra", "Tile", "Topaz", "Travertine", "Turf", "Umber", "Wedge", "Zircon"]

def male():
    return random.choice(NAMES)

def female():
    return random.choice(NAMES)