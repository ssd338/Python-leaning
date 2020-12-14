# Keyword Argument

def mius(a, b):
  return a - b

#result = plus(2, 4)
result = mius(b=30, a=1) # Keyword Argument - 인자에 값을 순서가 아닌 이름으로 지정해줌
print(result)

def say_hello(name, age,country):
  return f"Hello {name} you are {age} years old and you are from {country}"

hello = say_hello(name="승연", age=26, country="Korea")
print(hello)