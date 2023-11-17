# viewer.py

from imageLoadReadWrite import load_image_scores, get_sorted_images


def get_highest_rated_image():
    image_scores = load_image_scores()
    highest_rated_image = max(image_scores, key=image_scores.get, default=None)
    return highest_rated_image


def get_next_highest_rated_image(currentImage):
    sorted_images = get_sorted_images()
    if currentImage in sorted_images:
        index = sorted_images.index(currentImage)
        if index + 1 < len(sorted_images):
            return sorted_images[index + 1]
        else:
            return None


def get_previous_highest_rated_image(currentImage):
    sorted_images = get_sorted_images()
    if currentImage in sorted_images:
        index = sorted_images.index(currentImage)
        if index - 1 >= 0:
            return sorted_images[index - 1]
    return None