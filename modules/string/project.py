# random userID project
import string
from random import *

def passw_gen():
 letters = string.ascii_letters
 digits = string.digits
 punc = string.punctuation

 cha = letters + punc + digits
 passw = " "
 for x in range(8):
   passw+=choice(cha)
   print(passw[-1],end="")
   # print(passw,"  ")


passw_gen()
