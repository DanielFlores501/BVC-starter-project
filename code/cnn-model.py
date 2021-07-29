from preprocess import get_data

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import \
    Conv2D, MaxPool2D, Dropout, Flatten, Dense

def build_model():
    #input num images, height, width, 3(rgb)
        model = Sequential()#add model layers
        model.add(Conv2D(16, (3,3), padding="same", activation='relu', input_shape=(200, 200, 3)))
        model.add(MaxPool2D(2, 2))

        model.add(Conv2D(32, (3,3), activation='relu'))
        model.add(MaxPool2D(2,2))

        model.add(Conv2D(64, (3,3), activation='relu'))
        model.add(MaxPool2D(2,2))
        
        model.add(Conv2D(64, (3,3), activation='relu'))
        model.add(MaxPool2D(2,2))
        
        model.add(Flatten())
        model.add(Dense(512, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))

        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        #model.compile(optimizer='adam', tf.keras.losses.SparseCategoricalCrossentropy()), metrics=['accuracy'])
        return model

def main():
        model = build_model()
        images, labels = get_data()
        print("images shape: ", images.shape) #(715, 120000)
        print("labels shape: ", labels.shape) #(715,)
        model.fit(images, labels, validation_split=0.3, epochs=10, shuffle='false')

if __name__ == '__main__':
    main()
