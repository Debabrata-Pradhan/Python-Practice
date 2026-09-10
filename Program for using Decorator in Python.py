#Program for using Decorator in Python
def square(gv):
    def operation():
        val=gv()
        res=val**2
        return val,res
    return operation
def get_value():
    return float(input("Enter a number to find its SQUARE:"))

op=square(get_value)
gn,res=op()
print("SQUARE ({}) = {}".format(gn,res))