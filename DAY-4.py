# List: An ordered, mutable collection that allows duplicates

numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "Two", 3.0, True]

print(numbers[2])
print(names[0])
print(mixed[1])
print(numbers+names)


# Tuple: An ordered, immutable collection that allows duplicates

coordinates = (10.0, 20.0)
fruits = ("apple", "banana", "cherry")
single_item = ("apple",)  # Note the comma for single-element tuple

print(fruits[1])

# Dictionary: A collection of key-value pairs with unique keys

person = {"name": "Alice", "age": 30, "city": "New York"}
scores = {1: "A", 2: "B", 3: "C"}
nested = {"John": {"age": 27, "hometown": "Boston"}, "Rebecca": {"age": 31, "hometown": "Chicago"}}

dict={'name':'rajesh',
      'age':21,
      'qualification':'B.Tech',
      'group':'cse'
}
dict1={('name'):'rajesh',
      'age':21,
      'qualification':'B.Tech',
      'group':'cse'
}

print(dict1)

print(dict)
print(dict['name'])
print(dict['age'],dict['qualification'])

#modifying dictionary
dict['address']='narsipatnam'
dict['phoneno']=9160463808
print(dict)

print(dict['phoneno'])

# Set: An unordered collection of unique elements

unique_numbers = {1, 2, 3, 4, 5}
colors = {"red", "green", "blue"}


# frozen set
# it is similar to set but it is immutable

raj=frozenset([1,2,3,4,5,3,2])
print(raj)
print(type(raj))

rajesh=frozenset([])
print(rajesh)

raj=[]
print(raj)
print(type(raj))

raj=()
print(raj)
print(type(raj))

raj={}
print(raj)
print(type(raj))

raj=set()
print(raj)
print(type(raj))