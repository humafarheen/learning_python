try:
    a=10/1
    print(a)
except:
    print("En error occured")
    #types of exceptions
n1=int(input("enter first number"))
n2=int(input("enter another number"))
try:
    answer=n1/n2
    print(answer)
except ValueError:
        print("value error")
except ZeroDivisionError:
        print("Zero division error")
except Exception as e:
        print("unknow error",e)
        #IOError when an IO operation fails
        #IndexError when the 
        #ImportError 
        #KeyError-when dictionary key is not found
        #NameError-when local or global name is not found
        #TypeError
