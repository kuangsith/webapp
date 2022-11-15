import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*, and this is Kuang, by the way.
""")

#df = pdf.read_csv("dat.csv")
#st.bar_chart(df)
color = st.color_picker("What color do we want?",'#00f900')

n = 15

st.write("The number is "+str(n))