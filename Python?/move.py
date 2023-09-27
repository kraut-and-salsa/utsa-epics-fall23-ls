import os
import shutil

# Replace this with your source folder path
source_folder = '/Users/lukasalcedo/Documents/Python?'

# Replace this with your destination base folder path
destination_base = '/Users/lukasalcedo/Documents/Python?'

# Number of destination folders
num_destination_folders = 5

# Create destination folders if they don't exist
for i in range(1, num_destination_folders + 1):
    dest_folder = os.path.join(destination_base, f'folder_{i}')
    os.makedirs(dest_folder, exist_ok=True)

# Get a list of all files in the source folder
file_list = os.listdir(source_folder)

# Filter out only the image files based on their extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']  # Add more if needed
image_files = [f for f in file_list if os.path.splitext(f)[1].lower() in image_extensions]

# Calculate the number of images per destination folder
images_per_folder = len(image_files) // num_destination_folders

# Distribute images to destination folders
for i in range(num_destination_folders):
    start_index = i * images_per_folder
    end_index = start_index + images_per_folder
    current_images = image_files[start_index:end_index]
    destination_folder = os.path.join(destination_base, f'folder_{i+1}')
    
    for image in current_images:
        source_path = os.path.join(source_folder, image)
        destination_path = os.path.join(destination_folder, image)
        shutil.move(source_path, destination_path)
        print(f"Moved: {image} -> {destination_path}")
