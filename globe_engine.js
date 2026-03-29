/**
 * Delhi Think Tanks 3D Strategic Globe Engine - PREMIUM EDITION v6
 * High-Fidelity Textured Visualization & Flawless Interactivity
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

        // Expanded concentric distribution for better node visibility and clickability
        const spread = 15.0;
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

    // 2. PREMIUM TEXTURED RENDER
    myGlobe = Globe()(container)
        .globeImageUrl('https://unpkg.com/three-globe/example/img/earth-blue-marble.jpg')
        .bumpImageUrl('https://unpkg.com/three-globe/example/img/earth-topology.png')
        .backgroundColor('rgba(0,0,0,0)')
        .showAtmosphere(true)
        .atmosphereColor('#3b82f6')
        .atmosphereDaylightAlpha(0.2)
        .showGraticules(true)
        .pointsData(nodesData)
        .pointColor('color')
        .pointRadius(0.8)
        .pointAltitude(0.05)
        .pointResolution(32)
        .pointLabel(d => `
            <div class="globe-tooltip">
                <div style="font-weight: 800; color: ${d.color}; border-bottom: 2px solid ${d.color}44; padding-bottom: 4px; margin-bottom: 6px;">${d.name}</div>
                <div style="font-size: 0.8rem; color: #cbd5e1;">${d.focus}</div>
            </div>
        `)
        .onPointHover(node => {
            container.style.cursor = node ? 'pointer' : 'grab';
        })
        .onPointClick(node => handleGlobalNav(node));

    // Controls Configuration
    const controls = myGlobe.controls();
    controls.autoRotate = true;
    controls.autoRotateSpeed = 1.0;
    controls.enableZoom = true;

    // Initial Orientation (pulled back for a better holistic view)
    myGlobe.pointOfView({ lat: 20, lng: 77, altitude: 2.5 }, 0);
    console.log("Strategic Globe: Tactical Ready.");
}

function handleGlobalNav(node) {
    if (!node || !node.element) return;

    const controls = myGlobe.controls();
    controls.autoRotate = false;

    // Smooth transit to the exact node
    myGlobe.pointOfView({ lat: node.lat, lng: node.lng, altitude: 1.0 }, 1200);

    setTimeout(() => {
        // Scroll into viewport accounting for sticky headers
        node.element.scrollIntoView({ behavior: 'smooth', block: 'center' });

        // Highlight the selected card prominently
        node.element.style.transition = 'all 0.5s ease';
        node.element.style.outline = '8px solid ' + node.color;
        node.element.style.boxShadow = '0 0 50px ' + node.color + '88';
        node.element.style.transform = 'scale(1.02)';
        node.element.style.zIndex = '100';

        setTimeout(() => {
            node.element.style.outline = 'none';
            node.element.style.boxShadow = '';
            node.element.style.transform = '';
            node.element.style.zIndex = '';
            controls.autoRotate = true;
        }, 4000);
    }, 1300);
}

// Attach directly to window object to guarantee accessibility for the Discovery Mode button
window.triggerRandomDiscovery = function() {
    if (!nodesData || nodesData.length === 0) {
        console.warn("Nodes not fully loaded yet.");
        return;
    }
    const randomNode = nodesData[Math.floor(Math.random() * nodesData.length)];
    handleGlobalNav(randomNode);
};

// Robust bootstrapper covering various DOM states
if (document.readyState === 'complete' || document.readyState === 'interactive') {
    initGlobe();
} else {
    window.addEventListener('DOMContentLoaded', initGlobe);
}
