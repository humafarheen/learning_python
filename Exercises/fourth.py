#!/usr/bin/env python3
#Binary search on a list
def binary_search(l,item):
    start = 0
    end = len(l) - 1
    while(start <= end):
        mid = (start + end) // 2
        if(l[mid] == item):
            return mid
        elif(l[mid] > item):
            end = mid - 1
        else:
            start = mid + 1
    return -1
print("Enter a list")
l = [x for x in input().split()]
l = sorted(l)
print("Enter item to be searched:")
item = input()
found = binary_search(l,item)
if(found >= 0):
 print("The item found at index",found)
else:
 print("Item not found!!!")


