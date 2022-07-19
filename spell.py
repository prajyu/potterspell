
import urllib.request
from bs4 import BeautifulSoup
import json

url = 'https://www.oprahdaily.com/entertainment/a32598018/harry-potter-spells-list/'
keyClass = "body-h2 css-1cfsuft et3p2gv0"
file_name = 'potter.json'


def getSpells():
  with urllib.request.urlopen(url) as response:
   spells = []
   headings = []
   html = response.read()
   data = BeautifulSoup(html, 'html.parser')
   unordered_list = data.find_all('ol')
   keys = data.find_all('h2',{"class":keyClass})

   for ol in range(len(unordered_list)):
     headings.append(keys[ol].text)
     for li in unordered_list[ol].find_all('li'):
       spells.append(li.text.strip('*').split('-'))
  return {"spells":spells,"headings":headings}

def parseSpells(spells):
  ret = []
  spellList = spells["spells"]
  for i in spellList:
    inter = {}
    inter['spell'] =i[0].strip()
    inter['effect'] = i[1].strip()
    ret.append(inter)
  return ret
  

def main():
  spells = getSpells()
  parsedSpells = parseSpells(spells)
  json_object = json.dumps({"spells":parsedSpells},indent=0)
  with open(file_name, "w") as outfile:
    outfile.write(json_object)
  

main()