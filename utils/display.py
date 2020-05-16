import base64
import importlib
import pandas as pd
import streamlit as st

def render_page(menupage):
    menupage.write()

def title_awesome(body: str):
    
    st.markdown("<h1 style='text-align: center; color: white;'>10 years of Facebook Data</h1>", unsafe_allow_html=True)
    

def render_md(md_file_name):
    st.markdown(get_file_content_as_string(md_file_name))

def get_file_content_as_string(path):
    response = open(path, encoding="utf-8").read()
    return response

def show_code(file_name):
    return get_file_content_as_string(file_name)

def data_frame(filename):
    df = pd.read_csv(filename)
    st.write(df)