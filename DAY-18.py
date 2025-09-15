# FUNCTIONS:
# A function is a block of code to perform a certain action.
# Instead of repeating same line of codes again and again , i write them once in a function and call it wherever I need it's functonality.
# NOTE: a loop can repeat a task multiples times at same place where as a function performs the task only at the places where it is called.

# why functions:
# 1.Reduce code size
# 2.code reusability
# 3.breaking tasks of a program into smaller parts.

# RETURN STATEMENT:
# It used to use the output of a function for further operations.





# creating a function
# def add():
#     num1=int(input("enter the num1 value:"))
#     num2=int(input("enter the num2 value:"))
#     print("The sum is:",num1+num2)

#     # we call a function by it's name
# add()

# def sub():
#     num1=int(input("enter the num1 value:"))
#     num2=int(input("enter the num2 value:"))
#     print("The sub is:",num1-num2)
# sub()


# def mul():
#     num1=int(input("enter the num1 value:"))
#     num2=int(input("enter the num2 value:"))
#     print("The mul is:",num1*num2)
# mul()


# def calc():
#     num1=int(input("enter the num1 value:"))
#     num2=int(input("enter the num2 value:"))
#     print("The sum is:",num1+num2)
#     print("The sub is:",num1-num2)
#     print("The mul is:",num1*num2)
# calc()

#  A function without parameters:
# def greetings():
#     name=input("Enter the name:")
#     print(f"Thank you {name}, for taking course at 10k coders.")
# greetings()

# a function with parameters
# def greetings(name):
#     print(f"Thank you {name}, for taking course at 10k coders.")
# greetings("Rajesh")



# def greetings(name): #  here name is parameter.
#     print(f"Thank you {name}, for taking course at 10k coders.")
# name=input("Enter the name:") #here name is variable.
# greetings(name) #here name is argument.



# def add(a,b):
#     print(a+b)
# add(3,4)


# def evenorodd(num):
#     print("even" if num%2==0 else "odd")
# num=int(input("enter the number:"))
# evenorodd(num)



def prime(num):
    flag=0
    if num<0:
        print("It is a negative number.")
    elif num>1:
        for i in range(2,num):
            if num%i==0:
                flag=1
                break
        if flag==1:
            print("not prime.")
        else:
            print("prime.")
num=int(input("enter the number:"))
prime(num)




# RETURN STATEMENT:
# It used to use the output of a function for further operations.


# def add():
#     a=10
#     b=15
#     return a+b

# print(add()+5)
# print(add()-5)