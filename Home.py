import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Nikolay Hahenko")
    content = """
    Hi, I'm Nikolay! I'm a beginner Python developer. 
    I'm currently studying Python language and looking for my first job.
    Also, I'm in my sixth year of study at Sumy State University.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:int(len(df) / 2)].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[int(len(df) / 2):].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")
