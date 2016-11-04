#!/usr/bin/env python3
#Count the number of volwels in a string
def vowel_count(string):
    vowels = ['a','e','i','o','u']
    count = 0
    for i in string:
        if i in vowels:
         count = count+1
    return count
string=input("Enter a string :\n")
print("Number of vowels in the string: ",vowel_count(string))