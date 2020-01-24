from bs4 import BeautifulSoup
import requests

#electropeak web scraping raspberry pi

def jackfrost():
  r = requests.get("https://www.jfbb.com/snow-report/")
  soup = BeautifulSoup(r.text, 'html.parser')
  result = soup.find_all('div', attrs = {'class':'content-column snow-report-JFBB'})

  for new in result:
    if 'Trails' in new.text and len(new.text) < 250:
      print('Found something', len(new.text))
      slopes = new.div.contents[1].div.next_sibling.next_sibling.div.string
      strippedslopes = slopes.strip()
      print(strippedslopes)

print('Ski Scraper Party Time')
jackfrost()
print('Done')
