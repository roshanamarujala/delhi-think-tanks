/**
 * Delhi Think Tanks 3D Strategic Globe Engine - PREMIUM EDITION v7
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

// Hex-alpha suffixes for arc colours: primary (75%) and secondary (40%) opacity
const NEAR_ARC_OPACITY = 'bb';
const FAR_ARC_OPACITY  = '66';

// Delay (ms) before dispatching a resize event so the WebGL canvas measures its
// container correctly after the first render frame completes on desktop.
const CANVAS_RESIZE_DELAY = 300;

/**
 * Build a set of arcs that visually connect nodes into a network.
 * Each node `i` gets two arcs:
 *  1. A primary arc to its immediate neighbour (i+1) – full opacity.
 *  2. A secondary arc to a node further along the list (i + step) – half opacity.
 * @param {Array} nodes - Array of node objects with lat/lng/color properties.
 * @returns {Array} Array of arc descriptor objects for globe.gl arcsData().
 */
function buildArcs(nodes) {
    var arcs = [];
    var step = Math.max(1, Math.floor(nodes.length / 4));
    for (var i = 0; i < nodes.length; i++) {
        var a = nodes[i];
        var b = nodes[(i + 1) % nodes.length];
        var c = nodes[(i + step) % nodes.length];
        if (b !== a) {
            arcs.push({
                startLat: a.lat, startLng: a.lng,
                endLat: b.lat, endLng: b.lng,
                color: [a.color + NEAR_ARC_OPACITY, b.color + NEAR_ARC_OPACITY]
            });
        }
        if (c !== a && c !== b) {
            arcs.push({
                startLat: a.lat, startLng: a.lng,
                endLat: c.lat, endLng: c.lng,
                color: [a.color + FAR_ARC_OPACITY, c.color + FAR_ARC_OPACITY]
            });
        }
    }
    return arcs;
}

function initGlobe() {
    console.log("Strategic Globe Engine: Starting Collection...");
    var container = document.getElementById('globe-container');
    if (!container) return;

    // 1. DATA HARVESTING
    var cards = document.querySelectorAll('.tt-card');
    if (cards.length === 0) {
        console.warn("No .tt-card elements found in DOM. Retrying in 1s...");
        setTimeout(initGlobe, 1000);
        return;
    }

    nodesData = Array.from(cards).map(function(card, index) {
        var nameNode = card.querySelector('.tt-name');
        var focusNode = card.querySelector('.tt-focus');

        var name = nameNode ? nameNode.innerText : "Institution " + index;
        var focus = focusNode ? focusNode.innerText : "Strategic Research";

        var color = '#475569';
        var keys = Object.keys(SECTOR_COLORS);
        for (var k = 0; k < keys.length; k++) {
            if (card.classList.contains(keys[k])) { color = SECTOR_COLORS[keys[k]]; break; }
        }

        var spread = 15.0;
        return {
            lat: DELHI_COORDS.lat + (Math.random() - 0.5) * spread,
            lng: DELHI_COORDS.lng + (Math.random() - 0.5) * spread,
            name: name,
            focus: focus,
            color: color,
            element: card
        };
    });

    console.log("Globe Engine: Mapping " + nodesData.length + " Strategic Nodes.");

    var arcsData = buildArcs(nodesData);

    // 2. PREMIUM TEXTURED RENDER
    // rendererConfig with alpha:true ensures the WebGL canvas is transparent on all
    // browsers (desktop and mobile), preventing the solid-black fallback canvas.
    myGlobe = Globe({ rendererConfig: { antialias: true, alpha: true } })(container)
        .globeImageUrl('https://unpkg.com/three-globe/example/img/earth-blue-marble.jpg')
        .bumpImageUrl('https://unpkg.com/three-globe/example/img/earth-topology.png')
        .backgroundColor('rgba(0,0,0,0)')
        .showAtmosphere(true)
        .atmosphereColor('#3b82f6')
        .atmosphereDaylightAlpha(0.2)
        .showGraticules(true)
        // Nodes
        .pointsData(nodesData)
        .pointColor('color')
        .pointRadius(0.8)
        .pointAltitude(0.05)
        .pointResolution(32)
        .pointLabel(function(d) {
            return '<div class="globe-tooltip">' +
                '<div style="font-weight:800;color:' + d.color + ';border-bottom:2px solid ' + d.color + '44;padding-bottom:4px;margin-bottom:6px;">' + d.name + '</div>' +
                '<div style="font-size:0.8rem;color:#cbd5e1;">' + d.focus + '</div>' +
                '</div>';
        })
        .onPointHover(function(node) { container.style.cursor = node ? 'pointer' : 'grab'; })
        .onPointClick(function(node) { handleGlobalNav(node); })
        // Dotted animated arcs connecting nodes into a visible network
        .arcsData(arcsData)
        .arcColor('color')
        .arcAltitude(0.15)
        .arcStroke(0.4)
        .arcDashLength(0.4)
        .arcDashGap(0.2)
        .arcDashAnimateTime(3000);

    // Controls Configuration
    var controls = myGlobe.controls();
    controls.autoRotate = true;
    controls.autoRotateSpeed = 1.0;
    controls.enableZoom = true;

    // Initial Orientation
    myGlobe.pointOfView({ lat: 20, lng: 77, altitude: 2.5 }, 0);

    // Force the canvas to re-measure its container after the first render frame so
    // it fills the full width on desktop browsers.
    setTimeout(function() { window.dispatchEvent(new Event('resize')); }, CANVAS_RESIZE_DELAY);

    console.log("Strategic Globe: Tactical Ready.");
}

function handleGlobalNav(node) {
    if (!node || !node.element) return;

    var controls = myGlobe.controls();
    controls.autoRotate = false;

    // Smooth transit to the exact node
    myGlobe.pointOfView({ lat: node.lat, lng: node.lng, altitude: 1.0 }, 1200);

    setTimeout(function() {
        // Scroll into viewport accounting for sticky headers
        node.element.scrollIntoView({ behavior: 'smooth', block: 'center' });

        // Highlight the selected card prominently
        node.element.style.transition = 'all 0.5s ease';
        node.element.style.outline = '8px solid ' + node.color;
        node.element.style.boxShadow = '0 0 50px ' + node.color + '88';
        node.element.style.transform = 'scale(1.02)';
        node.element.style.zIndex = '100';

        setTimeout(function() {
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
    var randomNode = nodesData[Math.floor(Math.random() * nodesData.length)];
    handleGlobalNav(randomNode);
};

// Robust bootstrapper covering various DOM states
if (document.readyState === 'complete' || document.readyState === 'interactive') {
    initGlobe();
} else {
    window.addEventListener('DOMContentLoaded', initGlobe);
}
