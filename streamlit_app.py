import streamlit as st
import pandas as pd 

st.title('🤖 Machine Learning App')

st.info('This app builds a machine learning model!')

with st.expander(data):
  st.write('**Raw Data**')
  df = pd.read_csv('penguins_cleaned.csv')
  df
