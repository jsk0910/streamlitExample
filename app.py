import streamlit as st

st.title('Streamlit Example')
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
