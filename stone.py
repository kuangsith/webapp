import streamlit as st
import pandas as pd

st.write("""
# My first app
The stone game!
""")

#df = pdf.read_csv("dat.csv")
#st.bar_chart(df)

st.write("What is the rule?")

color = st.color_picker("What color do we want?",'#00f900')

if 'count' not in st.session_state:
    st.session_state.count = 15


st.columns(4)
with col1:
    minus1= st.button("-1")
with col2:
    minus2= st.button("-2")
with col3:
    minus3= st.button("-3")
with col4:
    minus4= st.button("-4")


if minus1:
    st.session_state.count = st.session_state.count-1

if minus2:
    st.session_state.count = st.session_state.count-2

if minus3:
    st.session_state.count = st.session_state.count-3

if minus4:
    st.session_state.count = st.session_state.count-4

st.write("The number is ")
st.title(str(st.session_state.count))
#st.latex(r'''x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}''')

#st.latex(r'''
#    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#    \sum_{k=0}^{n-1} ar^k =
#    a \left(\frac{1-r^{n}}{1-r}\right)
#    ''')