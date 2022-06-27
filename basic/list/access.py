names = ["samir","mosa","abid"]

print(names[-2])

names = ["Mike", "Kate", "Dan"]

print(names[-2])

# Indexing
#  0  1  2
# -3 -2 -1
print("""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

""")


# Access Range of Items

print(names[0:3])
print(names[:2])
print(names[1:])

# Loop

for name in names:
    print(name)
