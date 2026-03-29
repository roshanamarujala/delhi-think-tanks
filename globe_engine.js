/**
 * Delhi Think Tanks 3D Strategic Globe Engine
 * Powered by Globe.gl
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

function initGlobe() {
    const container = document.getElementById('globe-container');
    if (!container) return;

    // 1. Extract Data from DOM
    const cards = document.querySelectorAll('.tt-card');
    cards.forEach((card, index) => {
        const name = card.querySelector('.tt-name').innerText;
        const focus = card.querySelector('.tt-focus').innerText;
        const cardId = card.closest('.domain-row').id;
        
        // Find which sector class it has
        let color = '#475569'; // Default
        for (const [cls, hex] of Object.entries(SECTOR_COLORS)) {
            if (card.classList.contains(cls)) {
                color = hex;
                break;
            }
        }

        // Generate stylized "Impact Cluster" coordinates
        // We use a small spread to make them visible but centered on India
        const spread = 2.5; 
        nodesData.push({
            id: index,
            name: name,
            focus: focus,
            lat: DELHI_COORDS.lat + (Math.random() - 0.5) * spread,
            lng: DELHI_COORDS.lng + (Math.random() - 0.5) * spread,
            size: 0.15,
            color: color,
            element: card
        });
    });

    // 2. Initialize Globe
    myGlobe = Globe()
        (container)
        .backgroundColor('rgba(0,0,0,0)')
        .showAtmosphere(true)
        .atmosphereColor('#3b82f6') // Deep strategic blue
        .atmosphereDaylightAlpha(0.3)
        .showGraticules(true) // Tactical grid lines
        .pointsData(nodesData)
        .pointColor('color')
        .pointRadius(0.8) // Larger nodes for better visibility
        .pointAltitude(0.04)
        .pointLabel(d => `
            <div class="globe-tooltip">
                <div style="font-weight: 800; color: ${d.color}; border-bottom: 2px solid ${d.color}44; padding-bottom: 4px; margin-bottom: 6px; font-size: 1rem;">
                    ${d.name}
                </div>
                <div style="font-size: 0.8rem; color: #cbd5e1; line-height: 1.4;">
                    <span style="color: #94a3b8; font-weight: 700; text-transform: uppercase; font-size: 0.7rem;">Strategic Focus:</span><br/>
                    ${d.focus}
                </div>
            </div>
        `)
        .onPointClick(d => {
            // Stop rotation during focus
            myGlobe.controls().autoRotate = false;
            
            // Strategic zoom to node
            myGlobe.pointOfView({ lat: d.lat, lng: d.lng, altitude: 1.2 }, 1200);
            
            // Navigate to card
            setTimeout(() => {
                d.element.scrollIntoView({ behavior: 'smooth', block: 'center' });
                d.element.style.outline = '4px solid ' + d.color;
                d.element.style.boxShadow = '0 0 50px ' + d.color + '44';
                d.element.classList.add('discovery-glow');
                
                setTimeout(() => {
                    d.element.style.outline = '';
                    d.element.style.boxShadow = '';
                    d.element.classList.remove('discovery-glow');
                    myGlobe.controls().autoRotate = true; // Resume auto-rotate
                }, 4000);
            }, 800);
        });

    // Custom Globe Material for "Strategic Intelligence" Look
    const globeMaterial = myGlobe.globeMaterial();
    globeMaterial.color = new THREE.Color('#0f172a'); // Deep navy base
    globeMaterial.emissive = new THREE.Color('#1e293b');
    globeMaterial.emissiveIntensity = 0.1;
    globeMaterial.shininess = 0.8;

    // 3. Configure Controls
    const controls = myGlobe.controls();
    controls.autoRotate = true;
    controls.autoRotateSpeed = 0.6;
    controls.enableZoom = true;
    controls.enablePan = false; // Keep it focused on the sphere
    controls.minDistance = 250;
    controls.maxDistance = 500;

    // Center on India/Delhi initially
    myGlobe.pointOfView({ lat: 20, lng: 77, altitude: 2.2 }, 0);
}

function triggerRandomDiscovery() {
    if (!nodesData.length) return;
    
    const randomIndex = Math.floor(Math.random() * nodesData.length);
    const node = nodesData[randomIndex];

    // Spin and zoom to the node
    myGlobe.pointOfView({ lat: node.lat, lng: node.lng, altitude: 1 }, 2000);
    
    // Simulate a click after arrival
    setTimeout(() => {
        node.element.scrollIntoView({ behavior: 'smooth', block: 'center' });
        node.element.style.outline = '4px solid ' + node.color;
        node.element.style.transform = 'scale(1.02)';
        node.element.classList.add('discovery-glow');
        
        setTimeout(() => {
            node.element.style.outline = '';
            node.element.style.transform = '';
        }, 5000);
    }, 2100);
}

// Start when DOM is ready
window.addEventListener('load', () => {
    initGlobe();
});
