# import libraries required to scrape with BS
from bs4 import BeautifulSoup
import requests

# first define the link 
# root var is to help scrape multiple pages
root = 'https://subslikescript.com'
website = f'{root}/movies'

# send a request to a website
#obtain a response that is saved in results
result = requests.get(website)

# using the text method to obtain content
content = result.text

# using lxml parser to obtain object that
# contains all the data in a nested structure
soup = BeautifulSoup(content, 'lxml')

# using find method to locate an element
box = soup.find('article', class_='main-article')

# locate multiple elements
# href=True is to extract the link
# loop through all the inks from href
# save them into a list one by one
links = [link['href'] for link in box.find_all('a', href=True)]

# print the list to see the links you want
# to scrape
print(links)

# scrape the transcript of each link
# with for loop
for link in links:
    result = requests.get(f'{root}/{link}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    
    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
    
    with open(f'{title}.txt', 'w') as file:
        file.write(transcript)
    
    



