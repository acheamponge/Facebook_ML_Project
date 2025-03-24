import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st
from PIL import Image


def write():
    st.markdown('<style>body{background-color: #1c1e21;} .d8{background-color: #1c1e21 !important;} body{color: white;} p{color: white;} .reportview-container .dataframe.col-header, .reportview-container .dataframe.corner, .reportview-container .dataframe.row-header {background-color: #1c1e21 !important; color: white !important;} .br {background-color: #1c1e21;!important} h2{color: white;} .reportview-container .main .block-container {flex: 1 1 !important; max-width: 1000px !important;width: 100% !important; padding: 0 !important;} .btn-outline-secondary{border-color: white !important; color: white !important;} .bi{color: white !important} h1{color: white;} li{color: white;} .Widget>label {color: white !important;} .sidebar-content{background-color: #1c1e21 !important; background-image:none !important;}</style>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'>Ads & Businesses</h1>", unsafe_allow_html=True)
    image = Image.open('./1.jpeg')
    st.write(" ")
    st.write(" ")
    st.image(image, use_column_width=True)

    
    keys = {
    'Ad Interests': './data/ads_and_businesses/ad_interests.csv',
    'Advertisers Who Uploaded A Contact List With Your Information': './data/ads_and_businesses/advertisers_who_uploaded_a_contact_list_with_your_information.csv',   
    'Advertisers Kwame Interacted': "./data/ads_and_businesses/advertisers_you've_interacted_with.csv",} 
    st.header("Dataset")
    pick = st.selectbox("Select Dataset: ", list(keys.keys()))
    
    
    analysis = {
    'count',
    'date span'
            }
    
    if pick == 'Ad Interests':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Topic'] = df['topics']
        df = df[['Topic']]
        st.dataframe(df)
        
    elif pick == 'Advertisers Who Uploaded A Contact List With Your Information':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Custom Audiences'] = df['custom_audiences']
        df = df[['Custom Audiences']]
        st.dataframe(df)
        
        
    elif pick == 'Advertisers Kwame Interacted':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Title of Ad'] = df['history/title']
        df['Action on Ad'] = df['history/action']
        df['Date'] = pd.to_datetime(df['history/timestamp'],unit='s')
        df = df[['Title of Ad', 'Date', 'Action on Ad']]
        st.dataframe(df)
        
    else:     
        df = pd.read_csv(keys[pick], encoding='utf8')
    
    
        st.dataframe(df)
    
    st.header("")
    st.header("")
