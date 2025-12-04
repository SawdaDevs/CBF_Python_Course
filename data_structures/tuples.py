names = ("Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah", "Ian")
print("Names Tuple:", names)
numbers = (1, 2, 3, 4, 5)
print("Numbers Tuple:", numbers)

tuple_in_a_tuple = (1, 2, (3, 4), (5, 6))
print("Tuple in a Tuple:", tuple_in_a_tuple)

repeated_elements = ("hello",) * 3
print("Tuple with Repeated Elements:", repeated_elements)

# accessing tuple elements using indexing
print("First element in names:", names[0])
print("Last element in numbers:", numbers[-1])

cbf_tuple = ("C", "B", "F")
print("CBF Tuple:", cbf_tuple)
new_tuple = cbf_tuple + ("Python",)
print("New Tuple after concatenation:", new_tuple)
cbf_tuple_new = cbf_tuple[1:]
print("Sliced CBF Tuple:", cbf_tuple_new)
print("Orignal CBF Tuple remains unchanged:", cbf_tuple)
cbf_tuple_new_two = cbf_tuple[:2]
print("Another Sliced CBF Tuple:", cbf_tuple_new_two)

# names = ("Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah", "Ian")
new_names = names[1:5:2]
print("Sliced Names Tuple with step:", new_names)
reversed_new_names = names[::-1]
print("Reversed Names Tuple:", reversed_new_names)

#start at index 7 to index 1 with step -2
reversed_step_names = names[7:1:-2]
print("Reversed Step Sliced Names Tuple:", reversed_step_names)

# delete all elements from a tuple by deleting the tuple itself
mixed = (1, "two", 3.0, True)
del mixed
# print("Mixed Tuple after delete:", mixed)  # This will raise an error since '
print("Mixed Tuple has been deleted and cannot be accessed.", mixed)