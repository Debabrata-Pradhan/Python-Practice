#Write a Python program to check a list is empty or not.
lst=[x for x in input("Enter values separated by space:").split()]
print(lst)
print(len(lst))
if len(lst)==0:
    print("Empty list")
else:
    print("Filled list")
