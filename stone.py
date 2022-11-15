import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*, and this is Kuang, by the way.
""")

#df = pdf.read_csv("dat.csv")
#st.bar_chart(df)
color = st.color_picker("What color do we want?",'#00f900')

if 'count' not in st.session_state:
    st.session_state.count = 15



minus1= st.button("-1")

if minus1:
    st.session_state.count = st.session_state.count-1

st.write("The number is ")
st.title(str(n))
st.latex(r'''x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}''')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')