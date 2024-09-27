import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# Load the saved model
model = tf.keras.models.load_model('model/horse_or_human_model.keras')

# Define a function for prediction
def predict(image):
    if image.mode == 'RGBA':
        image = image.convert('RGB')  # Convert to RGB if the image has an alpha channel
    image = image.resize((300, 300))  # Resize the image
    image = np.array(image) / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    prediction = model.predict(image)[0][0]  # Get prediction
    return "Human" if prediction > 0.5 else "Horse"

# Styling for the page
st.markdown(
    """
    <style>
    /* Global Background */
    .main {
        background-color: #f0f0f5;
        background-image: linear-gradient(135deg, #00c6ff 10%, #0072ff 100%);
    }
    
    /* Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0072ff;
        color: white;
        text-align: center;
        padding: 10px;
        font-family: 'Arial', sans-serif;
    }

    /* Dashboard Style */
    .dashboard {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        font-family: 'Arial', sans-serif;
        margin-top: 10px;
    }

    /* Image uploader */
    .file-uploader {
        border: 2px dashed #32CD32;
        padding: 20px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        font-family: 'Arial', sans-serif;
        margin-bottom: 20px;
    }

    </style>
    """, unsafe_allow_html=True
)

# Add the left sidebar content
with st.sidebar:
    st.markdown(
        """
        <div style="text-align: center; font-size: 24px; color: #32CD32; font-weight: bold;">
        🧠 Horse or Human Classifier
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div style="font-size: 18px; text-align: justify;">
        Welcome to the Horse or Human Classifier App! This app uses a deep learning model to classify whether an uploaded image contains a horse 🐴 or a human 🧍.
        </div>
        """, unsafe_allow_html=True
    )
    
    # Upload image
    st.markdown('<div class="file-uploader">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("🔄 Upload an image...", type=["jpg", "jpeg", "png"])
    st.markdown('</div>', unsafe_allow_html=True)

# Main content on the right (right bar)
st.markdown(
    """
    <div class="dashboard">
    <h4>Prediction Results 📊</h4>
    <p style="font-size: 16px;">Upload an image on the left sidebar to classify it as either a horse or a human.</p>
    </div>
    """, unsafe_allow_html=True
)

if uploaded_file is not None:
    # Load and display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='📷 Uploaded Image', use_column_width=True)
    
    st.write("🔍 Classifying...")

    # Add a loading spinner while processing
    with st.spinner('Please wait while AI is classifying...'):
        result = predict(image)

    # Show the prediction result
    st.success(f"🏆 Prediction: **{result}**")

# Add a footer
st.markdown(
    """
    <div class="footer">
        <p>Developed by <a href="https://www.linkedin.com/in/mansoor-bukhari-77549a264/" target="_blank" style="color: #FFD700;">Syed Mansoor ul Hassan Bukhari</a> | 
        Follow me on <a href="https://github.com/CyberFantics" target="_blank" style="color: #FFD700;">GitHub</a> for more cool projects!</p>
    </div>
    """, unsafe_allow_html=True
)
