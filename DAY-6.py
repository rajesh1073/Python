# operators
# it is a symbol which is used to perform certain operation on one or more than one value.
# example: a=b+c
# b,c==>operands
# a==>resultant
# +,= ==>operators 

# types of operators ==>

# 1.arithemetic ==> +-*/ //
# these operators are used to perform mathematical operations in our program.
a=10
b=5
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division it gives float value as result
print(a//b) #floor division it gives integer value as result
print(a%b)  #modulus it gives remainder as result
print(a**b) #power function




# 2.comparsion ==> > < >= => == !=
# To compare two values and it returns boolean value as result.

a=20
b=90
print(a<b) #true
print(a==b) #false
print(a!=b) #true
print(a>b) #false
print(a<=b) #true
print(a>=b) #false



# 3.assignment and augmented==> += -= *= /=
# these operators are used to assign a value to a variable and to perform an operation and assignment at the same time using augmented operators.
#normal way means x=x+1
x=10
x=x+1
print(x)
# augmented means combination of arithemetic operator and assigning (=) like +=,-=,*=,/=......
x=10
x+=1
print(x)
# NOTE: if you pass a float to floor division operator it will return float value.
x=35.0
x//=7
print(x)



# 4.logical ==> and or not
# these operators compares two condition and returns a boolean value.
# 1. and ==> if the both the values are said to be true then the result is true otherwise false.
# 2. or  ==> if either of the value is said to be true then the result is true otherwise false.
# 3. not ==> if the value is true then the result is false.
#            if the value is false then the result is true.

a=4 
b=8
print((a>b)and(a<b))
print(True and False)
print(True or False)
print(not True) 


# 5.bitwise ==> & | ^ << >> ~
# it operates on the data bit by bit.
# BIT : it is the smallest memory value in our computer.
# 0--> 0*2(3) + 0*2(2) + 0*2(1) + 0*2(1)
# 1--> 0001
# 2--> 0010...............10-->1010
# ~n=-(n+1)



a=5
b=4
print(a&b)
print(a|b)
print(a^b)
a=5
b=2
c=-5 
print(a<<b)
print(a>>b)
print(~a) # -(5+1)==>-6
print(~b) # -(2+1)==>-
print(~c) # -((-5+1))==>-(-4)==>4
print(~7)
print(~(-7))



#6.identity ==> is isnot




# 7.membership ==> in notin
# to find the element in sequence result as boolean value.
a=[1,2,3]
print(2 in a)


