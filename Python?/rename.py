import os

# Replace this with your folder path LS
folder_path = '/Users/lukasalcedo/Documents/Python?'

# Get a list of all files in the folder
file_list = os.listdir(folder_path)

# Filter out only the image files based on their extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif']  # Add more if needed
image_files = [f for f in file_list if os.path.splitext(f)[1].lower() in image_extensions]

# Sort the image files to ensure sequential renaming
image_files.sort()

# Rename and sequentially number the image files
for index, old_name in enumerate(image_files, start=1):
    extension = os.path.splitext(old_name)[1]
    new_name = f"Luka_{index:03d}{extension}"
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed: {old_name} -> {new_name}")
