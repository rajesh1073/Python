#ternary operator
# 

age=int(input())
print("eligible" if age>=18 else "not eligible")


# nested ternary operator

age=int(input())
print("child" if age<13 else "youth" if age<40 else "old")