import os
import shutil
import random

source_folder = 'C:/Users/GOUTHAM REDDY/OneDrive/Desktop/BTP/live'
train_folder = 'C:/Users/GOUTHAM REDDY/OneDrive/Desktop/BTP/train/live'
validation_folder = 'C:/Users/GOUTHAM REDDY/OneDrive/Desktop/BTP/validation/live'
test_folder = 'C:/Users/GOUTHAM REDDY/OneDrive/Desktop/BTP/test/live'

num_train = 2160
num_validation = 1440
num_test = 3600

# Create the train, validation, and test folders if they don't exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(validation_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Get a list of all image files in the source folder
image_files = [file for file in os.listdir(source_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Create a permutation of indices for randomization
permuted_indices = random.sample(range(len(image_files)), len(image_files))

# Divide the permuted indices into train, validation, and test sets
train_indices = permuted_indices[:num_train]
validation_indices = permuted_indices[num_train:num_train + num_validation]
test_indices = permuted_indices[num_train + num_validation:num_train + num_validation + num_test]

def copy_images(indices, destination_folder):
    for idx, image_idx in enumerate(indices):
        image_name = image_files[image_idx]
        source_path = os.path.join(source_folder, image_name)
        destination_path = os.path.join(destination_folder, image_name)

        # Create the destination directory if it doesn't exist
        os.makedirs(destination_folder, exist_ok=True)
        
        # Copy the image
        shutil.copy(source_path, destination_path)

copy_images(train_indices, train_folder)
copy_images(validation_indices, validation_folder)
copy_images(test_indices, test_folder)

print(f"Copied {len(train_indices)} images to {train_folder}.")
print(f"Copied {len(validation_indices)} images to {validation_folder}.")
print(f"Copied {len(test_indices)} images to {test_folder}.")
