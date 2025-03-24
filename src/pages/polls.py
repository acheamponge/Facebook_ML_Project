import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st
from PIL import Image

def write():
    st.markdown('<style>body{background-color: #1c1e21;} .d8{background-color: #1c1e21 !important;} body{color: white;} p{color: white;} .reportview-container .dataframe.col-header, .reportview-container .dataframe.corner, .reportview-container .dataframe.row-header {background-color: #1c1e21 !important; color: white !important;} .br {background-color: #1c1e21;!important} h2{color: white;} .reportview-container .main .block-container {flex: 1 1 !important; max-width: 1000px !important;width: 100% !important; padding: 0 !important;} .btn-outline-secondary{border-color: white !important; color: white !important;} .bi{color: white !important} h1{color: white;} li{color: white;} .Widget>label {color: white !important;} .sidebar-content{background-color: #1c1e21 !important; background-image:none !important;}</style>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'>Other Activity</h1>", unsafe_allow_html=True)
    image = Image.open('./1.jpeg')
    st.write(" ")
    st.write(" ")
    st.image(image, use_column_width=True)
    
    
    keys = {
    'Pokes 1': './data/other_activity/pokes1.csv',
    'Pokes 2': './data/other_activity/pokes2.csv',
    'Polls Voted On': './data/other_activity/polls_you_voted_on.csv',
    'Supported Correspondences': './data/other_activity/support_correspondences.csv'  } 
    st.header("Dataset")
    pick = st.selectbox("Select Dataset: ", list(keys.keys()))
    
    
    analysis = {
    'count',
    'date span'
            }
    
    
    if pick == 'Pokes 1':
        df = pd.read_csv(keys[pick], encoding='utf8')
    
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df = df[['poker', 'Date', 'pokee']]
        st.dataframe(df)


    elif pick == 'Pokes 2':
        df = pd.read_csv(keys[pick], encoding='utf8')
    
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Name'] = df['data/0/name']
        df['Title'] = df['title']
        
        df = df[['Name', 'Date', 'Title']]
        st.dataframe(df)
        
    elif pick == 'Polls Voted On':
        df = pd.read_csv(keys[pick], encoding='utf8')
    
        df['Date'] = pd.to_datetime(df['poll_votes/timestamp'],unit='s')
        df['Attachment'] = df['poll_votes/attachments/0/data/0/poll/options/0/option']
        df['Title'] = df['poll_votes/title']
        
        df = df[['Title', 'Date', 'Attachment']]
        st.dataframe(df)
        
    else:
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Date'] = pd.to_datetime(df['support_correspondence/timestamp'],unit='s')
        df['Subject'] = df['support_correspondence/subject']

   
        df = df[['Subject', 'Date']]

    
        st.dataframe(df)
    
    st.header("")
    st.header("")
