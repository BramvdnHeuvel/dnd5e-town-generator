import random

nm1 = ["", "", "", "", "b", "br", "c", "cr", "h", "l", "m", "n", "p", "r", "t", "v", "w", "z"]
nm2 = ["a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "au", "ai", "ea", "ei"]
nm3 = ["d", "dr", "g", "gg", "gr", "gw", "k", "kr", "kl", "l", "ld", "lg", "lw", "lr", "lt", "n", "nr", "nw", "nl", "r", "rn", "rr", "rw", "rl", "v", "vr", "w"]
nm4 = ["a", "i", "a", "i", "a", "i", "a", "i", "a", "i", "a", "i", "e", "a", "i", "e", "a", "i", "e", "o", "o", "u", "u", "ee", "ia", "ie", "ai", "ei"]
nm5 = ["d", "l", "m", "n", "t", "v"]
nm6 = ["l", "m", "n", "nt", "r"]
nm7 = ["", "", "", "", "", "br", "d", "dr", "h", "l", "m", "n", "ph", "r", "rh", "th", "v", "w", "z"]
nm8 = ["a", "i", "o", "a", "i", "o", "a", "i", "o", "a", "i", "o", "a", "i", "o", "a", "i", "o", "e", "e", "ia", "io", "ea", "eo"]
nm9 = ["d", "j", "l", "ld", "ldr", "lv", "ll", "lt", "m", "mm", "mn", "n", "nr", "nv", "nl", "ndr", "nm", "r", "rd", "rk", "rs", "s", "sr", "sl", "v"]
nm10 = ["a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "ea", "ia", "ie"]
nm11 = ["l", "m", "n", "r", "s", "z"]
nm12 = ["a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "au", "ou", "oe"]
nm13 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "h", "l", "m", "n", "r"]

c = random.choice

def female():
    choice = random.randint(1, 2)

    if choice == 1:
        return c(nm7) + c(nm8) + c(nm9) + c(nm10) + c(nm13)
    if choice == 2:
        return c(nm7) + c(nm8) + c(nm9) + c(nm10) + c(nm11) + c(nm12) + c(nm13)

def male():
    choice = random.randint(1, 2)

    if choice == 1:
        return c(nm1) + c(nm2) + c(nm3) + c(nm4) + c(nm6)
    if choice == 2:
        return c(nm1) + c(nm2) + c(nm3) + c(nm4) + c(nm5) + c(nm4) + c(nm6)

def last_name():
    return c(nm1) + c(nm2) + c(nm3) + c(nm4) + c(nm11) + c(nm12) + c(nm13)