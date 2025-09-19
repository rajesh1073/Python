def localFunc():
    global var1
    var1="rajesh"
    print(var1)
localFunc()
print(var1)


# shadowing

rajesh="jobless"
def global_func():
    global rajesh
    rajesh="aspirants"
    print(rajesh)
global_func()
print(rajesh)


# ENCLOSING OR NONLOCAL
# Defined in the outer function,which is available in itself and to its inner functions.
# But we can't access it out of the outer function.

def outer():
    var1="Rajesh" #non local variable
    def inner():
        var1="masada"
        print(var1)
    print(var1)
    inner()
outer()


def outer():
    var1="Rajesh"
    def inner():
        nonlocal var1
        var1="masada"
        print(var1)
    # print(var1)
    inner()
    print(var1)
outer()



classname="python"
def class1():
    classname="java"
    def class2():
        nonlocal classname
        classname="c"
        print(classname)
    print(classname)  
    class2()
class1()
print(classname)


# without using keywords:
classname="python"
def class1():
    classname="java"
    def class2():
        classname="c"
        print(classname)
    print(classname)  
    class2()
print(classname)
class1()


# built-in variable
# If I use keywords as variable name it looses its functionality.
# example:
list1=[12,3,4,5]
len=10
print(len(list1))

