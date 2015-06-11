
"""
Fetching data from news sites index pages
Use Anaconda ipython distro for Beautiful Soup

"""


import urllib

url = 'http://www.usatoday.com'

# url = 'http://www.nytimes.com'
# url = 'http://www.cnn.com'
# url = 'http://www.miamiherald.com'
# url = 'http://www.latimes.com'

u = urllib.urlopen(url)
# u is a file-like object
html_data = u.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_data)
#print(soup)   gives HTML format of index page


soup.find_all('article')  #gives XML format of all articles


"""
for link in soup.find_all("a"):
    print link.get("href")

for link in soup.find_all("a"):
    print link.text

for link in soup.find_all("a"):
    print link.text, link.get("href")

outfile = open('output.ipynb', "w")
outfile.write(html_data)
outfile.close()

"""    
