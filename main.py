from flask import Flask, render_template, request, jsonify
import os
from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the TensorFlow model
model = tf.keras.models.load_model('best_modelwnoa.h5')

# Function to preprocess the uploaded image
def preprocess_image(image_path, target_size=(224, 224)):
    img = image.load_img(image_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})
    
    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No image selected'})
    
    # Save the uploaded image
    image_path = os.path.join('uploads', image_file.filename)
    image_file.save(image_path)

    # Preprocess the image
    img = preprocess_image(image_path)

    # Make predictions
    predictions = model.predict(img)
    print(predictions)

    # Convert predictions to human-readable format
    class_names = ['Blogs', 'FACS', 'Macroscopy', 'Microscopy', 'Negative(none of the 4 classes)']
    predicted_class = class_names[np.argmax(predictions)]

    # Delete the uploaded image after processing
    os.remove(image_path)

    return render_template('index.html', result=predicted_class)

if __name__ == '__main__':
    app.run(debug=True)
