# type conversion and type casting:
# conversion happens automaticallly by the python.
# casting is done by the user manually.


# CONVERSION

a=10 #int
b=5.5 #float
print(a+b) #float

a=True #true = 1
b=10
print(a+b)

a=5
b=5+3j
print(a+b)

# CASTING
a=10
b=5.5
c=a+b
print(int(c))

a=10
b=20
print(float(a+b))

a='123'
b=int(a)
c=30
print(b+c)

a=3+5j
b=a.real
c=a.imag
print(b)
print(c)
print(int(b))
print(int(c))
print(type(b))
print(type(c))
