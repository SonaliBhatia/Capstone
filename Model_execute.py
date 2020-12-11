import pandas as  pd
import numpy as np
import streamlit as st
import pickle

st.set_page_config(
    page_title = 'Predict Accent From Audio file provided'
)
#@st.cache
#def load_audio():
st.title('Recognize Speech Accent....')
