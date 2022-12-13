from bs4 import BeautifulSoup
from datetime import date
import requests

#electropeak web scraping raspberry pi

def jackfrost():
  r = requests.get("https://www.jfbb.com/the-mountain/mountain-conditions/lift-and-terrain-status.aspx")
  soup = BeautifulSoup(r.text, 'html.parser')
  result = soup.find_all('div', attrs = {'class':'terrain_summary__tab_main__text'})
  print(result[0].span.contents[0], 'Lifts of 15');
  print(result[2].span.contents[0], 'Trails of 37')

def bearcreek():
  r = requests.get("https://www.bcmountainresort.com/activities/ski-snowboarding/ski-conditions/")
  soup = BeautifulSoup(r.text, 'html.parser')
  
  result = soup.find_all('h3')
  for check in result:
    if check.text.strip() == "Open trails":
      print(check.parent.parent.next_sibling.next_sibling.contents[1].p.string, 'of 23')
    if check.text.strip() == "Open Lifts":
      print(check.parent.parent.next_sibling.next_sibling.contents[1].p.string, 'of 6 (including Snowtubing)')

def camelback():
  r = requests.get("https://conditions.camelbackresort.com/conditions/snow-report/snow-report/")
  soup = BeautifulSoup(r.text, 'html.parser')
  dttags = soup.body.find_all('dt')
  for check in dttags:
    if check.text.strip() == "Open Trails":
      print(check.next_sibling.string, 'of 37')

def bluemountain():
  r = requests.get("https://snow.skibluemt.com/conditions/snow-report/")
  soup = BeautifulSoup(r.text, "html.parser")
  result = soup.find_all('dt')
  for check in result:
    if check.text.strip() == "Open Trails":
      print(check.next_sibling.string, 'Trails')
    if check.text.strip() == "Open Lifts":
      print(check.next_sibling.string, 'Lifts')
  

print('Lowrie Ski Scraper')
print('Report for', date.today())
print('----\n', 'Jack Frost and Big Boulder:')
jackfrost()
print('----\n', 'Bear Creek:')
bearcreek()
print('----\n', 'Camelback:')
camelback()
print('----\n', 'Blue Mountain:')
bluemountain()

print('\n\n', 'Happy skiing!')
