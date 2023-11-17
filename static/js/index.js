/* index.js */

const voterButton = document.getElementById('voter-button');
const viewerButton = document.getElementById('viewer-button');

voterButton.addEventListener('click', () => {
    // Redirect to the voter route
    window.location.href = '/voter';
});

viewerButton.addEventListener('click', () => {
    // Redirect to the viewer route
    window.location.href = '/viewer';
});
