#Write a Python program to multiply all the items in a list.
import functools
lst=[int(i) for i in input("Enter numbers separated by space:").split()]
res=functools.reduce(lambda x,y:x*y,lst)
print("Multiplication of given list items is:",res)
#___OR___
l=1
for i in lst:
   l*=i
print("Multiplication of given list items is:",l)
