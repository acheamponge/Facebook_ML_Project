import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st
from PIL import Image

def write():
    st.markdown('<style>body{background-color: #1c1e21;} .d8{background-color: #1c1e21 !important;} body{color: white;} p{color: white;} .reportview-container .dataframe.col-header, .reportview-container .dataframe.corner, .reportview-container .dataframe.row-header {background-color: #1c1e21 !important; color: white !important;} .br {background-color: #1c1e21;!important} h2{color: white;} .reportview-container .main .block-container {flex: 1 1 !important; max-width: 1000px !important;width: 100% !important; padding: 0 !important;} .btn-outline-secondary{border-color: white !important; color: white !important;} .bi{color: white !important} h1{color: white;} li{color: white;} .Widget>label {color: white !important;} .sidebar-content{background-color: #1c1e21 !important; background-image:none !important;}</style>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'>Following & Followers</h1>", unsafe_allow_html=True)
    image = Image.open('./1.jpeg')
    st.write(" ")
    st.write(" ")
    st.image(image, use_column_width=True)

    
    keys = {
    'Followed Pages': './data/following_and_followers/followed_pages.csv',
    'Followers': './data/following_and_followers/followers.csv',
    'Following': './data/following_and_followers/following.csv',
    'Unfollowed Pages': './data/following_and_followers/unfollowed_pages.csv',    
    } 
    st.header("Dataset")
    pick = st.selectbox("Select Dataset: ", list(keys.keys()))
    
    
    analysis = {
    'count',
    'date span'
            }
    
    if pick == 'Followed Pages':
        df = pd.read_csv(keys[pick], encoding='utf8')
    
        df['Date'] = pd.to_datetime(df['pages_followed/timestamp'],unit='s')
        df['Pages'] = df['pages_followed/data/0/name']
        df['Title'] = df['pages_followed/title']
        df = df[['Pages', 'Date', 'Title']]
        st.dataframe(df)
        
    elif pick == 'Followers':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Follower'] = df['name']
        df = df[['Follower']]
        st.dataframe(df)
        
        
    elif pick == 'Following':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Date'] = pd.to_datetime(df['following/timestamp'],unit='s')
        df['Following'] = df['following/name']
        df = df[['Following', 'Date']]
        st.dataframe(df)
    
    else:
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Unfollowed Pages'] = df['data/0/name']
        df = df[['Unfollowed Pages', 'Date']]

        st.dataframe(df)
    
    st.header("")
    st.header("")
