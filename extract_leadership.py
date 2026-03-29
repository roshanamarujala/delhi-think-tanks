import json
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.find_all(class_='tt-card')

data = []
for card in cards:
    name_el = card.find(class_='tt-name')
    if not name_el:
        continue
    name = name_el.text.strip()
    
    meta_info = {}
    details = card.find_all(class_='tt-detail-item')
    for item in details:
        label_el = item.find(class_='tt-detail-label')
        val_el = item.find(class_='tt-detail-value')
        if label_el and val_el:
            meta_info[label_el.text.strip()] = val_el.text.strip()
                
    data.append({
        'name': name,
        'founder': meta_info.get('Founder', ''),
        'head': meta_info.get('Current Head', '')
    })

with open('leadership_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
