## Get user input
#name = input("Please enter your name: ")

# Display the input
#print("Hello, " + name + "!")

name = input("Please enter your name: ")

# Open a file for writing
with open("users.txt", "w") as f:
    # Write the input to the file
    f.write(name)

# Display the input
print("Hello, " + name + "!")