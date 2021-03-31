from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def extract_wework(term):
  word= term
  URL = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  result = requests.get(URL, headers = headers)
  try:
    soup = BeautifulSoup(result.text,"html.parser")
    article = soup.find("article")
    items = article.find_all("li")

    wework_data=[]
    for i in items[:]:
      title = i.find("span",{"class":"title"})
      comp = i.find("span",{"class":"company"})
      link = i.find("a")
      link = link['href']
      if title and comp and link is not None:
        data={
          'title':title.string,
          'company':comp.string,
          'link': f"https://weworkremotely.com{link}"
        }
        wework_data.append(data)
  except:
    return "error"
  return wework_data
    