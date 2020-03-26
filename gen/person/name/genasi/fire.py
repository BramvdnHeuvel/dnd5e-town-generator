import random
from gen.person.name.human import last_name

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

NAMES = ["Ablaze", "Alight", "Ardor", "Ardour", "Arson", "Ash", "Austral", "Bake", "Beacon", "Blaze", "Blight", "Boil", "Bonfire", "Brand", "Broil", "Burn", "Calcine", "Candle", "Cauterize", "Char", "Charcoal", "Cinder", "Coal", "Combust", "Conflagration", "Cremate", "Crisp", "Dante", "Dantean", "Ember", "Enkindle", "Explosion", "Fervor", "Fever", "Fiery", "Flame", "Flare", "Flash", "Flicker", "Flux", "Forge", "Frizzle", "Fry", "Fuego", "Fuel", "Fume", "Furnace", "Glare", "Gleam", "Glint", "Glow", "Grill", "Heat", "Hell", "Hellfire", "Hot", "Igneous", "Ignite", "Ignition", "Incendiary", "Incinerate", "Infernal", "Inferno", "Kiln", "Kindle", "Lantern", "Lava", "Light", "Lit", "Magma", "Melt", "Nether", "Oven", "Parch", "Phoenix", "Piping", "Pyre", "Pyro", "Roast", "Scald", "Scorch", "Scoria", "Sear", "Seethe", "Shine", "Singe", "Sizzle", "Smoke", "Smolder", "Soot", "Spark", "Sultry", "Sun", "Swelter", "Thermal", "Thermo", "Tinder", "Toast", "Torch", "Torrid", "Volcano", "Warmth", "Wildfire", "Wither"]

def male():
    return random.choice(NAMES)

def female():
    return random.choice(NAMES)