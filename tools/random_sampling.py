import os
import random

def delete_random_pictures(folder_path, min_count=500, max_count=550):
    # Get a list of all files in the folder
    all_files = os.listdir(folder_path)
    
    # Filter only files with common image extensions (you may need to modify this list)
    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    # Calculate the number of pictures to keep
    target_count = random.randint(min_count, max_count)
    
    # Check if the current count is already within the desired range
    current_count = len(image_files)
    if min_count <= current_count <= max_count:
        print(f"Already within the desired range ({min_count} - {max_count}). No pictures deleted.")
        return
    
    # Calculate the number of pictures to delete
    pictures_to_delete = max(current_count - target_count, 0)
    
    # Randomly select and delete pictures
    pictures_to_delete_list = random.sample(image_files, pictures_to_delete)
    
    for file_name in pictures_to_delete_list:
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    
    print(f"Remaining pictures count: {len(os.listdir(folder_path))}")

# Replace 'your_folder_path' with the path to your folder containing pictures
folder_path = 'D:\TITO\Documents\Deep-learning\FOODITION-FOOD-EDIBLE-CLASSIFICATION\dataset/mango-inedible'

delete_random_pictures(folder_path)
