# requests - 파이썬에서 요청을 만드는 기능을 모아놓은 것
#indeed 페이지를 추출
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div",{"class":"pagination"})

pages = pagination.find_all('a')
spans= []
for page in pages:
  spans.append(page.find("span"))
spans = spans[:-1]