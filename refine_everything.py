from bs4 import BeautifulSoup
import re
import urllib.parse

INDEX_PATH = "index.html"

# Top-tier Verified High-Res Logos
# (Manually sourced or high-probability official paths)
VERIFIED_LOGOS = {
    "ORF": "https://www.orfonline.org/wp-content/themes/orf/img/orf_logo.png",
    "IDSA": "https://www.idsa.in/sites/default/files/idsa-logo.png",
    "CLAWS": "https://www.claws.in/wp-content/themes/claws/images/logo.png",
    "CAPSS": "https://capssindia.org/wp-content/uploads/2021/04/Logo.png",
    "CPR": "https://cprindia.org/wp-content/themes/cprindia/images/logo.png",
    "TAKSHASHILA": "https://takshashila.org.in/wp-content/uploads/2021/08/takshashila-logo.png"
}

def refine():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # A. RE-SORT & VERIFY COUNT
    cards = soup.find_all('div', class_='tt-card')
    total = len(cards)
    print(f"Final Count: {total}")
    
    # B. RE-INJECT LOGOS WITH ROBUST PROXY
    for card in cards:
        name_tag = card.find('a', class_='tt-name')
        if not name_tag: continue
        name = name_tag.get_text().strip()
        href = name_tag.get('href', '')
        
        domain = ""
        try:
            parsed = urllib.parse.urlparse(href)
            domain = parsed.netloc
            if domain.startswith('www.'):
                domain = domain[4:]
        except:
            pass
            
        img = card.find('img')
        if img:
            # High-fidelity source
            logo_src = f"https://t1.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://{domain}&size=128"
            
            # Check if we have a top-tier override
            for key, val in VERIFIED_LOGOS.items():
                if key in name.upper():
                    logo_src = val
                    break
            
            img['src'] = logo_src
            # Robust error handling for the monogram
            # Using a more standard fallback for the monogram
            img['onerror'] = "this.style.display='none'; this.nextElementSibling.style.display='flex';"

    # C. CENSUS DASHBOARD SYNC (Line 505 / Class-based)
    # Re-calculate type counts
    types = {'govt': 0, 'semi': 0, 'private': 0}
    for card in cards:
        t_div = card.find('div', class_='tt-type')
        if t_div:
            if 'govt' in t_div['class']: types['govt'] += 1
            elif 'semi' in t_div['class']: types['semi'] += 1
            elif 'private' in t_div['class']: types['private'] += 1

    # Apply to Census Dashboard
    census_grid = soup.find('div', class_='metrics-grid')
    if census_grid:
        metric_cards = census_grid.find_all('div', class_='metric-card')
        for m_card in metric_cards:
            label = m_card.find('span', class_='label').get_text().strip()
            count_span = m_card.find('span', class_='count')
            if 'Total Institutions' in label:
                count_span.string = str(total)
            elif 'Govt Bodies' in label:
                count_span.string = str(types['govt'])
            elif 'Semi-Govt' in label:
                count_span.string = str(types['semi'])
            elif 'Private' in label:
                count_span.string = str(types['private'])

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        # Prettify may change whitespace, but we want it clean
        f.write(str(soup))
    
    print("Refinement complete.")

if __name__ == "__main__":
    refine()
