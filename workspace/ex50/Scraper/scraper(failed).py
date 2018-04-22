from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

base_url = "http://sasundergrad.rutgers.edu/degree-requirements/core"
twenty_first_centry_url = "/21st-century-challenges"
print(base_url + twenty_first_centry_url)
r  = requests.get(urljoin(base_url, twenty_first_centry_url))
data = r.text

soup = BeautifulSoup(data, "html5lib")


table_body = soup.find_all('tbody')[1]
print(table_body)

info = []

rows = table_body.find_all('tr')

for row in rows:
    print(row)
    cols = row.findAll('td')
    cols = [ele.text.strip() for ele in cols]
    info.append([ele for ele in cols if ele]) # Get rid of empty values
    
print (info)