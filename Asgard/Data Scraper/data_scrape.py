import requests
import pandas as pd
from bs4 import BeautifulSoup

# Send an HTTP GET request to the website
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
csv_filename = "quotes.csv"
# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract quotes, authors, and tags
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tag_lists = soup.find_all('div', class_='tags')

    output = []
    # Process and print the extracted data
    for i in range(len(quotes)):
        data = {}
        data["quote"] = quotes[i].text
        data["author"] = authors[i].text
        data["tags"] = [tag.text for tag in tag_lists[i].find_all('a', class_='tag')]

        print(data)
        print("-" * 40)
        output.append(data)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

df = pd.DataFrame(output)
df.to_csv(csv_filename, index=False)
