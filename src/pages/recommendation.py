import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st


def write():
    udisp.title_awesome("Data Analytics")
    
    
    keys = {
    'Facebook Watch Topics For Recommendation': './data/information_used_for_recommendations/facebook_watch_topics_for_recommendations.csv',
    'Facebook News Feed Topics For Recommendation': './data/information_used_for_recommendations/news_feed_topics_for_recommendations.csv'
    'Facebook News Topics For Recommendations': './data/information_used_for_recommendations/news_topics_for_recommendations.csv'
      } 
    st.header("Dataset")
    pick = st.selectbox("Select Dataset: ", list(keys.keys()))
    
    
    analysis = {
    'count',
    'date span'
            }
    
    
    df = pd.read_csv(keys[pick], encoding='utf8')
    
    
    st.dataframe(df)
    
    st.header("")
    st.header("")
    
