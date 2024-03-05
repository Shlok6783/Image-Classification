import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input

# Define parameters
img_width, img_height = 224, 224  # ResNet50 input size
input_shape = (img_width, img_height, 3)
batch_size = 128
epochs = 10
num_classes = 5

# Define data generators for train and validation sets
train_data_dir = 'train_data'

train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)  # 20% of the data will be used for validation

# test_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=True,
    subset='training'
)  # This is for training set
classes = train_generator.classes
print(classes)
validation_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)  # This is for validation set

# Load pre-trained ResNet50 model without top (fully connected) layers
resnet_base = ResNet50(weights='imagenet', include_top=False, input_shape=input_shape)

# Freeze the ResNet50 layers
for layer in resnet_base.layers:
    layer.trainable = False

# Add custom classifier layers on top of ResNet50
x = layers.Flatten()(resnet_base.output)
x = layers.Dense(512, activation='relu')(x)
x = layers.Dropout(0.5)(x)
output = layers.Dense(num_classes, activation='softmax')(x)

# Define the model
model = models.Model(inputs=resnet_base.input, outputs=output)

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Define a callback to save the best model during training
checkpoint_filepath = 'best_modelwnoa.h5'
model_checkpoint_callback = ModelCheckpoint(
    filepath=checkpoint_filepath,
    save_best_only=True,  # Save only the best model
    monitor='val_loss',  # Monitor validation loss
    mode='min',  # Save the model when validation loss decreases
    verbose=1
)

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size,
    callbacks=[model_checkpoint_callback]  # Use the callback to save the best model
)

# Save the final model
model.save('final_modelwnoa.h5')
