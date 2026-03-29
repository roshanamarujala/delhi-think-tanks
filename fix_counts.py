import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

domains = [
    ('section-geo', 'GEO'),
    ('section-def', 'DEF'),
    ('section-pol', 'POL'),
    ('section-eco', 'ECO'),
    ('section-tec', 'TEC'),
    ('section-env', 'ENV'),
    ('section-soc', 'SOC'),
    ('section-law', 'LAW'),
    ('section-art', 'ART'),
]

# Calculate true counts
domain_counts = {}
type_counts = {'govt': 0, 'semi': 0, 'private': 0}
total_cards = 0

for id_val, abbr in domains:
    section = soup.find(id=id_val)
    if section:
        cards = section.find_all(class_='tt-card')
        count = len(cards)
        domain_counts[id_val] = count
        total_cards += count
        
        for card in cards:
            type_div = card.find(class_='tt-type')
            if type_div:
                classes = type_div.get('class', [])
                if 'govt' in classes: type_counts['govt'] += 1
                elif 'semi' in classes: type_counts['semi'] += 1
                elif 'private' in classes: type_counts['private'] += 1

print(f"Total: {total_cards}")
print(f"Types: {type_counts}")
print(f"Domains: {domain_counts}")

# Regex replacements for badges
for id_val, abbr in domains:
    true_count = domain_counts[id_val]
    # Find the badge inside the section block regex
    # Pattern looks for <div id="section-xxx"> ... <div class="domain-badge">YY Institutions</div>
    
    # We will just find the badge with the exact previous wrong count and replace it safely
    # Wait, simple way: we can just match the domain-title block
    pass

# We will just use regex to replace the exact metrics block
def replace_metric(html_str, label, new_count):
    pattern = r'(<span class="count"[^>]*>)\d+(</span>\s*<span class="label">{}</span>)'.format(label)
    return re.sub(pattern, rf'\g<1>{new_count}\g<2>', html_str)

html = replace_metric(html, 'Total Institutions', total_cards)
html = replace_metric(html, 'Govt Bodies', type_counts['govt'])
html = replace_metric(html, 'Semi-Govt / Quasi', type_counts['semi'])
html = replace_metric(html, 'Private / Independent', type_counts['private'])

# Replace the text "191 verified institutions" in the header paragraph
html = re.sub(r'<strong>\d+ verified institutions</strong>', f'<strong>{total_cards} verified institutions</strong>', html)
# Replace "THE 190+ INSTITUTIONAL LIST" in subtitle
html = re.sub(r'THE \d+\+ INSTITUTIONAL LIST', f'THE {total_cards} INSTITUTIONAL LIST', html)
html = re.sub(r'Search \d+\+ institutions', f'Search {total_cards} institutions', html)

# Replace domain badges
# Let's find all domain badges and replace their content based on the section id they are in.
# It's easier to find them by iterating the string.
import re
new_html = html
for section_id, count in domain_counts.items():
    # regex to match from id="section-xxx" to the next domain-badge
    pattern = rf'(id="{section_id}"[\s\S]*?<div class="domain-badge">)\d+ Institutions(</div>)'
    new_html = re.sub(pattern, rf'\g<1>{count} Institutions\g<2>', new_html, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("HTML updated with correct counts.")
