n=int(input("Enter a number:"))
if (n<=0):
    print("Invalid input")
else:
    for i in range(1,n+1,2):
        print(i)