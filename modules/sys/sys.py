

"""
`sys.stdin`, `sys.stdout` and `sys.stderr` are [file objects](files.md),
just like the file objects that `open()` gives us.

"""


import sys
print("Hello!", file=sys.stdout)  # this is where prints go by default
Hello!
print("Hello!", file=sys.stderr)  # use this for error messages
Hello!
line = sys.stdin.readline()  # i will type hello and press enter

print(line)
"""
'hello\n'
"""

# information about Python's version, behaves like a tuple
sys.version_info
sys.version_info(major=3, minor=7, micro=3, releaselevel='final', serial=0)
sys.version_info[:3]  # this is Python 3.7.3
#(3, 7, 3)

sys.exit()  # exit out of Python
