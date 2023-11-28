/* voter.js */

function vote(winImage, loseImage, image_path) {
    $.ajax({
        url: "/vote",
        type: "POST",
        data: { win_img: winImage, lose_img: loseImage},
        success: function(response) {
            var imagePath = '/static/' + image_path + '/';
            $('#image1').attr('src', imagePath + response.image1);
            $('#image2').attr('src', imagePath + response.image2);
        }
    });
}