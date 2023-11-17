/* viewer.js */

function nextImage(current_image) {
    $.ajax({
        url: "/next",
        type: "POST",
        data: { current_image: current_image },
        success: function (response) {
            const nextHighestRatedImage = response.current_image;
            if (nextHighestRatedImage) {
                // Add the base path to the next image
                $('#current_image').attr('src', imagePath + nextHighestRatedImage);
            } else {
                console.log("No more images in the database.");
            }
        }
    });
}

function prevImage(current_image) {
    $.ajax({
        url: "/previous",
        type: "POST",
        data: { current_image: current_image },
        success: function (response) {
            const prevHighestRatedImage = response.current_image;
            if (prevHighestRatedImage) {
                // Add the base path to the previous image
                const imagePath = "{{ url_for('static', filename='images/imagez/') }}";
                $('#current_image').attr('src', imagePath + prevHighestRatedImage);
            } else {
                console.log("No more images in the database.");
            }
        }
    });
}
