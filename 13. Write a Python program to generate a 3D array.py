#Write a Python program to generate a 3*4*6 3D array whose each element is *.

array_3d = [[['*' for col in range(6)] for row in range(4)] for layer in range(3)]

print(array_3d)
