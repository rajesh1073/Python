#METHODS:
# Built in functions which are used to manipulate or acccess data in data structure.

# types:
# list,tuple,string,set and dictionary

# LIST METHODS:
# 1.APPEND():
# it is used to add an element at the end of the list.
# example:
l=[1,2,3,4,5]
l.append(6)
print(l)


l=[1,2,3,4,5,6,7,8,9]
el=[]
ol=[]
for i in l:
    if i%2==0:
        el.append(i)
    else:
        ol.append(i)
print(el)
print(ol)

# INSERT():
# to add an element at a specific index value.
l=[1,2,3,4,5,6,7,8,9]
l.insert(1,1.5)
l.insert(6,5.5)
print(l)

#extend:
# it is used add multiple values to our list. 
l=[1,2,3,4,5,6,7,8,9]
l.extend([10,11,12])
print(l)


#remove:
# it is used to remove the specific value from a list.
l=[1,2,3,4,5,6,7,8,9]
l.remove(7)
print(l)
# NOTE: If we have duplicate values in our list it removes first occurance value.
l=[7,1,2,3,4,5,6,7,7,8,9]
l.remove(7)
print(l)
# [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]



#pop:
# it is used to remove the last element of the list. 
l=[1,2,3,4,5,6,7,8,9]
l.pop()
print(l)
# NOTE: If we give the value in pop it removes index position value.
l=[1,2,3,4,5,6,7,8,9]
l.pop(3)  #pop(3) here 3 denotes index position.
print(l)
# [1, 2, 3, 5, 6, 7, 8, 9]


#clear:
# to remove all the elements from the list.
l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
l.clear()
print(l) #it prints the empty list.[]


#TUPLE METHODS:


# count:
# To know the number of occurances of an element. 

t=(1,2,3,4,5,6,7,6,5,4,3,2,1)
a=t.count(7)
b=t.count(5)
print(a) # 1
print(b) # 2

# index:
# It returns the index value of first occurance of the element.
t=(1,2,3,4,5)
a=t.index(4)
b=t.index(5)
print(a) # 3
print(b) # 4

# NOTE: If we have duplicate values in our tuple it returns first occurance value of position.
t=(1,2,3,4,5,6,7,6,5,4,3,2,1)
a=t.index(4)
b=t.index(5)
print(a) # 3
print(b) # 4




