import os
import random
import shutil

source_folder = 'C:/Users/GOUTHAM REDDY/OneDrive/Desktop/BTP/YOLO_ZJU_Segmentation/grayscale'
destination_folder = 'C:/Users/GOUTHAM REDDY/OneDrive/Desktop/BTP/live'
num_images_to_select = 7200

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Get a list of all image files in the source folder and its subfolders
image_files = []
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_files.append(os.path.join(root, file))

# Randomly select num_images_to_select images
selected_images = random.sample(image_files, min(num_images_to_select, len(image_files)))

# Copy the selected images to the destination folder with the desired naming
for idx, image_path in enumerate(selected_images):
    image_name = f"{str(idx+1).zfill(4)}_live.png"
    destination_path = os.path.join(destination_folder, image_name)
    shutil.copy(image_path, destination_path)

print(f"Selected {len(selected_images)} images and saved them in {destination_folder}.")
