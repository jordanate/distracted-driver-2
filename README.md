# Distracted Driver Detection Using Convolutional Neural Networks

![images/distracted-driver-photo.png](https://github.com/jordanate/distracted-driver-detection/blob/main/images/distracted-driver-photo.png)

### Deployed Model

**By:** Jordana Tepper

## Overview


## Business Problem


## Data Understanding

The data that I used for this project comes from a dataset from Kaggle titled "State Farm Distracted Driver Detection."

The dataset consists of 22,424 photos belonging to 10 classes. I split each class into train and validation groupings with 80% of the images in the train data and 20% in the validation data.

Regarding the test data, the data source provided a folder of 79,388 unlabeled images. After going through many of these images, I manually labeled 338 of them, with each class containing 33 test photos, on average.

A critical component of this project is that no driver appeared in both the train/validation data and the test data. This was done to prevent the model from learning the drivers' faces as opposed to the drivers' actions.

**The 10 classes are as follows:**

**c0 = SAFE DRIVING   
c1 = TEXTING WITH RIGHT HAND   
c2 = TALKING ON THE PHONE WITH RIGHT HAND   
c3 = TEXTING WITH LEFT HAND   
c4 = TALKING ON THE PHONE WITH LEFT HAND  
c5 = OPERATING THE RADIO  
c6 = DRINKING A BEVERAGE  
c7 = REACHING BEHIND  
c8 = HAIR AND MAKEUP  
c9 = TALKING TO PASSENGER**

![sample_images.png](https://github.com/jordanate/distracted-driver-detection/blob/main/images/sample_images.png)

## Data Analysis

### Visualizing Class Sizes

![class_size.png](https://github.com/jordanate/distracted-driver-detection/blob/main/images/class_size.png)

The dataset is quite large and the classes are relatively balanced, so no data augmentation is needed.

## Modeling

## Evaluation

After reviewing the test accuracy for each model, the final model for my project is Model 9. It has a test accuracy of 88.17%, which was achieved by using VGG16, a pre-trained model, with all but the last 9 layers frozen.

### Final Model Confusion Matrix

<p align = 'center'>
  <img width = '730' height = '550' src="https://github.com/jordanate/distracted-driver-detection/blob/main/images/model9_cm.png"> 
</p>

### Final Model Accuracy Graph

<p align = 'center'>
  <img width = '730' height = '550' src="https://github.com/jordanate/distracted-driver-detection/blob/main/images/model9_acc.png"> 
</p>

### Final Model Loss Graph

<p align = 'center'>
  <img width = '730' height = '550' src="https://github.com/jordanate/distracted-driver-detection/blob/main/images/model9_loss.png"> 
</p>

## Conclusions

### Limitations
* The test images had to be manually labeled, and as a result, the size of the test data is small
* The images are from a single angle, so in practice, the State Farm DashCam would need to be positioned the same way

### Next Steps
* Obtain a greater amount of labeled test data
* Build the model based on images from various angles
* Analyze a potential relationship between the use of a DashCam and improvements in driving behaviors

## For More Information

For a full analysis, please look at my [Jupyter Notebook](./distracted-driver-detection.ipynb)

For a more concise summary, please review my [presentation]().

For any additional questions, please contact Jordana Tepper at <a href="mailto:jtepper724@gmail.com">jtepper724@gmail.com</a> 

## Repository Structure
```
├── images
├── .gitignore
├── .jovianrc
├── README.md
├── distracted-driver-detection.ipynb
├── model.py
├── presentation.pdf
└── requirements.txt

```
