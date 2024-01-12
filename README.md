# Introduction 👋

Hi everyone! Savory Hacker

| Nama | Email | Role | University | LinkedIn |
| ---      | ---       | ---       | ---       | ---       |
| Novebri Tito Ramadhani | novebritito@gmail.com | Hacker | Universitas Negeri Yogyakarta | [![text](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/novebri-tito-ramadhani/) |
| Aditya Bayu Aji | adityabayu861@gmail.com | Hacker | Universitas Muhammadiyah Cirebon | [![text](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/iniadittt/) |

# Project overview

This project aims to classify edible food or inedible food using deep learning techniques implemented with TensorFlow Keras. The goal is to create a robust multi-classification model that can accurately classify edible and inedible food.

## Model Architecture

The deep learning model is built using the TensorFlow Keras libraries. The architecture typically involves:

- Preprocessing the food images(convert to RGB, resize, convert to array)
- Define pre-trained model MobileNetV2 with input
- Creating a classifier layer and output layer
- combine pre-trained model with classifier layer and output layer with 15 neuron
- Compiling the model with an appropriate loss function and optimizer
- Training the model on the dataset

## Data split
![image](https://github.com/Savory-Team/foodition-edible-food-classification/assets/97221880/28c21ce9-df49-48bf-bf97-302487377af9)


## Training Result
### training and validation acccuracy graph
![image](https://github.com/Savory-Team/foodition-edible-food-classification/assets/97221880/67f9517e-24ba-4858-aa3b-12d32c564ce9)


### training and validation loss graph
![image](https://github.com/Savory-Team/foodition-edible-food-classification/assets/97221880/53146ab5-9d37-44fd-90ad-761db4441ea6)



### training and validation acccuracy on last epoch
```bash
Epoch 9/10
368/368 [==============================] - 24s 65ms/step - loss: 0.0970 - accuracy: 0.9691 - categorical_accuracy: 0.0644 - val_loss: 0.0344 - val_accuracy: 0.9893 - val_categorical_accuracy: 0.0559 - lr: 4.4933e-04
Epoch 10/10
368/368 [==============================] - 23s 64ms/step - loss: 0.0921 - accuracy: 0.9708 - categorical_accuracy: 0.0636 - val_loss: 0.0332 - val_accuracy: 0.9889 - val_categorical_accuracy: 0.0559 - lr: 4.0657e-04
```
### Confusion matrix
![image](https://github.com/Savory-Team/foodition-edible-food-classification/assets/97221880/7e75cd91-63ed-49f1-8d06-66b1f6315bc4)

# Technology we to use in model
- Python : The main programming language will be used in this project 
- TensorFlow/scikit-learn : Framework for building a model.
- Keras API from TensorFlow : an API from tensorflow for building a model.
- Git/GitHub : Version control and collaborative development.
- Matplotlib/Seaborn : Useful to visualize data used for ML development.
- Numpy :  Open-source library for data preparing and manipulating.
- Pre-trained model for image classification : for transfer learning on marine product grading model .
