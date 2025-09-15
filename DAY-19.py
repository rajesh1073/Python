# Functions with different types of arguments:
# 1.positional arguments
# 2.default arguments
# 3.keyword arguments
# 4.variable length arguments
# 5.variable length keyword arguments

# 1.positional arguments:
# In this function the arguments can be passed same as the position.
# these arguments are passed based on the positions of the parameters of the function they are passed to.

# def div(a,b):
#     return a/b
# # print(div(10,0))
# print(div(0,10))

# def names(myname,clgname):
#     print(f"My name is {myname} and my clg name is {clgname}")

# myname=input("enter your name:")
# clgname=input("enter your clgname:")
# # names("rajesh","bvc")
# # names("bvc","rajesh")
# names(myname,clgname)
# names(clgname,myname)

# def marriage(bride,bride_groom):
#     print(f"Bride name is {bride} and Bride Groom name is {bride_groom}")
# # bride=input("enter bride name:")
# # bride_groom=input("enter bride groom name:")
# marriage("sobitha","chay")
# # marriage(bride,bride_groom)

# 2.Default Arguments:
# these arguments are passed inside function declaration,which acts as a default values to our parameters.

# def greetings(name,address="Hyderabad"):
#     print(f"Hello {name}, we are happy to invite you to our {address} office")
# greetings("Rajesh")



# # NOTE:If the value passed in the arguments it can takes arguments value only otherwise it takes default parameter value.
# def greetings(name,address="Hyderabad"):
#     print(f"Hello {name}, we are happy to invite you to our {address} office")
# greetings("Rajesh","KPHB")


# def name(fname,lname="MASADA"):
#     print(f"My name is {fname} {lname}")
# name("RAJESH")






