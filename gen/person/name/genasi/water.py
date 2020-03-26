import random
from gen.person.name.human import last_name

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

NAMES = ["Agua", "Aqua", "Azure", "Basin", "Bath", "Bathe", "Beck", "Bore", "Branch", "Brine", "Brook", "Cleanse", "Course", "Creek", "Current", "Dabble", "Damp", "Deluge", "Dew", "Dewdrop", "Douse", "Downpour", "Drain", "Drench", "Drift", "Drip", "Drizzle", "Drop", "Droplet", "Drown", "Eagre", "Estuary", "Expanse", "Flood", "Flow", "Flux", "Fog", "Fountain", "Geyser", "Gush", "Hose", "Hydra", "Hydrogen", "Influx", "Jet", "Lagoon", "Lake", "Lakelet", "Liquid", "Mere", "Mist", "Monsoon", "Neptune", "Ocean", "Paddle", "Plash", "Plunge", "Pond", "Pool", "Precip", "Puddle", "Quagmire", "Rain", "Rill", "Rinse", "Ripple", "River", "Rivulet", "Run", "Runnel", "Rush", "Sea", "Seiche", "Shower", "Soak", "Spatter", "Splash", "Spout", "Spring", "Sprinkle", "Storm", "Stream", "Streamlet", "Surf", "Surge", "Swish", "Tear", "Teardrop", "Tempest", "Tidal", "Tide", "Torrent", "Tributary", "Tsunami", "Typhoon", "Vapor", "Wash", "Wave", "Well", "Wet"]

def male():
    return random.choice(NAMES)

def female():
    return random.choice(NAMES)