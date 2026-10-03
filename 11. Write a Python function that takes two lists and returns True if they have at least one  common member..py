#Write a Python function that takes two lists and returns True if they have at least one common member.
llst=[x for x in input("Enter values separated by space:").split()]
rlst=[y for y in input("Enter values separated by space:").split()]
p=set(llst).intersection(set(rlst))
print(bool(p),list(p))

#__OR__

for i in llst:
    if i in rlst:
        print(True)
        break
    else:
        print(False)