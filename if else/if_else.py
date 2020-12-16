#if else문
# if 조건: 실행
# else : 실행

def plus(a, b):
  if type(b) is int or type(b) is float:
    return a + b
  else:
    return None

print(plus(12,"2"))