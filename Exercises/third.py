#!/usr/bin/env python3
#find the sum of unique numbers in alist ,ignore if input is not integer
print("Enter a list of integers:\n")
a = [x for x in input().split()]
b = set(a)
sum = 0
for i in b:
    try:
        sum = sum + int(i)
    except:
        continue
print(sum)
