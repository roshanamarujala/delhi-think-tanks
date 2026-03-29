import re

INDEX_PATH = "index.html"

def integrate():
    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add Globe container and Button
    # Target: <div class="search-container" ...> ... </div>
    # We want to insert BEFORE it.
    
    search_pattern = r'<div class="search-container".*?>\s*<input id="tt-search".*?>\s*</div>'
    replacement = """    <div id="globe-container"></div>
    <div class="search-container" style="margin-top: 20px; margin-bottom: 20px;">
     <input id="tt-search" placeholder="Search 177 institutions by name or focus (e.g. AI, Geopolitics, Blue Economy)..." type="text"/>
     <button class="discover-btn" onclick="triggerRandomDiscovery()">
      <svg height="16" viewbox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg">
       <path d="M12 2L4.5 20.29l.71.71L12 18l6.79 3 .71-.71L12 2z" fill="currentColor"></path>
      </svg>
      Discovery Mode: Random Think Tank
     </button>
    </div>"""
    
    new_content = re.sub(search_pattern, replacement, content, flags=re.DOTALL)
    
    # 2. Add Script at the end
    script_pattern = r'</body>\s*</html>'
    script_replacement = '  <script src="globe_engine.js"></script>\n </body>\n</html>'
    
    new_content = re.sub(script_pattern, script_replacement, new_content)

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("UI Integration complete via Python.")

if __name__ == "__main__":
    integrate()
