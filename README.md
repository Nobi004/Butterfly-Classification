# Butterfly-Classification
#  1. Introduction
## 1.1 Background
Butterflies play a crucial role in ecosystems, particularly in pollination, that maintains plant reproduction and food. Their diversity and abundance are critical indicators of the health of ecosystems since they are very sensitive to environmental changes. Species identification of butterflies, however, is a tedious and challenging task because there are detailed and similar patterns of wings on different species and great intra-class variation due to factors like environment and level of development. This makes the process of identification greatly dependent on professional knowledge, which may not be readily available all the time.

## 1.2 Problem Statement
This project suggests automating the species recognition of butterflies by deep learning techniques, specifically Convolutional Neural Networks (CNNs). The idea is to create an automated system that can classify butterfly images into 75 species correctly. By automating this, we can overcome the constraints imposed by hand identification and render it more efficient and public-friendly, as well as accessible to conservationists and researchers.

##  1.3 Objectives
 - Train a deep learning model to recognize images of butterflies into 75 species.
 - Enhance model performance through transfer learning from pre-trained CNN models and data augmentation techniques.
 - Host the trained model as a web-based application for the identification of real-time butterfly species from uploaded images.

## 1.4 Significance
Butterfly species identification automation has enormous potential for the conservation of biodiversity. By providing a quick, scalable method of species identification, this system can assist researchers and conservationists in tracking and monitoring butterfly populations, especially rare and endangered species. Furthermore, the project encourages citizen science through enabling the public to participate in biodiversity tracking, allowing data collection from different localities. Furthermore, this device can be utilized as an automatic research tool for ecological and entomological studies to collect scale data and perform analysis.

# 2. Literature Review
## 2.1 Traditional Approaches
Traditionally, the identification of butterfly species has been performed manually by taxonomists based on visual inspection of physical samples or images. Identification involves the detection of characteristic features such as wing patterns, colors, and size. It is not only a time-consumption process but also requires specialized knowledge, hence being inconvenient when applied to large data sets or in real-time. Additionally, species determination is also complicated by species that look very similar and share overlapping patterns and significant intra-class variation due to environmental factors such as light and developmental stages.

##  2.2 Deep Learning in Image Classification
In the recent years, deep learning techniques, especially Convolutional Neural Networks (CNNs), have been the benchmark for image classification. CNNs can learn hierarchical features from raw pixel data without the need for prior feature engineering, making them well-suited to handle complex tasks like species recognition. Pre-trained models such as ResNet, VGG, and EfficientNet have been heavily used to augment the accuracy of classification, especially after fine-tuning for the task at hand. Transfer learning, using such pretrained models and adapting them on new tasks, has been particularly effective at bringing about performance enhancements, particularly on small training sets. Data augmentation techniques such as rotation, flip, and changes in brightness also help in augmenting model resistance and preventing overfitting through artificially enhancing the diversity of training sets.

## 2.3 Existing Research
Several research studies have applied deep learning techniques for insect and butterfly identification. For example, CNN-based models have been used to classify butterfly species with accuracies ranging from 85% to 90%. One study was able to obtain an accuracy of 88% using a model built from 20,000 images of butterflies. However, the majority of these models lack class diversity to be applied in real-world contexts or are limited to a particular region and are hence less generalizable. The majority of existing models have also not been fully deployed in real-world contexts, which limits their access to researchers and the general public. This project aims to address these shortcomings by creating a model that can classify a wide variety of butterfly species and can be deployed as an accessible tool for researchers and the public at large.

# 3. Dataset & Preprocessing
## 3.1 Dataset Overview
The data set for the project consists of over 1000 labeled images of 75 butterfly species. The images are species-labeled and stored in a directory structure that can be loaded to train. The data set is split into a test set and a training set. The Training_set.csv contains the file names of the images and their corresponding species labels. The Testing_set.csv contains the names of image files which are not labeled and are to be predicted by the model. The training set contains the labeled images to train the model, while the testing set is used to test the model's performance after training.

##  3.2 Preprocessing Steps
To train the images, certain preprocessing tasks are performed:

 - **Image Resizing:** Images are resized to a uniform size of 224x224 pixels to ensure symmetry when fed into the model.
 - **Normalization:** The pixel value is normalized between [0, 1] by dividing all pixel values by 255. This ensures uniformity so that the model can learn with ease from input data.
 - **Data Augmentation:** To improve dataset diversity and prevent overfitting, the following augmentation methods are employed:
    - **Rotation:** Random ±20° rotation.
    - **Flipping:** Images horizontally flipped.
    - **Adjustments for Brightness:** Random brightness adjustment in images.
    - **Synthetic Data Generation:** For less-representative species, synthetic images are generated using the above-discussed augmentation techniques to balance the dataset.
 
These preprocessing steps help in improving model resilience by providing a more diverse input of images and ensuring that the network is not biased towards any specific class or feature.

##  3.3 Exploratory Data Analysis
Prior to training the model, exploratory data analysis (EDA) is conducted to gain a better insight into the dataset:
 - **Class Distribution Visualization:** A bar plot is created to display the distribution of the various species in the dataset. This enables us to detect any imbalance in the number of images per species.
 - **Sample Image Grid:** A sample image grid is presented to display representative images of different species such that it can be seen how appearance differs within and between species.
 - **Outlier Detection:** Defective images and images that are not in input requirement format are rejected for data quality assurance purposes. Additionally, any outliers, for example, images that are too dark or distorted, will be identified and removed from the data set.
