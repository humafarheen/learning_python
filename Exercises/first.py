#!/usr/bin/env python3
#Sort a given string in alphabetical order
def string_sort(s):
 return ''.join(sorted(s))
s = input("Enter a string\n")
print("The Sorted string is: ",string_sort(s))
