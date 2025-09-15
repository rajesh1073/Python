# LOOP CONTROL STATEMENTS
# break,continue and pass 
# BREAK:
    # it abruptly ends a loop in between when a condition is matched.
# CONTINUE:
    # It skips the current iteration and goes for next iteration.
# PASS:
    # It does nothing ,it just acts as a placeholder.
    # It does not throws error.

# example of pass
# i=0
# while i<5:
#     pass
#     i+=1

# print("Rajesh Masada")


# example of continue
# n=int(input("enter the value:"))
# for i in range(1,n+1):
#     if i%2==0:
#         continue
#     print(i)


# example of break
# n=int(input("enter the n value:"))
# for i in range(1,n+1):
#     if i==6:
#         break
#     print(i)

n=int(input("enter the value:"))
for i in range(1,n+1):
    if i%2==0:
        pass
    if i==5:
        continue
    if i==10:
        break 
    print(i)