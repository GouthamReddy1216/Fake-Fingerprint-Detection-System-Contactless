import cv2
import os
from PIL import Image
def find_red_box(image_path,box_color_rgb):
    """
    Find the red box (rectangle) in the image using color-based segmentation.

    Parameters:
        image_path (str): Path to the input image.
        box_color_rgb (tuple): Tuple containing the RGB values of the box border color.

    Returns:
        tuple: Tuple containing the top-left and bottom-right coordinates of the red box.
    """
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to RGB (to match the given box_color_rgb)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the tolerance for the color matching (adjust as needed)
    tolerance = 50

    # Create a mask for the box border color using color matching
    lower_color = (box_color_rgb[0] - tolerance, box_color_rgb[1] - tolerance, box_color_rgb[2] - tolerance)
    upper_color = (box_color_rgb[0] + tolerance, box_color_rgb[1] + tolerance, box_color_rgb[2] + tolerance)

    mask = cv2.inRange(image_rgb, lower_color, upper_color)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the largest area (assumed to be the red box)
    max_area = 0
    max_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour

    # Get the bounding box of the contour (rectangle)
    x, y, w, h = cv2.boundingRect(max_contour)

    # Calculate the top-left and bottom-right coordinates of the red box
    top_left = (x, y)
    bottom_right = (x + w, y + h)

    return top_left, bottom_right


def crop_image_by_rectangle(image_path, top_left, bottom_right, output_path):
    """
    Crop the area inside the rectangle defined by the top-left and bottom-right coordinates.

    Parameters:
        image_path (str): Path to the input image.
        top_left (tuple): Tuple containing the (x, y) coordinates of the top-left corner of the rectangle.
        bottom_right (tuple): Tuple containing the (x, y) coordinates of the bottom-right corner of the rectangle.
        output_path (str): Path to save the cropped image.

    Returns:
        None
    """
    # Read the image
    image = cv2.imread(image_path)

    # Calculate the coordinates for cropping inside the box (without border)
    x1, y1 = top_left
    x2, y2 = bottom_right

    # Crop the area inside the rectangle (without the border)
    cropped_image = image[y1+22:y2-5, x1+5:x2-5]  # Adjusted the cropping coordinates

    # Save the cropped image
    cv2.imwrite(output_path, cropped_image)

# Rest of the code (find_red_box function and example usage) remains the same as provided earlier.


# Rest of the code (crop_image_by_rectangle function and example usage) remains the same as provided earlier.



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
                    box_color_rgb = (243, 64, 53)
                    output_image_path = os.path.join(output_subfolder,file_name)
                    top_left_corner, bottom_right_corner = find_red_box(input_image_path,box_color_rgb)

                    crop_image_by_rectangle(input_image_path, top_left_corner, bottom_right_corner, output_image_path)

if __name__ == "__main__":
    main_directory = 'C:/Users/GOUTHAM REDDY/Desktop/YOLO_ZJU_Segmentation/runs/detect'
    output_directory ='C:/Users/GOUTHAM REDDY/Desktop/YOLO_ZJU_Segementation/segemented'
    
    process_and_save_images(main_directory, output_directory)

