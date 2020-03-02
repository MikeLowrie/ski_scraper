from bs4 import BeautifulSoup
import requests

#electropeak web scraping raspberry pi

def jackfrost():
  r = requests.get("https://www.jfbb.com/snow-report/")
  soup = BeautifulSoup(r.text, 'html.parser')
  result = soup.find_all('div', attrs = {'class':'content-column snow-report-JFBB'})

  for new in result:
    if 'Trails' in new.text and len(new.text) < 250:
      #print('Found something', len(new.text))
      slopes = new.div.contents[1].div.next_sibling.next_sibling.div.string
      strippedslopes = slopes.strip()
      print(strippedslopes, 'Trails of 20')

def bearcreek():
  r = requests.get("https://www.bcmountainresort.com/play/snowsports/pa-ski-area-snowtubing-conditions/")
  soup = BeautifulSoup(r.text, 'html.parser')
  # Finding the "Open Trails" tag has been cumbersome so instead just yank every <dt> and filter
  dttags = soup.body.find_all('dt')
  for check in dttags:
    if check.text.strip() == "Open Trails":
      #print(check.text, check.next_sibling.string) <-- Removing if statement will show more detailed report
      print(check.next_sibling.string, 'of 22')

def camelback():
  r = requests.get("https://www.skicamelback.com/plan-your-trip/snow-report/")
  soup = BeautifulSoup(r.text, 'html.parser')
  dttags = soup.body.find_all('dt')
  for check in dttags:
    if check.text.strip() == "Open Trails":
      #print(check.text, check.next_sibling.string) <-- Removing if statement will show more detailed report
      print(check.next_sibling.string, 'of 37')

def bluemountain():
  r = requests.get("https://www.skibluemt.com/blue-current/")
  soup = BeautifulSoup(r.text, "html.parser")
  spantags = soup.find_all('span', attrs = {'class':'open'})
  print(spantags[0].string, 'Trails of 40')
  

print('Lowrie Ski Scraper')
print('----\n', 'Jack Frost:')
jackfrost()
print('----\n', 'Bear Creek:')
bearcreek()
print('----\n', 'Camelback:')
camelback()
print('----\n', 'Blue Mountain:')
bluemountain()

print('\n\n', 'Happy skiing!')
