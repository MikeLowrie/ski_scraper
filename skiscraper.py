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
      print(strippedslopes, 'Trails of 20 open')
    if 'Lifts' in new.text and len(new.text) < 250:
      lifts = new.div.contents[1].div.next_sibling.next_sibling.div.string
      strippedlifts = lifts.strip()
      print(strippedlifts, 'Lifts of 9 running')
    if 'Parks' in new.text and len(new.text) < 250:
      parks = new.div.contents[1].div.next_sibling.next_sibling.div.string
      strippedparks = parks.strip()
      parkinfo = "Park is OPEN"
      if strippedparks == "0":
        parkinfo = "Park is CLOSED"
      print(parkinfo)

def bigboulder():
  r = requests.get("https://www.jfbb.com/snow-report/")
  soup = BeautifulSoup(r.text, 'html.parser')
  result = soup.find_all('div', attrs = {'class':'content-column snow-report-BBP'})

  for new in result:
    if 'Trails' in new.text and len(new.text) < 250:
      #print('Found something', len(new.text))
      slopes = new.div.contents[1].div.next_sibling.next_sibling.div.string
      strippedslopes = slopes.strip()
      print(strippedslopes, 'Trails of 16 open')
    if 'Lifts' in new.text and len(new.text) < 250:
      lifts = new.div.contents[1].div.next_sibling.next_sibling.div.string
      strippedlifts = lifts.strip()
      print(strippedlifts, 'Lifts of 8 running')
    if 'Parks' in new.text and len(new.text) < 250:
      parks = new.div.contents[1].div.next_sibling.next_sibling.div.string
      strippedparks = parks.strip()
      print(strippedparks, 'Parks of 8 open')

def bearcreek():
  r = requests.get("https://www.bcmountainresort.com/play/snowsports/pa-ski-area-snowtubing-conditions/")
  soup = BeautifulSoup(r.text, 'html.parser')
  # Finding the "Open Trails" tag has been cumbersome so instead just yank every <dt> and filter
  dttags = soup.body.find_all('dt')
  for check in dttags:
    tag = check.text.strip()
    if tag == "Open Trails":
      #print(check.text, check.next_sibling.string) <-- Removing if statement will show more detailed report
      print(check.next_sibling.string, 'of 23 open')
    if tag == "Open Lifts":
      print(check.next_sibling.string, 'of 6 running')
    if tag == "Terrain Parks":
      print(check.next_sibling.string, 'Parks of 3 open')

def camelback():
  r = requests.get("https://www.skicamelback.com/plan-your-trip/snow-report/")
  soup = BeautifulSoup(r.text, 'html.parser')
  dttags = soup.body.find_all('dt')
  trailinfo = '';
  liftinfo = '';
  for check in dttags:
    if check.text.strip() == "Open Trails":
      #print(check.text, check.next_sibling.string) <-- Removing if statement will show more detailed report
      trailinfo = check.next_sibling.string + ' of 39 open';
    if check.text.strip() == "Open Lifts":
      liftinfo = check.next_sibling.string + ' of 14 running';
  print(trailinfo)
  print(liftinfo)
  print('Park info not currently present. Please check skicamelback.com directly.')

  #articletags = soup.body.find_all('article', attrs = {'class':'SnowReport-Trail SnotReport-feature'});
  # Park info is in <article class="SnowReport-Trail SnowReport-feature">
  # Open/Closed can be checked for the image tag i class="pti pti-open"

def bluemountain():
  r = requests.get("https://www.skibluemt.com/blue-current/")
  soup = BeautifulSoup(r.text, "html.parser")
  spantags = soup.find_all('span', attrs = {'class':'open'})
  print(spantags[0].string, 'Trails of 40 open')
  print(spantags[1].string, 'Lifts of 16 running')
  print('Park info not currently present. Please check skibluemt.com directly.')
  

print('Lowrie Ski Scraper')
print('----\n', 'Jack Frost:')
jackfrost()
print('----\n', 'Big Boulder:' )
bigboulder()
print('----\n', 'Bear Creek:')
bearcreek()
print('----\n', 'Camelback:')
camelback()
print('----\n', 'Blue Mountain:')
bluemountain()

print('\n\n', 'Happy skiing!')
