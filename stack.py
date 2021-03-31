from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def extract_stack(term):
  word= term
  URL = f"https://stackoverflow.com/jobs?r=true&q={word}"
  result = requests.get(URL, headers = headers)
  try:
    soup = BeautifulSoup(result.text,"html.parser")
    div = soup.find("div",{"class":"listResults"})
    items = soup.find_all("div",{"class":"grid--cell fl1"})
  #h2: title,link
  #h2 = div.find_all("h2",{"class":"mb4 fc-black-800 fs-body3"})
  #h3: company
  #h3 = div.find_all("h3",{"class":"fc-black-700 fs-body1 mb4"})
  
    stack_data=[]
    for i in items:
      title = i.find("a")['title']
      link = i.find("a")['href']
      comp = i.find("span")
      if title and comp and link is not None:
        comp = comp.get_text()
        comp = comp.replace(" ","")
        comp = comp.replace("\r\n","")
        data={
          'title':title,
          'company':comp,
          'link': f"https://stackoverflow.com{link}"
        }
        stack_data.append(data)
  except:
    return "error"
  return stack_data
    