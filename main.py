
#===============================================================
def p_plus(a, b):
  print(a + b)

def r_plus(a, b):
  return a + b

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)  #return 값이 없으므로 p_result는 none