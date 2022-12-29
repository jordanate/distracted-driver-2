import streamlit as st
st.set_page_config(layout="wide")
import pickle
import numpy as np
from skimage import transform
import tensorflow as tf 
import os
import base64
from keras.models import model_from_json
from keras import optimizers


from PIL import Image

with open('models/model9.json', 'r') as json_file:
    model9 = json_file.read()

model9 = tf.keras.models.model_from_json(model9)

model9.load_weights('models/model9.h5')

model9.compile(loss='categorical_crossentropy',
              optimizer=optimizers.Adam(lr=1e-4),
              metrics=['acc'])

def load(filename):
    image = Image.open(filename)
    image = np.array(image).astype('float32')/255
    image = transform.resize(image, (160, 120, 3))
    image = np.expand_dims(image, axis=0)
    return image

file_ = open("images/car.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True)

title = '<p style="font-weight:bold; color:Black; font-size:45px;">Distracted Driver Detector</p>'

st.markdown(title, unsafe_allow_html=True)


prompt = '<p style="font-weight:bold; color:Black; font-size:22px;">Upload an Image: </p>'

st.markdown(prompt, unsafe_allow_html=True) 

input = st.file_uploader(" ")


button = st.button('Enter')

if button:

	image = load(input)

	null = '<p style="color:Black; font-size:20px;">  </p>'

	prediction = model9.predict(image)

	prediction_list = prediction[0].tolist()

	max_value = max(prediction_list)

	index = prediction_list.index(max_value)

	c0 = '<p style="color:Black; font-size:20px;"><strong>ACTION:</strong> SAFE DRIVING</p>'

	c1 = '<p style="color:Black; font-size:20px;"><strong>ACTION:</strong> TEXTING WITH RIGHT HAND</p>'

	c2 = '<p style="color:Black; font-size:20px;"><strong>ACTION:</strong> TALKING ON THE PHONE WITH RIGHT HAND</p>'

	c3 = '<p style="color:Black; font-size:20px;"><strong>ACTION:</strong> TEXTING WITH LEFT HAND</p>'
	
	c4 = '<p style="color:Black; font-size:20px;"><strong>ACTION:</strong> TALKING ON THE PHONE WITH LEFT HAND</p>'

	c5 = '<p style="color:Black; font-size:20px;"><strong>ACTION:</strong> OPERATING THE RADIO</p>'

	c6 = '<p style="color:Black; font-size:20px;"><strong>ACTION:</strong> DRINKING A BEVERAGE</p>'

	c7 = '<p style="color:Black; font-size:20px;"><strong>ACTION:</strong> REACHING BEHIND</p>'

	c8 = '<p style="color:Black; font-size:20px;"><strong>ACTION:</strong> HAIR AND MAKEUP</p>'

	c9 = '<p style="color:Black; font-size:20px;"><strong>ACTION:</strong> TALKING TO PASSENGER</p>'

	dd = '<p style="color:Black; font-size:20px;"><strong>DISTRACTED DRIVING?</strong> YES </p>'

	sd = '<p style="color:Black; font-size:20px;"><strong>DISTRACTED DRIVING?</strong> NO </p>'

	if index == 0:
		col3,col4 = st.columns([12, 10])
		with col3:
			st.image(input)
		with col4:
			st.markdown(c0, unsafe_allow_html=True)
			st.markdown(sd, unsafe_allow_html=True)
			check = Image.open('images/check.png')
			st.image(check, width=150)
		
	if index == 1:
		col3,col4 = st.columns([12, 10])
		with col3:
			st.image(input)
		with col4:
			st.markdown(c1, unsafe_allow_html=True)
			st.markdown(dd, unsafe_allow_html=True)
			x_mark = Image.open('images/x_mark.png')
			st.image(x_mark, width=150)
	if index == 2:
		col3,col4 = st.columns([12, 10])
		with col3:
			st.image(input)
		with col4:
			st.markdown(c2, unsafe_allow_html=True)
			st.markdown(dd, unsafe_allow_html=True)
			x_mark = Image.open('images/x_mark.png')
			st.image(x_mark, width=150)
	if index == 3:
		col3,col4 = st.columns([12, 10])
		with col3:
			st.image(input)
		with col4:
			st.markdown(c3, unsafe_allow_html=True)
			st.markdown(dd, unsafe_allow_html=True)
			x_mark = Image.open('images/x_mark.png')
			st.image(x_mark, width=150)
	if index == 4:
		col3,col4 = st.columns([12, 10])
		with col3:
			st.image(input)
		with col4:
			st.markdown(c4, unsafe_allow_html=True)
			st.markdown(dd, unsafe_allow_html=True)
			x_mark = Image.open('images/x_mark.png')
			st.image(x_mark, width=150)
		
	if index == 5:
		col3,col4 = st.columns([12, 10])
		with col3:
			st.image(input)
		with col4:
			st.markdown(c5, unsafe_allow_html=True)
			st.markdown(dd, unsafe_allow_html=True)
			x_mark = Image.open('images/x_mark.png')
			st.image(x_mark, width=150)
	if index == 6:
		col3,col4 = st.columns([12, 10])
		with col3:
			st.image(input)
		with col4:
			st.markdown(c6, unsafe_allow_html=True)
			st.markdown(dd, unsafe_allow_html=True)
			x_mark = Image.open('images/x_mark.png')
			st.image(x_mark, width=150)
	if index == 7:
		col3,col4 = st.columns([12, 10])
		with col3:
			st.image(input)
		with col4:
			st.markdown(c7, unsafe_allow_html=True)
			st.markdown(dd, unsafe_allow_html=True)
			x_mark = Image.open('images/x_mark.png')
			st.image(x_mark, width=150)
	if index == 8:
		col3,col4 = st.columns([12, 10])
		with col3:
			st.image(input)
		with col4:
			st.markdown(c8, unsafe_allow_html=True)
			st.markdown(dd, unsafe_allow_html=True)
			x_mark = Image.open('images/x_mark.png')
			st.image(x_mark, width=150)
	if index == 9:
		col3,col4 = st.columns([12, 10])
		with col3:
			st.image(input)
		with col4:
			st.markdown(c9, unsafe_allow_html=True)
			st.markdown(dd, unsafe_allow_html=True)
			x_mark = Image.open('images/x_mark.png')
			st.image(x_mark, width=150)

st.markdown("***")

stats_title = '<p style="font-weight:bold; color:Black; font-size:27px;">Information About Distracted Driving <a href="https://www.cdc.gov/transportationsafety/distracted_driving/index.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fmotorvehiclesafety%2Fdistracted_driving%2Findex.html"> (CDC) </a></p>'

st.markdown(stats_title, unsafe_allow_html=True)

subhead_1 = '<p style="color:Black; font-size:22px;"><strong>What is Distracted Driving?<strong></p>'

visual = '<p style="color:Black; font-size:18px;"><strong>Visual:</strong> taking your eyes off the road</p>'
manual = '<p style="color:Black; font-size:18px;"><strong>Manual:</strong> taking your hands off the wheel</p>'
cognitive = '<p style="color:Black; font-size:18px;"><strong>Cognitive:</strong> taking your mind off driving</p>'

subhead_2 = '<p style="color:Black; font-size:22px;"><strong>Why is Distracted Driving a Problem?<strong></p>'

subhead_3 = '<p style="color:Black; font-size:20px;"> According to United States statistics, in 2019...</p>'

stat_1 = '<p style="color:Black; font-size:18px;"> • 		9 people per day were killed due to distracted driving</p>'
stat_2 = '<p style="color:Black; font-size:18px;"> • 		424,000 people were injured from a car crash involving a distracted driver</p>'
stat_3 = '<p style="color:Black; font-size:18px;"> • 		Of the people killed in distracted driving accidents, 1 in 5 of these individuals were not in vehicles (i.e., walking, biking, etc.)</p>'

st.markdown(subhead_1, unsafe_allow_html=True)
st.markdown(visual, unsafe_allow_html=True)
st.markdown(manual, unsafe_allow_html=True)
st.markdown(cognitive, unsafe_allow_html=True)
st.markdown(subhead_2, unsafe_allow_html=True)
st.markdown(subhead_3, unsafe_allow_html=True)
st.markdown(stat_1, unsafe_allow_html=True)
st.markdown(stat_2, unsafe_allow_html=True)
st.markdown(stat_3, unsafe_allow_html=True)



