#control statements control the flow of execution in a program

# if statement
x = 10
if x > 5:
    print("x is greater than 5")


# if-else statement
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")



# if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
else:
    print("Grade: F")


#something to note about elif statements is that they are checked in order, and the first condition that evaluates to True will execute its block, and the rest will be skipped.
score = 95
if score >= 80:
    print("Score is 80 or above")
elif score >= 90:
    print("Score is 90 or above")  # This will never be reached if score is 85


