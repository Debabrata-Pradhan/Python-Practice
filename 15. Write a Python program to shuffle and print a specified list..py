#Write a Python program to shuffle and print a specified list.
lst=[x for x in input("Enter values separated by space:").split()]
print(lst)
print(list(set(lst).intersection(set(lst))))

#__OR__

import random
random.shuffle(lst)
print(lst)