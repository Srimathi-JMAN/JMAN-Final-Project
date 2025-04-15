
import requests
from bs4 import BeautifulSoup

# Step 1: Make a GET request to the website
url = 'https://www.priem.be'  # Replace with the target URL
headers = {
    'User -Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Referer': 'https://player.vimeo.com/',
    'Accept-Language': 'en-US,en;q=0.9'
}

# Make the GET request with the specified headers
response = requests.get(url, headers=headers)
print(response.text)

# Step 2: Check if the request was successful
# if response.status_code == 200:
#     # Step 3: Parse the HTML content
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # Step 4: Extract specific data (e.g., all paragraph texts)
#     paragraphs = soup.find_all('p')
#     for paragraph in paragraphs:
#         print(paragraph.text)
# else:
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")