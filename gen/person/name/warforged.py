import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["Abider", "Achiever", "Actor", "Adapter", "Adviser", "Aegis", "Agent", "Animal", "Apparatus", "Armament", "Artist", "Audience", "Author", "Awakener", "Basher", "Bastion", "Battler", "Bear", "Beast", "Beauty", "Beetle", "Bender", "Binder", "Blade", "Book", "Booster", "Boot", "Bouncer", "Brain", "Brander", "Brawler", "Breaker", "Bringer", "Browser", "Bruiser", "Buffet", "Bug", "Builder", "Bulwark", "Calmer", "Candle", "Cannon", "Carer", "Carriage", "Carrier", "Cart", "Carver", "Case", "Caster", "Catcher", "Chain", "Chains", "Challenger", "Champion", "Chaperon", "Charger", "Chaser", "Chopper", "Claymore", "Cleaver", "Climber", "Clock", "Club", "Clubber", "Coil", "Commander", "Controller", "Cook", "Counter", "Creator", "Creature", "Creese", "Crew", "Croaker", "Crow", "Crumbler", "Crusher", "Curator", "Curtana", "Custodian", "Cutlas", "Cutlass", "Cutter", "Dagger", "Data", "Dealer", "Decipherer", "Defender", "Definer", "Delver", "Designer", "Destroyer", "Diagnoser", "Director", "Dirk", "Diver", "Doctor", "Dozer", "Dreamer", "Drifter", "Driver", "Drone", "Echo", "Edge", "Enchanter", "Epee", "Eraser", "Estoc", "Etcher", "Examiner", "Expert", "Falchion", "Familiar", "Fighter", "Figure", "Fire", "Five", "Flail", "Flame", "Fluke", "Foil", "Follower", "Forger", "Four", "Friend", "Fumbler", "Gasher", "Gauger", "Ghost", "Giant", "Gift", "Glaive", "Glancer", "Griller", "Grunter", "Guardian", "Guest", "Guide", "Hacker", "Hammer", "Handler", "Heart", "Help", "Hook", "Horn", "Host", "Hummer", "Hunter", "Image", "Inspector", "Iron", "Judge", "Junior", "Jury", "Katana", "Kid", "Killer", "Knife", "Knocker", "Kris", "Launcher", "Leaper", "Lifter", "Lock", "Locket", "Lurker", "Mace", "Machine", "Mark", "Marker", "Mask", "Masker", "Mauler", "Melter", "Menace", "Mentor", "Merger", "Metal", "Mime", "Mistake", "Model", "Molder", "Murderer", "Nameless", "Needle", "Nemo", "Novice", "Nurse", "Observer", "Officer", "Ogler", "One", "Ornament", "Painter", "Passenger", "Patient", "Patriot", "Pierce", "Pilot", "Pious", "Player", "Porter", "Preacher", "Pretender", "Prize", "Probe", "Protector", "Prowler", "Punisher", "Query", "Ravager", "Reader", "Reckoner", "Relic", "Render", "Rescuer", "Responder", "Reviewer", "Rider", "Rune", "Saber", "Sabre", "Safeguard", "Salvager", "Saviour", "Scimitar", "Scorcher", "Scratcher", "Scrubber", "Searcher", "Security", "Seeker", "Senior", "Senser", "Sentinel", "Sentry", "Servant", "Shaper", "Shepherd", "Shield", "Shielder", "Shredder", "Slasher", "Slicer", "Smasher", "Smiter", "Snooper", "Spark", "Sparkle", "Special", "Spirit", "Sprinter", "Sprite", "Squasher", "Stalker", "Status", "Steel", "Steeple", "Stick", "Sticks", "Stitcher", "Striker", "Student", "Stumbler", "Subject", "Suit", "Sunderer", "Supporter", "Surveyor", "Sword", "Tackler", "Taunter", "Teacher", "Teaser", "Tempter", "Tester", "Thief", "Thinker", "Three", "Thunder", "Tinkerer", "Titan", "Toad", "Toledo", "Tutor", "Twister", "Two", "Undoer", "Unit", "Unmaker", "Unsung", "Vessel", "Victor", "Visitor", "Voice", "Walker", "Ward", "Warden", "Watcher", "Whisperer", "Wielder", "Winker", "Winner", "Wonderer", "Wrestler", "Zealot", "Zero"]

c = random.choice

def female():
    return c(nm1)

def male():
    return c(nm1)

def last_name():
    return c(nm1)