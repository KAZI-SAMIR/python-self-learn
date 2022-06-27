################### normal function
import math

def area(r):
  return math.pi * (r ** 2)

radius = [2,3,5,7,3.6,7.9]

areas = []
for r in radius:
  areas.append(area(r))
#print(areas)



############### map function
import math

def area(r): 
 return math.pi * (r ** 2)


radius = [2,3,5,7,3.6,7.9]
result = list(map(area, radius))
print(result)


############ maltipal input in singal line
x, y = map(int,input("enter 2 nmber : ").split())
print(x,y)
print(y,x)

nums = list(map(int,input("enter some  numbers : ").split()))
print(nums)
print(*nums) #unpack
