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
        .atmosphereColor('#cbd5e1')
        .atmosphereDaylightAlpha(0.2)
        .showGraticules(true) // Professional strategic look
        .pointsData(nodesData)
        .pointColor('color')
        .pointRadius('size')
        .pointAltitude(0.01)
        .pointLabel(d => `
            <div class="globe-tooltip">
                <div style="font-weight: 800; color: ${d.color}; margin-bottom: 4px;">${d.name}</div>
                <div style="font-size: 0.75rem; color: #94a3b8;">${d.focus}</div>
            </div>
        `)
        .onPointClick(d => {
            d.element.scrollIntoView({ behavior: 'smooth', block: 'center' });
            // Add a temporary highlight effect to the card
            d.element.style.ring = '4px solid ' + d.color;
            d.element.style.boxShadow = '0 0 30px ' + d.color + '44';
            setTimeout(() => {
                d.element.style.ring = '';
                d.element.style.boxShadow = '';
            }, 3000);
        });

    // 3. Configure Controls
    myGlobe.controls().autoRotate = true;
    myGlobe.controls().autoRotateSpeed = 0.5;
    myGlobe.controls().enableZoom = true;

    // Center on India initially
    myGlobe.pointOfView({ lat: 20, lng: 77, altitude: 2 }, 1000);
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
