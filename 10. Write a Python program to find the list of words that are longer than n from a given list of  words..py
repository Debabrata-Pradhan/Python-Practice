#Write a Python program to find the list of words that are longer than n from a given list of words.
lst=[x for x in input("Enter values separated by:").split()]
n=int(input("Enter n value:"))
nlst=[]
for i in lst:
    if len(i)>n:
        nlst.append(i)
print(nlst)