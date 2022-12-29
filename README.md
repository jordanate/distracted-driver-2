# Distracted Driver Detection Using Convolutional Neural Networks

![images/distracted-driver-photo.png](https://github.com/jordanate/distracted-driver-detection/blob/main/images/distracted-driver-photo.png)

### Deployed Model

**By:** Jordana Tepper

## Overview

This project utilizes a dataset containing numerous images of various driving behaviors to perform image classification. The goal of this project is to build a model that can detect distracted driving tendencies and aid State Farm in implementing a new program that tracks drivers' behaviors through the use of a dashboard camera (with permission). Using the information collected by the dashcam, State Farm would offer their clients an insurance quote based on the respective driver's actions at the wheel (safer driving leads to a lower quote, and distracted driving leads to a higher quote). State Farm hopes that this new program can incentivize its clients to practice safer driving and consequently improve road safety.

Through the use of Convolutional Neural Networks (CNNs) and transfer learning, I produced 10 different models to eventually achieve the best accuracy score: 88.17%.

## Business Understanding

### What is Distracted Driving?

There are three main types of distracted driving:

**Visual:** taking your eyes off the road   
**Manual:** taking your hands off the wheel   
**Cognitive:** taking your mind off driving   

### Why is Distracted Driving a Problem?

According to [CDC data](https://www.cdc.gov/transportationsafety/distracted_driving/index.html#:~:text=Nine%20people%20in%20the%20United,to%20involve%20a%20distracted%20driver.&text=Distracted%20driving%20is%20doing%20another,of%20a%20motor%20vehicle%20crash.) from 2019, approximately 3,142 people were killed, and 424,000 people were injured from a car crash involving a distracted driver in the United States that year. This translates to 9 people per day being killed due to distracted driving. Furthermore, of the people killed in distracted driving accidents, 1 in 5 of these individuals were not in vehicles (i.e., walking, biking, etc.) 

### What can be done to help reduce Distracted Driving?

Due to the ongoing problem of distracted driving, State Farm has proposed the idea of offering clients the option of being recorded while driving to track their behavior at the wheel. This would be done through the means of a dashboard camera that would continuously take pictures of the driver and classify their actions according to 10 categories:   
  * safe driving   
  * texting with their right hand   
  * talking on the phone with their right hand   
  * texting with their left hand   
  * talking on the phone with their left hand  
  * operating the radio    
  * drinking a beverage   
  * reaching behind  
  * fixing hair and/or makeup  
  * talking to a passenger   

After two months of observation and a report produced by the dashcam, State Farm would then offer the client an insurance quote based on their driving tendencies. In other words, safer driving would result in paying less money for insurance, whereas unsafe driving would result in a higher quote. Hopefully, such an incentive could lead to individuals practicing safer driving habits - benefiting both them and the greater population.

## Data Understanding

The data that I used for this project comes from a dataset from [Kaggle](https://www.kaggle.com/c/state-farm-distracted-driver-detection) titled "State Farm Distracted Driver Detection."

The dataset consists of 22,424 photos belonging to 10 classes. I split each class into train and validation groupings, with 80% of the images in the train data and 20% in the validation data.

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
* The images are from a single angle, so in practice, the State Farm dashcam would need to be positioned the same way

### Next Steps
* Obtain a greater amount of labeled test data
* Build the model based on images from various angles
* Analyze a potential relationship between the use of a dashcam and improvements in driving behaviors

## For More Information

For a full analysis, please look at my [Jupyter Notebook](./distracted-driver-detection.ipynb)

For a more concise summary, please review my [presentation](https://github.com/jordanate/distracted-driver-detection/blob/main/presentation.pdf).

For any additional questions, please contact Jordana Tepper at <a href="mailto:jtepper724@gmail.com">jtepper724@gmail.com</a> 

## Repository Structure
```
├── images
├── models
├──.gitattributes
├──.gitignore
├── .jovianrc
├── README.md
├── distracted-driver-detection.ipynb
├── model.py
├── presentation.pdf
└── requirements.txt

```
