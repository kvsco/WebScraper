from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def extract_remote(term):
  word= term
  URL = f"https://remoteok.io/remote-{word}-jobs"
  result = requests.get(URL, headers = headers)
  #print(result)
  try:
    soup = BeautifulSoup(result.text,"html.parser")
    table = soup.find("table",{"id":"jobsboard"})
    td = table.find_all("td",{"class":"company position company_and_position"})

    remote_data=[]
    for i in td:
      title = i.find("h2",{"itemprop":"title"})
      comp = i.find("h3",{"itemprop":"name"})
      link = i.find("a",{"itemprop":"url"})
    
      if title and comp and link is not None:
        link = link['href']
        data={
          'title':title.string,
          'company':comp.string,
          'link': f"https://remoteok.io{link}"
        }
        remote_data.append(data)
  except:
    return "error"
  return remote_data
    