# Data types
# =>The classification of values into certain categories.
# Types:
# 1.primitive => which are immutable => integer,float,string,boolean,complex,none
# 2.non primitive => which are mutable => list,tuple,set,dictionary


#PRIMITIVE DATATYPES ==>


# Integer
# It is a whole numbers without having decimal points
a=12
b=-12
print(a)
print(b)
print(type(a))
print(type(b))

#Float
#it is a number having decimal points
a=1.2
b=0.0
print(a)
print(b)
print(type(a))
print(type(b))


#complex
# a number having real part and imaginary part having letter "j"
# and it will print in float points
a=2+3j
print(a.real) #2.0
print(a.imag) #3.0
print(a)
print(type(a))

#Boolean
# we acquire these values after evaluating the condition.
# it evaluates the condition is either true or false .
a=True
b=False
print(3==2)
print(2==2)
print(bool(1))
print(bool(0))
print(type(a))
print(type(b))

# String
# it is a collection of characters,the characters can be alphabets,numbers,special characters.
# we declare a string by placing the characters between quote.
# the quotes can be double or single.
str1="rajesh masada"
print(str1)
print(type(str1))
print(len(str1))
count=0 
for char in str1:
    count+=1
print(count)

# Nonetype
a=None
print(a)
print(type(a))



