import pathlib
import utils.display as udisp
from PIL import Image
import streamlit as st

def write():
    udisp.title_awesome("Resources")

    image = Image.open('./img/2.jfif')

    st.image(image, use_column_width=True)
    
    keys = {
    'Videos',
    'Datasets',
    'Articles',
    'Publications',
    'Citations'
            }
            
    pick = st.selectbox("Select An Option", list(keys))


    if pick=='Datasets':
        udisp.render_md("resources/datasets.md")
    
    elif pick=='Videos':
        udisp.render_md("resources/videos.md")
    
    elif pick=='Articles':
        udisp.render_md("resources/articles.md")
        
    elif pick=='Publications':
        udisp.render_md("resources/publications.md")
        
    elif pick=='Citations':
        udisp.render_md("resources/citations.md")
    