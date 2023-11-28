#voting.py

import random
from imageLoadReadWrite import load_image_pool, load_image_scores, save_image_scores


# Constants
DEFAULT_SCORE = 1000  # Default score assigned to images if no score is available
K_FACTOR = 20        # Weight factor determining the impact of each game on a png's score
RATING_DIFF_FACTOR = 500  # Factor controlling the sensitivity of the Elo rating system to score differences

# List to keep track of available image files
displayed_images = set()

def select_image_pair(image_pool):

    if len(image_pool) >= 2:
        # Select two random images from the pool
        image1 = random.choice(image_pool)
        image_pool.remove(image1)  # Remove the selected image from the pool
        image2 = random.choice(image_pool)
        image_pool.remove(image2)
        return image1, image2
    else:
        image_pool = load_image_pool()
        # Select two random images from the pool
        image1 = random.choice(image_pool)
        image_pool.remove(image1)  # Remove the selected image from the pool
        image2 = random.choice(image_pool)
        image_pool.remove(image2)
        return image1, image2


def get_score(image):
    image_scores = load_image_scores()
    return image_scores.get(image, DEFAULT_SCORE)



def update_image_scores(win_img, win_img_score, lose_img, lose_img_score):
    image_scores = load_image_scores()

    image_scores[win_img] = win_img_score
    image_scores[lose_img] = lose_img_score

    save_image_scores(image_scores)


def score_elo(win_img, lose_img):
    win_img_score = get_score(win_img)
    lose_img_score = get_score(lose_img)

    expected_win = 1 / (1 + 10 ** ((lose_img_score - win_img_score) / RATING_DIFF_FACTOR))
    expected_lose = 1 / (1 + 10 ** ((win_img_score - lose_img_score) / RATING_DIFF_FACTOR))

    win_img_score += K_FACTOR * (1 - expected_win)
    lose_img_score += K_FACTOR * (0 - expected_lose)

    update_image_scores(win_img, win_img_score, lose_img, lose_img_score)