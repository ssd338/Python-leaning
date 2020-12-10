#Dictionary {}
# key 와 value로 이루어짐 key : value
# 모든 타입이 들어갈 수 있다.
''' []는 list ()는 tuple {}는 dictionary '''
Choo = {
  "name" : "Nico",
  "age" : 25,
  "Korean" : True,
  "fav_food" : ["Kimchi","garbi"]
}

#print(Choo)
print(Choo["name"])

#Dictionary에 추가하는 방법
Choo["smart"] = True
print(Choo)
