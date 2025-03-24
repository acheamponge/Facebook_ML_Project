import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st
from PIL import Image

def write():
    st.markdown('<style>body{background-color: #1c1e21;} .d8{background-color: #1c1e21 !important;} body{color: white;} p{color: white;} .reportview-container .dataframe.col-header, .reportview-container .dataframe.corner, .reportview-container .dataframe.row-header {background-color: #1c1e21 !important; color: white !important;} .br {background-color: #1c1e21;!important} h2{color: white;} .reportview-container .main .block-container {flex: 1 1 !important; max-width: 1000px !important;width: 100% !important; padding: 0 !important;} .btn-outline-secondary{border-color: white !important; color: white !important;} .bi{color: white !important} h1{color: white;} li{color: white;} .Widget>label {color: white !important;} .sidebar-content{background-color: #1c1e21 !important; background-image:none !important;}</style>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'>Information Used for Recommendations</h1>", unsafe_allow_html=True)
    image = Image.open('./1.jpeg')
    st.write(" ")
    st.write(" ")
    st.image(image, use_column_width=True)
    keys = {
    'Facebook Watch Topics for Recommendations': './data/information_used_for_recommendations/facebook_watch_topics_for_recommendations.csv',
    'News Feed Topics for Recommendations': './data/information_used_for_recommendations/news_feed_topics_for_recommendations.csv',
    'News Topics for Recommendations': './data/information_used_for_recommendations/news_topics_for_recommendations.csv',
      } 
    st.header("Dataset")
    pick = st.selectbox("Select Dataset: ", list(keys.keys()))
    
    
    analysis = {
    'count',
    'date span'
            }
    
    if pick == 'Facebook Watch Topics for Recommendations':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Facebook Watch Topics'] = df['facebook_watch_topics']
        df = df[['Facebook Watch Topics']]
        st.dataframe(df)
        
    elif pick == 'News Feed Topics for Recommendations':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['News Feed Topics'] = df['news_feed_topics']
        df = df[['News Feed Topics']]
        st.dataframe(df)
    
    else:
        df = pd.read_csv(keys[pick], encoding='utf8')  
        df['News Topics'] = df['news_topics']
        df = df[['News Topics']]
   
        st.dataframe(df)
    
    st.header("")
    st.header("")
    # filtered_data_sex = df[df['Sex'] == str(pick_sex)]
    # st.dataframe(filtered_data_sex)
