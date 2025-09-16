# 4.variables length arguments:
# these are used when you don't know specifically , how many arguments to pass.

def add(*numbers):
    add=0
    for i in numbers:
        add+=i
    return add
res=add(1,2,3,4,5,6,7,8,9,10)
print(f"Sum of numbers:{res}")


def mul(*numbers):
    multi=1
    for i in numbers:
        multi*=i
    return multi
res=mul(1,2,3,4,5)
print(f"mul of numbers:{res}")




# 5.variable length keyword arguments:
# They are used to pass multiple keyword arguments to a function with single parameter.
# SYNTAX:
# def funcName(**parameter):
#      block of code

def flight(**passengerdetails):
    for i,j in passengerdetails.items():
        print(f"{i}:{j}")
flight(name="rajesh",source="hyd",destination="vzg",date="12-05-2005",airline="indigo")
print()
flight(name="narayana",source="chennai",airline="kingfisher")
print()
flight(name="naidu",date="25-10-2025")


#combination of default and keyword arguments: 

def details(name,age,gender="male"):
    print(f"""name:{name},
    age:{age},
    gender:{gender}""")
details(name="Rajesh",age=20)
details(name="tejasri",age=21,gender="female")


# Both combination of variable length and variable length keywords:

def details(*vl,**vlk):
    sum=0
    for i in vl:
        sum+=i
    print(sum)
    for i,j in vlk.items():
        print(f"{i}:{j}")
    # print("vl details",vl)
    # print("vlk details:",vlk)
details(1,2,3,name="rajesh",age=20)

def calc(a,b):
   return a+b,a-b,a*b
add,sub,mul=calc(5,2)
print(add)
print(sub)
print(mul)



def calc(num1,num2):
   a,b,c=num1+num2,num1-num2,num1*num2
   return a,b,c
res=calc(5,2)
for i in res:
   print(i)
