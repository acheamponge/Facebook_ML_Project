import pathlib
import utils.display as udisp

import streamlit as st

def write():
    udisp.title_awesome("About")

    udisp.render_md("resources/about.md")
