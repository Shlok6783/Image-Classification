import pandas as pd
from sklearn.model_selection import train_test_split
import shutil
import os

# Define your directory containing images
data_dir = 'classified_images'

# Initialize lists to store image paths and labels
image_paths = []
labels = []

# Iterate through each class directory
for class_name in os.listdir(data_dir):
    class_dir = os.path.join(data_dir, class_name)
    if os.path.isdir(class_dir):
        # Iterate through each image file in the class directory
        for image_name in os.listdir(class_dir):
            image_path = os.path.join(class_dir, image_name)
            # Append image path and corresponding label to the lists
            image_paths.append(image_path)
            labels.append(class_name)

# Display the number of images found
print("Total images:", len(image_paths))

# Example: Display the first few image paths and labels
for i in range(5):
    print("Image Path:", image_paths[i])
    print("Label:", labels[i])
    print()

# Load your data into a DataFrame or lists
data = pd.DataFrame({
    'image_path': image_paths,
    'label': labels
})

# Split the data into training and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Define directories for training and test data
train_dir = 'train_data'
test_dir = 'test_data'
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Move training images to the training directory
for index, row in train_data.iterrows():
    label_dir = os.path.join(train_dir, row['label'])
    os.makedirs(label_dir, exist_ok=True)
    shutil.copy(row['image_path'], label_dir)

# Move test images to the test directory
for index, row in test_data.iterrows():
    label_dir = os.path.join(test_dir, row['label'])
    os.makedirs(label_dir, exist_ok=True)
    shutil.copy(row['image_path'], label_dir)
