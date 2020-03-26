import random
from gen.person.name.human import last_name

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

NAMES = ["Aerate", "Aerial", "Air", "Ascend", "Atmosphere", "Aura", "Aviate", "Azure", "Blast", "Blow", "Breath", "Breeze", "Celeste", "Celestial", "Chinook", "Cruise", "Current", "Cyclone", "Draft", "Drift", "Eddy", "Empyrean", "Fan", "Float", "Flow", "Flurry", "Flute", "Flutter", "Fly", "Funnel", "Gale", "Gasp", "Glide", "Gust", "Heave", "Heaven", "Hiss", "Hover", "Hurricane", "Lift", "Mistral", "Murmur", "Oxygen", "Ozone", "Pipe", "Pneumatic", "Puff", "Rise", "Sail", "Shriek", "Sigh", "Sky", "Soar", "Squall", "Storm", "Stratosphere", "Surge", "Tempest", "Tornado", "Troposphere", "Tumult", "Turbine", "Turbulence", "Twister", "Vent", "Waft", "Wheeze", "Whiff", "Whirl", "Whirlwind", "Whisk", "Whistle", "Wind", "Wing", "Zephyr"]

def male():
    return random.choice(NAMES)

def female():
    return random.choice(NAMES)