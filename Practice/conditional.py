user=input("Enter 1 or 2")
if user=="1":
 print("you entered 1")
elif user=="2":
 print("you entered 2")
else:
 print("neither 1 nor 2")
#inline if-if we need to perfrom a simple task
a=12 if user==1 else 13
print(a)
print("u entered 2" if a==13 else "u eneterd 1")
