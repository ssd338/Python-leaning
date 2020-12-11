#function을 정의
  #def는 Definition - Define 의 약자
  #들여쓰기로 function의 시작과 끝을 판단한다 
def say_hello():
  print("hello")
#print("bye")

say_hello()
say_hello()


def say_helloWho(who):
  print("hello",who)

say_helloWho("choo")

def plus(a, b):
  print(a + b)

def minus(a, b):
  print(a - b)

plus(3, 5)
minus(3, 5)