#!/usr/bin/env python3
#find maximum element in a list and replace others with max
#Check this is develop
print("Enter a list")
l = [int(x) for x in input().split()]
a = max(l)
i = 0
while i < len(l):
    l[i] = a
    i = i + 1
print (l)