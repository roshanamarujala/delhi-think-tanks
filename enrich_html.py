import re
import bs4
import json

data = {
    "ORCA (Research on China & Asia)": {"type": "private", "label": "Private / Independent", "est": "2021", "founder": "Eerishika Pankaj", "head": "Eerishika Pankaj (Director)"},
    "Usanas Foundation": {"type": "private", "label": "Private / Independent", "est": "2020", "founder": "Dr. Abhinav Pandya", "head": "Dr. Abhinav Pandya (Founder & CEO)"},
    "RIS (MEA Think Tank)": {"type": "semi", "label": "Semi-Government", "est": "1983", "founder": "Ministry of External Affairs", "head": "Prof. Sachin Chaturvedi (DG)"},
    "Observer Research Foundation (ORF)": {"type": "private", "label": "Private / Independent", "est": "1990", "founder": "R. K. Mishra", "head": "Samir Saran (President)"},
    "Indian Council of World Affairs (ICWA)": {"type": "semi", "label": "Semi-Government", "est": "1943", "founder": "Sir Tej Bahadur Sapru", "head": "Amb. Vijay Thakur Singh (DG)"},
    "Vivekananda Int'l Foundation (VIF)": {"type": "private", "label": "Private / Independent", "est": "2009", "founder": "Ajit Doval", "head": "Dr. Arvind Gupta (Director)"},
    "Delhi Policy Group (DPG)": {"type": "private", "label": "Private / Independent", "est": "1994", "founder": "K. S. Bajpai", "head": "Amb. Hemant Krishan Singh (DG)"},
    "The Geostrata": {"type": "private", "label": "Private / Independent", "est": "2021", "founder": "Shantanu Sharma", "head": "Shantanu Sharma (Founder & CEO)"},
    "Carnegie India": {"type": "private", "label": "Private / Independent", "est": "2016", "founder": "Carnegie Endowment", "head": "Rudra Chaudhuri (Director)"},
    "Global Policy Insights (GPI)": {"type": "private", "label": "Private / Independent", "est": "2018", "founder": "Arpit Chaturvedi", "head": "Arpit Chaturvedi (CEO)"},
    "CPRG India": {"type": "private", "label": "Private / Independent", "est": "2017", "founder": "Ramanand Pandey", "head": "Ramanand Pandey (Director)"},
    "South Asia Analysis Group (SAAG)": {"type": "private", "label": "Private / Independent", "est": "1998", "founder": "S. Chandrasekharan", "head": "S. Chandrasekharan (Director)"},
    "Foreign Policy Research Centre": {"type": "private", "label": "Private / Independent", "est": "2011", "founder": "Dr. Mahendra Gaur", "head": "Dr. Mahendra Gaur (Director)"},
    "Indian Strategic Studies Forum": {"type": "private", "label": "Private / Independent", "est": "2022", "founder": "Abhishek Jha", "head": "Abhishek Jha (Director)"},
    "GCTC (New Delhi)": {"type": "private", "label": "Private / Independent", "est": "2019", "founder": "Dr. R.K. Mishra", "head": "Acharya Shailesh (DG)"},
    "Takshashila Institution": {"type": "private", "label": "Private / Independent", "est": "2010", "founder": "Nitin Pai", "head": "Nitin Pai (Director)"},
    "ISIL (Int'l Law & IR)": {"type": "private", "label": "Private / Independent", "est": "1959", "founder": "V. K. Krishna Menon", "head": "Pravin Parekh (President)"},
    "Centre for Escalation of Peace": {"type": "private", "label": "Private / Independent", "est": "2011", "founder": "S.K. Misra / Munjal Family", "head": "Arun Kapur (Director)"},
    "IPCS (Peace & Conflict)": {"type": "private", "label": "Private / Independent", "est": "1996", "founder": "Maj. Gen. Dipankar Banerjee", "head": "Maj. Gen. Dipankar Banerjee (Founder)"},
    "Gateway House Delhi": {"type": "private", "label": "Private / Independent", "est": "2009", "founder": "Manjeet Kripalani", "head": "Manjeet Kripalani (Exec. Director)"},
    "SNS Strategic News Service": {"type": "private", "label": "Private / Independent", "est": "2018", "founder": "Nitin Gokhale", "head": "Nitin Gokhale (Editor-in-Chief)"},
    "StratNews Global": {"type": "private", "label": "Private / Independent", "est": "2018", "founder": "Nitin Gokhale", "head": "Nitin Gokhale (Editor-in-Chief)"},
    "Red Lantern Analytica": {"type": "private", "label": "Private / Independent", "est": "2021", "founder": "Abhishek Darbey", "head": "Abhishek Darbey (Director)"},
    "India Foundation": {"type": "private", "label": "Private / Independent", "est": "2009", "founder": "Ram Madhav", "head": "Shaurya Doval (Director)"},
    "Ananta Centre": {"type": "private", "label": "Private / Independent", "est": "2013", "founder": "Jamshyd Godrej", "head": "Kiran Pasricha (CEO)"},
    "CSDR (Indo-Pacific focus)": {"type": "private", "label": "Private / Independent", "est": "2018", "founder": "Happymon Jacob", "head": "Happymon Jacob (Founder)"},
    "Policy Perspectives Foundation (PPF)": {"type": "private", "label": "Private / Independent", "est": "2005", "founder": "R. K. Ohri", "head": "Syed Ata Hasnain (President)"},
    "C-NES (North East Studies)": {"type": "private", "label": "Private / Independent", "est": "2000", "founder": "Sanjoy Hazarika", "head": "Sanjoy Hazarika (Managing Trustee)"},
    "South Asia Monitor": {"type": "private", "label": "Private / Independent", "est": "2013", "founder": "C. Uday Bhaskar", "head": "C. Uday Bhaskar (Director)"},
    "SPMRF (Strategic)": {"type": "private", "label": "Private / Independent", "est": "2002", "founder": "BJP / RSS Trust", "head": "Dr. Anirban Ganguly (Director)"},
    "PP&R Division, MEA": {"type": "govt", "label": "Government", "est": "1966", "founder": "Ministry of External Affairs", "head": "Joint Secretary (PP&R)"},
    "NSAB (Security Advisory)": {"type": "govt", "label": "Government", "est": "1998", "founder": "Government of India", "head": "NSA (Convener)"},
    "MP-IDSA (National Defence)": {"type": "semi", "label": "Semi-Government", "est": "1965", "founder": "Ministry of Defence", "head": "Sujan R. Chinoy (Director General)"},
    "BharatShakti.in": {"type": "private", "label": "Private / Independent", "est": "2015", "founder": "Nitin Gokhale", "head": "Nitin Gokhale (Founder)"},
    "CAPS (Air Power Studies)": {"type": "semi", "label": "Semi-Government", "est": "2002", "founder": "Indian Air Force", "head": "Air Marshal Anil Chopra (DG)"},
    "CLAWS (Land Warfare)": {"type": "semi", "label": "Semi-Government", "est": "2004", "founder": "Indian Army", "head": "Lt Gen Dr. S.S. Mahal (DG)"},
    "NMF (Maritime Foundation)": {"type": "semi", "label": "Semi-Government", "est": "2005", "founder": "Indian Navy", "head": "Vice Admiral Pradeep Chauhan (DG)"},
    "CENJOWS (Tri-Services)": {"type": "semi", "label": "Semi-Government", "est": "2007", "founder": "Ministry of Defence", "head": "Lt Gen Sunil Srivastava (Director)"},
    "USI (United Service Institution)": {"type": "semi", "label": "Semi-Government", "est": "1870", "founder": "Col Sir Charles MacGregor", "head": "Maj Gen BK Sharma (Director)"},
    "Force Analysis": {"type": "private", "label": "Private / Independent", "est": "2003", "founder": "Pravin Sawhney", "head": "Pravin Sawhney (Editor)"},
    "Delhi Defence Review": {"type": "private", "label": "Private / Independent", "est": "2015", "founder": "Saurav Jha", "head": "Saurav Jha (Chief Editor)"},
    "SATP (Conflict Mgmt)": {"type": "private", "label": "Private / Independent", "est": "2000", "founder": "K. P. S. Gill", "head": "Ajai Sahni (Executive Director)"},
    "ICS (China Defence Focus)": {"type": "semi", "label": "Semi-Government", "est": "1990", "founder": "Prof. Manoranjan Mohanty", "head": "Prof. Alka Acharya (Honorary Director)"},
    "IPCS Nuclear Focus": {"type": "private", "label": "Private / Independent", "est": "1996", "founder": "Dipankar Banerjee", "head": "Manpreet Sethi (Distinguished Fellow)"},
    "Indian Military Review (IMR)": {"type": "private", "label": "Private / Independent", "est": "2010", "founder": "Maj Gen Ravi Arora", "head": "Maj Gen Ravi Arora (Chief Editor)"},
    "CENREC (Regional Conflict)": {"type": "private", "label": "Private / Independent", "est": "2020", "founder": "Strategic Thinkers Group", "head": "Board of Directors"},
    "Defence Research & Analysis": {"type": "private", "label": "Private / Independent", "est": "2019", "founder": "Independent Analysts", "head": "Editorial Board"},
    "USI CAFHR (Military History)": {"type": "semi", "label": "Semi-Government", "est": "2000", "founder": "USI Trust", "head": "Sqdn Ldr Rana TS Chhina (Director)"},
    "NMF Blue Economy": {"type": "semi", "label": "Semi-Government", "est": "2005", "founder": "Indian Navy", "head": "Cmde Abhay Kumar Singh (Head)"},
    "Aerospace Policy Hub": {"type": "semi", "label": "Semi-Government", "est": "2002", "founder": "CAPS", "head": "Research Board"},
    "StratNews Defence": {"type": "private", "label": "Private / Independent", "est": "2018", "founder": "Nitin Gokhale", "head": "Nitin Gokhale (Editor-in-Chief)"},
    "Society for Policy Studies (SPS)": {"type": "private", "label": "Private / Independent", "est": "2010", "founder": "C. Uday Bhaskar", "head": "C. Uday Bhaskar (Director)"},
    "KIIPS (Indo-Pacific Studies)": {"type": "private", "label": "Private / Independent", "est": "2015", "founder": "Chintamani Mahapatra", "head": "Prof. Chintamani Mahapatra (Chairman)"},
    "BPR&D (Police Research)": {"type": "govt", "label": "Government", "est": "1970", "founder": "Ministry of Home Affairs", "head": "Balaji Srivastava (Director General)"},
    "NSCS (Security Council)": {"type": "govt", "label": "Government", "est": "1998", "founder": "Government of India", "head": "Ajit Doval (NSA)"},
    "Centre for Policy Research (CPR)": {"type": "private", "label": "Private / Independent", "est": "1973", "founder": "V. A. Pai Panandiker", "head": "Yamini Aiyar (President & CE)"},
    "NIUA (Urban Excellence)": {"type": "semi", "label": "Semi-Government", "est": "1976", "founder": "Ministry of Housing", "head": "Hitesh Vaidya (Director)"},
    "PRS Legislative Research": {"type": "private", "label": "Private / Independent", "est": "2005", "founder": "C. V. Madhukar", "head": "M. R. Madhavan (President)"},
    "ADR (Democratic Reform)": {"type": "private", "label": "Private / Independent", "est": "1999", "founder": "Trilochan Sastry", "head": "Maj. Gen. Anil Verma (Head)"},
    "Centre for Civil Society": {"type": "private", "label": "Private / Independent", "est": "1997", "founder": "Parth J. Shah", "head": "Parth J. Shah (Founder & President)"},
    "SPRF India": {"type": "private", "label": "Private / Independent", "est": "2018", "founder": "Rishabh Malhotra", "head": "Rishabh Malhotra (Director)"},
    "IMPRI (Policy Research)": {"type": "private", "label": "Private / Independent", "est": "2018", "founder": "Simi Mehta", "head": "Dr. Simi Mehta (CEO)"},
    "PPRC (Public Policy Centre)": {"type": "private", "label": "Private / Independent", "est": "2011", "founder": "Vinay Sahasrabuddhe", "head": "Dr. Vinay Sahasrabuddhe (Director)"},
    "CBGA India (Budgets)": {"type": "private", "label": "Private / Independent", "est": "2002", "founder": "NCAS initiative", "head": "Subrat Das (Executive Director)"},
    "IIIDEM (Electon Mgmt)": {"type": "govt", "label": "Government", "est": "2011", "founder": "Election Commission of India", "head": "Dharmendra Sharma (Director General)"},
    "IIDS (Social Exclusion)": {"type": "private", "label": "Private / Independent", "est": "2003", "founder": "S.K. Thorat", "head": "Prof. S.K. Thorat (Chairman)"},
    "Global Governance Initiative (GGI)": {"type": "private", "label": "Private / Independent", "est": "2018", "founder": "Shatakshi Sharma & Naman Shrivastava", "head": "Shatakshi Sharma (Co-CEO)"},
    "Janaagraha (Delhi City)": {"type": "private", "label": "Private / Independent", "est": "2001", "founder": "Ramesh Ramanathan", "head": "Srikanth Viswanathan (CEO)"},
    "SOLPO (Policy Research)": {"type": "private", "label": "Private / Independent", "est": "2020", "founder": "Policy Associates", "head": "Managing Director"},
    "Public Policy India": {"type": "private", "label": "Private / Independent", "est": "2019", "founder": "PPI Team", "head": "Executive Director"},
    "IGPP (Governance & Policy)": {"type": "private", "label": "Private / Independent", "est": "2012", "founder": "Prof. Ashwani Kumar", "head": "Sanjeev Kumar (Director)"},
    "Accountability Initiative (CPR)": {"type": "private", "label": "Private / Independent", "est": "2008", "founder": "Yamini Aiyar", "head": "Avani Kapur (Director)"},
    "NITI Aayog (Apex House)": {"type": "govt", "label": "Government", "est": "2015", "founder": "Government of India", "head": "B.V.R. Subrahmanyam (CEO)"},
    "Civis India": {"type": "private", "label": "Private / Independent", "est": "2018", "founder": "Antaraa Vasudev", "head": "Antaraa Vasudev (Founder)"},
    "CIPR (Independent Policy)": {"type": "private", "label": "Private / Independent", "est": "2015", "founder": "Legal Experts Group", "head": "Director"},
    "ISPP (Public Policy)": {"type": "private", "label": "Private / Independent", "est": "2019", "founder": "Parth J. Shah & Luis Miranda", "head": "Dr. Sanjaya Baru (Founder Dean)"},
    "National Foundation for India (NFI)": {"type": "private", "label": "Private / Independent", "est": "1992", "founder": "C. Subramaniam", "head": "Biraj Patnaik (Executive Director)"},
    "IIPA (Public Administration)": {"type": "semi", "label": "Semi-Government", "est": "1954", "founder": "Jawaharlal Nehru", "head": "S.N. Tripathi (Director General)"},
    "Samagra Governance": {"type": "private", "label": "Private / Independent", "est": "2012", "founder": "Gaurav Goel", "head": "Gaurav Goel (Founder & CEO)"},
    "Swaniti Initiative": {"type": "private", "label": "Private / Independent", "est": "2012", "founder": "Rwitwika Bhattacharya", "head": "Rwitwika Bhattacharya (CEO)"},
    "The Quantum Hub (TQH)": {"type": "private", "label": "Private / Independent", "est": "2017", "founder": "Rohit Kumar", "head": "Rohit Kumar (Founding Partner)"},
    "Koan Advisory Group": {"type": "private", "label": "Private / Independent", "est": "2012", "founder": "Vivan Sharan", "head": "Vivan Sharan (Partner)"},
    "DDC Delhi (Governance)": {"type": "govt", "label": "Government", "est": "2015", "founder": "Govt of NCT of Delhi", "head": "Jasmine Shah (Vice Chairperson)"},
    "The Dialogue (Tech Policy)": {"type": "private", "label": "Private / Independent", "est": "2017", "founder": "Kazimuddin Ahmed", "head": "Kazimuddin Ahmed (Director)"},
    "NCAS India (Social Watch)": {"type": "private", "label": "Private / Independent", "est": "1992", "founder": "Social Activists Group", "head": "Director"},
    "NILERD (Labour Policy)": {"type": "semi", "label": "Semi-Government", "est": "1962", "founder": "Planning Commission", "head": "Dr. K. J. Joseph (Director)"},
    "NCERT (Edu Research)": {"type": "semi", "label": "Semi-Government", "est": "1961", "founder": "Min of Education", "head": "Prof. Dinesh Prasad Saklani (Director)"},
    "NIEPA (Edu Planning)": {"type": "semi", "label": "Semi-Government", "est": "1962", "founder": "Min of Education", "head": "Prof. Shashikala Wanjari (VC)"},
    "NIDM (Disaster Mgmt)": {"type": "semi", "label": "Semi-Government", "est": "1995", "founder": "Ministry of Home Affairs", "head": "Rajendra Singh (Executive Director)"},
    "Quality Council of India": {"type": "semi", "label": "Semi-Government", "est": "1997", "founder": "DPIIT", "head": "JaxsAY Shah (Chairperson)"},
    "NIHFW (Health/Family)": {"type": "semi", "label": "Semi-Government", "est": "1977", "founder": "Min of Health", "head": "Dr. Nanthini Subbiah (Director)"},
    "NCAER (National Economic)": {"type": "semi", "label": "Semi-Government", "est": "1956", "founder": "Pt. Jawaharlal Nehru", "head": "Dr. Poonam Gupta (DG)"},
    "ICRIER (Global Trade)": {"type": "private", "label": "Private / Independent", "est": "1981", "founder": "K. B. Lall", "head": "Deepak Mishra (Director)"},
    "NIPFP (Public Finance)": {"type": "semi", "label": "Semi-Government", "est": "1976", "founder": "Ministry of Finance", "head": "Pinaki Chakraborty (Director)"},
    "CSEP (Brookings India)": {"type": "private", "label": "Private / Independent", "est": "2020", "founder": "Vikram Singh Mehta", "head": "Rakesh Mohan (President)"},
    "IEG (Economic Growth)": {"type": "semi", "label": "Semi-Government", "est": "1952", "founder": "V. K. R. V. Rao", "head": "Prof. Chetan Ghate (Director)"},
    "Pahle India Foundation": {"type": "private", "label": "Private / Independent", "est": "2013", "founder": "Dr. Rajiv Kumar", "head": "Dr. Rajiv Kumar (Chairman)"},
    "CUTS International": {"type": "private", "label": "Private / Independent", "est": "1983", "founder": "Pradeep S. Mehta", "head": "Pradeep S. Mehta (Secretary General)"},
    "Inclusion Economics": {"type": "private", "label": "Private / Independent", "est": "2021", "founder": "Rohini Pande", "head": "Rohini Pande (Faculty Director)"},
    "ISID (Industrial Dev)": {"type": "semi", "label": "Semi-Government", "est": "1986", "founder": "Prof. S.K. Goyal", "head": "Prof. Nagesh Kumar (Director)"},
    "IIFT (Trade Policy)": {"type": "semi", "label": "Semi-Government", "est": "1963", "founder": "Ministry of Commerce", "head": "Prof. Rakesh Mohan Joshi (VC)"},
    "IGC India (Growth Centre)": {"type": "private", "label": "Private / Independent", "est": "2008", "founder": "LSE / Oxford", "head": "Pronab Sen (Country Director)"},
    "DBE (Business Econ)": {"type": "semi", "label": "Semi-Government", "est": "1973", "founder": "Delhi University / V.K.R.V. Rao", "head": "Prof. V.K. Kaul (Head)"},
    "SDE (Sustainable Economics)": {"type": "private", "label": "Private / Independent", "est": "2005", "founder": "Research Collective", "head": "Director"},
    "Agri Economics Research": {"type": "semi", "label": "Semi-Government", "est": "1954", "founder": "Ministry of Agriculture", "head": "Dr. Usha Tuteja (Director)"},
    "ICRIER Digital focus": {"type": "private", "label": "Private / Independent", "est": "1981", "founder": "ICRIER", "head": "Rajat Kathuria (Lead)"},
    "CPD (Policy Design)": {"type": "private", "label": "Private / Independent", "est": "2000", "founder": "Policy Team", "head": "Director"},
    "EAC-PM (Economics)": {"type": "govt", "label": "Government", "est": "2017", "founder": "Government of India", "head": "Dr. Bibek Debroy (Chairman)"},
    "CCI (Competition)": {"type": "govt", "label": "Government", "est": "2003", "founder": "Government of India", "head": "Ravneet Kaur (Chairperson)"},
    "ICAR (Agri Research)": {"type": "semi", "label": "Semi-Government", "est": "1929", "founder": "Government of India", "head": "Dr. Himanshu Pathak (DG)"},
    "NSO (Statistics)": {"type": "govt", "label": "Government", "est": "2019", "founder": "Government of India", "head": "Secretary, MoSPI"},
    "Esya Centre": {"type": "private", "label": "Private / Independent", "est": "2018", "founder": "Vivan Sharan", "head": "Vivan Sharan (Director)"},
    "Aapti Institute": {"type": "private", "label": "Private / Independent", "est": "2018", "founder": "Sarayu Natarajan", "head": "Sarayu Natarajan (Founder)"},
    "IFF (Internet Freedom)": {"type": "private", "label": "Private / Independent", "est": "2016", "founder": "Apar Gupta", "head": "Prateek Waghre (Executive Director)"},
    "MediaNama Policy": {"type": "private", "label": "Private / Independent", "est": "2008", "founder": "Nikhil Pahwa", "head": "Nikhil Pahwa (Founder & Editor)"},
    "CIS (Digital Policy)": {"type": "private", "label": "Private / Independent", "est": "2008", "founder": "Sunil Abraham", "head": "Pranesh Prakash (Director)"},
    "Pranava Institute": {"type": "private", "label": "Private / Independent", "est": "2020", "founder": "Sai Nivedita", "head": "Sai Nivedita (Founder)"},
    "CCG-NLU Delhi": {"type": "semi", "label": "Semi-Government", "est": "2016", "founder": "NLU Delhi / Chinmayi Arun", "head": "Dr. Daniel Mathew (Director)"},
    "India Smart Grid Forum": {"type": "semi", "label": "Semi-Government", "est": "2010", "founder": "Ministry of Power", "head": "Reji Kumar Pillai (President)"},
    "Ikigai Law (Policy)": {"type": "private", "label": "Private / Independent", "est": "2012", "founder": "Anirudh Rastogi", "head": "Anirudh Rastogi (Founder)"},
    "IndiaAI Portal": {"type": "govt", "label": "Government", "est": "2020", "founder": "MeitY / NASSCOM", "head": "Abhishek Singh (CEO)"},
    "DSCI (Data Security)": {"type": "private", "label": "Private / Independent", "est": "2008", "founder": "NASSCOM", "head": "Vinayak Godse (CEO)"},
    "STPI (Tech Policy)": {"type": "semi", "label": "Semi-Government", "est": "1991", "founder": "Ministry of Electronics & IT", "head": "Arvind Kumar (DG)"},
    "TIFAC (Tech Vision)": {"type": "semi", "label": "Semi-Government", "est": "1988", "founder": "Department of Science & Tech", "head": "Prof. Pradeep Srivastava (ED)"},
    "MeitY (R&D Policy)": {"type": "govt", "label": "Government", "est": "2016", "founder": "Government of India", "head": "Alkesh Kumar Sharma (Secretary)"},
    "CSE India (Science & Env)": {"type": "private", "label": "Private / Independent", "est": "1980", "founder": "Anil Agarwal", "head": "Sunita Narain (Director General)"},
    "TERI (Resource Institute)": {"type": "private", "label": "Private / Independent", "est": "1974", "founder": "Darbari Seth", "head": "Dr. Vibha Dhawan (DG)"},
    "CEEW India": {"type": "private", "label": "Private / Independent", "est": "2010", "founder": "Dr. Arunabha Ghosh", "head": "Dr. Arunabha Ghosh (CEO)"},
    "LIFE (Environmental Law)": {"type": "private", "label": "Private / Independent", "est": "2005", "founder": "Ritwick Dutta", "head": "Ritwick Dutta (Founder)"},
    "iFOREST": {"type": "private", "label": "Private / Independent", "est": "2019", "founder": "Chandra Bhushan", "head": "Chandra Bhushan (President & CEO)"},
    "Shakti Foundation": {"type": "private", "label": "Private / Independent", "est": "2009", "founder": "Philanthropic Collaborative", "head": "Anshu Bharadwaj (CEO)"},
    "WRI India (New Delhi)": {"type": "private", "label": "Private / Independent", "est": "2011", "founder": "World Resources Institute", "head": "Madhav Pai (CEO)"},
    "Toxics Link": {"type": "private", "label": "Private / Independent", "est": "1996", "founder": "Ravi Agarwal", "head": "Ravi Agarwal (Director)"},
    "Chintan Environmental": {"type": "private", "label": "Private / Independent", "est": "1999", "founder": "Bharati Chaturvedi", "head": "Bharati Chaturvedi (Director)"},
    "Vasudha Foundation": {"type": "private", "label": "Private / Independent", "est": "2010", "founder": "Srinivas Krishnaswamy", "head": "Srinivas Krishnaswamy (CEO)"},
    "DA (Dev Alternatives)": {"type": "private", "label": "Private / Independent", "est": "1983", "founder": "Ashok Khosla", "head": "Ashok Khosla (Chairman)"},
    "CPCB (Pollution Board)": {"type": "govt", "label": "Government", "est": "1974", "founder": "Government of India", "head": "Tanmay Kumar (Chairman)"},
    "MNRE (Renewable R&D)": {"type": "govt", "label": "Government", "est": "1992", "founder": "Government of India", "head": "Bhupinder Singh Bhalla (Secretary)"},
    "DPCC (Pollution)": {"type": "govt", "label": "Government", "est": "1991", "founder": "Govt of NCT of Delhi", "head": "Dr. K.S. Jayachandran (Member Sec.)"},
    "FSI (Delhi Hub)": {"type": "govt", "label": "Government", "est": "1981", "founder": "MoEFCC", "head": "Anoop Singh (DG)"},
    "PHFI India (Public Health)": {"type": "private", "label": "Private / Independent", "est": "2006", "founder": "Dr. K. Srinath Reddy", "head": "Prof. Sanjay Zodpey (President)"},
    "One Health Trust": {"type": "private", "label": "Private / Independent", "est": "2010", "founder": "Ramanan Laxminarayan", "head": "Ramanan Laxminarayan (President)"},
    "CSR (Gender Rights)": {"type": "private", "label": "Private / Independent", "est": "1983", "founder": "Dr. Ranjana Kumari", "head": "Dr. Ranjana Kumari (Director)"},
    "CCDC India": {"type": "private", "label": "Private / Independent", "est": "2000", "founder": "Health Experts", "head": "Dr. D Prabhakaran (Executive Director)"},
    "CSDS Delhi": {"type": "private", "label": "Private / Independent", "est": "1963", "founder": "Rajni Kothari", "head": "Awadhendra Sharan (Director)"},
    "Population Council Delhi": {"type": "private", "label": "Private / Independent", "est": "1994", "founder": "John D. Rockefeller III", "head": "Niranjan Saggurti (Director)"},
    "Mobile Creches Policy": {"type": "private", "label": "Private / Independent", "est": "1969", "founder": "Meera Mahadevan", "head": "Sumitra Mishra (Executive Director)"},
    "CRY Policy Research": {"type": "private", "label": "Private / Independent", "est": "1979", "founder": "Rippan Kapur", "head": "Puja Marwaha (CEO)"},
    "Helpage Policy Hub": {"type": "private", "label": "Private / Independent", "est": "1978", "founder": "Jackson Cole", "head": "Rohit Prasad (CEO)"},
    "CFAR (Advocacy Research)": {"type": "private", "label": "Private / Independent", "est": "1998", "founder": "Activists Group", "head": "Akhila Sivadas (Executive Director)"},
    "Pratham Education Foundation": {"type": "private", "label": "Private / Independent", "est": "1995", "founder": "Madhav Chavan", "head": "Rukmini Banerji (CEO)"},
    "J-PAL South Asia": {"type": "private", "label": "Private / Independent", "est": "2007", "founder": "Abhijit Banerjee / Esther Duflo", "head": "Shobhini Mukerji (Executive Director)"},
    "Dasra (Strategic Philanthropy)": {"type": "private", "label": "Private / Independent", "est": "1999", "founder": "Neera Nundy / Deval Sanghavi", "head": "Neera Nundy (Co-Founder)"},
    "Central Square Foundation": {"type": "private", "label": "Private / Independent", "est": "2012", "founder": "Ashish Dhawan", "head": "Ashish Dhawan (Founder & Chairman)"},
    "Indus Action": {"type": "private", "label": "Private / Independent", "est": "2013", "founder": "Tarun Cherukuri", "head": "Tarun Cherukuri (CEO)"},
    "ICMR (Medical Research)": {"type": "govt", "label": "Government", "est": "1911", "founder": "Government of India", "head": "Dr. Rajiv Bahl (DG)"},
    "AYUSH (Research)": {"type": "govt", "label": "Government", "est": "2014", "founder": "Government of India", "head": "Vaidya Rajesh Kotecha (Secretary)"},
    "NCPCR (Child Rights)": {"type": "govt", "label": "Government", "est": "2007", "founder": "Government of India", "head": "Priyank Kanoongo (Chairperson)"},
    "NCW (Women Policy)": {"type": "govt", "label": "Government", "est": "1992", "founder": "Government of India", "head": "Rekha Sharma (Chairperson)"},
    "Vidhi Centre for Legal Policy": {"type": "private", "label": "Private / Independent", "est": "2013", "founder": "Arghya Sengupta", "head": "Arghya Sengupta (Research Director)"},
    "Daksh (Delhi Central)": {"type": "private", "label": "Private / Independent", "est": "2008", "founder": "Harish Narasappa", "head": "Harish Narasappa (Co-Founder)"},
    "ISIL": {"type": "private", "label": "Private / Independent", "est": "1959", "founder": "V. K. Krishna Menon", "head": "Pravin Parekh (President)"},
    "LPRS (Legal & Policy)": {"type": "private", "label": "Private / Independent", "est": "2015", "founder": "Legal Experts", "head": "Director"},
    "Indian Law Institute": {"type": "semi", "label": "Semi-Government", "est": "1956", "founder": "Govt of India / SC", "head": "Prof. Manoj Kumar Sinha (Director)"},
    "NLU Delhi Policy Centers": {"type": "semi", "label": "Semi-Government", "est": "2008", "founder": "Govt of NCT Delhi", "head": "Prof. G.S. Bajpai (Vice Chancellor)"},
    "JGU Public Law Hub": {"type": "private", "label": "Private / Independent", "est": "2009", "founder": "Naveen Jindal", "head": "Prof. C. Raj Kumar (VC)"},
    "Law Commission of India": {"type": "govt", "label": "Government", "est": "1955", "founder": "Government of India", "head": "Justice Ritu Raj Awasthi (Chairperson)"},
    "BCI (Legal R&D)": {"type": "semi", "label": "Semi-Government", "est": "1961", "founder": "Advocates Act", "head": "Manan Kumar Mishra (Chairman)"},
    "NJ Academy (Delhi Hub)": {"type": "semi", "label": "Semi-Government", "est": "1993", "founder": "Supreme Court of India", "head": "Justice A.P. Sahi (Director)"},
    "DOJ (Policy Division)": {"type": "govt", "label": "Government", "est": "1971", "founder": "Ministry of Law", "head": "Secretary, Department of Justice"},
    "INTACH (National Trust)": {"type": "semi", "label": "Semi-Government", "est": "1984", "founder": "Pupul Jayakar", "head": "Maj. Gen. L.K. Gupta (Chairman)"},
    "IGNCA (Arts Centre)": {"type": "semi", "label": "Semi-Government", "est": "1987", "founder": "Rajiv Gandhi", "head": "Dr. Sachidanand Joshi (Member Secretary)"},
    "CCRT (Cultural Training)": {"type": "semi", "label": "Semi-Government", "est": "1979", "founder": "Dr. Kapila Vatsyayan", "head": "Rishi Vashist (Director)"},
    "Sanskriti Foundation": {"type": "private", "label": "Private / Independent", "est": "1978", "founder": "O. P. Jain", "head": "O. P. Jain (Founder & President)"},
    "IIC (International Research)": {"type": "private", "label": "Private / Independent", "est": "1962", "founder": "C. D. Deshmukh", "head": "K.N. Shrivastava (Director)"},
    "Sahapedia": {"type": "private", "label": "Private / Independent", "est": "2011", "founder": "Dr. Sudha Gopalakrishnan", "head": "Dr. Sudha Gopalakrishnan (Executive Director)"},
    "CASP (Artistic Practice)": {"type": "private", "label": "Private / Independent", "est": "2013", "founder": "Artistic Collective", "head": "Director"},
    "Heritage Policy Division": {"type": "govt", "label": "Government", "est": "1985", "founder": "Ministry of Culture", "head": "Secretary (Culture)"},
    "PMML (Research Library)": {"type": "semi", "label": "Semi-Government", "est": "1964", "founder": "Government of India", "head": "Nripendra Misra (Chairman)"},
    "Sahitya Akademi Policy": {"type": "semi", "label": "Semi-Government", "est": "1954", "founder": "Government of India", "head": "Madhav Kaushik (President)"},
    "National Museum (Res)": {"type": "govt", "label": "Government", "est": "1949", "founder": "Ministry of Culture", "head": "B.R. Mani (Director General)"},
    "National Archives (Policy)": {"type": "govt", "label": "Government", "est": "1891", "founder": "Government of India", "head": "Chandan Sinha (Director General)"}
}

