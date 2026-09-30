#Write a Python program to sum all the items in a list.
import functools
lst=[int(i) for i in input("Enter numbers separated by space:").split()]
res=functools.reduce(lambda a,b:a+b,lst)
print(res)

#or
res=sum(lst)
print("The sum is:",res)