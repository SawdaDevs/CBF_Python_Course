x = None

print(None)
print(type(None))
print(x)

if None:
    print("Will not run")
else:
    print("None is Falsy")

print(x is None)
print(x == None)

x = "Jude"
if x is not None:
    print("This has a value")
else:
    print("This is None")