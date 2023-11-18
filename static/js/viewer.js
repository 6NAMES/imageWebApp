/* viewer.js */

/* viewer.js */

let current_image = '{{ current_image }}'; // Make sure to set the initial value based on your template

function updateImage(response) {
    console.log('Current Image:', current_image);  // Log the current_image to the console
    $('#current_image').attr('src', '/static/' + response.image_path + '/' + response.current_image);
}

function nextImage() {
    $.ajax({
        url: "/next",
        type: "POST",
        success: function (response) {
            console.log('Success! Response:', response); // Log the response to the console
            updateImage(response);
        },
    });
}

function previousImage() {
    $.ajax({
        url: "/previous",
        type: "POST",
        success: function (response) {
            console.log('Success! Response:', response); // Log the response to the console
            updateImage(response);
        },
    });
}
