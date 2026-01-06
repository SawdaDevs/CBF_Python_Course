#looping also known as iteration
#allows us to execute a block of code multiple times

# # # for loop
for i in range(10):  # iterates from 0 to 9
    print("For Loop Iteration:", i)
    
for i in range(5, 15):  # iterates from 5 to 14
    print("Second For Loop Iteration:", i)

# # iterating over a list
# fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
# for fruit in fruits:
#     print("Fruit:", fruit)

for number in [10, 20, 30]:
    print("Number:", number)

# ages = [25, 30, 35]
# for age in ages:
#     print("Age:", age)  

# # iterating over a tuple
# for number in (1, 2, 3):
#     print("Number:", number)
# # iterating over a string
# for char in "CBF":
#     print("Character:", char)

#iterating over a dictionary
person = {
    "name": "Alice", 
    "age": 30, 
    "city": "New York"
}
for attr in person:
    print("Key:", attr, "Value:", person[attr])
# iterating over dictionary items
for key, value in person.items():
    print("Key:", key, "Value:", value) 
#iterating over a set
colours = {"red", "green", "blue", "green", "purple"}  
for colour in colours:
    print("Unique colour:", colour)
