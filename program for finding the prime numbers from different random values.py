#program for finding the prime numbers from different random values
print("Enter values separated by space: ")
lst=[int(val) for val in input().split() if int(val)>0]
res=[]
for i in lst:
    if i<2:
        continue
    prime=True
    for j in range(2,(i//2)+1):
        if i%j==0:
            prime=False
    if prime==True:
        res.append(i)
print(res)