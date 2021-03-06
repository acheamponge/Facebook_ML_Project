import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st
from PIL import Image

def write():
    st.markdown('<style>body{background-color: #1c1e21;} .d8{background-color: #1c1e21 !important;} body{color: white;} p{color: white;} .reportview-container .dataframe.col-header, .reportview-container .dataframe.corner, .reportview-container .dataframe.row-header {background-color: #1c1e21 !important; color: white !important;} .br {background-color: #1c1e21;!important} h2{color: white;} .reportview-container .main .block-container {flex: 1 1 !important; max-width: 1000px !important;width: 100% !important; padding: 0 !important;} .btn-outline-secondary{border-color: white !important; color: white !important;} .bi{color: white !important} h1{color: white;} li{color: white;} .Widget>label {color: white !important;} .sidebar-content{background-color: #1c1e21 !important; background-image:none !important;}</style>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'>Information Used for Recommendations</h1>", unsafe_allow_html=True)
    image = Image.open('./img/2.JPG')
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
    #df.columns = ['State','Year','Month','Day','Victim','County','Race','Sex','Mob','Offense','Note','2nd Name','3rd Name','Comments','Source']
        st.dataframe(df)
        
    elif pick == 'News Feed Topics for Recommendations':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['News Feed Topics'] = df['news_feed_topics']
        df = df[['News Feed Topics']]
    #df.columns = ['State','Year','Month','Day','Victim','County','Race','Sex','Mob','Offense','Note','2nd Name','3rd Name','Comments','Source']
        st.dataframe(df)
    
    else:
        df = pd.read_csv(keys[pick], encoding='utf8')  
        df['News Topics'] = df['news_topics']
        df = df[['News Topics']]
   
    #df.columns = ['State','Year','Month','Day','Victim','County','Race','Sex','Mob','Offense','Note','2nd Name','3rd Name','Comments','Source']
        st.dataframe(df)
    
    st.header("")
    st.header("")
    # st.header("")
    # st.header("Aggregation")
    # #ana = st.selectbox("Select Aggregation: ", list(analysis))
    
    # #if ana=='count':
    # #    st.info("Total Number of Lynchings: " + str(df.shape[0]))
    
    # if ana=='date span':
        # st.info("This data set spans from 1882 - 1930 (48 years)")
        
    # victims = df["Victim"].tolist()    
    
    
    # st.header("")
    # st.header("")
    # st.header("")
    # st.header("Victims")
    # tags = st.multiselect("Choose a name", victims)
    
    # for i in tags:
        # filtered_data_vic = df[df['Victim'] == str(i)]
        # st.dataframe(filtered_data_vic)
    
    
    # st.header("")
    # st.header("")
    # st.header("")
    # st.header("Group Dataset")
    # group = {
    # 'State',
    # 'Year',
    # 'Month',
    # 'Race',
    # 'County',
    # 'Offense',
    # 'Sex'    
            # }
    # pick_grp = st.selectbox("Groupby: ", list(group))
    
    # df3 = df.groupby(pick_grp).count()
    
    # df3 = df3[['Victim']]
    # df3.columns = ['Count']
    
    # st.dataframe(df3)
    
    
    # st.header("")
    # st.header("")
    # st.header("")
    # st.header("Filter Data Set")
    
    # st.subheader("Month")
    # month_to_filter = st.slider('Filter Data By Month', 0, 12, 8)
    # filtered_data_mon = df[df['Month'] == str(month_to_filter)]
    # st.dataframe(filtered_data_mon)
    
    
    # st.header("")
    # st.subheader("Year")
    # year_to_filter = st.slider('Filter Data By Year', 1882, 1930, 1900)
    # filtered_data_yr = df[df['Year'] == str(year_to_filter)]
    # st.dataframe(filtered_data_yr)
    
    
    # states = {
    # 'AL',
    # 'AR',
    # 'FL',
    # 'GA',
    # 'KY',
    # 'LA',
    # 'MS',
    # 'NC',
    # 'SC',
    # 'TN'
            # }
            
    # st.header("")
    # st.subheader("State")        
    # pick_st = st.selectbox("Filter By State: ", list(states))
    # filtered_data_st = df[df['State'] == str(pick_st)]
    # st.dataframe(filtered_data_st)
    
    
    # race = {
    # 'Blk',
    # 'Other',
    # 'Unk',
    # 'Wht'
            # }
    
    # st.header("")
    # st.subheader("Race")
    # pick_rc = st.selectbox("Filter By Race: ", list(race))
    # filtered_data_rc = df[df['Race'] == str(pick_rc)]
    # st.dataframe(filtered_data_rc)
    
    
    # sex = {
    # 'Male',
    # 'Fe',
    # 'Unk'
            # }
    # st.header("")
    # st.subheader("Sex")        
    # pick_sex = st.selectbox("Filter By Sex: ", list(sex))
    # filtered_data_sex = df[df['Sex'] == str(pick_sex)]
    # st.dataframe(filtered_data_sex)