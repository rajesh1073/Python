#SET METHODS:
s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8}

#add:
# to add an element to a set.
s1={1,2,3,4,5,6}
s1.add(11)
print(s1)

#remove:
# it removes the value in a set. 
s1={1,2,3,4,5,6}
s1.remove(6)
print(s1)
# NOTE:
# it raises an error if the element to be removed is not found.
# inorder to rectify this we have to use another method called discard.

# discard:
# it is also used to remove an element ,but unlike remove it doesnot raises an error ,when the element is not found.
s1={1,2,3,4,5,6}
s1.discard(13)
print(s1)


#union:
# it add sets but removes the duplicates.
s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8}
s3={5,6,7,8,9}
print(s1.union(s2)) #or (s1 | s2)
print(s1 | s2)

#intersection:
# it gives common elements.

print(s1.intersection(s2))
print(s1&s2)

# difference:

print(s1.difference(s2))
print(s1-s2)
print(s2-s1)
print(s1-s2-s3)




#DICTIONARY METHODS:
d={
    "name":"rajesh",
    "address":"hyderabad"
}


#update:
# it is used to add a dictionary to another dictionary. 
d.update({"age":18,"clg":"bvc"})
print(d)
# {'name': 'rajesh', 'address': 'hyderabad', 'age': 18, 'clg': 'bvc'}

# get:
# it is used to access a value in a dictionary. 
a=d.get("clg")
print(a)

print(d.keys())
# it prints the all the keys in the form of list.
# dict_keys(['name', 'address', 'age', 'clg'])


print(d.values())
# it prints the all the values in the form of list.
# dict_values(['rajesh', 'hyderabad', 18, 'bvc'])


print(d.items())
# it prints the key value pairs in the form of list of tuples ,tuple consists key,value pair.
# dict_items([('name', 'rajesh'), ('address', 'hyderabad'), ('age', 18), ('clg', 'bvc')])