import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["", "", "", "b", "d", "f", "h", "j", "l", "m", "n", "p", "r", "s", "t", "v", "w", "y"]
nm2 = ["a", "i", "o", "u", "a", "i", "o", "u", "a", "i", "o", "u", "a", "i", "o", "u", "ee", "ie", "ea", "ae", "ai", "oo", "ou"]
nm3 = ["c", "g", "gs", "k", "ks", "kt", "m", "n", "rx", "rt", "rs", "s", "sk", "t", "ts", "x", "z"]

c = random.choice

def male():
    return (c(nm1) + c(nm2) + c(nm3)).capitalize()

def female():
    return male()

def last_name():
    return (c(nm1) + c(nm2) + c(nm3) + c(nm2) + c(nm3)).capitalize()
    