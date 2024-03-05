import os
import json
import shutil

# Load classification mapping from JSON file
with open('classification.json') as f:
    classification_mapping = json.load(f)

# Define source and destination directories
source_dir = 'biofors_images'
destination_dir = 'classified_images'

# Create destination directories if they don't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# A dictionary to keep track of the count of files with the same name
file_counts = {}

# Iterate over each folder in the source directory
for folder_name in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder_name)
    if os.path.isdir(folder_path):
        # Iterate over each image in the folder
        for image_name in os.listdir(folder_path):
            # Get classification label from mapping
            classification_label = classification_mapping.get(folder_name, {}).get(image_name)
            if classification_label:
                # Create subfolder in destination directory if it doesn't exist
                subfolder_path = os.path.join(destination_dir, classification_label)
                if not os.path.exists(subfolder_path):
                    os.makedirs(subfolder_path)
                
                # Handle duplicate filenames
                file_count = file_counts.get(image_name, 0) + 1
                file_counts[image_name] = file_count
                filename, ext = os.path.splitext(image_name)
                new_filename = f"{filename}_{file_count}{ext}"
                
                # Move the image to the corresponding subfolder
                source_image_path = os.path.join(folder_path, image_name)
                destination_image_path = os.path.join(subfolder_path, new_filename)
                shutil.move(source_image_path, destination_image_path)