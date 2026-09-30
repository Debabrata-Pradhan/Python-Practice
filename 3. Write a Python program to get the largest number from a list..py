#Write a Python program to get the largest number from a list.
lst=[int(x) for x in input("Enter digits separated by space:").split()]
res=max(lst)
print("The largest number in list:",res)

#___OR___
L=0
for i in lst:
    if i>L:
        L=i
print("The largest number in list:",L)

#___OR___

result=list(filter(lambda x: all(x>=y for y in lst),lst))
print("The largest number in list:",result)