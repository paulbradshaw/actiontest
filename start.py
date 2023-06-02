import urllib.request

url = "https://www.gov.uk/search/news-and-communications?people%5B%5D=braverman&order=updated-newest"

with urllib.request.urlopen(url) as response:
    html_content = response.read().decode('utf-8')

print(html_content)
