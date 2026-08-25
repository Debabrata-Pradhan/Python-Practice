# program for generating 1 to N numbers where N is +ve
n=int(input("Enter a number:"))
if (n<=0):
    print('Invalid input',n)
else:
    for i in range(1,n+1):
        print(i)