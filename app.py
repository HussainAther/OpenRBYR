# app.py
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from pathlib import Path
from models.yolo_detector import detect_defects_yolo
from models.cnn_detector import detect_defects_cnn

st.set_page_config(page_title="CT Defect Detection", layout="centered")
st.title("🧠 Industrial CT Defect Detection Dashboard")

# ---- Model Caching ----
@st.cache_resource
def load_yolo_model():
    return detect_defects_yolo(load_model_only=True)

@st.cache_resource
def load_cnn_model():
    return detect_defects_cnn(load_model_only=True)

# ---- Sidebar ----
model_choice = st.sidebar.selectbox("Select AI Model", ["YOLOv8n", "CNN-Light"])
use_gpu = st.sidebar.checkbox("Use GPU (if available)", value=True)

# ---- Image Upload ----
uploaded_file = st.file_uploader("Upload a CT Image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Input Image", use_column_width=True)

    # Convert to NumPy
    img_array = np.array(image)

    # ---- Model Inference ----
    st.subheader("🔍 Detecting Defects...")
    if model_choice == "YOLOv8n":
        model = load_yolo_model()
        result_img, detections = detect_defects_yolo(img_array, model)
    else:
        model = load_cnn_model()
        result_img, detections = detect_defects_cnn(img_array, model)

    st.image(result_img, caption="Defect Detection Output", use_column_width=True)

    if detections:
        st.success(f"✅ {len(detections)} potential defect(s) found.")
        st.json(detections)
    else:
        st.info("No defects detected.")

# ---- Feedback Form (Optional PR #11 Feature) ----
with st.expander("💬 Submit Feedback"):
    feedback = st.text_area("How can we improve this app?")
    if st.button("Submit Feedback"):
        with open("feedback.log", "a") as f:
            f.write(feedback + "\n")
        st.success("Thanks for your feedback!")

