#Write a Python program to clone or copy a list.
lst=[x for x in input("Enter Values separated by space:").split()]
clst=lst.copy()
print("Original List:",lst)
print("Copied List:",clst)