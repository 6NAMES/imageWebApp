/* voter.js */

function vote(winImage, loseImage, image_path) {
    $.ajax({
        url: "/vote",
        type: "POST",
        data: { win_img: winImage, lose_img: loseImage},
        success: function(response) {
            $('#image1').attr('src', '/static/images' + image_path + '/' + response.image1);
            $('#image2').attr('src', '/static/images' + image_path + '/' + response.image2);
        }
    });
}
