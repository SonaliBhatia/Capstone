# Speech Accent Recognition
## Executive Summary

This project was about recognizing and classifying user accent using user's speech in audio files and classify them into 3 categories American , Chinese and Indian. Data was collected from Kaggle and GMU's Speech accent archive. Different models used for classification are SVM and CNN. Both the models achieved accuracy of over 60%.

## Problem Statement
People from different parts of the world speak in different accent and hence it is difficult for AI enabled devices like  Alexa , Google home or even Self Driving cars to understand user commands. 
This project aims to recognize and classify speaker accents by AI enabled devices.

## Repository Structure: 

Capstone
|--code
  |--01_WebScrapping_Audio_Data.ipynb
  |--02_Initial_EDA_for_Data.ipynb
  |--03_Audio_EDA.ipynb
  |--04_Audio_Feature_Extraction_MFCC_And_SVMModel.ipynb
  |--05_CNN.ipynb
  |--06_CNN_With_Balancing_Technique_SMOTE.ipynb
  |--07_CNN_With_Undersampling.ipynb
|--Data
  |--archive-2  
|--images
|--Capstone_Presentation.pdf

## Brief description on analysis
  After downloading and scraping sufficient data, below steps were followed for analysis.
  1) Did initial EDA on audio data using #librosa
  2) Extract audio features(MFCC) from audio file for modeling
  3) Try different models for classification. 
  4) Predict accent for a single audio file using trained model.

# Audio EDA 
  # Audio Waveplot
    ![](http://localhost:8888/view/Capstone/images/audio_waveplot.png)

  # Spectogram 
      ![](http://localhost:8888/view/Capstone/images/spectogram.png)
      
  # MFCC 
    ![](http://localhost:8888/view/Capstone/images/MFCC.png)

  ## Models used

  Feed Forward Neural Network – to check baseline
    1) Simple Vector Machine – LinearSVC
    2) Adaboost with DecisionTreeClassifier
    3) Convolutional Neural Network (CNN) with regularization
    4) CNN with SMOTE 
    5) CNN with Undersampling

  Results :

  
 | Train Accuracy               | Test Accuracy | Predictability  (Y/N) |
 |------------------------------| --------------| ----------------------|
 |SVM    68 %                   |      63 %     |         Y             |
 |CNN with SMOTE 62 %           |      63 %     |         Y             |
 |CNN with Regularization 63 %  |      61 %     |         N             |


   ## Conclusion 

--SVM is best performing model - good accuracy and optimal precision and recall for all classes.
--After using balancing technique SMOTE , precision and recall gets better, and CNN can predict all    classes with slight compromise on accuracy.
--Data is insufficient and imbalanced.
--Due to imbalanced data CNN gives biased results and does not predict 1 class at all.


