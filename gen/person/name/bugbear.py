import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["b","br","chr","d","g","gh","hr","kh","n","r","st","t","th","v","z","zh"]
nm2 = ["a","e","i","o","u"]
nm3 = ["d","dd","dr","g","gh","gg","gr","rr","rd","rg","rn","t","tt","tr","v","vr","z","zz"]
nm4 = ["a","i","o","u"]
nm5 = ["k","lk","mkk","n","nn","nk","r","rk","rr","th"]

c = random.choice

def male():
    if random.random() < 0.5:
        return (c(nm1) + c(nm2) + c(nm3) + c(nm4) + c(nm5)).capitalize()
    return (c(nm1) + c(nm4) + c(nm5)).capitalize()

def female():
    return male()

def last_name():
    return male()