import pathlib
import utils.display as udisp
import pandas as pd
import calendar
import streamlit as st
from PIL import Image


def write():
    st.markdown('<style>body{background-color: #1c1e21;} .d8{background-color: #1c1e21 !important;} body{color: white;} p{color: white;} .reportview-container .dataframe.col-header, .reportview-container .dataframe.corner, .reportview-container .dataframe.row-header {background-color: #1c1e21 !important; color: white !important;} .br {background-color: #1c1e21;!important} h2{color: white;} .reportview-container .main .block-container {flex: 1 1 !important; max-width: 1000px !important;width: 100% !important; padding: 0 !important;} .btn-outline-secondary{border-color: white !important; color: white !important;} .bi{color: white !important} h1{color: white;} li{color: white;} .Widget>label {color: white !important;} .sidebar-content{background-color: #1c1e21 !important; background-image:none !important;}</style>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'>Ads & Businesses</h1>", unsafe_allow_html=True)
    image = Image.open('./img/2.JPG')
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
    #df.columns = ['State','Year','Month','Day','Victim','County','Race','Sex','Mob','Offense','Note','2nd Name','3rd Name','Comments','Source']
        st.dataframe(df)
        
    elif pick == 'Advertisers Who Uploaded A Contact List With Your Information':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Custom Audiences'] = df['custom_audiences']
        df = df[['Custom Audiences']]
    #df.columns = ['State','Year','Month','Day','Victim','County','Race','Sex','Mob','Offense','Note','2nd Name','3rd Name','Comments','Source']
        st.dataframe(df)
        
        
    elif pick == 'Advertisers Kwame Interacted':
        df = pd.read_csv(keys[pick], encoding='utf8')
        df['Title of Ad'] = df['history/title']
        df['Action on Ad'] = df['history/action']
        df['Date'] = pd.to_datetime(df['history/timestamp'],unit='s')
        df = df[['Title of Ad', 'Date', 'Action on Ad']]
    #df.columns = ['State','Year','Month','Day','Victim','County','Race','Sex','Mob','Offense','Note','2nd Name','3rd Name','Comments','Source']
        st.dataframe(df)
        
    else:     
        df = pd.read_csv(keys[pick], encoding='utf8')
    
    
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