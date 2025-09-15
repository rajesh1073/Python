# nested for loop
# it is the process of defining one for loop inside another for loop.
# // syntax:
#     for variable1 in sequence1:
#         for variable2 in sequence2:
#             //block of code

# for every one iteration of the outer loop , inner loop completes all its iterations.
# note:
# nested for loops are mostly preffered for patterns,matrices and grids.



# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j)

# To print a square:

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()

# To print a rectangle:
# for i in range(5):
#     for j in range(10):
#         print("*",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()