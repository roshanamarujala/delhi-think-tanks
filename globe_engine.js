/**
 * Delhi Think Tanks 3D Strategic Globe Engine - VECTOR EDITION v5
 * Zero-Texture, High-Contrast Strategic Visualization
 */

let myGlobe;
let nodesData = [];

const SECTOR_COLORS = {
    'geo-card': '#1d4ed8', 'def-card': '#b91c1c', 'pol-card': '#15803d',
    'eco-card': '#a16207', 'tec-card': '#6d28d9', 'env-card': '#0e7490',
    'soc-card': '#be185d', 'law-card': '#334155', 'art-card': '#8b5cf6'
};

const DELHI_COORDS = { lat: 28.61, lng: 77.23 };

function initGlobe() {
    console.log("Strategic Globe Engine: Starting Collection...");
    const container = document.getElementById('globe-container');
    if (!container) return;

    // 1. DATA HARVESTING
    const cards = document.querySelectorAll('.tt-card');
    if (cards.length === 0) {
        console.warn("No .tt-card elements found in DOM. Retrying in 1s...");
        setTimeout(initGlobe, 1000);
        return;
    }

    nodesData = Array.from(cards).map((card, index) => {
        const nameNode = card.querySelector('.tt-name');
        const focusNode = card.querySelector('.tt-focus');
        
        const name = nameNode ? nameNode.innerText : "Institution " + index;
        const focus = focusNode ? focusNode.innerText : "Strategic Research";
        
        let color = '#475569';
        for (const [cls, hex] of Object.entries(SECTOR_COLORS)) {
            if (card.classList.contains(cls)) { color = hex; break; }
        }

        // Concentric distribution around India
        const spread = 4.0; 
        return {
            lat: DELHI_COORDS.lat + (Math.random() - 0.5) * spread,
            lng: DELHI_COORDS.lng + (Math.random() - 0.5) * spread,
            name: name,
            focus: focus,
            color: color,
            element: card
        };
    });

    console.log(`Globe Engine: Mapping ${nodesData.length} Strategic Nodes.`);

    // 2. VECTOR RENDER
    myGlobe = Globe()(container)
        .backgroundColor('rgba(0,0,0,0)')
        .globeColor('#0f172a') // SOLID NAVY - NO TEXTURE DEPENDENCY
        .showAtmosphere(true)
        .atmosphereColor('#3b82f6')
        .atmosphereDaylightAlpha(0.3)
        .showGraticules(true)
        .pointsData(nodesData)
        .pointColor('color')
        .pointRadius(1.2)
        .pointAltitude(0.12) // High visibility
        .pointLabel(d => `
            <div class="globe-tooltip">
                <div style="font-weight: 800; color: ${d.color}; border-bottom: 2px solid ${d.color}44; padding-bottom: 4px; margin-bottom: 6px;">${d.name}</div>
                <div style="font-size: 0.8rem; color: #cbd5e1;">${d.focus}</div>
            </div>
        `)
        .onPointClick(node => handleGlobalNav(node));

    // Controls Configuration
    const controls = myGlobe.controls();
    controls.autoRotate = true;
    controls.autoRotateSpeed = 1.0;
    controls.enableZoom = true;
    
    // Initial Orientation
    myGlobe.pointOfView({ lat: 20, lng: 77, altitude: 2.5 }, 0);
    console.log("Strategic Globe: Tactical Ready.");
}

function handleGlobalNav(node) {
    if (!node || !node.element) return;
    myGlobe.controls().autoRotate = false;
    myGlobe.pointOfView({ lat: node.lat, lng: node.lng, altitude: 1.4 }, 1200);
    
    setTimeout(() => {
        node.element.scrollIntoView({ behavior: 'smooth', block: 'center' });
        node.element.style.transition = 'all 0.5s ease';
        node.element.style.outline = '10px solid ' + node.color;
        node.element.style.boxShadow = '0 0 60px ' + node.color + '66';
        
        setTimeout(() => {
            node.element.style.outline = 'none';
            node.element.style.boxShadow = '';
            myGlobe.controls().autoRotate = true;
        }, 5000);
    }, 1300);
}

function triggerRandomDiscovery() {
    if (!nodesData.length) return;
    handleGlobalNav(nodesData[Math.floor(Math.random() * nodesData.length)]);
}

// Robust bootstrapper
if (document.readyState === 'complete') {
    initGlobe();
} else {
    window.addEventListener('load', initGlobe);
}
