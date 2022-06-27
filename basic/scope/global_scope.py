def cal_a(ps):
  global ex_p

  ex_p = 20
  am = 0

  for p in ps:
   am += p

  am += ex_p
  return am


ex_p = 10
my_a = [10,20]
am = cal_a(my_a)
print("")
print(my_a,"(My amounds)")
print(ex_p,"(extra prize)")
print(am , "(Total Amounds)")
