from bs4 import BeautifulSoup

INDEX_PATH = "index.html"

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# 1. Delete the duplicate "Aerospace Policy Hub" card
cards = soup.find_all('div', class_='tt-card')
removed = 0
for card in cards:
    name_tag = card.find('a', class_='tt-name')
    if name_tag and name_tag.get_text().strip() == "Aerospace Policy Hub":
        card.decompose()
        removed += 1
        print("Removed duplicate card: Aerospace Policy Hub")

# 2. Fix the footer text
footer = soup.find('footer')
if footer:
    footer_text = footer.get_text()
    if "186 Exhaustive Edition" in str(footer):
        # We need to find the specific <p> or tag
        p_tags = footer.find_all('p')
        for p in p_tags:
            if "186 Exhaustive Edition" in p.get_text():
                p.string = p.get_text().replace("186 Exhaustive Edition", "177 Exhaustive Edition")
                print("Updated footer census to 177.")

# Save
with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(str(soup.prettify()))
