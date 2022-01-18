#!/usr/share/python

import sys
import crypt 
 

file = open("lista.txt")


salt1 = raw_input("digite o salt: ")

hash_original = raw_input("digite a hash:")

for senha1 in file:
        senha2 = senha1 + "\n"
        hash_teste = crypt.crypt(senha1,salt1)
        if hash_original  == hash_teste:
                print ("_____________________________________________________")
                print ("[+] the hash has been broken, the password is bellow:") 
                print(senha1)
                print ("_____________________________________________________")


