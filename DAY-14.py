# WHILE LOOP:
# it is used when we don't know how many times a loop must run.
# it takes a condition and runs untill the conditions turns false.

# syntax:
#       while condition:
#            //block of code
#            //increment or decrement

# i=1
# while i<=5:
#     print("Rajesh")
#     i+=1



# while True:
#     username=input("enter the username:")
#     password=input("enter the password:")
#     if username=="rajesh" and password=="12345":
#         print("Login Successful..!")
#         break
#     else:
#         print("Check Details..!")


username='rajesh'
password='12345'
attempts=0
while attempts<3:
    User_name=input("enter the username:")
    Pass_word=input("enter the password:")
    if username==User_name and password==Pass_word:
        print("login successful.")
        break
    else:
        print("Invalid details.")
        attempts+=1
        if attempts==3:
            print("account locked,,too many wrong attempts.")


# i=1
# while i<11:
#     print(i,end=' ')
#     i+=1

i=1
el=[]
ol=[]
while i<10:
    if i%2==0:
        el+=[i]
    else:
        ol+=[i]
    i+=1
print(el) 
print(ol) 



    
