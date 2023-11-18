# viewer.py

from imageLoadReadWrite import load_image_scores


# this gets all rated imges in image_pool.json, and puts there keys(the png names) in descending order a list, set as a global so other functions in this file can call it
def sort_images():
    image_scores = load_image_scores()
    sorted_dict_desc = dict(sorted(image_scores.items(), key=lambda item: item[1], reverse=True))
    global sorted_images_list
    sorted_images_list = list(sorted_dict_desc.keys())
    print(sorted_images_list)


# This just gets the first img for the viewr page, it would be the Highest rated, so we just get index 0 of sorted_images_list
def get_first_image():
    global sorted_images_list_cur_index
    
    if len(sorted_images_list) > 0:
        sorted_images_list_cur_index = 0
        return sorted_images_list[0]


# This usees a global index (sorted_images_list_cur_index) and it is in sorted_images_list, and then Increments in the list for one in returns the item(png name) For that index
def get_next_image():
    global sorted_images_list_cur_index

    if sorted_images_list_cur_index < len(sorted_images_list) - 1:
        sorted_images_list_cur_index += 1
        print(sorted_images_list_cur_index)
        return sorted_images_list[sorted_images_list_cur_index]
    else:
        sorted_images_list_cur_index = 0
        return sorted_images_list[sorted_images_list_cur_index]


# This usees a global index (sorted_images_list_cur_index) and it is in sorted_images_list, and then Increments in the list for one in returns the item(png name) For that index
def get_previous_image():
    global sorted_images_list_cur_index

    if sorted_images_list_cur_index > 0:
        sorted_images_list_cur_index -= 1
        return sorted_images_list[sorted_images_list_cur_index]
    else:
        sorted_images_list_cur_index = len(sorted_images_list) - 1
        return sorted_images_list[sorted_images_list_cur_index]
