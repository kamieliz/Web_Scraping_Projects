# import libraries required to scrape with BS
from bs4 import BeautifulSoup
import requests

# first define the link
website = 'https://subslikescript.com/movie/Mean_Girls-377092'

# send a request to a website
#obtain a response that is saved in results
result = requests.get(website)

# using the text method to obtain content
content = result.text

# using lxml parser to obtain object that
# contains all the data in a nested structure
soup = BeautifulSoup(content,'lxml')

# print the HTML in a readable format 
# using prettify method
print(soup.prettify())

# using find method to locate an element
box = soup.find('article', class_='main-article')

# locate the movie title inside h1 tag
title = box.find('h1').get_text()

# locate transcript inside a div tag
transcript = box.find('div', class_='full-script')

# modify the default params of get_text 
# to remove leading and trailing spaces
# add blank space after every new line
transcript = transcript.get_text(strip=True, separator=' ')

# print title and transcript vars to check
print(title)
print(transcript)

#export data in a text fie
with open(f'{title}.txt','w') as file:
    file.write(transcript)

