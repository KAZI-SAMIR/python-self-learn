names = ["samir","mosa","abid"]

names = ["Mike", "Kate", "Dan"]

# Length
print(len(names))

# Check if item exists
if "Kate" in names:
    print("Kate is in the list")

# Add item
names.append("Dave")
names.insert(2, "Dave")

# Remove item
names.remove("Kate")
print(names.pop())
del names[2]
del names[1:3]
names.clear()

# Join lists
names = names + ["Dave"]

# Sorting
names.sort()

print(names)
