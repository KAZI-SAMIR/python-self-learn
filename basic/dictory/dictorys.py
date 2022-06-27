players = {
    "Messi": { "number": 10, "club": "Barcelona"},
    "Ronaldo": { "number": 7, "club": "Juventus"}
}
#indexable

# Length
print(len(players))

# Check if item exists
if "Messi" in players:
    print("Messi is in the dict")

# Add item
players["Salah"] = { "number": 11, "club": "Liverpool" }

# Remove
#players.pop("Ronaldo")
#players.clear()

#print(players)

for key in players:
    print(key)

for value in players.values():
    print(value)

for key, value in players.items():
    print(key, value)

