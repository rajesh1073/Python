# BUILT-IN FUNCTIONS:
# these are provided by the python itseld,and are available readily for use.

# 1.NUMBER FUNCTIONS:

# 1.Absolute():
# It is a number function with is used to know the distance of a number from 0.
# syntax:
        # abs(num or var)

# example:
var1=-3.5
print(abs(var1))

# for complex number abs retrun the magnitude of the number.
# num=a+bj
# then magnitude=sqrt(a**2+b**2)

var1=3+4j
print(abs(var1))


# 2.power():
# It raises a the first value passed to it to the power of second value respectively.
# syntax:
#         pow(a,b) returns a**b
#         pow(a,b,c) returns a**b%c 

a=2
b=3
print(pow(a,b))

print(pow(3,3))

a=10
b=2
c=23
print(pow(a,b,c)) #it returns a**b%c 

#round():
# It returns the nearest integers to the passed value
# syntax:
#         round(num)

a=2.51
print(round(a)) 

b=3.6
print(round(b))

a=3.145267895
print(round(a,2))



# 3.divmod():
# It returns quotient and modules of two numbers.
# syntax:
#         divmod(a,b) returns (quotient,remainder) as result.

print(divmod(23,13))

# min() and max():
# used to return minimum and maximum values in a sequence:
# syntax:
        # max(sequence_name)
        # min(sequence_name)

list1=[7,6,8,12,23]
print(max(list1))
print(min(list1))


list1=[7,6,8,12,23]
maxi=list1[0]
for i in list1:
    if i>maxi:
        maxi=i
print(maxi)

list1=[7,6,8,12,23]
mini=list1[0]
for i in list1:
    if i<mini:
        mini=i
print(mini)



# sum():
# it returns the sum of the sequence
list1=[7,6,8,12,23]
print(sum(list1))

list1=[7,6,8,12,23]
sum=0
for i in list1:
    sum+=i
print(sum)




# MATH MODULES:
    # To perform advanced math operations we used math module.


# use import keyword to import all the functions of math module into our program.
# ex:
        # import math
import math
# 1.ceil function:
# It is used to round up to the next integer. like 4.1 to 4.9 is there then it shows result as 5.
print(math.ceil(4.2))

# 2.floor function
# It is used to round down to the closest integer. like 4.1 to 4.9 is there then it shows result as 4.
print(math.floor(4.1))

# 3.square root function:
# It is used to return the squareroot of a number.
# in result return as float value.
print(math.sqrt(25))

#4.power function:
# in the math module pow function return as float value.
print(math.pow(2,3))


# 5.constants are used when we want to use exact values of constants in  an operation.
print(math.pi)
print(math.e)

# 6.log function
print(math.log(math.e))


# 7.sine function
print(math.sin((math.pi)/2))


#RANDOM  MODULE:
# It is used to generate pseudo-random numbers.(fake/dummy random numbers)
# Here we are using a algorithm to simulate random numbers.
# import random keyword using random modules

import random

# 1.random():
# it is used generate random float numbers betweem 0.0 to 1.0
print(random.random())

# 2.uniform():
# it is used to generate random float numbers between given range in uniform function.
print(random.uniform(1,9))

# 3.randint():-->rand means random int means integer
# it is used to generate random integers between the given range in randint function.
print(random.randint(1,6))

# 4.choice():
# to get a value randomly from a sequence
list1=['pavan','rajesh','prasanth','sai','naidu']
print(random.choice(list1))

# 5.choices():
# to get a multiple random values from a sequence.
# it allows duplicates.
# syntax:
#         random.choices(sequence_name,k=how many choices we wanted to return)
print(random.choices(list1,k=3))

# 6.sample():
# to choose unique values in a sequence.
# with key using:
print(random.sample(list1,k=2))
# without key using:
print(random.sample(list1,2))


# 7.shuffle():
# to jumble values in a sequence.
cards=['A','K','Q','J','2','3','4','5','6','7','8','9','10']
random.shuffle(cards)
print(cards)
