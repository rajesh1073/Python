#COMPREHENSIONS:
# It is used to generate a sequence from an existing sequence in one line.
# types:
# list,tuple,set and dict

#why comprehensions:    
# 1.to reduce code size
# 2.to improve code readability and making it more understandable.



# 1. list comprehension:
# generating a list from an existing list.
# syntax:
# [expression for item in sequence if condition]

list1=[1,2,3,4,5,6,7,8,9,10,11,12]
squares=list(map(lambda x:x*x,list1))
print("squares:",squares)

l=[1,2,3,4,5]
sq=[]
for i in l:
    sq+=[i**2]
print(sq)


sq=[i**2 for i in l]
print(sq)



odds = [x for x in range(1, 11) if x% 2 != 0]
print("odds: ",odds)


list2=list(range(1,11))
odds=[x for x in list2 if x%2!=0]
print(odds)



#2.tuple comprehension:
# we can't generate a tuple using open braces().In order to generate a tuple  we have to use tuple keyword.

cel=(45,56,76,34,87,68)
fah=tuple((9/5)*temp+32 for temp in cel)
print(fah)

names=("rajesh","mani","prasanth","ravi","sunil")
gen=tuple(i[0] for i in names)
print(gen)

#3.set comprehension

names={"rajesh","mani","prasanth","ravi","sunil","rajesh"}
gen={i for i in names if len(i)>5 }
print(gen)


collection_of_marks=[1,2,3,5,6,7,62,458,1,2,3,5]
cubes={i**3 for i in collection_of_marks }
print(cubes)

#4.dictionary comprehension:
names=["rajesh","mani","prasanth","ravi","sunil","rajesh"]
gen_dict={i:len(i) for i in names}
gen_dict1={len(i):i for i in names}
print(gen_dict)
print(gen_dict1)

dict2={value:key for key,value in gen_dict.items()}
print(dict2)


# matrix generation:
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
l=[num for row in matrix for num in row]
print(l)

