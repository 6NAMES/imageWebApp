# imageLoadReadWrite.py

import os
import json

# Directory where PNG images are stored



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_TO_IMAGE_FOLDER = os.path.join("static", "images")
DATABASE_DIR = os.path.join(BASE_DIR, "database")
IMAGE_EXTENSION = '.png'


def load_folders():
    folder_options = []
    try:
        entries = os.listdir(PATH_TO_IMAGE_FOLDER)
        folders = [entry for entry in entries if os.path.isdir(os.path.join(PATH_TO_IMAGE_FOLDER, entry))]
        folders.sort()
        folder_options = folders

    except Exception as e:
        # Handle exceptions based on your needs
        print(f"Error reading folders: {e}")

    return folder_options

def give_folder(selectedfolder):
    global CURRENT_IMAGE_FOLDER
    global PATH_TO_JSON
    global selected_folder
    selected_folder = selectedfolder
    CURRENT_IMAGE_FOLDER = os.path.join(PATH_TO_IMAGE_FOLDER, selected_folder)
    PATH_TO_JSON = os.path.join(DATABASE_DIR, selected_folder, "image_pool.json")
    

def load_image_pool():
    image_pool = [image for image in os.listdir(CURRENT_IMAGE_FOLDER) if image.endswith(IMAGE_EXTENSION)]
    return image_pool


def load_image_scores():
    image_scores = {}
    
    if os.path.exists(PATH_TO_JSON):
        try:
            with open(PATH_TO_JSON, "r") as file:
                image_scores = json.load(file)
        except Exception as e:
            print(f"Error loading image scores: {e}")
    
    return image_scores
    

def save_image_scores(image_scores):
    try:
        with open(PATH_TO_JSON, "w") as file:
            json.dump(image_scores, file)
    except Exception as e:
        print(f"Error saving image scores: {e}")


def get_sorted_images():
    try:
        with open(PATH_TO_JSON, "r") as file:
            image_scores = json.load(file)
    except FileNotFoundError:
        # Handle the case when the file is not found
        return []

    # Create a list of tuples (image_path, score)
    image_tuples = [(image_path, image_scores[image_path]) for image_path in image_scores]

    # Sort the list of tuples by score in descending order
    sorted_images = sorted(image_tuples, key=lambda x: x[1], reverse=True)

    # Extract only the image paths from the sorted list
    sorted_image_paths = [image_path for image_path, _ in sorted_images]

    return sorted_image_paths


# if there is no image_pool this makes one
def write_image_json():
    # Check if the image scores file exists
    if not os.path.exists(PATH_TO_JSON):
        # If not, create the folder and file
        try:
            os.makedirs(os.path.join(DATABASE_DIR, selected_folder))
            with open(PATH_TO_JSON, "w") as file:
                # You can initialize the JSON file with an empty dictionary or any default data
                json.dump({}, file)
        except Exception as e:
            print(f"file: {e}")