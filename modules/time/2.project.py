import sys
import time


answer = input("How long do you want to wait in seconds? ")
waitingtime = float(answer)
if waitingtime < 0:
    print("Error: cannot wait a negative time.", file=sys.stderr)
    sys.exit(1)

print("Waiting...")
time.sleep(waitingtime)
print("Done!")
