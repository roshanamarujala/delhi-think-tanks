from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

names = [tag.get_text().strip() for tag in soup.find_all('a', class_='tt-name')]
with open('all_names.txt', 'w') as f:
    for name in names:
        f.write(f"'{name}'\n")
