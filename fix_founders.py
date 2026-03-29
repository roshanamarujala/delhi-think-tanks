from bs4 import BeautifulSoup

INDEX_PATH = "index.html"

FIXES = {
    "CLAWS (Land Warfare)": {
        "Founder": "Indian Army / MoD"
    },
    "The Geostrata": {
        "Founder": "Harsh Suri (Co-founder / Team Lead)"
    },
    "MP-IDSA (National Defence)": {
        "Founder": "Govt of India / MoD"
    },
    "Vivekananda Int'l Foundation (VIF)": {
        "Founder": "Ajit Doval (Founding Director)"
    },
    "Observer Research Foundation (ORF)": {
        "Founder": "R.K. Mishra (Founder)"
    },
    "Centre for Policy Research (CPR)": {
        "Founder": "V.A. Pai Panandiker (Founder)"
    },
    "RIS (MEA Think Tank)": {
        "Founder": "Ministry of External Affairs (Govt of India)"
    },
    "Takshashila Institution": {
        "Founder": "Nitin Pai (Co-founder / Director)"
    },
    "IIDS (Social Exclusion)": {
        "Founder": "Prof. Sukhadeo Thorat (Founder Chairman)"
    },
    "CPRG India": {
        "Founder": "Dr. Raman Jha (Founder Director)"
    },
    "SPRF India": {
        "Founder": "Neha Simlai (Founder / Director)"
    },
    "Usanas Foundation": {
        "Founder": "Dr. Abhinav Pandya (Founder / CEO)"
    }
}

def apply_fixes():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    cards = soup.find_all('div', class_='tt-card')
    corrected = 0

    for card in cards:
        name_tag = card.find('a', class_='tt-name')
        if not name_tag: continue
        name = name_tag.get_text().strip()
        
        if name in FIXES:
            fix = FIXES[name]
            details = card.find('div', class_='tt-details')
            if details:
                items = details.find_all('div', class_='tt-detail-item')
                for item in items:
                    label_tag = item.find('span', class_='tt-detail-label')
                    if not label_tag: continue
                    label = label_tag.get_text().strip()
                    value_span = item.find('span', class_='tt-detail-value')
                    
                    if label == "Founder" and "Founder" in fix:
                        value_span.string = fix["Founder"]
                        print(f"Fixed Founder for: {name}")
                        corrected += 1

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print(f"Total founder corrections applied: {corrected}")

if __name__ == "__main__":
    apply_fixes()
