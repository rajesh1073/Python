# LAMBDA FUNCTIONS:
# These are nameless(anonymous) functions which are used to perform simple operations which are not reused again again.
# These are declared using lambda keyword.
# SYNTAX:
        # variable = lambda variables : expression
# NOTE:
# 1.Lambda functions must start with keyword lambda.
# 2.It can have any number of arguments/parameters.
# 3.It can have only one expression.
# 4.There is no need of return inside lamda functions.
# 5.we can't write loop and pass values inside a lambda function.

#addition of numbers
add=lambda a,b:a+b
print(add(3,4)) #7

#square of a number
squar=lambda a:a*a
print(squar(5)) #25

print(lambda a,b:a+b(3,4)) #it prints a address


# lambda with one if-else:
even_odd=lambda num:"even" if num%2==0 else "odd"
print(even_odd(5))
print(even_odd(10))


# lambda with two if-else:
value=lambda weather:"carry" if weather=="rain" else "don't carry" if weather=="sunny" else "don't need"
print(value("rain"))
print(value("sunny"))


fullname=lambda a,b="masada":f"{a} {b}"
print(fullname("rajesh"))
print(fullname("naidu","surla"))

#passing a lambda function to another function:
#1.map():

list1=[1,2,3,4,5,6,7,8,9,10,11,12]

squares=list(map(lambda x:x*x,list1))
print("squares:",squares)

cubes=list(map(lambda x:x**3,list1))
print("cubes:",cubes)

# 2.filter():
evens=list(filter(lambda x:x%2==0,list1))
print("evens:",evens)

nums=list(filter(lambda x:x>2,list1))
print(nums)

multiples_of_three=list(filter(lambda x:x%3==0,list1))
print(multiples_of_three)


names=["rajesh","naidu","prasanth"]
name=list(filter(lambda x:x.endswith("h"),names))
print(name)


numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
mul_of_three_and_five=list(filter(lambda x:x%3==0 and x%5==0,numbers))
print(mul_of_three_and_five)


#3.reduce
from functools import reduce
tuple1=(1,2,3,4,5)
mul=reduce(lambda a,b:a*b,tuple1)
print(mul)


add=reduce(lambda a,b:a+b,tuple1)
print(add)


# # list=["Rajesh Masada","Naidu Surla","Prasanth Macharla"]


list=["rajesh","masadad"]
adding=reduce(lambda a,b:(a*2,a+b),list)
print(adding)



n=lambda a,b:(a+b,a-b,a*b,a/b,a//b,a%b)
print(n(3,4))