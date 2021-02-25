# Guided Exploration No. 3
# Levi Williams

# Import the random library
import random

# Create an empty list to hold the possible names
possible_names = []

# Open a file to write the final handles to
outputFile = open('rap-names-output.txt', 'w')

# Open the rap-names.txt file in read mode
with open('rap-names.txt', 'r') as dataFile:
    # Iterate through each line of the file
    for name in dataFile:
        # Remove the newline character and append that line's name to the possible_names list
        possible_names.append(name.rstrip())

# Ask the user how many names they'd like to create
count = int(input('How many rap names would you like to create? '))
# Ask the user how many parts each name should have
parts = int(input('How many parts should the name contain? '))

# Use a counted loop to create the number of names specified by the user
for i in range(count):
    # Create an empty list to hold parts of names
    name_parts = []
    # Use a counted loop to add the number of parts requested to the name_parts list
    for j in range(parts):
        # Append a random name part to the name_parts list
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
    # Combine all the name parts and write the finished handle to the rap-names-output.txt file
    outputFile.write(f"{' '.join(name_parts)}\n")
    # Also print each handle to the console
    print(f"{' '.join(name_parts)}")

# Close the rap-names-output.txt file
outputFile.close()
