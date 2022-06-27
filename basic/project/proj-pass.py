def hello(name, mes):
  print("Hello "+ name +". "+ mes)
  ans = input("password: ")
  if ans == "0000":
   print("good!")
  elif ans == "00000000" or ans == "password":
   print("you you fucking mad!..")
  else:
   print("Password incorrect! ")



name = input("Hey! What's your name: ")

if name:
  hello(name,mes=" inout password: ")


else:
  print("(no name)")
