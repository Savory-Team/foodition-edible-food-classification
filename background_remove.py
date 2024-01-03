import os
from rembg import remove
from PIL import Image

def remove_background(input_path, output_path):
    with open(input_path, "rb") as input_file:
        input_data = input_file.read()
        output_data = remove(input_data)
    
    with open(output_path, "wb") as output_file:
        output_file.write(output_data)

def process_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Initialize a counter for the number of backgrounds removed
    count = 0

  
    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)

        remove_background(input_path, output_path)
        count += 1
        print("Number of backgrounds removed:", count, end='\r')
    

if __name__ == "__main__":
    input_folder = 'D:\TITO\Documents\Deep-learning\FOODITION-FOOD-EDIBLE-CLASSIFICATION\dataset/rice-edible-notrm'
    output_folder = 'D:\TITO\Documents\Deep-learning\FOODITION-FOOD-EDIBLE-CLASSIFICATION\dataset/rice-edbile'

    process_images(input_folder, output_folder)
