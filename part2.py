#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

wordlist = "/Users/isaacLockwood/Documents/UMD/2018spring/CMSC389R/CMSC389Rrepo/389Rspring18/week/9/challenges/wdlist.txt"       # download the wordlist and enter the ABSOLUTE path here

h1 = "7e0b893f2448c8476a0dd5d34f89a88f3ffa24e70f03e47d4de98f23bbfa0a2d4c89a84ceae6e3eabc8570a0027babd726611100df19335373665ff0eb1a13e6"
h2 = "71ed98458540dd6aff8cc2683c6450310f3a2d4bddd8c0bca7dcbe002e70614671127a59a543139fc40ed7f73ac259a3fdcb0426ff8433fe85e7adf3fa047771"
h3 = "c7072e350fa8794e78b864d6cb3fe06281e933743d26f00c0ec55a66e7394cb8e0ee0840d7fd0aa80177bc5c7e1bfe65c6d73e7491243959bf738957c97f125a"
h4 = "765d54e7e4cc23ea3cf9c820844d192c8cc80fc20701cd16fb7a0b9dafc5f8a8d526534ae0cea78d6b878ca4beb7a6fbdcdf012a0ec95d8067a015a6327153dd"
h5 = "9164498b4652250420d3b3ae2a121dd58750598740f79080b3c45f3d6c25a4f5f840f506d4427453ee85c6f79c0c674f45b1c21933f3161c4fa674eebf9e2f00"

soln = "no soln found"
#print(str.ascii_lowercase)
file = open("wdlist.txt", "r")
for line in file:
    strippedLine = line.strip()
    #print("-------- "+strippedLine+" --------")
    for letter in string.ascii_lowercase:
        #print("trying sha512( " + letter + " || " + strippedLine + " )")
        #newHash = hashlib.sha256()
        newString = letter + strippedLine
        newHash = hashlib.sha512(newString.encode('utf-8'))
        #newHash.update(letter.encode('utf-8'))
        #newHash.update(strippedLine.encode('utf-8'))
        #newHash.update(newString.encode('utf-8'))
        #print(newHash.hexdigest())
        #print(h1)
        if (newHash.hexdigest() == h1):
            print("h1 cracked:  " + letter + " " + strippedLine)
        if (newHash.hexdigest() == h2):
            print("h2 cracked:  " + letter + " " + strippedLine)
        if (newHash.hexdigest() == h3):
            print("h3 cracked:  " + letter + " " + strippedLine)
        if (newHash.hexdigest() == h4):
            print("h4 cracked:  " + letter + " " + strippedLine)
        if (newHash.hexdigest() == h5):
            print("h5 cracked:  " + letter + " " + strippedLine)

#print(soln)
#h0 = "28b07c7a913e77b17b857af9dc78af41779d63cd7973ae6716a657e065cceda3"
#soccer = "soccer10"
#test = hashlib.sha256()
#test.update(soccer.encode('utf-8'))
#print(test.hexdigest() == h0)

