import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["c", "d", "dh", "j", "jh", "k", "kh", "m", "n", "r", "v", "z"]
nm2 = ["a", "e", "i", "o", "u"]
nm3 = ["d", "dd", "g", "gl", "hn", "hl", "hr", "l", "lg", "lm", "ld", "ln", "lz", "m", "mn", "mr", "n", "nn", "nd", "nl", "nr", "nv", "r", "rl", "rn", "rv", "rz", "v", "vn", "z"]
nm4 = ["", "", "", "", "", "", "", "", "b", "bh", "d", "dh", "f", "fl", "h", "l", "m", "n", "s", "sh", "vl", "w", "wh", "y"]
nm5 = ["a", "e", "o", "u", "a", "e", "o", "u", "i"]
nm6 = ["d", "dd", "dr", "gr", "gl", "hl", "hn", "l", "lr", "lt", "lth", "ml", "nl", "nth", "nr", "r", "rn", "rl", "rr", "s", "sh", "st", "sl", "sn", "t", "th", "tr", "thr", "tl", "thl"]
nm7 = ["d", "h", "l", "m", "n", "r"]
nm8 = ["e", "y", "y", "y", "y", "y", "y"]
nm9 = ["", "", "", "b", "bh", "d", "dh", "j", "g", "l", "m", "n", "p", "r", "s", "v", "z"]
nm10 = ["a", "u", "a", "u", "a", "u", "e", "o"]
nm11 = ["b", "d", "g", "gh", "hl", "hn", "hm", "hr", "l", "n", "m", "r", "v"]
nm12 = ["a", "o", "a", "o", "e", "u"]
nm13 = ["d", "g", "l", "ll", "ln", "lm", "lv", "m", "mn", "n", "ns", "nz", "r", "rs", "s", "sn", "x", "z"]

c = random.choice

def female():
    if random.random() < 0.5:
        return (c(nm4)+c(nm5)+c(nm6)+c(nm8)+'n').capitalize()
    return (c(nm4)+c(nm5)+c(nm6)+c(nm5)+c(nm7)+c(nm8)+'n').capitalize()

def male():
    return (c(nm1)+c(nm2)+c(nm3)+c(nm2)+'s').capitalize()

def last_name():
    return (c(nm9)+c(nm10)+c(nm11)+c(nm12)+c(nm13)+'ath').capitalize()
