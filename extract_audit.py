import json
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

domains = [
    ('section-geo', 'Geopolitics & International Relations'),
    ('section-def', 'Defence & Strategic Studies'),
    ('section-pol', 'Public Policy & Governance'),
    ('section-eco', 'Economics & Development'),
    ('section-tec', 'Technology & Cyber Policy'),
    ('section-env', 'Environment & Climate Change'),
    ('section-soc', 'Social Sector'),
    ('section-law', 'Law & Justice'),
    ('section-art', 'Arts & Culture')
]

audit_data = {}

for id_val, section_name in domains:
    section = soup.find(id=id_val)
    if not section:
        continue
    cards = section.find_all(class_='tt-card')
    section_list = []
    
    for card in cards:
        name_el = card.find(class_='tt-name')
        if not name_el: continue
        name = name_el.text.strip()
        url = name_el.get('href', '')
        
        meta = {}
        for item in card.find_all(class_='tt-detail-item'):
            lbl = item.find(class_='tt-detail-label')
            val = item.find(class_='tt-detail-value')
            if lbl and val:
                meta[lbl.text.strip()] = val.text.strip()
                
        section_list.append({
            'name': name,
            'url': url,
            'year': meta.get('Est. Year', ''),
            'founder': meta.get('Founder', ''),
            'head': meta.get('Current Head', '')
        })
    audit_data[section_name] = section_list

with open('audit_data.json', 'w', encoding='utf-8') as f:
    json.dump(audit_data, f, indent=2, ensure_ascii=False)

print(f"Extracted {sum(len(v) for v in audit_data.values())} records across {len(audit_data)} sections.")
