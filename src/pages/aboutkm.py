import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st
from PIL import Image






def write():
    st.markdown('<style>body{background-color: #1c1e21;} .d8{background-color: #1c1e21 !important;} body{color: white;} p{color: white;} .reportview-container .dataframe.col-header, .reportview-container .dataframe.corner, .reportview-container .dataframe.row-header {background-color: #1c1e21 !important; color: white !important;} .br {background-color: #1c1e21;!important} h2{color: white;} .reportview-container .main .block-container {flex: 1 1 !important; max-width: 1000px !important;width: 100% !important; padding: 0 !important;} .btn-outline-secondary{border-color: white !important; color: white !important;} .bi{color: white !important} h1{color: white;} li{color: white;} .Widget>label {color: white !important;} .sidebar-content{background-color: #1c1e21 !important; background-image:none !important;}</style>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'>Kwame Technologist Profile</h1>", unsafe_allow_html=True)
    image = Image.open('./1.jpeg')
    st.write(" ")
    st.write(" ")
    st.image(image, use_column_width=True)
    keys = {
    'Ads': './data/about_you/ads.csv',
    'Amount of Time of Watched Videos': './data/about_you/amount_of_time_video.csv',
    'Read Articles': './data/about_you/articles_read.csv',
    'Events Visited': './data/about_you/events_visits.csv',
    'Watched Facebook Videos and Shows': './data/about_you/facebook_watch_videos_and_shows.csv',
    'Friend Peer Group': './data/about_you/friend_peer_group.csv',
    'Groups Visited': './data/about_you/groups_visited.csv',
    'Live Videos': './data/about_you/live_videos.csv',
    'Market Place': './data/about_you/market place.csv',
    'Pages Visited': './data/about_you/pages_visted.csv',
    'Preferences': './data/about_you/preferences.csv',
    'Profile Visited': './data/about_you/profile visted.csv',
    'Shows': './data/about_you/shows.csv',
            } 
    st.header("Dataset")
    pick = st.selectbox("Select Dataset: ", list(keys.keys()))
    
    
    analysis = {
    'count',
    'date span'
            }
    
    
    if pick == 'Ads':
        df = pd.read_csv(keys[pick], encoding='utf8')
    
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Ad'] = df['data/name']
        df['Link'] = df['data/uri']
        df = df[['Ad', 'Date', 'Link']]
        st.dataframe(df)
    
    
    elif pick == 'Amount of Time of Watched Videos':
        df = pd.read_csv(keys[pick], encoding='utf8')
    
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Video'] = df['data/name']
        df['Link'] = df['data/uri']
        df['Time Spent'] = df['data/watch_position_seconds']
        df = df[['Video', 'Link', 'Date', 'Time Spent']]
        st.dataframe(df)
        
    
    elif pick == 'Read Articles':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Article'] = df['data/name']
        df['Link'] = df['data/uri']
        df = df[['Article', 'Link', 'Date']]
        st.dataframe(df)
        
    elif pick == 'Events Visited':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Events'] = df['data/name']
        df['Link'] = df['data/uri']
        df = df[['Events', 'Link', 'Date']]
        st.dataframe(df)
        
    elif pick == 'Watched Facebook Videos and Shows':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Facebook Shows'] = df['data/name']
        df['Link'] = df['data/uri']
        df['Time of Video'] = df['data/watch_time']
        df = df[['Facebook Shows', 'Link', 'Date', 'Time of Video']]
        st.dataframe(df)


    elif pick == 'Friend Peer Group':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Peer Group'] = df['friend_peer_group']
        df = df[['Peer Group']]
        st.dataframe(df)


    elif pick == 'Groups Visited':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Groups'] = df['data/name']
        df['Link'] = df['data/uri']
        df = df[['Groups', 'Link', 'Date']]
        st.dataframe(df)


    elif pick == 'Live Videos':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Live Videos'] = df['data/name']
        df['Link'] = df['data/uri']
        df = df[['Live Videos', 'Link', 'Date']]
        st.dataframe(df)
    

    
    elif pick == 'Market Place':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Ad'] = df['data/name']
        df['Link'] = df['data/uri']
        df = df[['Ad', 'Link', 'Date']]
        st.dataframe(df)
        
        
    elif pick == 'Pages Visited':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Page'] = df['data/name']
        df['Link'] = df['data/uri']
        df = df[['Page', 'Link', 'Date']]
        st.dataframe(df)
        
        
    elif pick == 'Preferences':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Language'] = df['data/name']
        df = df[['Language', 'Date']]
        st.dataframe(df)
        
    elif pick == 'Profile Visited':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Profile'] = df['data/name']
        df['Link'] = df['data/uri']
        df = df[['Profile', 'Date', 'Link']]
        st.dataframe(df)


    elif pick == 'Shows':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Date'] = pd.to_datetime(df['timestamp'],unit='s')
        df['Show'] = df['data/name']
        df['Link'] = df['data/uri']
        df = df[['Show', 'Date', 'Link']]
        st.dataframe(df)        
        
    else:
        df = pd.read_csv(keys[pick], encoding='utf8')
        st.dataframe(df)
    st.header("")
    st.header("")
