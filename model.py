import streamlit as st
st.set_page_config(layout="wide")
import pickle
import numpy as np
from skimage import transform
import tensorflow as tf 
import os

from PIL import Image

with open('models/model1.pkl' , 'rb') as f:
    lr = pickle.load(f)

def load(filename):
    image = Image.open(filename)
    image = np.array(image).astype('float32')/255
    image = transform.resize(image, (160, 120, 3))
    image = np.expand_dims(image, axis=0)
    return image


input = st.text_input('Enter a file path:')

st.image(input)

image = load(input)

prediction = lr.predict(image)

prediction_list = prediction[0].tolist()

max_value = max(prediction_list)
index = prediction_list.index(max_value)

c0 = '<p style="color:Black; font-size:20px;">SAFE DRIVING</p>'

c1 = '<p style="color:Black; font-size:20px;">TEXTING WITH RIGHT HAND</p>'

c2 = '<p style="color:Black; font-size:20px;">TALKING ON THE PHONE WITH RIGHT HAND</p>'

c3 = '<p style="color:Black; font-size:20px;">TEXTING WITH LEFT HAND</p>'

c4 = '<p style="color:Black; font-size:20px;">TALKING ON THE PHONE WITH LEFT HAND</p>'

c5 = '<p style="color:Black; font-size:20px;">OPERATING THE RADIO</p>'

c6 = '<p style="color:Black; font-size:20px;">DRINKING A BEVERAGE</p>'

c7 = '<p style="color:Black; font-size:20px;">REACHING BEHIND</p>'

c8 = '<p style="color:Black; font-size:20px;">HAIR AND MAKEUP</p>'

c9 = '<p style="color:Black; font-size:20px;">TALKING TO PASSENGER</p>'

dd = '<p style="color:Black; font-size:20px;">DISTRACTED DRIVING? YES </p>'

sd = '<p style="color:Black; font-size:20px;">DISTRACTED DRIVING? NO </p>'

if index == 0:
	st.markdown(c0, unsafe_allow_html=True)
	st.markdown(sd, unsafe_allow_html=True)
if index == 1:
	st.markdown(c1, unsafe_allow_html=True)
	st.markdown(dd, unsafe_allow_html=True)
if index == 2:
	st.markdown(c2, unsafe_allow_html=True)
	st.markdown(dd, unsafe_allow_html=True)
if index == 3:
	st.markdown(c3, unsafe_allow_html=True)
	st.markdown(dd, unsafe_allow_html=True)
if index == 4:
	st.markdown(c4, unsafe_allow_html=True)
	st.markdown(dd, unsafe_allow_html=True)
if index == 5:
	st.markdown(c5, unsafe_allow_html=True)
	st.markdown(dd, unsafe_allow_html=True)
if index == 6:
	st.markdown(c6, unsafe_allow_html=True)
	st.markdown(dd, unsafe_allow_html=True)
if index == 7:
	st.markdown(c7, unsafe_allow_html=True)
	st.markdown(dd, unsafe_allow_html=True)
if index == 8:
	st.markdown(c8, unsafe_allow_html=True)
	st.markdown(dd, unsafe_allow_html=True)
if index == 9:
	st.markdown(c9, unsafe_allow_html=True)
	st.markdown(dd, unsafe_allow_html=True)














