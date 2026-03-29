import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

domains = [
    ('Geopolitics & International Relations', 'section-geo'),
    ('Public Policy & Governance', 'section-pol'),
    ('Defence & Strategic Studies', 'section-def'),
    ('Economics & Finance', 'section-eco'),
    ('Technology & Cyber Security', 'section-tec'),
    ('Environment & Climate Change', 'section-env'),
    ('Social Sector & Development', 'section-soc'),
    ('Law & Justice', 'section-law'),
    ('Arts, Culture & Heritage', 'section-art'),
]

total_count = 0
results = []
for name, id_val in domains:
    section = soup.find(id=id_val)
    if section:
        cards = section.find_all(class_='tt-card')
        count = len(cards)
        total_count += count
        
        # Check the badge in the HTML
        badge = section.find(class_='domain-badge')
        badge_text = badge.text if badge else 'N/A'
        
        results.append((name, id_val, count, badge_text))
    else:
        results.append((name, id_val, "No section found", "N/A"))

print(f"Total count calculated: {total_count}")
for name, id_val, count, badge_text in results:
    print(f"{name} ({id_val}): {count} actual cards, badge says: {badge_text}")
