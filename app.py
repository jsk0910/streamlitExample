import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit Example')
x = st.slider('Select a value')
df = pd.DataFrame(np.random.randn(x,2) / [50,50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)

#st.write(x, 'squared is', x * x)
