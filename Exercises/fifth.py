#!/usr/bin/env python3
#To find out if the given string is pangram or not
def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
     if i not in s:
        return False
    return True
print ("Enter a string")
s = input()
if is_pangram(s.lower()):
    print ("The given string is pangram")
else:
    print ("The given string is not pangram")

