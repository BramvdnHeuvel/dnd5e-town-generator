import random

# The following code is a substitute of the JavaScript name generators from FantasyNameGenerators.com
# I do not claim to have constructed the original generators. To contact the people
# to whom the intellectual property belongs, go to https://www.fantasynamegenerators.com/contact.php
#
# For more name generators, make sure to check out https://www.fantasynamegenerators.com/
# Copyright (C) 2012 - 2020 FantasyNameGenerators.com.

nm1 = ["Al","Ari","Bil","Bri","Cal","Cor","Dav","Dor","Eni","Er","Far","Fel","Ga","Gra","His","Hor","Ian","Ipa","Je","Jor","Kas","Kel","Lan","Lo","Man","Mer","Nes","Ni","Or","Oru","Pana","Po","Qua","Quo","Ras","Ron","Sa","Sal","Sin","Tan","To","Tra","Um","Uri","Val","Vor","War","Wil","Wre","Xal","Xo","Ye","Yos","Zan","Zil"]
nm2 = ["bar","ben","bis","corin","cryn","don","dri","fan","fiz","gim","grim","hik","him","ji","jin","kas","kur","len","lin","min","mop","morn","nan","ner","ni","pip","pos","rick","ros","rug","ryn","ser","ston","tix","tor","ver","vyn","win","wor","xif","xim","ybar","yur","ziver","zu"]
nm3 = ["Alu","Ari","Ban","Bree","Car","Cel","Daphi","Do","Eili","El","Fae","Fen","Fol","Gal","Gren","Hel","Hes","Ina","Iso","Jel","Jo","Klo","Kri","Lil","Lori","Min","My","Ni","Ny","Oda","Or","Phi","Pri","Qi","Que","Re","Rosi","Sa","Sel","Spi","Ta","Tifa","Tri","Ufe","Uri","Ven","Vo","Wel","Wro","Xa","Xyro","Ylo","Yo","Zani","Zin"]
nm4 = ["bi","bys","celi","ci","dira","dysa","fi","fyx","gani","gyra","hana","hani","kasys","kini","la","li","lin","lys","mila","miphi","myn","myra","na","niana","noa","nove","phina","pine","qaryn","qys","rhana","roe","sany","ssa","sys","tina","tra","wyn","wyse","xi","xis","yaris","yore","za","zyre"]

c = random.choice

def female():
    return c(nm3) + c(nm4)

def male():
    return c(nm1) + c(nm2)

def last_name():
    return (c(nm3) + c(nm2) + c(nm4)).capitalize()
