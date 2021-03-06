# BVC-starter-project : CNN Binary Classifier

In this project, I used a convolutional nerual net to detect the presence of an International Symbol of Access (ISA) within an image. This project allowed me to revisit a model that I had studied before in classes that can take some fine tuning to get to optimal performance, as well as practice gathering and cleaning data. 

# Usage
To run this project, download the dataset below. Then run the following commands in a terminal:
```
python image-set-generator.py
python preprocess.py
python cnn-model.py
```
To run gradCAM Implementation, create the model with the commands above then use the following:
```
python gradcam-implementation.py
```
# Data

The dataset used is the Stanford Background Dataset, and it consists of 715 images of outdoor scenes. These images served as random backgorunds, to which I applied the ISA to at random in 'image-set-generator.py'. I also cropped the images, and placed the ISA at random positions in the image. This resulted in a dataset where about half of the images contained the sign. I chose this dataset and the International Symbol of Access to create a project that resembles what I hope to do in CS, which is to use machine learning to help others and benefit humanity. 

The link to download the dataset: https://www.kaggle.com/balraj98/stanford-background-dataset

Some example photos:
![4100246](https://user-images.githubusercontent.com/44532574/127711506-c77a4af5-ff5e-4188-8775-d3a3c24ba90c.jpg)
![5000131](https://user-images.githubusercontent.com/44532574/127711512-2ed9ff63-4ace-4c38-bfe2-880d5c6ac77a.jpg)
![6000049](https://user-images.githubusercontent.com/44532574/127711561-b348033d-c363-494e-a9f1-6c87e53befdb.jpg)

# Architecture

The CNN architecure went through many iterations as I grappled with the model overfitting to the relatively small amount of data I had, and the model not training at all. In its current iteration, the model uses Keras' Sequental model class with four 2D Convolution layers, four 2D Max Pooling layers, a Flatten layer, and two Dense layers with the final one using sigmoid activation, while all others use RELU. 

![image](https://user-images.githubusercontent.com/44532574/127577498-10d8de61-1d05-418d-8727-9b99850025de.png)

# Results
The final architecture results in the model reaching up to 100% training accuracy, and 95% validation accuracy. On some iterations, this model will not train as well, so there can be some variation in the results.

![epoch_10](https://user-images.githubusercontent.com/44532574/127577735-88a69230-4b0a-4a9b-b550-086145ccc730.png)

To gain a deeper understand as to how the model was classifying the images, I implemented GradCAM based on Adrian Rosebrock's similar implementation. The results show the model correctly identifying where in the image the International Symbol of Access is. In the examples below, the first image is the original, followed by the heatmap, then a text bar indicating the Truth (T), and Prediction from the model (P), if there is a sign present. At the bottom is the image with the heatmap overlayed to show that they do indeed line up. 
![sign_ex1](https://user-images.githubusercontent.com/44532574/130299097-e1603bdb-491c-4673-bdef-320b3d0c1f9e.png)
![no_sign_ex2](https://user-images.githubusercontent.com/44532574/130299497-0fd7230b-47f0-4127-a84f-9c3963b2bb8a.png)
![sign_ex2](https://user-images.githubusercontent.com/44532574/130299505-01d8c285-d0c4-4e5b-aed7-a4465a817f4f.png)

# Potential Future Steps
There are several improvements I can see for this model. For example, a larger dataset would provide more insight to the viability of this model on a larger scale, as the dataset of 715 images only tells us so much about what the model can do. Also, the model only trains on images where the sign appears facing the camera, unobstructed. A more difficult but realistic dataset with obstructions, light changes, and transformed signs would challenge this model and be more useful. Beyond the scale of this project, identifying an International Symbol of Access is just one of the many tasks a deep learning model such as this one would need to help the people who need it. 

# References

S. Gould, R. Fulton, D. Koller. Decomposing a Scene into Geometric and Semantically Consistent Regions. 
Proceedings International Conference on Computer Vision (ICCV), 2009. [pdf]
