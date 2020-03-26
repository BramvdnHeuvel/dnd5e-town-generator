import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["","","c","cr","d","g","h","j","kr","m","n","p","r","s","st","t","v","vr","z","zr"]
nm2 = ["a","e","i","o","u","a","u"]
nm3 = ["ch","dg","dr","g","gd","gl","gg","gr","j","ll","rr","rd"]
nm4 = ["","b","g","gg","k","lk","rg","rk","s","t"]

nm5 = ["","","b","d","g","j","m","n","p","q","r","v","z"]
nm6 = ["a","i","u","a","i","u","o","e"]
nm7 = ["b","br","d","dr","g","gn","gv","gr","lg","lgr","ld","ldr","lv","lz","ln","nd","nv","nr","rg","rz","rdr","rgr","rt"]
nm8 = ["d","dd","g","l","ld","ll","n","nd","nn","y","v","z"]
nm9 = ["","","k","l","n","r","s","t"]

nm10 = ["Ant","Bait","Baitworm","Bearbelch","Bearbite","Beardung","Beetle","Belch","Bigchin","Birdbrain","Bitenose","Bitesize","Blockhead","Boarbait","Boardung","Bonehead","Bottomfeeder","Bottomfood","Brainmush","Breadstick","Bucket","Buffoon","Bugbite","Candlestick","Chickenbrain","Chowder","Clam","Coldnose","Crawly","Deviant","Dirtbrain","Dirtface","Donkey","Dungbreath","Fly","Frogface","Froghead","Frogwart","Gnat","Gnatface","Grubface","Grubgrub","Guano","Ingrate","Insect","Larva","Leech","Leechbrain","Leechhead","Leechnose","Louse","Lousehead","Maggot","Maggotbrain","Malformed","Mealworm","Mite","Mitemouth","Moldbrain","Moldnose","Mongrel","Mud","Mudface","Mudmouth","Mudmug","Mudnose","Mule","No-Ear","No-Ears","No-Eyes","No-Nose","No-Toes","One-Eye","Owlball","Peon","Pest","Pig","Pigface","Pighead","Pigmud","Pigmug","Pinkeye","Redeye","Sleaze","Slime","Slug","Slugmug","Snack","Snailbrain","Snailnose","Snot","Snotnose","Spiderbait","Toadbrain","Toadface","Toadwart","Toenail","Uglymug","Vermin","Wartface","Weasel","Weevil","Worm","Wormfood","Wormmouth","Wriggler"]
nm11 = ["Wide","Ugly","Strange","Slime","Pale","Grime","Grease","Bone","Bent","Bitter","Broken","Dirt","Dull","Fat","Flat","Frail","Glob","Gout","Grim","Grub","Half","Ichor","Limp","Lump","Mad","Meek","Mold","Moss","Muck","Mud","Murk","Numb","Oaf","Shrill","Sick","Smug","Snail","Snot","Slug","Stink","Stub","Wart","Weak","Worm"]
nm12 = ["arm","arms","ear","eye","eyes","bone","bones","brain","cheek","cheeks","chin","face","flab","flank","foot","feet","gob","gut","guts","head","knuckle","knuckles","leg","legs","maw","mug","nose","tooth","teeth","will"]

c = random.choice

def male():
    if random.random() < 0.5:
        return (c(nm1)+c(nm2)+c(nm4)).capitalize()
    return (c(nm1)+c(nm2)+c(nm3)+c(nm2)+c(nm4)).capitalize()

def female():
	choice = random.randint(1, 3)

	if choice == 1:
		return (c(nm5)+c(nm6)+c(nm9)).capitalize()
	if choice == 2:
		return (c(nm5)+c(nm6)+c(nm7)+c(nm6)+c(nm9)).capitalize()
	if choice == 3:
		return (c(nm5)+c(nm6)+c(nm7)+c(nm6)+c(nm8)+c(nm6)+c(nm9)).capitalize()

def last_name():
	return c(nm11) + c(nm12)