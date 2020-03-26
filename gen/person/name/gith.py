import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["Am","Ar","Ara","Aza","Bar","Bra","Bran","Bru","Da","Dar","Dor","Dra","Dro","Du","Fa","Far","Fer","Fur","Gan","Gra","Gran","Gre","Gro","Gru","Hra","Hu","Ka","Kar","Kha","Kra","Kro","Ma","Mar","Mu","Na","Nar","Nir","Nu","On","Or","Ora","Oro","Ra","Ran","Rhu","Rin","Ru","Sa","Sha","Shra","Sra","Un","Una","Ur","Ura","Zar","Zra"]
nm2 = ["d","dahn","dak","dar","dh","dran","gahr","gh","gor","k","kahr","kar","khar","kiak","kk","kran","lag","lahr","lian","lid","lis","llak","loth","mag","mak","miak","mir","nag","nak","niar","nod","rad","rag","rak","ram","rath","rek","rg","rm","rth","ruk","tar","th","tig","zad","zag","zak","zar","zeg","zirg","zth"]
nm3 = ["Ad","Alm","Ar","Arw","Ash","Dah","Dhar","Dolm","Dran","Ell","Erzh","Esz","Ezh","Genr","Grel","Grin","Halm","Han","Harn","Heln","Ihr","Iln","Imm","Iz","Kan","Kharm","Khaz","Krez","Laz","Lez","Lhash","Lir","Magd","Marm","Meir","Mir","Nagr","Nah","Nalm","Nash","Niar","Ohn","Or","Rasz","Rez","Sham","Sharm","Shund","Sil","Um","Ur","Uw"]
nm4 = ["a","ah","aka","al","alin","alla","ane","anith","anya","arah","arin","aya","ayah","ayis","eah","eka","ekus","el","ela","elna","elya","elzal","ena","enah","era","erah","erath","erra","eth","eya","ihn","ila","ilias","ilzin","in","ina","ines","ira","iren","iris","ith","iza","mina","mira","nel","nera","nia","niya","ya","yara"]

def female():
    return (random.choice(nm3) + random.choice(nm4)).capitalize()

def male():
    return (random.choice(nm1) + random.choice(nm2)).capitalize()

def last_name():
    return (random.choice(nm1) + random.choice(nm4) + random.choice(nm2)).capitalize()
