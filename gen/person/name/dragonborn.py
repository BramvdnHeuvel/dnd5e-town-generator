import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["Ali", "Ar", "Ba", "Bal", "Bel", "Bha", "Bren", "Caer", "Calu", "Dur", "Do", "Dra", "Era", "Faer", "Fro", "Gre", "Ghe", "Gora", "He", "Hi", "Ior", "Jin", "Jar", "Kil", "Kriv", "Lor", "Lumi", "Mar", "Mor", "Med", "Nar", "Nes", "Na", "Oti", "Orla", "Pri", "Pa", "Qel", "Ravo", "Ras", "Rho", "Sa", "Sha", "Sul", "Taz", "To", "Trou", "Udo", "Uro", "Vor", "Vyu", "Vrak", "Wor", "Wu", "Wra", "Wul", "Xar", "Yor", "Zor", "Zra"]
nm2 = ["barum", "bor", "broth", "ciar", "crath", "daar", "dhall", "dorim", "farn", "fras", "gar", "ghull", "grax", "hadur", "hazar", "jhan", "jurn", "kax", "kris", "kul", "lasar", "lin", "mash", "morn", "naar", "prax", "qiroth", "qrin", "qull", "rakas", "rash", "rinn", "roth", "sashi", "seth", "skan", "trin", "turim", "varax", "vroth", "vull", "warum", "wunax", "xan", "xiros", "yax", "ythas", "zavur", "zire", "ziros"]
nm3 = ["Ari", "A", "Bi", "Bel", "Cris", "Ca", "Drys", "Da", "Erli", "Esh", "Fae", "Fen", "Gur", "Gri", "Hin", "Ha", "Irly", "Irie", "Jes", "Jo", "Ka", "Kel", "Ko", "Lilo", "Lora", "Mal", "Mi", "Na", "Nes", "Nys", "Ori", "O", "Ophi", "Phi", "Per", "Qi", "Quil", "Rai", "Rashi", "So", "Su", "Tha", "Ther", "Uri", "Ushi", "Val", "Vyra", "Welsi", "Wra", "Xy", "Xis", "Ya", "Yr", "Zen", "Zof"]
nm4 = ["birith", "bis", "bith", "coria", "cys", "dalynn", "drish", "drith", "faeth", "fyire", "gil", "gissa", "gwen", "hime", "hymm", "karyn", "kira", "larys", "liann", "lyassa", "meila", "myse", "norae", "nys", "patys", "pora", "qorel", "qwen", "rann", "riel", "rina", "rinn", "rish", "rith", "saadi", "shann", "sira", "thibra", "thyra", "vayla", "vyre", "vys", "wophyl", "wyn", "xiris", "xora", "yassa", "yries", "zita", "zys"]

nm5 = ["", "", "", "", "c", "cl", "cr", "d", "dr", "f", "g", "k", "kl", "kr", "l", "m", "my", "n", "ny", "pr", "sh", "t", "th", "v", "y"]
nm6 = ["a", "e", "i", "a", "e", "i", "o", "u", "a", "e", "i", "a", "e", "i", "o", "u", "a", "e", "i", "a", "e", "i", "o", "u", "aa", "ia", "ea", "ua", "uu"]
nm7 = ["c", "cc", "ch", "lm", "lk", "lx", "ld", "lr", "ldr", "lt", "lth", "mb", "mm", "mp", "mph", "mr", "mt", "nk", "nx", "nc", "p", "ph", "r", "rd", "rj", "rn", "rrh", "rth", "st", "tht", "x"]
nm8 = ["c", "cm", "cn", "d", "j", "k", "km", "l", "n", "nd", "ndr", "nk", "nsht", "nth", "r", "s", "sht", "shkm", "st", "t", "th", "x"]
nm9 = ["d", "j", "l", "ll", "m", "n", "nd", "rg", "r", "rr", "rd"]
nm10 = ["c", "d", "k", "l", "n", "r", "s", "sh", "th"]

choose = random.choice

def female():
    return random.choice(nm3) + random.choice(nm4)

def male():
    return random.choice(nm1) + random.choice(nm2)

def last_name():
    choice = random.randint(1, 3)

    if choice == 1:
        return (choose(nm5) + choose(nm6) + choose(nm7) + choose(nm6) + choose(nm10)).capitalize()
    if choice == 2:
        return (choose(nm5) + choose(nm6) + choose(nm7) + choose(nm6) + choose(nm8) + choose(nm6) + choose(nm10)).capitalize()
    if choice == 3:
        return (choose(nm5) + choose(nm6) + choose(nm7) + choose(nm6) + choose(nm8) + choose(nm6) + choose(nm9) + choose(nm6) + choose(nm10)).capitalize()

if __name__ == '__main__':
    last = last_name()
    print(female() + ' ' + last)
    print(male() + ' ' + last)