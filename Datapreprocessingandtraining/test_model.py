from sklearn.metrics import classification_report
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np

validation_data_dir = 'test_data'
img_width, img_height = 224, 224
batch_size = 128

test_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)

# Define test generator
test_generator = test_datagen.flow_from_directory(
    validation_data_dir,  # or wherever your test data is located
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False
)

model = tf.keras.models.load_model('best_modelwnoa.h5')
# Evaluate the model on the test set
scores = model.evaluate_generator(test_generator)
print("Test Loss:", scores[0])
print("Test Accuracy:", scores[1])

# Predict the classes using the model
y_pred = model.predict_generator(test_generator)
y_pred_classes = np.argmax(y_pred, axis=1)

# Get true labels
true_classes = test_generator.classes

# Get class labels
class_labels = list(test_generator.class_indices.keys())

# Generate and print classification report
print(classification_report(true_classes, y_pred_classes, target_names=class_labels))
