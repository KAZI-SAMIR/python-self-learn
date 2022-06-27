number = { "0":"ZERO", "9":"NINE", 
   "8":"EIGHT", "7":"SEVEN", "6":"SIX", 
   "5":"FIVE", "4":"FORE", "3":"THREE", 
   "2":"TWO", "1":"one"
}

user_num = input("> ")
for i in user_num:
  print(number.get(i, "(!)"),end=" ")


