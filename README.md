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
![image](https://github.com/Savory-Team/foodition-edible-food-classification/assets/97221880/8d6f8541-5860-4f19-9d72-2e3d42d325d2)



## Training Result
### training and validation acccuracy graph
![image](https://github.com/Savory-Team/foodition-edible-food-classification/assets/97221880/5b400acd-4f6c-4de9-8861-7ba4a5ef7bf5)



### training and validation loss graph
![image](https://github.com/Savory-Team/foodition-edible-food-classification/assets/97221880/fabe835e-e958-47c3-8ecf-8c92be830c44)




### training and validation acccuracy on last epoch
```bash
Epoch 21/25
769/769 [==============================] - 73s 95ms/step - loss: 0.4648 - accuracy: 0.8301 - val_loss: 0.6558 - val_accuracy: 0.8547 - lr: 1.3534e-04
Epoch 22/25
769/769 [==============================] - 72s 93ms/step - loss: 0.4551 - accuracy: 0.8370 - val_loss: 0.6658 - val_accuracy: 0.8547 - lr: 1.2246e-04
```
### Testing
![image](https://github.com/Savory-Team/foodition-edible-food-classification/assets/97221880/29d1edc0-da78-451b-b088-6c0b2733f533)

```
Incorrect Predictions:
Image: /kaggle/input/foodition-test/foodition-test/nasi-jelek/Screenshot_2024-01-09-21-19-04-055_com.miui.videoplayer.jpg
Actual Class: nasi-jelek
Predicted Class: rice - edible

Image: /kaggle/input/foodition-test/foodition-test/pizza-jelek/old-moldy-pizza-on-wooden-260nw-439304512.jpg
Actual Class: pizza-jelek
Predicted Class: edible

Image: /kaggle/input/foodition-test/foodition-test/jeruk-jelek/stale-orange-white-green-mold-260nw-1643846443.jpeg
Actual Class: jeruk-jelek
Predicted Class: egg - edible

Image: /kaggle/input/foodition-test/foodition-test/roti-jelek/well_moldy-tmagArticle.jpg
Actual Class: roti-jelek
Predicted Class: bread - edible

Image: /kaggle/input/foodition-test/foodition-test/roti-jelek/download (2).jpeg
Actual Class: roti-jelek
Predicted Class: bread - edible

Accuracy: 88.64%
```


# Technology we to use in model
- Python : The main programming language will be used in this project 
- TensorFlow/scikit-learn : Framework for building a model.
- Keras API from TensorFlow : an API from tensorflow for building a model.
- Git/GitHub : Version control and collaborative development.
- Matplotlib/Seaborn : Useful to visualize data used for ML development.
- Numpy :  Open-source library for data preparing and manipulating.
- Pre-trained model for image classification : for transfer learning on marine product grading model .
