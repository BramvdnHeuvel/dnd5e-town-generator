import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["","","","","","d","dr","g","gl","gr","k","kh","kl","kr","l","m","n","r","rh","sh","v","vr","z","zr"]
nm2 = ["a","o","a","o","e","u"]
nm3 = ["d","dr","g","gr","gn","k","kk","kr","kn","kv","ldr","lv","lz","lvr","nd","ndr","nk","r","rb","rd","rk","v","vr","vl","z","zr"]
nm4 = ["e","e","a","o","i","u","e","a","o"]
nm5 = ["d","l","n","r","v","z"]
nm6 = ["a","e","o","u"]
nm7 = ["c","d","g","k","l","n","r","rg","rz"]
nm8 = ["Bark","Bash","Bellow","Bleed","Blow","Bolster","Bolt","Brawl","Break","Bruise","Buckle","Bully","Burn","Burst","Butcher","Cackle","Carve","Chomp","Conquer","Crash","Crunch","Crush","Dash","Devour","Dodge","Duel","Edge","Etch","Feign","Flail","Flare","Forge","Froth","Fume","Glare","Gnash","Grimace","Grin","Growl","Hook","Impale","Jolt","Kill","Lash","Lurch","Mangle","Mark","Maul","Pierce","Prowl","Pummel","Quake","Rage","Rebuke","Reign","Rend","Repel","Retch","Revel","Roam","Ruin","Rush","Saw","Scorch","Scrub","Seethe","Sever","Shock","Shred","Slay","Smirk","Smush","Snarl","Squish","Stalk","Sting","Stomp","Strike","Stunt","Swipe","Thrash","Thunder","Trail","Trample","Twist","Twitch","Vex","Whack","the Beast","the Behemoth","the Blade","the Boar","the Bold","the Brute","the Bull","the Butcher","the Cold","the Corrupt","the Cruel","the Dagger","the Demon","the Edge","the Fury","the Giant","the Grand","the Grim","the Harsh","the Hollow","the Hook","the Hungry","the Hunter","the Insane","the Knife","the Loud","the Mad","the Maniac","the Manslayer","the Marked","the Mask","the Mighty","the Monster","the Oaf","the Ox","the Razor","the Reckless","the Red","the Rogue","the Rotten","the Sabre","the Serpent","the Shallow","the Shank","the Shield","the Shiv","the Skeleton","the Slayer","the Snake","the Strong","the Sword","the Thief","the Tyrant","the Vengeful","the Vicious","the Violent","the Vulture","the Warlord","the Warmonger","the Warrior","the Watcher","the Wrath","the Wretched"]

c = random.choice

def female():
    if random.random() < 0.5:
        return (c(nm1) + c(nm2) + c(nm7)).capitalize()
    return (c(nm1) + c(nm2) + c(nm3) + c(nm4) + c(nm5) + c(nm6) + c(nm7)).capitalize()

def male():
    return female()

def last_name():
    return c(nm8)
