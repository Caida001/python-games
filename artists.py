import requests
from bs4 import BeautifulSoup
import csv

# collect first page of artists' list
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

# create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# remove bottom links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

# create a file to write to, add headers row
f = csv.writer(open('artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

# pull all text from the BodyText div
artist_name_list = soup.find(class_='BodyText')

# pull text from all instances of <a> tag
artist_name_list_items = artist_name_list.find_all('a')

# create for loop to print out all artists' names
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')
    # add each artist's name and associated link to a row
    f.writerow([names, links])
