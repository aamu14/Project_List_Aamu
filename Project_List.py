import streamlit as st
import subprocess
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Configure
st.set_page_config(
    page_title="Nur's Portofolio",
)
st.title('My Portfolio Project')
st.markdown("""
Hello, welcome to my project list. In this page, i will show all project that i have done. It contains description about the project and it's link if you want to see the project. It might not be a perfect one, but i'm open for any suggestion :)
""")
st.markdown("""---""")
st.markdown("""
For futher information, you can contact me here: \n
My Email: nurmuhammadherlim@gmail.com \n
LinkedIn: https://www.linkedin.com/in/nur-muhammad-herlim/
""")
st.markdown("""---""")

url1 = "https://bit.ly/RxPy_Streamlit"
url2 = "https://bit.ly/gbooks_analysis_st"
st.markdown("""
This is the project that I have already completed. I sorted it in reverse order to showcase the newest project at the beginning: \n       
""") 

st.subheader("""
             2. Google Books Analysis (In English)
             """)
st.markdown("""
            This project was created to demonstrate data cleaning, manipulation, and conduct a basic analysis through simple visualization. The primary objective is to emphasize the importance of having clean data and the necessity of manipulation to interpret and present the data effectively.  You can see the result on this link: 
            %s
            """ % url2)

st.subheader("""
              1. R x Python Using Streamlit (In Indonesian)
             """)
st.markdown("""
            This project was made to see how well Streamlit works when using 2 combined programming language, R and Python. You can see the result on this link: 
            %s
            """ % url1)
