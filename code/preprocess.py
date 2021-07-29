import numpy as np
import tensorflow as tf
import os
from PIL import ImageOps, Image

def get_data():
    with open('..\stanford-background-dataset\marked_images_labels.txt') as f:
        labels = np.array([int(x) for x in (f.readlines())[0]]) #splits all labels, turns into ints

    image_location = '..\stanford-background-dataset\marked_images' #location for images with pasted symbol

    #image_dims = (200, 200)
    images = []
    for path, subdirs, files in os.walk(image_location):
        for filename in files:
            img = Image.open(image_location + '/' + filename)
            img = img.convert('RGB')
            img = np.array(img, dtype=np.float32)
            img /= 255.0
            #print("image shape", img.shape) #(200, 200, 3)
            images.append(img)
    images = np.array(images)

    #labels = tf.one_hot(labels, 2)
    #print(labels)
    
    print("images shape: ", images.shape)
    print("labels shape: ", labels.shape)

    #shuffle images and labels together
    shuffle_list = list(zip(images, labels))
    np.random.shuffle(shuffle_list)
    images, labels = zip(*shuffle_list)

    return (np.array(images), np.array(labels))

def main():
    get_data()

if __name__ == '__main__':
    main()
