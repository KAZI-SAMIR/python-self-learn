import random

n_r = int(input("number of rollings: "))

for index in range(n_r):
  dice = random.randrange(1,7) # print(dic)
  #print(dice)
  if dice == 1:
        print("⚀")
  elif dice == 2:
        print("⚁")
  elif dice == 3:
        print("⚂")
  elif dice == 4:
        print("⚃")
  elif dice == 5:
        print("⚄")
  elif dice == 6:
        print("⚅")



