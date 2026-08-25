# program for generating odd numbers in reverse order
n=int(input("Enter number:"))
if n<=0:
    print("Invalid input:")
else:
    if n%2==0:
        n=n-1
    for i in range(n,0,-2):
        print(i)