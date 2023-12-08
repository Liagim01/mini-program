'''
Classifier class
'''
import tensorflow as tf
from tensorflow import keras
import numpy as np
from sklearn.model_selection import train_test_split
import sys
class Classifier:
    def __init__(self):
        self.model = self.build_model()
    def build_model(self):
        # Build and compile the model
        model = keras.Sequential([
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
        return model
    def classify(self, data):
        # Perform classification
        X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2)
        self.model.fit(X_train, y_train, epochs=10)
        predictions = self.model.predict(X_test)
        return predictions