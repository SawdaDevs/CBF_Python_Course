#control statements control the flow of execution in a program

# if statement
# x = 4
# if x > 5:
#     print("x is greater than 5")
#     print("This is inside the if block")
# print("x is ", x)

# z = 4 
# if z % 2 == 0:
#     print("checking "+ str(z))
#     parity = "even"
#     half = z / 2
#     print("z is "+ parity)
#     print("half of z is "+ str(half))
# print("This is outside the if block, where we go after the if statement block is executed, or if the condition isn't met.")


# if-else statement
# y = 7
# if y % 2 == 0:
#     print("y is even")
# else:
#     print("y is odd")
# print("This is outside the if-else block.")

# logged_in = True
# if logged_in:
#     print("Welcome back, user!")
# else:
#     print("Please log in to continue.")
# print("This is outside the if-else block.")

# age = 16
# is_student = False

# if age < 18:
#     if is_student:
#         price = 5
#     else:
#         price = 10
# else:
#     if is_student:
#         price = 8
#     else:
#         price = 12
# print(f"The ticket price is: ${price}")


# # if-elif-else statement
score = 39
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
elif score >= 50:
    print("Grade: E")
else:
    print("Grade: F")
print("The score was ", score)
print("This is outside the if-elif-else block.")





# #something to note about elif statements is that they are checked in order, and the first condition that evaluates to True will execute its block, and the rest will be skipped.
# score = 95
# if score >= 80:
#     print("Score is 80 or above")
# elif score >= 90:
#     print("Score is 90 or above")  # This will never be reached if score is 85


