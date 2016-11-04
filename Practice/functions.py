def ifprime(number):
    for num in range(2,number):
     if number%num==0:
      return False
    return True
ans=ifprime(13)
print(ans)
#importing modules
import random as r
print(r.randrange(0,5))
#or we can directly call the function
import random
print(random.randrange(0,5))
#we can also import particular functions from a modules
#from random import randrange,randint
#we can create our own module .. make a python script with functions and put it in the same folder.
#if the modules and files are in the different folder we have to add the path of module at the starting of file
#if "C:\\modulesfile" not in sys.path:
#sys.append("C:\\modulesfile")
