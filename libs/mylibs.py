import streamlit as st
import numpy as np
import os
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# @st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img

def process(image_file):
    if image_file is not None:
        # Load model
        classifier = load_model('my_model_CNN_20082021.h5')

        # Processing image
        if os.path.exists('uploads/') == False:
            os.mkdir('uploads')
        #file_details = {"FileName": image_file.name, "FileType": image_file.type}
        # st.write(file_details)
        img = load_image(image_file)
        st.image(img)
        with open(os.path.join("uploads", image_file.name), "wb") as f: 
            f.write(image_file.getbuffer())         
        
        # Predict
        test_image = image.load_img("uploads/" + image_file.name, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        # print(test_image.shape)
        test_image = test_image / 255
        test_image = np.expand_dims(test_image, axis = 0)
        # print(test_image.shape)
        result = classifier.predict(test_image)
        # print(result)
        # 0: cat, 1: dog; sigmoid có ngưỡng 0.5
        if result[0][0] >= 0.5:
            prediction = 'Dog'
        else:
            prediction = 'Cat'
        st.success('##### This is a ' + prediction)
        st.markdown("<br>", unsafe_allow_html=True)

        for file in os.listdir('uploads/'):
            os.remove('uploads/' + file)
