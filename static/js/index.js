/* index.js */

const voterButton = document.getElementById('voter-button');
const viewerButton = document.getElementById('viewer-button');
const folderDropdown = document.getElementById('folderDropdown');


voterButton.addEventListener('click', () => {
    // Redirect to the voter route
    window.location.href = '/voter';
});

viewerButton.addEventListener('click', () => {
    // Redirect to the viewer route
    window.location.href = '/viewer';
});

function changeFolder(selectedFolder) {
    console.log("Selected Folder:", selectedFolder);

    // Send the selected folder to the server using Fetch API
    fetch('/update_folder', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ folder: selectedFolder }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Successful server response:', data);
        // Additional logic for a successful send can be added here
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
