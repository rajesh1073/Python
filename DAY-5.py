# Frozen Dictionary
var1={1,2,3,4,5,3,4,1}
print(var1)
var2={6,7,8,9,10}
print(var2)

var3=var1.union(var2)
print(var3)

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


#Dictionary
# it is a seqeunce of data in the form of key-value pairs.
# it is mutable and unordered.
# key must be unique and immutable type.
# by using key we acan access a specific value.
# 
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