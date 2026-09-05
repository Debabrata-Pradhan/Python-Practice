#Program for using lambda function
# sum of two numbers
a=10
b=20
var=(lambda a,b :a+b)
res=var(a,b)
print(res)
sumop=(lambda a,b:a+b)
res=sumop(1020,2010)
print(res)

# subtract of two numbers
a=10
b=20
var=lambda a,b:a-b
res=var(a,b)
print(res)
var=lambda a,b:a-b
res=var(1020,2010)
print(res)

# Multiply of two numbers
a=10
b=20
var=lambda a,b:a*b
res=var(a,b)
print(res)
res=var(1020,2010)
print(res)

# Float Point Division
var=lambda a,b : a/b
res=var(10,3)
print(res)

# Floor Division
var=lambda a,b:a//b
res=var(10,3)
print(res)

# Modulo Division
var= lambda a,b:a%b
res=var(10,3)
print(res)
