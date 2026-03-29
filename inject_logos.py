from bs4 import BeautifulSoup
import urllib.parse

INDEX_PATH = "index.html"

def inject_logos():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all('div', class_='tt-card')
    
    print(f"Processing {len(cards)} cards for logo integration...")

    for card in cards:
        header = card.find('div', class_='tt-header')
        if not header: continue
        
        # Check if already injected
        if header.find('div', class_='tt-logo'):
            continue
            
        name_link = header.find('a', class_='tt-name')
        if not name_link: continue
        
        href = name_link.get('href', '')
        name = name_link.get_text().strip()
        first_char = name[0].upper() if name else "?"
        
        domain = ""
        try:
            parsed = urllib.parse.urlparse(href)
            domain = parsed.netloc
            if domain.startswith('www.'):
                domain = domain[4:]
        except:
            pass
            
        # Create Logo Container
        logo_div = soup.new_tag('div', attrs={"class": "tt-logo"})
        
        if domain:
            logo_img = soup.new_tag('img', attrs={
                "src": f"https://logo.clearbit.com/{domain}",
                "alt": f"{name} logo",
                "onerror": f"this.style.display='none'; this.nextElementSibling.style.display='flex';"
            })
            logo_div.append(logo_img)
            
        # Fallback Monogram
        monogram = soup.new_tag('span', attrs={"class": "monogram", "style": "display: none;" if domain else "display: flex;"})
        monogram.string = first_char
        logo_div.append(monogram)
        
        # Name Container
        name_container = soup.new_tag('div', attrs={"class": "tt-name-container"})
        
        # Move name and focus into container
        focus_span = header.find('span', class_='tt-focus')
        
        # We need to preserve the elements
        name_container.append(name_link.extract())
        if focus_span:
            name_container.append(focus_span.extract())
            
        # Re-assemble header
        header.append(logo_div)
        header.append(name_container)

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print("Logo injection complete.")

if __name__ == "__main__":
    inject_logos()
