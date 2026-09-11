#Program for using Decorator in Python2
def square(gv):
    def calculations():
        n=gv()
        res=n**2
        return n,res
    return calculations
@square
def getval():
    return float(input("Enter a number:"))
n,res=getval()
print("Square({})={}".format(n,res))