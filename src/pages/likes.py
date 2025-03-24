import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st
from PIL import Image

def write():
    st.markdown('<style>body{background-color: #1c1e21;} .d8{background-color: #1c1e21 !important;} body{color: white;} p{color: white;} .reportview-container .dataframe.col-header, .reportview-container .dataframe.corner, .reportview-container .dataframe.row-header {background-color: #1c1e21 !important; color: white !important;} .br {background-color: #1c1e21;!important} h2{color: white;} .reportview-container .main .block-container {flex: 1 1 !important; max-width: 1000px !important;width: 100% !important; padding: 0 !important;} .btn-outline-secondary{border-color: white !important; color: white !important;} .bi{color: white !important} h1{color: white;} li{color: white;} .Widget>label {color: white !important;} .sidebar-content{background-color: #1c1e21 !important; background-image:none !important;}</style>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'>Interactions</h1>", unsafe_allow_html=True)
    image = Image.open('./1.jpeg')
    st.write(" ")
    st.write(" ")
    st.image(image, use_column_width=True)
    
    keys = {
    'Pages': './data/likes_and_reactions/pages.csv',
    'Posts and Comments': './data/likes_and_reactions/posts_and_comments.csv',
      } 
    st.header("Dataset")
    pick = st.selectbox("Select Dataset: ", list(keys.keys()))
    
    
    analysis = {
    'count',
    'date span'
            }
    
    if pick == 'Pages':
        df = pd.read_csv(keys[pick], encoding='utf8')
    
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Name'] = df['name']
        df = df[['Name', 'Date']]
        st.dataframe(df)
    
    else: 
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Reaction'] = df['data/0/reaction/reaction']
        df['Title'] = df['title']

        df = df[['Title', 'Reaction']]
    
        st.dataframe(df)
    
    st.header("")
    st.header("")
