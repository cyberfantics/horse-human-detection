# Horse or Human Classifier

This project is a Streamlit-based web application that classifies images as either **Horse** or **Human** using a deep learning model trained with TensorFlow. The model achieves an impressive accuracy of **99.9%**, providing highly reliable predictions.

## Features

- **User-Friendly Interface**: Simple, intuitive layout built with Streamlit.
- **Image Classification**: Upload an image, and the app will classify it as either a horse or a human.
- **Real-Time Predictions**: Once an image is uploaded, the prediction result is displayed immediately.
- **Dashboard Layout**: Features a professional dashboard design with a left sidebar for easy navigation.

## How It Works

The application allows users to upload an image, which is then resized and preprocessed before being passed through a trained deep learning model. Based on the prediction result, the app will classify the image as either a "Horse" or a "Human."

### Model Details

- The model is trained using the **Horse or Human** dataset from Google.
- Achieves **99.9% accuracy** on test data.

## Installation

To run the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/cyberfantics/horse-human-detection.git
   ```

2. **Install the required dependencies:**
  ```pip install -r requirements.txt```

## Download the Dataset

- **[Training Dataset](https://storage.googleapis.com/learning-datasets/horse-or-human.zip)**
- **[Validation Dataset](https://storage.googleapis.com/learning-datasets/validation-horse-or-human.zip)**

Unzip the datasets and place them in your preferred folder.

## Run the Streamlit App

To run the app, execute the following command in your terminal:

```bash
streamlit run app.py
```

## Dataset

- **Horse or Human Training Dataset**: Contains images for training the model.
- **Horse or Human Validation Dataset**: Contains images for validating the model.

The dataset consists of images of horses and humans for training and testing purposes.

## Usage

1. Upload an image via the "Upload an image" button.
2. The image will be displayed in the app, and the classification result will appear beneath the image.
3. You can navigate through the app using the sidebar for additional functionalities.

## Author

Developed by **Syed Mansoor ul Hassan Bukhari**.

