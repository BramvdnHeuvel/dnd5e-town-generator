import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["","","","b","bh","br","d","dh","dr","g","gh","gr","j","l","m","n","r","rh","sh","z","zh"]
nm2 = ["a","o","u"]
nm3 = ["b","br","bz","d","dd","dz","dg","dr","g","gg","gr","gz","gv","hr","hz","j","kr","kz","m","mz","mv","n","ng","nd","nz","r","rt","rz","rd","rl","rz","t","tr","v","vr","z","zz"]
nm4 = ["b","d","g","g","k","k","kk","kk","l","ll","n","r"]

nm5 = ["","","","","b","bh","d","dh","g","gh","h","k","m","n","r","rh","s","sh","v","z"]
nm6 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","ee","au","ye","ie","aa","ou","ua","ao"]
nm7 = ["d","dd","dk","dg","dv","g","gg","gn","gv","gz","l","ll","lv","lz","m","md","mz","mv","ng","nk","ns","nz","t","thr","th","v","vn","vr","vg","vd","wnk","wg","wn"]
nm8 = ["","","","","","f","h","k","l","m","n","ng","v","z"]

nm9 = ["Aberrant","Ancient","Angry","Anguished","Arrogant","Barbarian","Barbaric","Barren","Berserk","Bitter","Bloody","Broad","Broken","Brutal","Brute","Butcher","Coarse","Cold","Colossal","Crazy","Crooked","Cruel","Dark","Defiant","Delirious","Deranged","Disfigured","Enormous","Enraged","Fearless","Feisty","Fierce","Filthy","Forsaken","Frantic","Gargantuan","Giant","Glorious","Grand","Grave","Grim","Gross","Gruesome","Hollow","Infernal","Lethal","Lost","Loyal","Macabre","Mad","Maniac","Merciless","Mighty","Miscreant","Noxious","Outlandish","Powerful","Prime","Proud","Putrid","Radical","Reckless","Repulsive","Rotten","Ruthless","Shady","Sick","Silent","Simple","Smug","Spiteful","Swift","Turbulent","Ugly","Unsightly","Vengeful","Venomous","Vicious","Violent","Vivid","Volatile","Vulgar","Warped","Wicked","Wild","Worthless","Wrathful","Wretched"]
nm10 = ["Anger","Ankle","Ash","Battle","Beast","Bitter","Black","Blood","Bone","Brain","Brass","Breath","Chaos","Chest","Chin","Cold","Dark","Death","Dirt","Doom","Dream","Elf","Eye","Fang","Feet","Fiend","Finger","Flame","Flesh","Foot","Ghost","Giant","Gnoll","Gnome","Gore","Hand","Hate","Head","Heart","Heel","Hell","Horror","Iron","Joint","Kidney","Kill","Knee","Muscle","Nose","Pest","Poison","Power","Pride","Rib","Scale","Skin","Skull","Slave","Smoke","Sorrow","Spine","Spite","Steel","Storm","Talon","Teeth","Throat","Thunder","Toe","Tooth","Vein","Venom","Vermin","War"]
nm11 = ["Axe","Blade","Brand","Breaker","Bruiser","Burster","Butcher","Carver","Chopper","Cleaver","Clobberer","Conquerer","Cracker","Cruncher","Crusher","Cutter","Dagger","Defacer","Despoiler","Destroyer","Dissector","Ender","Flayer","Gasher","Glaive","Gouger","Hacker","Hammer","Killer","Lance","Marauder","Masher","Mutilator","Piercer","Pummel","Quasher","Quelcher","Queller","Razer","Render","Ripper","Saber","Sabre","Scalper","Shatterer","Skinner","Slayer","Slicer","Smasher","Snapper","Spear","Splitter","Squasher","Squelcher","Squisher","Strangler","Sunderer","Sword","Trampler","Trasher","Vanquisher","Wrecker"]

c = random.choice

def female():
    if random.random() < 0.5:
        return (c(nm5) + c(nm6) + c(nm8)).capitalize()
    return (c(nm5) + c(nm6) + c(nm7) + c(nm6) + c(nm8)).capitalize()

def male():
    if random.random() < 0.5:
        return (c(nm1) + c(nm2) + c(nm4)).capitalize()
    return (c(nm1) + c(nm2) + c(nm3) + c(nm2) + c(nm4)).capitalize()

def last_name():
    choice = random.randint(1, 3)
    
    if choice == 1:
        return c(nm9)
    if choice == 2:
        return c(nm10)
    if choice == 3:
        return c(nm11)
