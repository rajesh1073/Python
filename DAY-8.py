# operators preceedence
# it decides the order in which operators are evaluated in expressions.

# Table==>
# 1.(),{},[] ==> left to right
# ex: print((2+3)*3+5) // 20

# 2.power or exponenent
#  ** ==>right to left

# 3.right to left 
# ex:+x,-x,*x

# 4.* / or // % (left to right)

# 5. + - ==>left to right

# 6.<<,>> ==>left to right

# 7. &  ==>left to right
# 8. ^  ==>left to right
# 9. |  ==>left to right

# 10. in,not in,is,is not,==,!=,>,<,>=,<=     ==>left to right
# 11. not ==>right to left
# 12. and ==>left to right
# 13. or  ==>left to right

# 14. =,/=,//=       ==>right to left
# 15. **=,&=,|=      ==>right to left
# 16. ^=,>>=,<<=     ==>right to left

print(10+5*2)
print((10+5)*2)
print(-3**2)
print(2**3**2)
print(True or False and False)