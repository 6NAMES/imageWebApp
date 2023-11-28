# elimination.py

from imageLoadReadWrite import load_image_scores

def get_bottom_10_percent_scores():
    # Load image scores
    image_scores = load_image_scores()

    # Sort images by score in ascending order
    sorted_images_by_score = sorted(image_scores.items(), key=lambda item: item[1])

    # Calculate the number of images in the bottom 10%
    num_images_bottom_10_percent = int(len(sorted_images_by_score) * 0.1)

    # Extract the names of images in the bottom 10%
    bottom_10_percent_images = [image for image, _ in sorted_images_by_score[:num_images_bottom_10_percent]]

    print(bottom_10_percent_images)
    return bottom_10_percent_images
    

# Implement the logic to delete the image in the delete_image_logic function
def delete_image_logic(image_to_delete):
    # Add your image deletion logic here
    print(image_to_delete)

