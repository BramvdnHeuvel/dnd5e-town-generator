import random

nm1 = ["", "", "", "", "", "c", "cl", "cr", "d", "g", "gr", "h", "k", "kh", "kl", "kr", "q", "qh", "ql", "qr", "r", "rh", "s", "y", "z"]
nm2 = ["a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "ae", "aia", "ee", "oo", "ou", "ua", "uie"]
nm3 = ["c", "cc", "k", "kk", "l", "ll", "q", "r", "rr"]
nm4 = ["a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "aa", "ea", "ee", "ia", "ie"]
nm5 = ["", "", "", "", "c", "ck", "d", "f", "g", "hk", "k", "l", "r", "rr", "rc", "rk", "rrk", "s", "ss"]
br = ""

def female():
    if random.random() < 0.5:
        return random.choice(nm1) + random.choice(nm2) + random.choice(nm3)
    return random.choice(nm1) + random.choice(nm2) + random.choice(nm3) + random.choice(nm4) + random.choice(nm5)

def male():
    return female()

def last_name():
    return female()

def full_name(gender):
    if gender == 'male':
        return male() + ' ' + last_name()
    else:
        return female() + ' ' + last_name()