for i in range(1,11,2):
 print(i)
# 1 2 3 4 5 6 7 8 9 10 11 (1,11,2)
#[1 2]  3
#[3 4]  5
#[5 6]  7
#[7 8]  9

r = range(0, 10)
print(r)
for i in r[::-1]:
    print(i)
