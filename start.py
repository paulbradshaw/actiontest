import urllib.request
from datetime import datetime

url = "https://www.gov.uk/search/news-and-communications?people%5B%5D=braverman&order=updated-newest"

with urllib.request.urlopen(url) as response:
    html_content = response.read().decode('utf-8')

# Get the current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Generate the filename with the current date and time
filename = f"output_{current_datetime}.html"

# Write the HTML content to the generated filename
with open(filename, 'w') as file:
    file.write(html_content)
