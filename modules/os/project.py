import os
import sys

print("You are currently in %s." % os.getcwd())

while True:
    path = input("A path, or nothing at all to quit: ")
    if path == '':
        # We could just break out of the loop, but I'll show how
        # this can be done with sys.exit. The difference is that
        # break only breaks the innermost loop it is in, and
        # sys.exit ends the whole program.
        sys.exit()
    if os.path.isfile(path):
        print("It's a file!")
    elif os.path.isdir(path):
        print("It's a folder!")
    elif os.path.exists(path):
        # i have no idea when this code would actually run
        print("Interesting, it exists but it's not a file or a folder.")
    else:
        print("I can't find it :(", file=sys.stderr)
