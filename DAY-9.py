# DECISION STATEMENTS
# These are used to make decisions in a program based on a certain condition.
# Keywords: if , elif ,else


#INDENTATION:
# The space give in front if a statement while defining a block is called indentation.
# By default the indentation provided consists of 4 spaces.

# if-else syntax:


# if condition is true if block can be executed if condition is false else block can be executedd.
# if condition:
#     //block of Code
# else:
#     //block of code


# weather=input("enter weather condition:")
# if weather=='raining':
#     print("Dont go")
# else:
#     print("Go")

# classname=input("enter the classname:")
# if classname=="python":
#     print("venkat sir")
# else:
#     print("free hour")

# placement=input("enter yes or no:")
# if placement=="yes":
#     print("go to company")
# else:
#     print("go to 10k")


# elif syntax:

# is used when we have multiple conditionns to check
# note:once a condition is true then block is executed and the execution ends right after that block.
# a program can have multiple if and elif statements but there must be only one else for that specific if-else block.

# if condition:
#     //block of Code
# elif condition:
#     //block of code 
# else:
#     //block of code


# placement=input("enter placement status:")
# skills=input('do you have skills:')
# if placement=='True':
#     print("go to compamy")
# elif skills=='True':
#     print("do freelance")
# else:
#     print("go to 10k")

# num=int(input('enter the number:'))
# if num%3==0 and num%5==0:
#     print('divisible by both')
# elif num%5==0:
#     print('divisible by 5')
# elif num%3==0:
#     print("divisible by 3")
# else:
#     print('not divisible')
