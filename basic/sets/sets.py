a = { 1, 2, 3 }
b = { 1, 2 }
# not indexable
# Union

a.add(4)
print(a)


a.update([5,6,7,8])
print(a)

print(a | b)
print(a.union(b))

# Intersection
print(a & b)
print(a.intersection(b))

# Difference
print(a - b)
print(a.difference(b))
