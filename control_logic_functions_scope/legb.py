#what is LEGB in Python?
# LEGB is an acronym that stands for Local, Enclosing, Global, and Built-in. It describes the order in which Python looks up variable names when they are referenced in the code.


# Local (L): Variables defined within a function are in the local scope. They can only be accessed within that function.
def local_scope_example():
    local_var = "I am a local variable"
    print(local_var)

local_scope_example()
# print(local_var)  
# This would raise a NameError because local_var is not accessible outside the function.

# Enclosing (E): Variables in the local scope of enclosing functions. This is relevant for nested functions.
def outer_function():
    enclosing_var = "I am an enclosing variable"
    
    def inner_function():
        print(enclosing_var)  # Accessing the enclosing variable
    
    inner_function()

outer_function()
# print(enclosing_var)      

# This would raise a NameError because enclosing_var is not accessible outside outer_function.



# Global (G): Variables defined at the top level of a script or module are in the global scope. They can be accessed from any function within the same module.
global_var = "I am a global variable"

def global_scope_example():
    print(global_var)

global_scope_example()  # Output: I am a global variable    

print(global_var)  # Output: I am a global variable     



# Built-in (B): These are names that are pre-defined in the Python standard library. They can be accessed from any part of the code.
def built_in_example():
    print(len("Hello, World!"))  # Using the built-in len() function        
