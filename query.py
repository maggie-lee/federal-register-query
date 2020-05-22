from urllib.request import Request
import urllib.parse

# This is the base url you'll need to query federalregister.gov

url = 'https://www.federalregister.gov/api/v1/documents.json'

# these parameters tell it the search you want to perform
# give up to 1000 results per page
# for a search on the word 'georgia'
# show docs published since May 1, 2020
# and show docs only from the National Park Service

params = {'per_page': 1000,
          'conditions[term]': 'georgia',
          'conditions[publication_date][gte]': '2020/05/01',
          'conditions[agencies][]':'national-park-service'
          }
          
# This line takes those plain English parameters and puts them in this format the API wants like:
# 'per_page=1000&conditions%5Bterm%5D=georgia&conditions%5Bpublication_date%5D%5Bgte%5D=2020%2F05%2F01&conditions%5Bagencies%5D%5B%5D=national-park-service'
data = urllib.parse.urlencode(params)

# Then this smushes together the base url and a question mark and your encoded search parameters and calls it
response = requests.get(url + '?' + data)

# a response in bytes:
byte_response = response.content

# a response as a json object:
json_response = response.json()
