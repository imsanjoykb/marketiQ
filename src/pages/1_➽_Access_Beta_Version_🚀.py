import streamlit as st
import os
import hashlib
from sqlalchemy import create_engine
from dotenv import load_dotenv
import templates.page_config

load_dotenv()
page_icon = os.environ.get('PAGE_ICON')
st.set_page_config(layout="wide", page_icon=page_icon)

# Use HTML and CSS to center and bold the text
st.markdown(
    """
    <div style="text-align: center;">
        <h1><strong>Coming Soon......</strong></h1>
    </div>
    """,
    unsafe_allow_html=True
)
