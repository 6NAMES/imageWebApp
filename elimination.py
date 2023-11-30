# elimination.py

from imageLoadReadWrite import BASE_DIR, PATH_TO_STATIC
import os
import json


def delete_image(image_name, PATH_TO_JSON, CURRENT_IMAGE_FOLDER):
    json_path = os.path.join(PATH_TO_JSON)
    image_path = os.path.join(BASE_DIR, PATH_TO_STATIC, CURRENT_IMAGE_FOLDER, image_name)
    key_to_delete = image_name

    # Check if the image file exists
    if os.path.exists(image_path):
        # Remove the image file
        os.remove(image_path)

    # Read the JSON file
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)

    if key_to_delete in data:
        del data[key_to_delete]

        # Write the updated data back to the JSON file
        with open(json_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        print(f'Key {key_to_delete} not found in the JSON file.')

    

    
