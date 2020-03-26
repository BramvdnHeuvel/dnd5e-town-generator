import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["","","","","b","d","g","j","k","kr","l","n","pl","q","s","t","w","x","y"]
nm2 = ["ue","uo","ua","ia","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u"]
nm3 = ["b","d","k","l","lb","ld","lk","m","n","nn","nl","nq","nqw","qw","p","pp","r","rdl","rt","rtl","z","zl"]
nm4 = ["y","a","e","i","o","u","a","e","i","o","u"]
nm5 = ["","","","","","c","d","g","k","l","ll","m","n","r","t","tt"]

c = random.choice

def male():
    if random.random() < 0.5:
        return (c(nm1) + c(nm2) + c(nm5)).capitalize()
    return (c(nm1)+c(nm2)+c(nm3)+c(nm4)+c(nm5)).capitalize()

def female():
    return male()

def last_name():
    return (c(nm1)+c(nm2)+c(nm3)+c(nm4)+c(nm5)+c(nm4)+c(nm5)).capitalize()
