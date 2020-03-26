import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["","","","","","h","m","n","s","sh","ss","ssh","sz","t","th","y","z","zh","zs"]
nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","oa","ui"]
nm3 = ["h","hl","htl","hl","hs","hsh","k","kh","kl","ktl","ks","l","lk","ls","ltl","lts","lsh","m","n","s","sh","ss","st","stl","sz","sk","t","tl","ts","tsh","tsz","tz","tstl","zs","zh","zsh","zt","ztl"]
nm4 = ["h","hs","hl","l","ll","s","sh","ss","shl","t","th","y","z","zh"]
nm5 = ["a","i","u","a","i","u","a","i","u","a","i","u","a","i","u","a","i","u","ie","ia","ei","ee","iu","ui"]
nm6 = ["","","","","","","","","h","h","l","ll","s","ss","sh"]

c = random.choice

def male():
    if random.random() < 0.5:
        return (c(nm1)+c(nm2)+c(nm3)+c(nm5)+c(nm6)).capitalize()
    return (c(nm1)+c(nm2)+c(nm3)+c(nm2)+c(nm4)+c(nm5)+c(nm6)).capitalize()

def female():
    return male()

def last_name():
    return (c(nm1)+c(nm2)+c(nm3)+c(nm2)+c(nm4)+c(nm5)+c(nm6)).capitalize()
