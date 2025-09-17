# scoping
# it denotes where we can access a specific variable.

# Types of scopes:

# 1.local scope:
# here varaibles are available only with in the function.
# in this local variables cant use in global

# def add():
#     a="rajesh" #local scope or local variable
#     print(a)
# add()


# NOTE:
# we can use local variable outside using "global variablename" inside the function.

# def add():
#     global a
#     a="rajesh"
#     print(a)
# add()
# print(a)


# 2.global scope:
# these variables are available throught the program.
# inside and outside the function.
# in this global variables also can access in local also.


# a="raj"
# def add():
#     a="rajesh"
#     print(a)
# add()
# print(a)

# surname="masada"
# def name():
#     name="rajesh"
#     print(f"My name is {surname} {name}")
# name()

# NOTE:
# We have same varible names inside function and outside function we can print same output we use 
# global keyword it can change local value as global value.

# name="rajesh"
# def Name():
#     global name
#     name="raj"
#     print(name)
# Name()
# print(name)

# num1=5
# num2=3
# add=num1+num2
# def adding(num1,num2):
#     add=num1+num2
#     print(add)
# adding(5,5)
# print(add)


# NOTE:
# we cannot edit a global variable directly inside a function without assigning a value to it.If we want to make change
# to a global variable inside a function then we use "global" keyword.


# 1.global variable used in a local:
# num=10
# def adding():
#     global num
#     num+=1
#     print(num)
# adding()
# print(num)


# starting_name="Hello"
# def name():
#     global starting_name
#     print(f"{starting_name} World")
# name()


# 2.local variable used in a global
# def adding():
#     global num
#     num=15
#     num+=1
#     print(num)
# adding()
# print(num)



# def name():
#     global starting_name
#     starting_name="Hello"  
# name()
# print(f"{starting_name} World")
