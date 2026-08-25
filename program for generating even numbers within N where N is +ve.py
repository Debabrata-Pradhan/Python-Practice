# program for generating even numbers within N where N is +ve
n=int(input("Enter a number:"))
if (n<=0):
    print("Invalid input")
else:
    for i in range(2,n+1,2):
        print(i)
