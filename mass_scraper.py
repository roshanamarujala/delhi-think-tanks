import json
import urllib.request
import urllib.error
import ssl
from bs4 import BeautifulSoup

# Bypass SSL verify for simple scraping
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch_text(url, timeout=5):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as response:
            soup = BeautifulSoup(response.read(), 'html.parser')
            # remove scripts and styles
            for script in soup(["script", "style"]): script.decompose()
            text = soup.get_text(separator=' ', strip=True)
            return text
    except Exception as e:
        return ""

def scan_text(text):
    text = text.lower()
    keywords = ['found', 'establish', 'head', 'director', 'president', 'secretary', 'ceo']
    words = text.split()
    results = []
    # just grab a 30-word window around the keywords
    for i, w in enumerate(words):
        if any(k in w for k in keywords):
            start = max(0, i-15)
            end = min(len(words), i+15)
            snippet = " ".join(words[start:end])
            results.append(snippet)
    # Deduplicate and limit
    return "\n-- ".join(list(set(results))[:5])

with open('audit_data.json', 'r') as f:
    audit_data = json.load(f)

# Batch 1: Geopolitics and Defence
batch_1_sections = ['Geopolitics & International Relations', 'Defence & Strategic Studies']

with open('batch1_evidence.txt', 'w', encoding='utf-8') as f:
    for sec in batch_1_sections:
        f.write(f"\n==== {sec} ====\n")
        for org in audit_data.get(sec, []):
            url = org['url']
            print(f"Scanning {org['name']} ({url})...")
            # try main and /about
            text1 = fetch_text(url)
            text2 = fetch_text(url.rstrip('/') + '/about') if url else ""
            
            snippets = scan_text(text1 + " " + text2)
            
            f.write(f"Org: {org['name']}\nListed Year: {org['year']} | Founder: {org['founder']} | Head: {org['head']}\n")
            f.write(f"Evidence:\n-- {snippets}\n")
            f.write("------------------------\n")
