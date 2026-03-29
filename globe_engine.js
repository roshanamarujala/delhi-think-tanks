/**
 * Delhi Think Tanks 3D Strategic Globe Engine - RECONSTRUCTED
 * High-Reliability rendering for Strategic Intelligence
 */

let myGlobe;
let nodesData = [];

const SECTOR_COLORS = {
    'geo-card': '#1d4ed8',
    'def-card': '#b91c1c',
    'pol-card': '#15803d',
    'eco-card': '#a16207',
    'tec-card': '#6d28d9',
    'env-card': '#0e7490',
    'soc-card': '#be185d',
    'law-card': '#334155',
    'art-card': '#8b5cf6'
};

const DELHI_COORDS = { lat: 28.61, lng: 77.23 };
// 1x1 Transparent Base64 to satisfy Globe.gl without loading external images
const BLANK_TEXTURE = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=";

function initGlobe() {
    const container = document.getElementById('globe-container');
    if (!container) return;

    // 1. EXTRACT DATA - 177 VERIFIED NODES
    nodesData = [];
    const cards = document.querySelectorAll('.tt-card');
    cards.forEach((card, index) => {
        const name = card.querySelector('.tt-name').innerText;
        const focus = card.querySelector('.tt-focus').innerText;
        
        let color = '#475569';
        for (const [cls, hex] of Object.entries(SECTOR_COLORS)) {
            if (card.classList.contains(cls)) {
                color = hex;
                break;
            }
        }

        const spread = 2.8; 
        nodesData.push({
            id: index,
            name: name,
            focus: focus,
            lat: DELHI_COORDS.lat + (Math.random() - 0.5) * spread,
            lng: DELHI_COORDS.lng + (Math.random() - 0.5) * spread,
            size: 0.18,
            color: color,
            element: card
        });
    });

    // 2. INITIALIZE GLOBE WITH TACTICAL FALLBACKS
    myGlobe = Globe()
        (container)
        .globeImageUrl(BLANK_TEXTURE)
        .backgroundColor('rgba(0,0,0,0)')
        .showAtmosphere(true)
        .atmosphereColor('#3b82f6')
        .atmosphereDaylightAlpha(0.25)
        .showGraticules(true)
        .pointsData(nodesData)
        .pointColor(d => d.color || '#3b82f6')
        .pointRadius(0.8) // Explicit large radius for better visibility
        .pointAltitude(0.08)
        .pointLabel(d => `
            <div class="globe-tooltip">
                <div style="font-weight: 800; color: ${d.color}; border-bottom: 2px solid ${d.color}44; padding-bottom: 4px; margin-bottom: 6px; font-size: 0.95rem;">
                    ${d.name}
                </div>
                <div style="font-size: 0.8rem; color: #cbd5e1; line-height: 1.4;">
                    <span style="color: #94a3b8; font-weight: 700; text-transform: uppercase; font-size: 0.65rem;">Strategic Focus</span><br/>
                    ${d.focus}
                </div>
            </div>
        `)
        .onPointClick(node => {
            handleInstitutionalNavigation(node);
        });

    // ROBUST MATERIAL SETTER
    setTimeout(() => {
        try {
            const material = myGlobe.globeMaterial();
            if (material) {
                if (window.THREE) {
                    material.color = new THREE.Color('#0f172a');
                } else {
                    material.color.set('#0f172a');
                }
                material.opacity = 0.98;
                material.transparent = true;
            }
        } catch (e) {
            console.error("Globe material tweak failed", e);
        }
    }, 100);

    // 3. CONFIGURE CONTROLS
    const controls = myGlobe.controls();
    controls.autoRotate = true;
    controls.autoRotateSpeed = 0.6;
    controls.enableZoom = true;
    controls.minDistance = 200;
    controls.maxDistance = 600;

    // Start Focus
    myGlobe.pointOfView({ lat: 20, lng: 77, altitude: 2.2 }, 0);
}

function handleInstitutionalNavigation(node) {
    if (!node || !node.element) return;

    // Stop rotation
    myGlobe.controls().autoRotate = false;
    
    // Zoom focus
    myGlobe.pointOfView({ lat: node.lat, lng: node.lng, altitude: 1.1 }, 1000);
    
    // Trigger scroll and visual feedback
    setTimeout(() => {
        node.element.scrollIntoView({ behavior: 'smooth', block: 'center' });
        
        // High-vis pulse
        node.element.style.transition = 'all 0.5s ease';
        node.element.style.outline = '8px solid ' + node.color;
        node.element.classList.add('discovery-glow');
        
        setTimeout(() => {
            node.element.style.outline = 'none';
            node.element.classList.remove('discovery-glow');
            myGlobe.controls().autoRotate = true;
        }, 5000);
    }, 1100);
}

function triggerRandomDiscovery() {
    if (!nodesData.length) return;
    const randomIndex = Math.floor(Math.random() * nodesData.length);
    handleInstitutionalNavigation(nodesData[randomIndex]);
}

window.addEventListener('load', () => {
    // Small delay to ensure WebGL context is ready
    setTimeout(initGlobe, 500);
});
