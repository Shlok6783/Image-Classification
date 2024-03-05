## Scientific Image Classifier (Deep Learning Approach)

### Dataset Source:
The dataset used for this project is sourced from [BioFors](https://github.com/vimal-isi-edu/BioFors). It comprises images belonging to four classes: BlotGel, FAC, Macroscopy, and Microscopy. Additionally, a Noneoftheabove category was added for images not belonging to any of the four primary categories.

### Dependencies/ Packages Required for Training the Model:
Ensure you have the following dependencies/libraries/models preinstalled:
```
pip install numpy tensorflow keras matplotlib opencv-python scikit-learn seaborn
```

### Prerequisites for Project Locally:
Ensure you have the following dependencies/libraries/models preinstalled:
```
pip install Flask
pip install tensorflow
```

### Running the Project Locally:
To view the frontend and backend and test the working model, download this GitHub repository and run the following command in the terminal opened in the repository folder:
```
python main.py
```

### Description of Work Done:
1. **Data Mapping**: Utilized the `classification.json` file to get structured folder which is used for labeling the dataset for the application of Deep Learning algorithms. Check the file `transfer.py` for this mapping code.

2. **Data Split**: The labeled data was split into training, validation, and test sets in a 65:15:20 ratio for the first ResNet50 model. Augmentation was performed using Keras ImageDataGenerator.

3. **Transfer Learning**: Employed the ResNet50 transfer learning model for training on the training data and validating using the validation data. Model checkpoints were saved to preserve the best model based on maximum validation accuracy.

4. **Custom CNN Model**: Additionally, attempted to build a CNN model from scratch to potentially improve accuracy. Oversampling was applied to under-sampled classes, and basic CNN architecture was employed with specified hyperparameters. The CNN model architecture consisted of convolutional layers, max-pooling layers, flatten layer, fully connected layers with ReLU activation and L2 regularization, and a softmax activation in the output layer. The train, validation and test split was changed to 70:15:15 as well.

Feel free to explore the repository for more details and code implementation.
