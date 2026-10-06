#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
lst=[x for x in input("Enter Values separated by space:").split()]
lst.pop(5)
lst.pop(4)
lst.pop(0)
print(lst)