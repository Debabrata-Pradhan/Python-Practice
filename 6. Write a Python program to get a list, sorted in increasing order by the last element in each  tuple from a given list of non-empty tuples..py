# #6. Write a Python program to get a list, sorted in increasing order by the last element in each
# tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
n=int(input("How many Tuples you have:"))
if n<=0:
    print("Invalid Input")

else:
    l=[]
    for i in range(1,n+1):
        g=[int(x) for x in input("Enter value separated by space:").split()]
        l.append(tuple(g))
    print(l)
    for i in l:
        for e in l:
            if i[-1]>e[-1]:
                l.insert(l.index(e),i)
                l.remove(i)
            else:
                l.insert(0,i)
    print(l)
