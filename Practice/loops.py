name=["huma","farheen","atiya","bano","ansari"]
for names in name:
 print(names)
 #we can also print indices of the list using enumerate
for index,names in enumerate(name):
 print(index,names)
#loop through string
a='hello world!'
for i in a:
 print(i)
#looping through a sequence of numbers 
for i in range(0,5): #if start is not given ,it automatically takes 0.
    print(i)
for i in range(0,10,2):
    print(i)
a=5
while a>=0:
    print("value =",a)
    a=a-1
while a<=5:
    print(a)
    a=a+1
    if(a==3):
        break  
while a<=5:
    print(a)
    a=a+1
    if(a==3):
        continue #the rest of the loop after continue is skipped  
  
