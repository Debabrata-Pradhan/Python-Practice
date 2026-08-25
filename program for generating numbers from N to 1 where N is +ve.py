# program for generating numbers from N to 1 where N is +ve
n=int(input("Enter a number:"))
if (n<=0):
    print("Invalid input")
else:
    for i in range(n,0,-1):
        print(i)