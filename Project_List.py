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
url3 = "bit.ly/SalarySurveyHRDBCT3"
ulr4 = "bit.ly/VisualizationEstimatedSalarySurvey"
ulr5 = "bit.ly/3WGmBUv"

st.markdown("""
This is the project that I have already completed. I sorted it in reverse order to showcase the newest project at the beginning: \n       
""") 
#--------------------------------------------------------------------------------------

st.subheader("""
             3. Visualization of Salary Survey HRDBCT 3.0 (In Indonesia)
             """)
st.markdown("""
This dashboard is inspired by the results of a salary survey, indicating that the data used is not real, but randomly generated. The reason for this is that the salary data available in the survey only includes the Q1, Median, and Q3 figures. I felt that this data would be insufficient for my practice, so I opted to use randomly generated salary data instead.

The randomly generated data was created based on several considerations:
a) Assuming that the generated data follows a normal distribution.
b) Assuming that the sample median can be estimated as the same as the sample mean.
c) Since the parameters require the number of data points, the mean, and the standard deviation (SD), the SD value was obtained using the formula SD = (Interquartile Range / 1.35).
d) To prevent the salary values from being negative or too low, I decided to set a limit that the generated salary values should not be negative and should not deviate too far from the Q1 value.
e) Finally, I used RStudio to help generate this data, with some assistance from ChatGPT when errors occurred.

There is a new column replacing the Q1, Median, and Q3 values, called "estimated salary." Additionally, there is a new column to check whether the salary obtained is above or below the 2024 minimum wage (UMP) for each province.
""")
st.markdown("""
Here is a sample image from my visualization results.
            """)
st.image("Visualization Sample.jpeg")

st.markdown("""
If you interested more, you can download the file that i provided below:
            """)
st.markdown("""Salary Survey HRDBACOT Document Result:         
            %s
            """ % url3)

st.markdown("""Visualization of Estimated Salary Survey with Power BI:
            %s
            """ % url4)

st.markdown("""Cleaned Dataset of Estimated Salary Survey:        
            %s
            """ % url5)
#------------------------------------------------------------------------------
st.subheader("""
             2. Google Books Analysis (In English)
             """)
st.markdown("""
            This project was created to demonstrate data cleaning, manipulation, and conduct a basic analysis through simple visualization. The primary objective is to emphasize the importance of having clean data and the necessity of manipulation to interpret and present the data effectively.  You can see the result on this link: 
            %s
            """ % url2)
#-------------------------------------------------------------------------------
st.subheader("""
              1. R x Python Using Streamlit (In Indonesian)
             """)
st.markdown("""
            This project was made to see how well Streamlit works when using 2 combined programming language, R and Python. You can see the result on this link: 
            %s
            """ % url1)
