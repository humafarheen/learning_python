myname=input("Enter your name")
myage=input("Enter your age")
#all the inputs we enter is stored as a string
print("your name is",myname,"my age is ",myage)
#print("your name is %s and your age is %d"%(myname,myage))
#triple quote is used to print in multiple lines 
print('''Hello world!
my name is huma
i am 22 years old''')
#use of\
print("hello\tworld")
print("hello\nworld")
print("hello\'world")
print("hello\\world")
#if we dont want the character after \ interpreted as special caharacter
print(r"hello\tworld")