css = """
        .tt-type {
            display: inline-block;
            padding: 4px 10px;
            background: #e2e8f0;
            color: #475569;
            font-size: 0.65rem;
            font-weight: 800;
            text-transform: uppercase;
            border-radius: 6px;
            margin-bottom: 15px;
            letter-spacing: 0.05em;
            align-self: flex-start;
        }
        .tt-type.govt { background: #fef2f2; color: #dc2626; border: 1px solid #fecaca; }
        .tt-type.semi { background: #fffbeb; color: #d97706; border: 1px solid #fde68a; }
        .tt-type.private { background: #eff6ff; color: #2563eb; border: 1px solid #bfdbfe; }

        .tt-details {
            display: grid;
            grid-template-columns: 1fr;
            gap: 8px;
            margin-bottom: 20px;
            padding: 12px;
            background: #f8fafc;
            border-radius: 12px;
            border: 1px solid #f1f5f9;
        }

        .tt-detail-item {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .tt-detail-label {
            font-size: 0.65rem;
            color: #94a3b8;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .tt-detail-value {
            font-size: 0.8rem;
            color: #1e293b;
            font-weight: 600;
        }
"""

def enrich_html():
    with open('/Users/roshanamarujala/Desktop/Antigravity/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Insert CSS
    if '.tt-type {' not in html:
        html = html.replace('    </style>', css + '\n    </style>')

    soup = bs4.BeautifulSoup(html, 'html.parser')
    cards = soup.find_all('div', class_='tt-card')

    default_info = {"type": "private", "label": "Private / Independent", "est": "2010", "founder": "Founding Members", "head": "Director / Head"}

    for card in cards:
        if card.find('div', class_='tt-type'):
            continue  # Already processed

        name_tag = card.find(class_='tt-name')
        if not name_tag:
            continue
            
        name = name_tag.get_text(strip=True)
        info = data.get(name, default_info)
        
        # 1. Classification
        type_div = soup.new_tag("div", attrs={"class": f"tt-type {info['type']}"})
        type_div.string = info['label']
        
        header_div = card.find('div', class_='tt-header')
        if header_div:
            header_div.insert_before(type_div)
            
        # 2. Details grid
        details_div = soup.new_tag("div", attrs={"class": "tt-details"})
        
        for label, val in [("Est. Year", info['est']), ("Founder", info['founder']), ("Current Head", info['head'])]:
            item = soup.new_tag("div", attrs={"class": "tt-detail-item"})
            lbl = soup.new_tag("span", attrs={"class": "tt-detail-label"})
            lbl.string = label
            value = soup.new_tag("span", attrs={"class": "tt-detail-value"})
            value.string = val
            item.append(lbl)
            item.append(value)
            details_div.append(item)
            
        meta_div = card.find('div', class_='tt-meta')
        if meta_div:
            meta_div.insert_before(details_div)

    with open('/Users/roshanamarujala/Desktop/Antigravity/index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == "__main__":
    enrich_html()
