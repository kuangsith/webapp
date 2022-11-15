import streamlit as st
import pandas as pd
from PIL import Image

st.write("""
# My first app: The stone game!
""")

#df = pdf.read_csv("dat.csv")
#st.bar_chart(df)

if 'rule' not in st.session_state:
    st.session_state.rule = '1,2'

st.write("What is the rule?")
xol1,xol2,xol3 = st.columns(3)
with xol1:
    but12 = st.button("1,2")
with xol2:
    but123 = st.button("1,2,3")
with xol3:
    but1234 = st.button("1,2,3,4")

if but12:
    st.session_state.rule = '1,2'
if but123:
    st.session_state.rule = '1,2,3'
if but1234:
    st.session_state.rule = '1,2,3,4'

st.write("The current rule is you may take "+st.session_state.rule+" stones")

#color = st.color_picker("What color do we want?",'#00f900')

if 'count' not in st.session_state:
    st.session_state.count = 15

minus1=False
minus2=False
minus3=False
minus4=False

st.header("How many are you taking?")
col1,col2,col3,col4 = st.columns(4)
with col1:
    minus1= st.button("-1")
with col2:
    minus2= st.button("-2")
with col3:
    if st.session_state.rule == '1,2,3' or st.session_state.rule == '1,2,3,4':
        minus3= st.button("-3")
with col4:
    if st.session_state.rule == '1,2,3,4':
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
img = Image.open("peb.png")
for i in range(st.session_state.count):
    st.image(img,width=60)

#st.latex(r'''x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}''')

#st.latex(r'''
#    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#    \sum_{k=0}^{n-1} ar^k =
#    a \left(\frac{1-r^{n}}{1-r}\right)
#    ''')