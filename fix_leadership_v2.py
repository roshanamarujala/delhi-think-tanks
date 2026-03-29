import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    "SOLPO (Policy Research)": {
        "Founder": ("Policy Associates", "Sanjay Sen"),
        "Current Head": ("Managing Director", "Sanjay Sen (Director)")
    },
    "Public Policy India": {
        "Founder": ("PPI Team", "Yash Agarwal & Michelle Patrick"),
        "Current Head": ("Executive Director", "Yash Agarwal")
    },
    "NCAS India (Social Watch)": {
        "Founder": ("Social Activists Group", "Josantony Joseph"),
        "Current Head": ("Director", "N/A")
    },
    "SDE (Sustainable Economics)": {
        "Founder": ("Research Collective", "Sushil Kumar Sharma"),
        "Current Head": ("Director", "Sushil Kumar Sharma (CEO)")
    },
    "CPD (Policy Design)": {
        "Founder": ("Policy Team", "ATREE"),
        "Current Head": ("Director", "Dr. Abi Tamim Vanak (Director)")
    },
    "CFAR (Advocacy Research)": {
        "Founder": ("Activists Group", "Akhila Sivadas")
    },
    "CASP (Artistic Practice)": {
        "Founder": ("Artistic Collective", "Amrita Gupta & Parul"),
        "Current Head": ("Director", "Amrita Gupta (Director)")
    },
    "CENREC (Regional Conflict)": {
        "Founder": ("Strategic Thinkers Group", "N/A"),
        "Current Head": ("Board of Directors", "N/A")
    },
    "CIPR (Independent Policy)": {
        "Founder": ("Legal Experts Group", "N/A"),
        "Current Head": ("Director", "N/A")
    },
    "LPRS (Legal & Policy)": {
        "Founder": ("Legal Experts", "N/A"),
        "Current Head": ("Director", "N/A")
    }
}

# Find the block for each card, then replace within that block
for title, r_dict in replacements.items():
    # Find the starting index of the card
    card_idx = html.find(f">{title}</a>")
    if card_idx == -1:
        print(f"Could not find card for {title}")
        continue
    
    # Find the end of this card
    end_idx = html.find('class="tt-card"', card_idx)
    if end_idx == -1: end_idx = len(html)
    
    # Extract the card's HTML
    # We want from start of card. Backtrack to '<div class="tt-card'
    start_idx = html.rfind('<div class="tt-card', 0, card_idx)
    
    card_html = html[start_idx:end_idx]
    new_card_html = card_html
    
    for label, (old_val, new_val) in r_dict.items():
        # Look for the specific label block
        pattern = rf'(<div class="tt-detail-label">{label}</div>\s*<div class="tt-detail-value">){old_val}(</div>)'
        new_card_html = re.sub(pattern, rf'\g<1>{new_val}\g<2>', new_card_html)
        
    html = html[:start_idx] + new_card_html + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
