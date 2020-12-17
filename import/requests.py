# requests - 파이썬에서 요청을 만드는 기능을 모아놓은 것
import requests
import beautifulsoup4

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

print(indeed_result.text)