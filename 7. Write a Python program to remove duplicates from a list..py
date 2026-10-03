#Write a Python program to remove duplicates from a list.
lst=[x for x in input("Enter values separated by space:").split()]
for i in lst:
    if lst.count(i)>1:
        lst.remove(i)
print(lst)

#__OR__

result=list(set(lst))
print(result)