import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load trained model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("butterfly_model.h5")  # Update with your model file
    return model

model = load_model()

# Define class labels (Replace with actual butterfly species names)
class_labels = ["Species 1", "Species 2", "Species 3", "...", "Species 75"]

# Streamlit UI
st.title("🦋 Butterfly Species Classifier")
st.write("Upload an image of a butterfly to classify its species.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Preprocess image
    img = image.resize((224, 224))  # Resize to model's input size
    img_array = np.array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    # Make prediction
    predictions = model.predict(img_array)
    top_5_indices = np.argsort(predictions[0])[-5:][::-1]  # Get top-5 predictions
    
    # Display top-5 predicted species
    st.write("### Prediction Results:")
    for i, index in enumerate(top_5_indices):
        st.write(f"{i+1}. {class_labels[index]} - Confidence: {predictions[0][index]:.2f}")
