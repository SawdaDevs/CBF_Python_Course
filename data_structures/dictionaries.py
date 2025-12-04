# a mapping of key to value pairs
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    30: True
}

#keys of a dictionary must be immutable data types like strings, numbers, or tuples, not lists, sets, or other dictionaries.

print("my_dict", my_dict)
# accessing values by key
print('my_dict["name"]', my_dict["name"])  # Output: Alice
print('my_dict.get("age")', my_dict.get("age"))  # Output: 30
print('my_dict[30]', my_dict[30])  # Output: True

another_dict = dict(country="USA", profession="Engineer")
print("another_dict", another_dict)


# adding or updating key-value pairs
my_dict["email"] = "example@python.c.uk"
my_dict["age"] = 31  # updating existing key
print("Updated my_dict:", my_dict)

# removing key-value pairs
del my_dict["city"]
removed_value = my_dict.pop("age")
print("Removed age:", removed_value)
print("my_dict after removals:", my_dict)
popped_item = my_dict.popitem()  # removes and returns an arbitrary (key, value) pair
print("Popped item:", popped_item)
print("my_dict after popitem:", my_dict)
my_dict.clear()
print("After Clearing my_dict:", my_dict)

# dictionary methods
sample_dict = {"a": 1, "b": 2, "c": 3}
print("Keys:", sample_dict.keys())
print("Values:", sample_dict.values())
print("Items:", sample_dict.items())


