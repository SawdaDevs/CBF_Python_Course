#is or is not are identity operators in Python.
#They are used to compare the memory locations of two objects.

a = None
print(a is None)      # True, because a is None

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)
print(x is not z)
print(x == z)

print(id(x), id(y), id(z))

s1 = "CBF"
s2 = "CBF"

print(s1 is s2)
print(id(s1), id(s2))