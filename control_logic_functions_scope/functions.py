# a function is a reusable block of code that performs a specific task
# defining a function
def say_hello():
    """This function prints a greeting message."""
    print("Hello, World!")

# calling the function
say_hello()

# defining a function with a parameter  
def greet(name):
    """This function greets the person passed in as a parameter."""
    return f"Hello, {name}!"

# calling the function
print(greet("Alice"))   
print(greet("Bob"))
print(greet("Charlie"))

#defining a function with multiple parameters
def add_numbers(number_one, number_two):
    """This function returns the sum of two numbers."""
    return number_one + number_two

# calling the function
result = add_numbers(5, 10)
print(f"The sum is: {result}")
result = add_numbers(3.5, 2.5)
print(f"The sum is: {result}")
result = add_numbers(-1, 1)
print(f"The sum is: {result}")

#defining a function with default parameter values
def power(base, exponent=2):
    """This function returns the base raised to the exponent power."""
    return base ** exponent

# calling the function
print(power(3))          # uses default exponent value of 2
print(power(2, 3))       # uses provided exponent value of 3
print(power(5, 4))       # uses provided exponent value of 4

#defining a function with type hints
def divide_numbers(numerator: float, denominator: float) -> float:
    """This function returns the result of dividing the numerator by the denominator."""
    if denominator == 0:
        return "Error: Division by zero is not allowed."
    return numerator / denominator

# calling the function
print(divide_numbers(10, 2))
print(divide_numbers(7, 0))


#defining a function with keyword arguments
def introduce_person(name: str, age: int, city: str) -> str:
    """This function introduces a person with their name, age, and city."""
    return f"My name is {name}, I am {age} years old and I live in {city}."

# calling the function
print(introduce_person(name="Alice", age=30, city="New York"))
print(introduce_person(city="London", name="Bob", age=25))


#defining a function with variable-length arguments
def multiply_numbers(*args):
    """This function returns the product of all the numbers passed in as arguments."""
    result = 1
    for num in args:
        result *= num
    return result

# calling the function
print(multiply_numbers(2, 3, 4))


#defining a function with a placeholder
def placeholder_function():
    """This function is a placeholder and does nothing."""
    pass  # Placeholder for future implementation
# calling the placeholder function
placeholder_function()  # Output: No output