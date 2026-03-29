import os
from bs4 import BeautifulSoup

INDEX_PATH = "index.html"

def sort_all_sections():
    print("Reading index.html...")
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Find all domain rows
    domain_rows = soup.find_all('div', class_='domain-row')
    print(f"Found {len(domain_rows)} sectors.")

    for row in domain_rows:
        sector_id = row.get('id', 'Unknown')
        grid = row.find('div', class_='tt-grid')
        if not grid:
            print(f"Skipping {sector_id} (No grid found)")
            continue

        # Get all cards
        cards = grid.find_all('div', class_='tt-card', recursive=False)
        print(f"Sorting {len(cards)} cards in {sector_id}...")

        # Sort by institutional name (link text in .tt-name)
        def get_card_name(card):
            name_tag = card.find('a', class_='tt-name')
            return name_tag.get_text().strip().lower() if name_tag else ""

        sorted_cards = sorted(cards, key=get_card_name)

        # Clear existing cards and re-add in order
        grid.clear()
        for card in sorted_cards:
            grid.append(card)

    # Save the sorted HTML
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print("Sorting complete. index.html updated.")

if __name__ == "__main__":
    sort_all_sections()
