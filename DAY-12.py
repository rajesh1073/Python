# loops:
#       repetition of a certain condition     

# for loop:
#         it iterates over a sequence of values and 
#         continues till the last element in 
#         the sequence , if no inteerruption is caused.
# syntax:
# for variable in sequence:
#     //block of code

# range:
# it is used to generate a sequence of numbers within the limit specified.
# syntax ==> range(start,stop,step)

print("even numbers using range:")
print(list(range(0,10,2)))

print("odd numbers using range:")
print(list(range(1,10,2)))


list=[1,2,3,4,5,6,7,8,9,10]
# list=list(map(int,input().split()))
l=[]
for i in list:
    if i%2!=0:
        l.append(i) #l+=[i]
print(l)


for i in range(1,10):
    print(i,end=" ")