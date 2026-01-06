#what is LEGB in Python?
# LEGB is an acronym that stands for Local, Enclosing, Global, and Built-in. It describes the order in which Python looks up variable names when they are referenced in the code.


# Local (L): Variables defined within a function are in the local scope. They can only be accessed within that function.
# def local_scope_example():
#     local_var = "I am a local variable"
#     print(local_var)

# local_scope_example()
# print(local_var)  
# This would raise a NameError because local_var is not accessible outside the function.

# # Enclosing (E): Variables in the local scope of enclosing functions. This is relevant for nested functions.
# def outer_function():
#     message_one = "I am an enclosing variable"
    
#     def inner_function():
#         message_one = "I am an inner variable"
#         print(message_one)  # Accessing the inner variable
#         print("this is message_one", message_one) # Accessing the enclosing variable
#         message_two = "I am an inner variable"
#         print(message_two)  # Accessing the inner variable
#         print(message_one)  # Accessing the enclosing variable

#     # print("this is inner_var", inner_var)
#     inner_function()

# outer_function()     

# This would raise a NameError because enclosing_var is not accessible outside outer_function.



# Global (G): Variables defined at the top level of a script or module are in the global scope. They can be accessed from any function within the same module.
# global_var = "I am a global variable"


# def global_scope_example():
#     print(global_var)  # Accessing the global variable

# global_scope_example()  # Output: I am a global variable    

# print(global_var)  # Output: I am a global variable     



# Built-in (B): These are names that are pre-defined in the Python standard library. They can be accessed from any part of the code.
# def built_in_example():
#     print(len("Hello, World!"))  # Using the built-in len() function        

# built_in_example()  # Output: 13
# print(global_var)  


number_one = 10
print("before function, number_one:", number_one)  
def global_keyword_example():
    global number_one
    number_one = 20  # can now modify the global variable
    print("Inside function, number_one:", number_one)

global_keyword_example()
print("after function, number_one:", number_one)  # Output: 20

def nonlocal_example():
    outer_var = "Outer text"
    print("before inner call:", outer_var)
    def inner_function():
        nonlocal outer_var # use nonlocal to modify the enclosing variable
        outer_var = "Inner text"
        print("Inside inner function:", outer_var)

    inner_function()
    print("after inner call:", outer_var)

nonlocal_example()