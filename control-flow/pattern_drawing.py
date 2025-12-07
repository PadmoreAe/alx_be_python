# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Start counting rows from 0
row = 0

# Use a while loop to print each row
while row < size:
    # Inside the while loop, use a for loop to print stars on the same line
    for i in range(size):
        print("*", end="")

    # Print a new line after each row
    print()

    # Move to the next row
    row += 1
