import random

print("Enter things to mix, and press Enter without typing",
      "anything when you're done.")
things = []
while True:
    thing = input("Next thing: ")
    if thing == "":
        break
    things.append(thing)

random.shuffle(things)

print("After mixing:")
for thing in things:
    print(thing)

