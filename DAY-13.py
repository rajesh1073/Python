
# for loop on dictionary:
    #  By default the for loop returns on all keys in our dictionary,when it is iterated through a dictionary. 
    #  We have to use values() method of dictionary to access the values in it.



# dict={
#     's1':'rajesh',
#     's2':'pavan',
#     's3':'sunil'
# }
# l=[]
# for i in dict.keys():
# for i in dict:    #it will print keys by default or keys() method.
#     l=l+[i]
# print(l)

# l=[]
# for value in dict.values():  #it will print values using values() method.
#     l=l+[value]
# print(l)

# for key,value in dict.items(): #it will print both keys and values at a time using items() method.
#     print(f'Id = {key} : Name = {value}')

# ele=int(input("enter the number:"))
# for i in range(1,11):
#     if i==ele:
#         print("found")
#         break
# else:
#     print("not found")

l=list(map(int,input().split()))
for i in l:
    if i==5:
        print(f"found")
        break
else:
    print("not found")
