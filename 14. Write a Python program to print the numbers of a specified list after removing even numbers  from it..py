#14.Write a Python program to print the numbers of a specified list after removing even numbers from it.
lst=[int(x) for x in input("Enter values separated by space:").split()]
olst=filter(lambda x:x%2!=0,lst)
print(list(olst))