class investor:

   def __init__(self, name: str, age: int, cash: float):
     self.name = name
     self.age = age
     self.cash = cash

   def __repr__(self):
       return f"Name:{self.name}"


   def __eq__(self, other):
      return self.name == other.name

   def __lt__(self, other):
      return self.cash < other.cash

l1 = investor("samir",20,5000)
l2 = investor("hossain",10,1000)
l3 = investor("samir",30 ,6000)


print(l1 < l3)
