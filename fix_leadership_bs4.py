import json
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

replacements = {
    "SOLPO (Policy Research)": {
        "Founder": "Sanjay Sen",
        "Current Head": "Sanjay Sen (Director)"
    },
    "Public Policy India": {
        "Founder": "Yash Agarwal & Michelle Patrick",
        "Current Head": "Yash Agarwal"
    },
    "NCAS India (Social Watch)": {
        "Founder": "Josantony Joseph",
        "Current Head": "N/A"
    },
    "SDE (Sustainable Economics)": {
        "Founder": "Sushil Kumar Sharma",
        "Current Head": "Sushil Kumar Sharma (CEO)"
    },
    "CPD (Policy Design)": {
        "Founder": "ATREE",
        "Current Head": "Dr. Abi Tamim Vanak (Director)"
    },
    "CFAR (Advocacy Research)": {
        "Founder": "Akhila Sivadas"
    },
    "CASP (Artistic Practice)": {
        "Founder": "Amrita Gupta & Parul",
        "Current Head": "Amrita Gupta (Director)"
    },
    "CENREC (Regional Conflict)": {
        "Founder": "N/A",
        "Current Head": "N/A"
    },
    "CIPR (Independent Policy)": {
        "Founder": "N/A",
        "Current Head": "N/A"
    },
    "LPRS (Legal & Policy)": {
        "Founder": "N/A",
        "Current Head": "N/A"
    }
}

for card in soup.find_all(class_='tt-card'):
    name_el = card.find(class_='tt-name')
    if not name_el: continue
    
    name = name_el.text.strip()
    if name in replacements:
        r_dict = replacements[name]
        for item in card.find_all(class_='tt-detail-item'):
            label_el = item.find(class_='tt-detail-label')
            val_el = item.find(class_='tt-detail-value')
            if label_el and val_el:
                label = label_el.text.strip()
                if label in r_dict:
                    val_el.string = r_dict[label]

# Write out the modified HTML. We'll use str(soup)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
