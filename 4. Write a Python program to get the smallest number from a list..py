#Write a Python program to get the smallest number from a list.
lst=[int(x) for x in input("Enter digits separated by spaces:").split()]
res=min(lst)
print("The minimum number in list is:",res)

#___OR___

m=0
for i in lst:
    if i<m:
        m=i
print("The minimum number in list is:",m)

#___OR___

g=list(filter(lambda x:all(x<=y for y in lst),lst))
print("The minimum number in list is:",g)