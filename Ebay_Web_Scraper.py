import requests
from bs4 import BeautifulSoup

# Insert your ebay solds url here
url = 'https://www.ebay.com/sch/i.html?_nkw=anthony+richardson+auto+rookie+card&_sacat=0&LH_Complete=1&LH_Sold=1&rt=nc&Team=Indianapolis%2520Colts&_dcat=261328'
# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the item containers
    item_containers = soup.find('div', class_='s-item__info clearfix')

    # Extract item information
    # Find all the item containers
    item_containers = soup.select('.s-item__info.clearfix')

    # Extract item information
    for container in item_containers:
        title = container.select_one('.s-item__title').text
        price = container.select_one('.s-item__price').text
        date = container.select_one('span', {'class_': '.POSITIVE ',}).text
        link = container.select_one('a', {'class_': '.href ', })["href"]



        print(f'Title: {title}\nPrice: {price}\nDate: {date}\nLink: {link}')


