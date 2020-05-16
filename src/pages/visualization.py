import pathlib
import utils.display as udisp
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from wordcloud import WordCloud
from collections import Counter



def write():
    udisp.title_awesome("Data Visualizations")
    st.write("Strange Fruits")
    
    keys = {
    './data/lynchings.csv'
            }
    st.header("Dataset")        
    pick = st.selectbox("Select Dataset: ", list(keys))          
    
    df = pd.read_csv(pick, encoding='utf8')
    
    df.columns = ['State','Year','Month','Day','Victim','County','Race','Sex','Mob','Offense','Note','2nd Name','3rd Name','Comments','Source']
    st.dataframe(df)
    
    
    group = {
    'State',
    'Year',
    'Month',
    'Race',
    'County',
    'Offense',
    'Sex'    
            }
            
    st.header("")
    st.header("")
    st.header("")
    st.header("Choose an Attribute to Visualize")
    pick_grp = st.selectbox("Choose: ", list(group))
    
    df3 = df.groupby(pick_grp).count()
    
    df3 = df3[['Victim']]
    df3.columns = ['Count']
    df3['x-axis'] = df3.index
    
    
    st.header("")
    st.subheader("Line Graph")
    fig2 = px.line(df3, x="x-axis", y="Count", title="A graph of the number Lynchings grouped by " +str(pick_grp))
    st.plotly_chart(fig2)
    
    
    fig = px.scatter(df3, x="x-axis", y="Count")
    
    
    st.header("")
    st.subheader("Scatter Diagram of the number of Lynchings grouped by " + str(pick_grp))

    st.plotly_chart(fig)
    
    
 
    st.header("")
    st.subheader("Pie Chart of the number of Lynchings grouped by " + str(pick_grp))
    
    fig1 = go.Figure(data=[go.Pie(labels=df3['x-axis'], values=df3['Count'])])
    st.plotly_chart(fig1)
    
    words = df.Victim.tolist()
    word_could_dict=Counter(words)
    wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_could_dict)
    

    st.header("")
    st.subheader("WordCloud of the names of the Lynching Victims")
    plt.figure(figsize=[20,10])
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    st.pyplot()
    
    
     
    