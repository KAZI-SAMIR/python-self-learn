import time

start = time.time()
answer = input("What is 1 + 2? ")
end = time.time()
difference = end - start

if answer == '3':
    print("Correct! That took %.2f seconds." %difference)
else:
    print("That's not correct...")
