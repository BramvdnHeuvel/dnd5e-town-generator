import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["","","","","","b","d","g","jh","k","l","m","n","r","s","sh","t","tr","th","thr","v"]
nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","aa","ae","ao","au"]
nm3 = ["ch","d","dr","dh","g","gr","gh","gg","l","ll","lt","lth","lr","p","r","rg","rht","rk","rt","rd","rth","sh","sk","shr","sh","sl","t","th","tr","thr"]
nm4 = ["a","e","i","o","u","y","a","e","i","o","u","y","a","e","i","o","u","y","a","e","i","o","u","y","a","e","i","o","u","y","a","e","i","o","u","y","a","e","i","o","u","a","e","i","o","u","ea","ua","ae","ia","aa","ao"]
nm5 = ["c","g","gr","gn","k","kh","kr","r","rr","s","ss","sr","st","str","t","th","tr"]
nm6 = ["","","","","","","","ch","k","n","nd","nk","nt","r","rd","rk","rt","rth","s","ss","sh","sj","sk","t","th","v","x"]

c = random.choice

def male():
    choice = random.randint(1, 3)

    if choice == 1:
        return (c(nm1) + c(nm2) + c(nm6)).capitalize()
    if choice == 2:
        return (c(nm1) + c(nm2) + c(nm3) + c(nm4) + c(nm4) + c(nm6)).capitalize()
    if choice == 3:
        return (c(nm1) + c(nm2) + c(nm3) + c(nm2) + c(nm5) + c(nm4) + c(nm6)).capitalize()

def female():
    return male()

def last_name():
    return (c(nm1) + c(nm2) + c(nm3) + c(nm2) + c(nm5) + c(nm4) + c(nm6)).capitalize()