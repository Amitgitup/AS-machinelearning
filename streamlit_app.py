import streamlit as st
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier

st.title('🤖 Machine Learning App')

st.info('This app builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('penguins_cleaned.csv')
  df

  st.write('**X**')
  X_raw = df.drop('species', axis=1)
  X_raw

  st.write('**y**')
  y_raw = df.species
  y_raw

with st.expander('Data Visualization'):
  # "bill_length_mm","bill_depth_mm_","flipper_length_mm","flipper_lenth_mm","body_mass_g"
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

## Input Features
with st.sidebar:
  st.header('Input Features')
  ## species	island	bill_length_mm	bill_depth_mm	flipper_length_mm	body_mass_g	sex
  island = st.selectbox("Island", ("Biscoe", "Dream", "Toegersen"))
  bill_length_mm = st.slider("Bill Length (mm)", 32.1, 59.64, 43.9)
  bill_depth_mm = st.slider("Bill Depth (mm)", 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider("Flipper Length (mm)", 172.0, 231.0, 201.0)
  body_mass_g = st.slider("Body Mass (g)", 2700.0, 6300.0, 4207.0)
  gender = st.selectbox("Gender", ("Male", "Female"))
  
  ## Create a DataFrame
  data = {'island':island, 
          'bill_length_mm':bill_length_mm,
          'bill_depth_mm':bill_depth_mm,
          'flipper_length_mm':flipper_length_mm,
          'body_mass_g':body_mass_g,
          'sex':gender}
  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, X_raw], axis=0)

with st.expander('Input Features'):
  st.write("**Input Penguin**")
  input_df
  st.write('**Combined Penguin Data**')
  input_penguins

  
  ## Data Preparation
  ## Encode X
  encode = ['island', 'sex']
  df_penguins = pd.get_dummies(input_penguins, prefix=encode)

  X = df_penguins[1:]
  input_row = df_penguins[:1]

  ## Encode y
  target_mapper = {"Adelie":0,
                   "Chinstrap":1,
                   "Gentoo":2}
  def target_encode(val):
    return target_mapper[val] 

y = y_raw.apply(target_encode)

with st.expander('Data Preparation'): 
  st.write('**Encoded X (Input Penguin)**')
  input_row
  st.write("**Encoded Y**")
  y
  
## Model Training and Inference
## Train the ML Model
clf = RandomForestClassifier()
clf.fit(X, y)

## Apply the model to make predictions
prediciton = clf.predict(input_row)
prediciton_proba = clf.predict_proba(input_row)

df_prediction_proba = pd.DataFrame(data=prediction_proba, columns=["Adelie","Chinstrap","Gentoo"])
df_prediction_proba





