import os
import cv2
from PIL import Image

def convert_to_grayscale(input_image_path, output_image_path):
    try:
        # Open the input image using Pillow
        image = Image.open(input_image_path)
        
        # Convert the image to grayscale
        grayscale_image = image.convert("L")
        
        # Save the grayscale image to the specified output path
        grayscale_image.save(output_image_path)
        print("Grayscale image saved to:", output_image_path)
        
        # Close the images
        image.close()
        grayscale_image.close()
    except Exception as e:
        print("Error:", e)


def process_and_save_images(main_folder, output_folder):
    for folder_name in os.listdir(main_folder):
        folder_path = os.path.join(main_folder, folder_name)
        if os.path.isdir(folder_path):
            output_subfolder = os.path.join(output_folder, folder_name)
            os.makedirs(output_subfolder, exist_ok=True)  # Create output subfolder if it doesn't exist
            
            print("Processing folder:", folder_path)
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    input_image_path = file_path
                    output_image_path = os.path.join(output_subfolder,file_name)
                    convert_to_grayscale(input_image_path,output_image_path)

if __name__ == "__main__":
    main_directory = 'C:/Users/GOUTHAM REDDY/Desktop/YOLO_ZJU_Segmentation/segmented'
    output_directory ='C:/Users/GOUTHAM REDDY/Desktop/YOLO_ZJU_Segmentation/grayscale'
    
    process_and_save_images(main_directory, output_directory)
