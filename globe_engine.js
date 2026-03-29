/**
 * Delhi Think Tanks 3D Strategic Globe Engine - ULTRA RELIABILITY v4
 * Optimized for Strategic Intelligence & 100% Render Guarantee
 */

let myGlobe;
let nodesData = [];

// Tactical Navy Blue 1x1 Pixel
const STRATEGIC_TEXTURE = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mN8/+m7PQAIZAMmC99eFwAAAABJRU5ErkJggg==";

const SECTOR_COLORS = {
    'geo-card': '#1d4ed8', 'def-card': '#b91c1c', 'pol-card': '#15803d',
    'eco-card': '#a16207', 'tec-card': '#6d28d9', 'env-card': '#0e7490',
    'soc-card': '#be185d', 'law-card': '#334155', 'art-card': '#8b5cf6'
};

const DELHI_COORDS = { lat: 28.61, lng: 77.23 };

function initGlobe() {
    console.log("Strategic Globe Engine: Initializing...");
    const container = document.getElementById('globe-container');
    if (!container) return;

    // 1. COLLECT NODES
    const cards = document.querySelectorAll('.tt-card');
    console.log(`Found ${cards.length} institutional cards.`);
    
    nodesData = Array.from(cards).map((card, index) => {
        const name = card.querySelector('.tt-name')?.innerText || "Unknown";
        const focus = card.querySelector('.tt-focus')?.innerText || "Strategic Policy";
        
        let color = '#475569';
        for (const [cls, hex] of Object.entries(SECTOR_COLORS)) {
            if (card.classList.contains(cls)) { color = hex; break; }
        }

        const spread = 3.5; 
        return {
            lat: DELHI_COORDS.lat + (Math.random() - 0.5) * spread,
            lng: DELHI_COORDS.lng + (Math.random() - 0.5) * spread,
            name: name,
            focus: focus,
            color: color,
            element: card
        };
    });

    // 2. CONSTRUCT VIEW
    myGlobe = Globe()(container)
        .globeImageUrl(STRATEGIC_TEXTURE)
        .backgroundColor('rgba(0,0,0,0)')
        .showAtmosphere(true)
        .atmosphereColor('#2563eb')
        .atmosphereDaylightAlpha(0.2)
        .showGraticules(true)
        .pointsData(nodesData)
        .pointColor('color')
        .pointRadius(1.0) // Significant visibility
        .pointAltitude(0.08)
        .pointLabel(d => `
            <div class="globe-tooltip">
                <div style="font-weight: 800; color: ${d.color}; border-bottom: 2px solid ${d.color}44; padding-bottom: 4px; margin-bottom: 6px;">${d.name}</div>
                <div style="font-size: 0.8rem; color: #cbd5e1; line-height: 1.2;">${d.focus}</div>
            </div>
        `)
        .onPointClick(node => handleNav(node));

    // 3. APPLY TACTICAL SHADER (SAFE SETTER)
    setTimeout(() => {
        const material = myGlobe.globeMaterial();
        if (material) {
            material.opacity = 0.9;
            material.transparent = true;
            console.log("Strategic Globe: Material Ready.");
        }
    }, 200);

    const controls = myGlobe.controls();
    controls.autoRotate = true;
    controls.autoRotateSpeed = 0.8;
    controls.enableZoom = true;
    
    myGlobe.pointOfView({ lat: 20, lng: 77, altitude: 2.3 }, 0);
}

function handleNav(node) {
    if (!node || !node.element) return;
    myGlobe.controls().autoRotate = false;
    myGlobe.pointOfView({ lat: node.lat, lng: node.lng, altitude: 1.2 }, 1000);
    
    setTimeout(() => {
        node.element.scrollIntoView({ behavior: 'smooth', block: 'center' });
        node.element.style.transition = 'all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
        node.element.style.outline = '10px solid ' + node.color;
        node.element.style.transform = 'scale(1.03)';
        
        setTimeout(() => {
            node.element.style.outline = 'none';
            node.element.style.transform = 'scale(1)';
            myGlobe.controls().autoRotate = true;
        }, 4000);
    }, 1100);
}

function triggerRandomDiscovery() {
    if (!nodesData.length) return;
    handleNav(nodesData[Math.floor(Math.random() * nodesData.length)]);
}

window.addEventListener('load', () => { setTimeout(initGlobe, 800); });
