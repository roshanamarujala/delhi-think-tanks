from bs4 import BeautifulSoup
import urllib.parse

INDEX_PATH = "index.html"

def update_logos():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all('div', class_='tt-card')
    
    print(f"Updating {len(cards)} cards for Google Favicon API (128px)...")

    for card in cards:
        header = card.find('div', class_='tt-header')
        if not header: continue
        
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
            
        logo_div = header.find('div', class_='tt-logo')
        if not logo_div:
            # This shouldn't happen if inject_logos.py was run before, but for safety:
            logo_div = soup.new_tag('div', attrs={"class": "tt-logo"})
            header.insert(0, logo_div)
            
        # Update or create the img tag
        img = logo_div.find('img')
        if domain:
            new_src = f"https://www.google.com/s2/favicons?domain={domain}&sz=128"
            if not img:
                img = soup.new_tag('img', attrs={
                    "src": new_src,
                    "alt": f"{name} logo",
                    "onerror": "this.style.display='none'; this.nextElementSibling.style.display='flex';"
                })
                logo_div.insert(0, img)
            else:
                img['src'] = new_src
        
        # Ensure monogram exists
        monogram = logo_div.find('span', class_='monogram')
        if not monogram:
            monogram = soup.new_tag('span', attrs={"class": "monogram", "style": "display: none;" if domain else "display: flex;"})
            monogram.string = first_char
            logo_div.append(monogram)

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))
    
    print("Logo update complete.")

if __name__ == "__main__":
    update_logos()
