# while loops repeat a block of code as long as a specified condition is true

count = 0
while count < 5:
    print("While Loop Count:", count)
    count += 1  # incrementing count to avoid infinite loop

#here is an example of an infinite loop, which continues indefinitely because the condition is always true
# Uncomment the following lines to see the infinite loop in action
# while True:
#     print("This is an infinite loop. Press Ctrl+C to stop.")



#nested while loops
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"Nested While Loop - i: {i}, j: {j}")
        j += 1
    i += 1  

#while with for loop
count = 1
while count <= 3:
    for letter in ['A', 'B', 'C']:
        print(f"While with For Loop - Count: {count}, Letter: {letter}")
    count += 1

#use a while loop to iterate over a list
numbers = [10, 20, 30, 40, 50]
index = 0
while index < len(numbers):
    print("Number from list using while loop:", numbers[index])
    index += 1

#use a while loop to iterate over a string
text = "CBF"
index = 0
while index < len(text):
    print("Character from string using while loop:", text[index])
    index += 1

#using break and continue in while loops
num = 0
while num < 10:
    num += 1
    if num == 5:
        print("Breaking the loop at num =", num)
        break  # exit the loop when num is 5
    if num % 2 == 0:
        print("Continuing at even num =", num)
        continue  # skip the rest of the loop for even numbers
    print("Current num (odd):", num)
