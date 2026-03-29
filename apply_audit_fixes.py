import json
from bs4 import BeautifulSoup
import os

# Define the paths
INDEX_PATH = "/Users/roshanamarujala/Desktop/Antigravity/index.html"

# 8 Hallucinated Entities to Delete
HALLUCINATIONS_TO_DELETE = [
    "SNS Strategic News Service",
    "CENREC (Regional Conflict)",
    "Defence Research & Analysis",
    "StratNews Defence",
    "SDE (Sustainable Economics)",
    "CIPR (Independent Policy)",
    "Pranava Institute",
    "LPRS (Legal & Policy)"
]

# Corrections to apply with EXACT strings from HTML
CORRECTIONS = {
    "Usanas Foundation": {"Year": "2018"},
    "Delhi Policy Group (DPG)": {"Founder": "K. Shankar Bajpai"},
    "The Geostrata": {"Founder": "Harsh V. Pant / Incorrect Founder listed"},
    "Global Policy Insights (GPI)": {"Year": "2018"},
    "GCTC (New Delhi)": {"Founder": "Aditya Tikoo (Convener)", "Head": "Dr. Sandeep Marwah (Founder Exec)"},
    "Indian Strategic Studies Forum": {"Founder": "Unverifiable Claim", "Head": "Unverifiable Claim"},
    "StratNews Global": {"Year": "2020"},
    "Red Lantern Analytica": {"Founder": "Abhishek Ranjan"},
    "Ananta Centre": {"Head": "Indrani Bagchi (CEO)"},
    "CSDR (Indo-Pacific focus)": {"Year": "2021"},
    "South Asia Monitor": {"Year": "2002", "Founder": "Founding Group (Not C. Uday Bhaskar)"},
    "CAPSS (Aerospace Power)": {"Year": "2001", "Head": "Air Vice Marshal Anil Golani (Officiating/Current DG)"},
    "Delhi Defence Review": {"Year": "2017"},
    "Society for Policy Studies (SPS)": {"Founder": "Founding Group (Not C. Uday Bhaskar)"},
    "KIIPS (Indo-Pacific Studies)": {"Year": "2019"},
    "Centre for Policy Research (CPR)": {"Head": "Dr. Srinivas Chokkakula (President & CE)"},
    "NIUA (Urban Excellence)": {"Head": "Debashish Nayak / Outstanding (Tenure Completed)"},
    "SPRF India": {"Founder": "Neha Simlai (Founder / Director)", "Head": "Neha Simlai (Founder / Director)"},
    "IIIDEM (Electon Mgmt)": {"Head": "Vacant / Successor Unlisted (Tenure Completed)"},
    "Public Policy India": {"Year": "2020"},
    "IGPP (Governance & Policy)": {"Founder": "Aparajita Bharti (Co-Founder)", "Head": "Dr. Manish Tiwari (Director)"},
    "ISPP (Public Policy)": {"Year": "2018", "Head": "Shubhashis Gangopadhyay (Founding Dean)"},
    "DDC Delhi (Governance)": {"Head": "Vacant / Successor Unlisted (Tenure Completed)"},
    "The Dialogue (Tech Policy)": {"Founder": "Kazim Rizvi (Founder / Director)", "Head": "Kazim Rizvi (Founder / Director)"},
    "NIPFP (Public Finance)": {"Head": "Dr. Lekha Chakraborty / Outstanding (Tenure Completed)"},
    "EAC-PM (Economics)": {"Head": "S. Mahendra Dev (Chairman)"},
    "Esya Centre": {"Head": "Meghna Bal (Director)"},
    "CCG-NLU Delhi": {"Year": "2013"},
    "Ikigai Law (Policy)": {"Year": "2017"},
    "The Dialogue": {"Founder": "Kazim Rizvi (Founding Director)", "Head": "Kazim Rizvi (Founding Director)"},
    "MeitY (R&D Policy)": {"Head": "S. Krishnan (Secretary)"},
    "MNRE (Renewable R&D)": {"Head": "Prashant Kumar Singh (Secretary)"},
    "DPCC (Pollution)": {"Head": "Sandeep Mishra (Member Secretary)"},
    "FSI (Delhi Hub)": {"Head": "Santosh Tiwari (Director General)"},
    "NCPCR (Child Rights)": {"Head": "Tenure Ended (Currently Vacant / Acting)"},
    "NCW (Women Policy)": {"Head": "Vijaya Rahatkar (Chairperson)"},
    "Law Commission of India": {"Head": "Justice Dinesh Maheshwari (Chairperson)"},
    "NJ Academy (Delhi Hub)": {"Head": "Justice Aniruddha Bose (Director)"},
    "ISIL (Int'l Law & IR)": {"Head": "Prof. (Dr.) Manoj Kumar Sinha (President)"},
    "ISIL": {"Head": "Prof. (Dr.) Manoj Kumar Sinha (President)"},
    "Indian Law Institute": {"Head": "Prof. (Dr.) V. K. Ahuja (Director)"},
    "DOJ (Policy Division)": {"Head": "Niraj Verma (Secretary)"},
    "INTACH (National Trust)": {"Head": "Ashok Singh Thakur (Chairman)"},
    "Sanskriti Foundation": {"Head": "Dr. A.K. Shiva Kumar (President)"},
    "CCRT (Cultural Training)": {"Head": "Shri Rajeev Kumar (Director)"},
    "National Museum (Res)": {"Head": "Ashish Goyal (Director General)"}
}

def apply_fixes():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Delete Hallucinated Cards
    cards = soup.find_all('div', class_='tt-card')
    deleted_count = 0
    for card in cards:
        name_tag = card.find('a', class_='tt-name')
        if name_tag:
            name = name_tag.get_text().strip()
            if name in HALLUCINATIONS_TO_DELETE:
                card.decompose()
                deleted_count += 1
                print(f"Deleted hallucinated card: {name}")
    
    # 2. Apply Corrections
    cards = soup.find_all('div', class_='tt-card')
    corrected_count = 0
    for card in cards:
        name_tag = card.find('a', class_='tt-name')
        if name_tag:
            name = name_tag.get_text().strip()
            if name in CORRECTIONS:
                fix = CORRECTIONS[name]
                details = card.find('div', class_='tt-details')
                if details:
                    items = details.find_all('div', class_='tt-detail-item')
                    for item in items:
                        label_tag = item.find('span', class_='tt-detail-label')
                        if not label_tag: continue
                        label = label_tag.get_text().strip()
                        value_span = item.find('span', class_='tt-detail-value')
                        
                        if label == "Est. Year" and "Year" in fix:
                            value_span.string = fix["Year"]
                        elif label == "Founder" and "Founder" in fix:
                            value_span.string = fix["Founder"]
                        elif label == "Current Head" and "Head" in fix:
                            value_span.string = fix["Head"]
                
                corrected_count += 1
                print(f"Corrected card: {name}")

    print(f"Cleanup finished. Total corrected: {corrected_count}")
    
    # Save the updated HTML
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))

if __name__ == "__main__":
    apply_fixes()
