import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["", "", "", "", "d", "g", "h", "k", "m", "n", "r", "s", "sn", "t", "v", "z"]
nm2 = ["a", "e", "i", "o", "u"]
nm3 = ["b", "bl", "d", "dr", "g", "gg", "gl", "gn", "gr", "hz", "hr", "hl", "hs", "k", "kk", "kr", "kl", "kb", "kd", "l", "ld", "lb", "lt", "ll", "lp", "lg", "p", "pl", "pp", "r", "rt", "rp", "rb", "rk", "t", "tr", "tl", "v", "vl", "vn"]
nm4 = ["", "", "", "", "", "d", "g", "gs", "k", "ks", "m", "n", "r", "rn", "s", "ss", "tt", "v", "x"]

c = random.choice

def male():
    if random.random() < 0.5:
        return (c(nm1) + c(nm2) + c(nm4)).capitalize()
    return (c(nm1) + c(nm2) + c(nm3) + c(nm2) + c(nm4)).capitalize()

def female():
    return male()

def last_name():
    return (c(nm1) + c(nm2) + c(nm3) + c(nm2) + c(nm3) + c(nm2) + c(nm4)).capitalize()
