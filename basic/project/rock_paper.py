import random

p_t = 0                               #player thropies
c_t = 0                               #computer thropies

while p_t < 3 and c_t <3:
  p_h = input("ROCK: PAPER: SYGIER:   ") # p_h (player hand)
  c_h = random.randrange(3)             # 0,1,2  c_h (computer hand)

  if (                                  #putting conditions

   p_h !=  "rock"
   and p_h != "paper"
   and p_h != "sygier"

     ):
       print("")
       print(f'{"  invaild input! use:(rock , paper, sygier)  ":=^70}')
       #print("invaild input! (lower letter)") 
       print("")
       continue



  #computer conditions
  if c_h == 0:
      c_h = "rock"
  elif c_h == 1:
        c_h = "paper"
  else:
        c_h = "sygier"

  print("COMPUTER: " + c_h)


  #computer and player conditions
  if p_h == c_h:
        print("    DRAW !   ")
        print("")
  elif p_h == "rock":
        if c_h == "paper":
            c_t += 1
            print("You lost! 💀")
        else:
            p_t += 1
            print("You won! 🎉")
  elif p_h == "paper":
        if c_h == "sygier":
            c_t += 1
            print("You lost! 💀")
        else:
            p_t += 1
            print("You won! 🎉")
  elif p_h == "sygier":
        if c_h == "rock":
            c_t += 1
            print("You lost! 💀")
        else:
            p_t += 1
            print("You won! 🎉")
        pass

 # print("🏆")
  print("")

