print('Ski Scraper Party Time')

from bs4 import BeautifulSoup
import requests

#electropeak web scraping raspberry pi

r = requests.get("https://www.jfbb.com/snow-report/")
soup = BeautifulSoup(r.text, 'html.parser')
result = soup.find_all('div', attrs = {'class':'content-column snow-report-JFBB'})

for new in result:
        if 'Trails' in new.text:
                print('Found something', len(new.text))

#for new in result:
#        valuetag = result.find_all('div', attrs = {'class':'value1'})
        
print('Done')
