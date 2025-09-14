classAttributes = ["Fullstack AI", 2025, 2.4, 4.0, 15, "M. Ahmad Awan"]

print("----------------------------")


# Print the complete list.
print("Complete list:")
print(classAttributes)

print("----------------------------")


# Print the second item (index 1).
print("Print the second item only:")
print(classAttributes[1])

print("----------------------------")


# Using 'for' loop to print the complete list.
print("Use the for loop to print the list:")
for attributes in classAttributes:
    print(attributes)

print("----------------------------")


# Adding a new item.
print("Add a new item by using 'insert':")
classAttributes.insert(6, "October")
print(classAttributes)

print("----------------------------")


# Removing an item.
print("Removing an item:")
classAttributes.remove("October")
print(classAttributes)

print("----------------------------")


# Popping an item.
print("Popping an item (Index 2):")
classAttributes.pop(2)
print(classAttributes)

print("----------------------------")


# Adding '500' at item 2/index 1.
print("Adding '500' at index 1:")
classAttributes[1] = 500
print(classAttributes)

print("----------------------------")

# Printing the type of second item.
print("Type of second item:")
print(type(classAttributes[1]))

print("----------------------------")