/* viewer.js */

function nextImage() {
    console.log('Current Image:', current_image);  // Log the current_image to the console
    $.ajax({
        url: "/next",
        type: "POST",
        success: function (response) {
            console.log('Success! Response:', response); // Log the response to the console
            $('#current_image').attr('src', '/static/' + response.image_path + '/' + response.current_image);
        },
    });
}