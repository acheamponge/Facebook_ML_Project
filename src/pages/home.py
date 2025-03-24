import pathlib
import utils.display as udisp
from PIL import Image
import streamlit as st




def write():

    st.markdown('<style>body{background-color: #1c1e21;} p{color: white;} .reportview-container .main .block-container {flex: 1 1 !important; max-width: 1000px !important;width: 100% !important; padding: 0 !important;} .btn-outline-secondary{border-color: white !important; color: white !important;} .bi{color: white !important} h1{color: white;} li{color: white;} .Widget>label {color: white !important;} .sidebar-content{background-color: #1c1e21 !important; background-image:none !important;}</style>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'>A decade of Facebook Data</h1>", unsafe_allow_html=True)
    image = Image.open('./1.jpeg')
    st.write(" ")
    st.write(" ")
    st.image(image, use_column_width=True)
    
    st.write(
            """
This is a Data and Machine Learning project that seeks to use numerous data analysis, visualization techniques and machine learning algorithms to analyze 10 years of data from Facebook.

This project provides
- **Data Analytics** of every data Facebook has of the Kwame Technologist account.
- **Data Visualization** of text data.
- **Machine Learning Techniques** including NLP, Computer Vision and Classification.
    """
        )

    

