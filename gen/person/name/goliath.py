import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nmFF = ["Age","Ane","Are","Daa","Dau","Di","Ga","Gal","Gau","Ge","Gel","Ila","Ina","Ka","Kau","Ke","Ki","Kuo","La","Lau","Le","Lo","Maa","Man","Mau","Me","Na","Nal","Nau","Ni","No","Ola","One","Ore","Ori","Pa","Paa","Pau","Pe","Tha","Thau","The","Thu","Vaa","Vau","Ve","Vo","Vu","Za","Zaa","Zau","Zo"]
nmFL = ["gea","geo","ggeo","ghu","gia","gu","kea","keo","kha","ki","kia","kio","kko","la","lai","lane","lea","leo","lo","lu","ma","meo","mi","mia","ne","nea","neo","ni","nia","nna","nnio","nu","peo","peu","pu","rea","rheo","ri","ria","rra","rrea","the","thea","thi","thia","thio","thu","vea","vi","via","vu"]
nmMF = ["Ag","Apa","Ar","Au","Aug","Aur","Eag","Eg","Erg","Ga","Gau","Gea","Gha","Gra","Ila","Ili","Ira","Kana","Kava","Kaza","Keo","Khu","Kora","Kra","La","Lau","Laza","Loro","Ma","Mara","Mau","Mea","Mo","Na","Nara","Nau","Neo","Pa","Pu","Tara","Tau","Tha","Thava","Tho","Va","Vara","Vau","Vaura","Vega","Vi","Vo","Za","Zau"]
nmML = ["dak","dath","dhan","gak","gal","gan","gath","ghan","gith","glath","gun","kan","kein","khal","kin","kon","lath","lig","lok","mahg","mahk","mahl","mak","man","mith","mul","nak","nath","nihl","noth","path","phak","rad","rath","rein","rhak","rhan","riak","rian","rin","rok","roth","thag","thak","tham","thi","thok","veith","vek","vhal","vhik","vith","voi","zak","ziath"]
nmMdF = ["Adept","Bear","Brave","Bright","Dawn","Day","Deer","Dream","Flint","Fearless","Flower","Food","Fright","Goat","Hard","Hide","High","Honest","Horn","Keen","Lone","Long","Low","Lumber","Master","Mind","Mountain","Night","Rain","River","Rock","Root","Silent","Sky","Sly","Smart","Steady","Stone","Storm","Strong","Swift","Thread","Thunder","Tree","Tribe","True","Truth","Wander","Wild","Wise","Wound"]
nmMdL = ["aid","bearer","breaker","caller","carver","chaser","climber","cook","dream","drifter","eye","finder","fist","friend","frightener","guard","hand","hauler","heart","herder","hunter","jumper","killer","lander","leader","leaper","logger","maker","mender","picker","runner","shot","smasher","speaker","stalker","striker","tanner","twister","vigor","walker","wanderer","warrior","watcher","weaver","worker"]
nmSF= ["Agu-Ul","Agu-V","Anakal","Apuna-M","Athun","Egena-V","Egum","Elan","Ganu-M","Gathak","Gean","Inul","Kalag","Kaluk","Katho-Ol","Kolae-G","Kolak","Kulan","Kulum","Lakum","Maluk","Munak","Muthal","Nalak","Nola-K","Nugal","Nulak","Ogol","Oveth","Thenal","Thul","Thunuk","Ugun","Uthenu-K","Vaimei-L","Valu-N","Vathun","Veom","Vuma-Th","Vunak"]
nmSL = ["aga","ageane","akane","akanu","akume","alathi","amino","amune","anathi","atake","athai","athala","atho","avea","avi","avone","eaku","ekali","elo","iaga","iago","iala","iano","igala","igane","igano","igo","igone","ileana","ithino","olake","ugate","ugoni","ukane","ukate","ukena","ulane","upine","utha","uthea"]

c = random.choice

def female():
    return c(nmFF) + c(nmFL)

def male():
    return c(nmMF) + c(nmML)

def last_name():
    return c(nmMdF) + c(nmMdL)
