from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

names = [tag.get_text().strip() for tag in soup.find_all('a', class_='tt-name')]
for name in names:
    if "CENREC" in name or "CIPR" in name or "LPRS" in name or "SNS" in name:
        print(f"'{name}'")
