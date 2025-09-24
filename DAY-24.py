#   STRING METHODS:
# a string is a sequence of characters.(characters can be alphabets ,numbrs or symbols).
# it is denoted by single('string') or double quotes.("string")
# ex: 'venkat' 'rajesh' "naidu123"


# single line strings:
name="rajesh"
print(type(name)) #<class 'str'>

# Declaring strings in different types:
name="rajesh"
print(type(name)) #<class 'str'>

# multi line strings:
# i use three single quotes('''paragraph''') or three double quotes("""paragraph""").

details="""My name is Rajesh Masada,
I have done B.Tech in CSE."""
print(details)
#My name is Rajesh Masada,
#I have done B.Tech in CSE.


# INDEXING IN STRINGS:
# Just like in list and tuple we can perform indexing in strings based on their index value.

list1=["rajesh","pavan","naidu","prasanth","praneeth"]
print(list1[3])
#prasanth

name="rajesh"
count=0
for i in name:
    count+=1
# a=len(name)
print(name[count//2])
#e


# SLICING:
# It is a technique to access a part of string,using index value.
# syntax:
#         string[start:stop:step]

name="bandela maniteja"
print(name[8:12]) #mani
print(name[-8:-4]) #mani

name="sri sriram karthikeya"
print(name[7:10],name[11:18])  #ram karthik

print(name[-14:-11],name[-10:-3]) #ram karthik

print(name[-17:-11]) #sriram

# step index:
print(name[4::2]) #sia atiea


# printing even indexes without using slicing:
name='sri sriram karthikeya'
for i in range(len(name)):
    if i%2==0:
        print(name[i],end='')
print()
# printing odd indexes without using slicing:
name='sri sriram karthikeya'
for i in range(len(name)):
    if i%2!=0:
        print(name[i],end='')
print()


name="rajesh"
# when you dont't provide an index value at start point,it starts from 0.
print(name[:3]) #raj
# when you don't provide stop index value in slicing it prints the string till last.
print(name[3:]) #esh



name="sri sriram karthikeya"
print(name[-17:-11]) #sriram
# reverse using slicing:
print(name[::-1]) #ayekihtrak marirs irs

# reverse without using sllicing:
name="rajesh"
rev_name=""
for i in name:
    rev_name=i+rev_name
print(rev_name) #hsejar

# METHODS IN STRINGS:
# 1.upper() and lower():
# upper turns a entire string into upper case.
# lower turns a entire string into lower case.

name="rajesh"
print(name.upper()) #RAJESH
name='RAJESH'
print(name.lower()) #rajesh

# 2.capitalize():
#it converts starting letter can be converted to capital letter.
name="rajesh masada"
print(name.capitalize()) #Rajesh masada

# 3.title():
#it converts every word starting letter can be converted to capital letter.
name="rajesh masada"
print(name.title()) #Rajesh Masada

# 4.split():
# it returns a list of values separated using a separator.
name="rajesh pavan maniteja"
print(name.split()) #['rajesh', 'pavan', 'maniteja']
name="rajesh,pavan,maniteja"
print(name.split(",")) #['rajesh', 'pavan', 'maniteja']



# 5.join():
# list of values joins with separator and converts into string
# it is opposite to split , it joins with separator
name=['rajesh', 'pavan', 'maniteja']
print(",".join(name)) #rajesh,pavan,maniteja

name=['rajesh', 'pavan', 'maniteja']
print("-".join(name)) #rajesh-pavan-maniteja

name=['rajesh', 'pavan', 'maniteja']
print(" ".join(name))  #rajesh pavan maniteja