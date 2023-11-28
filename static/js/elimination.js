// elimination.js

function deleteImage(image) {
    // Send an AJAX request to delete the image
    $.ajax({
        url: '/delete_image',
        type: 'POST',
        data: { image_to_delete: imageToDelete },
        success: function(response) {
            // Log the success message to the console
            console.log(response.message);
        }
    });
}