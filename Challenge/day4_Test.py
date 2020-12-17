import os
import requests

def start_answer(yORn):
  if yORn == "y" or yORn =='Y':
    os.system("clear")
    return True
  elif yORn == 'n' or yORn == 'N':
    print("k. bye")
    return False
  else:
    print("That's not a valid anwer")
    return ask_answer()

def ask_answer():
  print("Do you want to start over(y/n)")
  return start_answer(input())


yes = True
while(yes):
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma)")
  urlList = input().split(",")
  for url in urlList:
    if("com" in url):
      if("http://" not in url):
        url = "http://"+url.strip().lower()
      else:
       url = url.strip().lower()
      try:
        indeed_result = requests.get(url)
        if indeed_result.status_code == 200:
          print(f"{url} is up!")
      except:
        print(f"{url} is down!")
        pass

    else:
      print(f"{url} is not a valid URL")
  
  yes = ask_answer()