import streamlit as st
import pandas as pd 

st.title('🤖 Machine Learning App')

st.info('This app builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('penguins_cleaned.csv')
  df

  st.write('**X**')
  X = df.drop('species', axis=1)
  X

  st.write('**y**')
  y = df.species
  y

with st.expander('Data Visualization'):
  # "bill_length_mm","bill_depth_mm_","flipper_length_mm","flipper_lenth_mm","body_mass_g"
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

## Data Preparations
with st.sidebar:
  st.header('Input Features')
  ## species	island	bill_length_mm	bill_depth_mm	flipper_length_mm	body_mass_g	sex
  island = st.selectbox("Island", ("Biscoe", "Dream", "Toegersen"))
  gender = st.selectbox("Gender", ("Male", "Female"))
  bill_length_mm = st.slider("Bill Length (mm)", 32.1, 59.64, 43.9)
  bill_depth_mm = st.slider("Bill Depth (mm)", 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider("Flipper Length (mm)", 172.0, 231.0, 201.0)
  body_mass_g = st.slider("Body Mass (g)", 2700.0, 6300.0, 4207.0)
  
