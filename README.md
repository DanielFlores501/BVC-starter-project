# BVC-starter-project : CNN Binary Classifier

In this project, I used a convolutional nerual net to detect the presence of an International Symbol of Access (ISA) within an image. This project allowed me to revisit a model that I had studied before in classes that can take some fine tuning to get to optimal performance, as well as practice gathering and cleaning data. 

# Data

The dataset used is the Stanford Background Dataset, and it consists of 715 images of outdoor scenes. These images served as random backgorunds, to which I applied the ISA to at random in 'image-set-generator.py'. I also cropped the images, and placed the ISA at random positions in the image. This resulted in a dataset where about half of the images contained the sign. I chose this dataset and the International Symbol of Access to create a project that resembles what I hope to do in CS, which is to use machine learning to help others and benefit humanity. 

The link to download the dataset: https://www.kaggle.com/balraj98/stanford-background-dataset

# Architecture

The CNN architecure went through many iterations as I grappled with the model overfitting to the relatively small amount of data I had, and the model not training at all. In its current iteration, the model uses Keras' Sequental model class with four 2D Convolution layers, four 2D Max Pooling layers, a Flatten layer, and two Dense layers with the final one using sigmoid activation, while all others use RELU. 

![image](https://user-images.githubusercontent.com/44532574/127577498-10d8de61-1d05-418d-8727-9b99850025de.png)

# Results
The final architecture results in the model reaching up to 100% training accuracy, and 95% validation accuracy. On some iterations, this model will not train as well, so there can be some variation in the results.

![epoch_10](https://user-images.githubusercontent.com/44532574/127577735-88a69230-4b0a-4a9b-b550-086145ccc730.png)


# Potential Future Steps
There are several improvements I can see for this model. For example, a larger dataset would provide more insight to the viability of this model on a larger scale, as the dataset of 715 images only tells us so much about what the model can do. Also, the model currently takes 7 - 9 epochs to reach 95% validation accuracy, so using pretrained weights or further tinkering with the model architecture could lead to better performance. And beyond the scale of this project, identifying an International Symbol of Access is just one of the many tasks a deep learning model such as this one would need to help the people who need it. 

# References

S. Gould, R. Fulton, D. Koller. Decomposing a Scene into Geometric and Semantically Consistent Regions. 
Proceedings International Conference on Computer Vision (ICCV), 2009. [pdf]
