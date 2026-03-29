import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    (r'(?s)(<a class="tt-name"[^>]*>SOLPO \(Policy Research\)</a>.*?<div class="tt-detail-label">Founder</div>\s*<div class="tt-detail-value">)Policy Associates(</div>)', r'\g<1>Sanjay Sen\g<2>'),
    (r'(?s)(<a class="tt-name"[^>]*>SOLPO \(Policy Research\)</a>.*?<div class="tt-detail-label">Current Head</div>\s*<div class="tt-detail-value">)Managing Director(</div>)', r'\g<1>Sanjay Sen (Director)\g<2>'),

    (r'(?s)(<a class="tt-name"[^>]*>Public Policy India</a>.*?<div class="tt-detail-label">Founder</div>\s*<div class="tt-detail-value">)PPI Team(</div>)', r'\g<1>Yash Agarwal & Michelle Patrick\g<2>'),
    (r'(?s)(<a class="tt-name"[^>]*>Public Policy India</a>.*?<div class="tt-detail-label">Current Head</div>\s*<div class="tt-detail-value">)Executive Director(</div>)', r'\g<1>Yash Agarwal\g<2>'),

    (r'(?s)(<a class="tt-name"[^>]*>NCAS India \(Social Watch\)</a>.*?<div class="tt-detail-label">Founder</div>\s*<div class="tt-detail-value">)Social Activists Group(</div>)', r'\g<1>Josantony Joseph\g<2>'),
    (r'(?s)(<a class="tt-name"[^>]*>NCAS India \(Social Watch\)</a>.*?<div class="tt-detail-label">Current Head</div>\s*<div class="tt-detail-value">)Director(</div>)', r'\g<1>N/A\g<2>'),

    (r'(?s)(<a class="tt-name"[^>]*>SDE \(Sustainable Economics\)</a>.*?<div class="tt-detail-label">Founder</div>\s*<div class="tt-detail-value">)Research Collective(</div>)', r'\g<1>Sushil Kumar Sharma\g<2>'),
    (r'(?s)(<a class="tt-name"[^>]*>SDE \(Sustainable Economics\)</a>.*?<div class="tt-detail-label">Current Head</div>\s*<div class="tt-detail-value">)Director(</div>)', r'\g<1>Sushil Kumar Sharma (CEO)\g<2>'),

    (r'(?s)(<a class="tt-name"[^>]*>CPD \(Policy Design\)</a>.*?<div class="tt-detail-label">Founder</div>\s*<div class="tt-detail-value">)Policy Team(</div>)', r'\g<1>ATREE\g<2>'),
    (r'(?s)(<a class="tt-name"[^>]*>CPD \(Policy Design\)</a>.*?<div class="tt-detail-label">Current Head</div>\s*<div class="tt-detail-value">)Director(</div>)', r'\g<1>Dr. Abi Tamim Vanak (Director)\g<2>'),

    (r'(?s)(<a class="tt-name"[^>]*>CFAR \(Advocacy Research\)</a>.*?<div class="tt-detail-label">Founder</div>\s*<div class="tt-detail-value">)Activists Group(</div>)', r'\g<1>Akhila Sivadas\g<2>'),

    (r'(?s)(<a class="tt-name"[^>]*>CASP \(Artistic Practice\)</a>.*?<div class="tt-detail-label">Founder</div>\s*<div class="tt-detail-value">)Artistic Collective(</div>)', r'\g<1>Amrita Gupta & Parul\g<2>'),
    (r'(?s)(<a class="tt-name"[^>]*>CASP \(Artistic Practice\)</a>.*?<div class="tt-detail-label">Current Head</div>\s*<div class="tt-detail-value">)Director(</div>)', r'\g<1>Amrita Gupta (Director)\g<2>'),

    (r'(?s)(<a class="tt-name"[^>]*>CENREC \(Regional Conflict\)</a>.*?<div class="tt-detail-label">Founder</div>\s*<div class="tt-detail-value">)Strategic Thinkers Group(</div>)', r'\g<1>N/A\g<2>'),
    (r'(?s)(<a class="tt-name"[^>]*>CENREC \(Regional Conflict\)</a>.*?<div class="tt-detail-label">Current Head</div>\s*<div class="tt-detail-value">)Board of Directors(</div>)', r'\g<1>N/A\g<2>'),

    (r'(?s)(<a class="tt-name"[^>]*>CIPR \(Independent Policy\)</a>.*?<div class="tt-detail-label">Founder</div>\s*<div class="tt-detail-value">)Legal Experts Group(</div>)', r'\g<1>N/A\g<2>'),
    (r'(?s)(<a class="tt-name"[^>]*>CIPR \(Independent Policy\)</a>.*?<div class="tt-detail-label">Current Head</div>\s*<div class="tt-detail-value">)Director(</div>)', r'\g<1>N/A\g<2>'),

    (r'(?s)(<a class="tt-name"[^>]*>LPRS \(Legal & Policy\)</a>.*?<div class="tt-detail-label">Founder</div>\s*<div class="tt-detail-value">)Legal Experts(</div>)', r'\g<1>N/A\g<2>'),
    (r'(?s)(<a class="tt-name"[^>]*>LPRS \(Legal & Policy\)</a>.*?<div class="tt-detail-label">Current Head</div>\s*<div class="tt-detail-value">)Director(</div>)', r'\g<1>N/A\g<2>'),
]

for pat, repl in replacements:
    html = re.sub(pat, repl, html, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
