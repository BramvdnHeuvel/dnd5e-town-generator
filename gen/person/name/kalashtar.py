import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["b","c","ch","d","g","gh","h","k","kh","l","m","n","s","t","v","z"]
nm2 = ["a","e","o","a","e","o","i"]
nm3 = ["l","n","r","s","v","w","y","z"]
nm4 = ["a","a","e","i","i","o"]
nm5 = ["ulad","hareth","khad","kosh","melk","tash","vash"]
nm6 = ["ashana","ashtai","ishara","nari","tara","vakri"]

nm7 = ["d","h","g","gh","k","kh","m","n","r","sh","sht","t","v","z"]
nm8 = ["a","e","i","o","u"]
nm9 = ["dr","kr","l","ld","ldr","lr","n","r","rr","v","z"]
nm10 = ["ai","ei","ia","a","e","i","a","e","i","a","e","i","a","e","i","a","e","i"]
nm11 = ["","","","","","d","l","lk","n","ns","nt","s","ss","sh","th"]

c = random.choice

def male():
    part = c(nm1)
    if (choice := random.randint(1, 4) >= 2):
        part += c(nm2)
        if choice >= 3:
            part += c(nm3)
            if choice == 4:
                part += c(nm4)
    
    nchoice = random.randint(1, 4)
    if nchoice == 1:
        return (part + c(nm6)).capitalize()
    if nchoice == 2:
        return (part + c(nm5)).capitalize()
    if nchoice == 3:
        return (part + c(nm7) + c(nm8) + c(nm11)).capitalize()
    if nchoice == 4:
        return (part + c(nm7) + c(nm8) + c(nm9) + c(nm10) + c(nm11)).capitalize()

def female():
    return male()

def last_name():
    return male()