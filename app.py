import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load trained model (Ensure butterfly_model.h5 is in the same folder)
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("butterfly_model.h5")  # Load your trained model
    return model

model = load_model()  # Load model once when app starts

# Define class labels (Replace these with actual butterfly species names)
class_labels = ["Monarch", "Swallowtail", "Painted Lady", "...", "Species 75"]

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
    predicted_class = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)
    
    # Display result
    st.write(f"### Prediction: {class_labels[predicted_class]}")
    st.write(f"Confidence: {confidence:.2f}")
