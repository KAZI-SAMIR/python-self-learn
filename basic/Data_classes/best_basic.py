from dataclasses import dataclass,field

@dataclass(order=True, unsafe_hash=True) #<,>(0rder)
class investor:
    sort_index : float = field(init=False, repr=False)
    name: str
    age: int
    cash: float = field(repr=True) #)False,compare=False)
#    cash: float = field(repr=True, default=0.0)
    favS: str

#rapresantation function
#    def __repr__(self):
#        return "Hello"

    def __post_init__(self):
        self.sort_index = self.cash



l1 = investor("samir",20,4000,"cricket")
#l2 = investor("hossian",20)
l2 = investor("hossain",20,1000,"footboll")
l3 = investor("samir", 20,5344,"cricket")
l4 = investor("mosa", 19, 2222,"cricket")
l5 = investor("mike",23,1111,"basketball")

mylist = [l1,l2,l3,l4,l5]
mylist.sort()
print(mylist)


print(hash(l1)," l1 hashed")
print(hash(l4)," l4 hashed")

#print(l1 < l3 )
