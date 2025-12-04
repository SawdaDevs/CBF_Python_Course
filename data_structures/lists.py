# creating lists using square brackets
names = ["Alice", "Bob", "Charlie", "Diana"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
print("Names List:", names)
print("Numbers List:", numbers)
print("Mixed List:", mixed)

# # create a list using the list() constructor
# weather_list = list(("sunny", "rainy", "cloudy"))
# print("Weather List:", weather_list)

# convert a string to a list of characters
# print(list("hello"))

# # create a list with repeated elements
shopping_list = ["eggs"] * 3
print("Shopping List:", shopping_list)
number_list = [0] * 5
print("Number List:", number_list)

# # accessing list elements using indexing
print("First element in names:", names[0])
#numbers = [1, 2, 3, 4, 5]
print("Last element in numbers:", numbers[-1])

# #appening elements to a list, means adding an element to the end of the list
# names = ["Alice", "Bob", "Charlie", "Diana"]
names.append("Eve")
print("Updated Names List after append:", names)
names.append(["Frank", "Grace"])
print("Updated Names List after appending a list:", names)
names.extend(["Hannah", "Ian"])
print("Updated Names List after extend:", names)
names.extend("JKL")
print("Updated Names List after extending with string:", names)
names.extend({"M", "N"})
print("Updated Names List after extending with set:", names)
names.extend(("O", "P"))
print("Updated Names List after extending with tuple:", names)

# inserting elements at a specific index
# numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)
print("Updated Numbers List after insert:", numbers)
numbers.insert(0, [0, 1, 3])
print("Updated Numbers List after inserting a list:", numbers)
numbers.insert(-1, 4.5)
print("Updated Numbers List after inserting at -1 index:", numbers)
numbers.insert(5, (3.5, 3.75))
print("Updated Numbers List after inserting a tuple:", numbers)
numbers.insert(len(numbers), 6)
print("Updated Numbers List after inserting at the end:", numbers)
numbers.insert(100, 7)
print("Updated Numbers List after inserting at out-of-bounds index:", numbers)

#clear all elements from a list
# mixed = [1, "two", 3.0, True]
mixed.clear()
print("Mixed List after clear:", mixed)










