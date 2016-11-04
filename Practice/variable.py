name="huma"
age=222345
num=4.65
print(name.upper())
print("the name is %s ,age is %10d"%(name,age))
#1.32 ---%4.2f will take total 4 places ,2 for decimal places 1 for point 
#1.32 ---%7.3f will take total 7 places , 3 for decimal places 1 for point and it will add extra 3 spaces in the starting.
print("{0:s} is easier than {1:s}".format('python','java'))
#usinf formater
print (int(4.567))
print(float(4))
print(int(age))
print(str(age))
print(str(num))
userage=[1,2,3,4,5]
userage1=userage[1:3]
print(userage1)
print(userage[0:5:2])#it will print every second number starting from 0 to 5
print(userage[0:7:2])#it takes max limit of index of the given index is more than the maximum index
userage[1]=89 #to modify a particular item
userage.append(99) #to add an item
print(userage)
del userage[2] #to delete an item
print(userage)
#tuple-the values cant be modified in tuples 
mylist=("a","b","c")
print(mylist[1])
#dictionary-to store pair of data
nameandage={"peter":32,"huma":22,"harshini":23}
#we can also use dictionary function
nameage=dict(huma=22,rehan=30,harshini=22)
print(nameage["huma"])
#add item
nameage["farzan"]=28
print(nameage["farzan"])
na={"peter":"huma","ab":"s","cb":"er"}
print(na["peter"])

