# app.py

# Imports
from voting import select_image_pair, score_elo
from viewer import sort_images, get_next_image, get_first_image, get_previous_image
from imageLoadReadWrite import write_image_json, load_image_pool, load_folders, give_folder
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

# Initializers
current_images = {'image1': None, 'image2': None}

# Route to leading page on start up
@app.route('/')
def index():
    global folder_options
    folder_options = load_folders()
    return render_template('index.html', folder_options=folder_options)

# Route to update folder
@app.route('/update_folder', methods=['POST'])
def update_folder():
    data = request.get_json()
    selected_folder = data.get('folder')
    give_folder(selected_folder)
    global CURRENT_IMAGE_PATH
    global PATH_TO_JSON
    global CURRENT_IMAGE_FOLDER
    from imageLoadReadWrite import CURRENT_IMAGE_PATH, PATH_TO_JSON, CURRENT_IMAGE_FOLDER
    write_image_json()
    response_data = {'message': 'Folder updated successfully'}
    return jsonify(response_data)


# Route to voter page
@app.route('/voter')
def voter():
    global image_pool
    image_pool = load_image_pool()
    image1, image2 = select_image_pair()
    current_images['image1'] = image1
    current_images['image2'] = image2
    return render_template('voter.html', image1=image1, image2=image2, image_path=CURRENT_IMAGE_FOLDER)

# function call vote
@app.route('/vote', methods=['POST'])
def vote():
    win_img = request.form['win_img']
    lose_img = request.form['lose_img']
    score_elo(current_images[win_img], current_images[lose_img])
    # Get two new random images for the next vote
    image1, image2 = select_image_pair()
    current_images['image1'] = image1
    current_images['image2'] = image2
    return jsonify({'image1': image1, 'image2': image2})


# Route to viewer page
@app.route('/viewer')
def viewer():
    sort_images()
    current_image = get_first_image()
    return render_template('viewer.html', current_image=current_image, image_path=CURRENT_IMAGE_FOLDER)
# TODO add the score on the viewer for each current_image

# function call next
@app.route('/next', methods=['POST'])
def next():
    next_image = get_next_image()
    return jsonify({'current_image': next_image, 'image_path': CURRENT_IMAGE_FOLDER})

# function call next
@app.route('/previous', methods=['POST'])
def previous():
    previous_image = get_previous_image()
    return jsonify({'current_image': previous_image, 'image_path': CURRENT_IMAGE_FOLDER})


# TODO add new page, image elimination, here we pick the Bottom, 10% of scors, we display them in acending order and ask wether the img should be kept or not, if not, then we dealte the imgage from the image_pool and from the image file.

if __name__ == "__main__":
    #run app
    app.run(debug=True)
