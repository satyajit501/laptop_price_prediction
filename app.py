import streamlit as st
from PIL import Image
import os

from pathlib import Path


# cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# prof_pic = cur_dir / "assets" / "ricky.jpg"

cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
prof_pic = cur_dir / "assets" / "mypic.jpg"


# Description
PAGE_TITLE = "LAPTOP PRICE RECOMMENDATION"
PAGE_ICON = "✨"
NAME = "Satyajit Sahoo"
DESCRIPTION = """
Data science intern with strong analytical skills in Python, Tableau, and Power BI. Proficient in machine learning algorithms such as regression, clustering, and classification. Effective communicator and collaborator with excellent organizational skills. Dedicated and enthusiastic about expanding knowledge in data science. 
"""
EMAIL = "dssahoosatyajit@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/satyajit-sahoo01/",
    "GitHub": "https://github.com/satyajit501",
}
PROJECTS_REQUIRMENTS_DONE= {
    "🍿🍿 The Things are done so far for this project......",
    "🏆 All the information are scraped from flipkart.com and are produced the raw data in a .csv file",
    "🏆 Cleaning and do all the preprocessing task through pandas library of python to get a clean dataframe",
    "🏆 Done the data preprocessing task by regex in python",
    "🏆 Done all the visualization task through plotly library of python"
    "🏆 Making the model through Random Forest Regressior, to get the desired prediction of laptop prize 😊"
    "🏆 Last but not the list make the website through streamlit framework through python and deploy in "
    "streamlit app."
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hi!! :red[Everyone]")
st.subheader("welcome all, let's enjoy together")

# Load css, pdf and profile pic

# with open(css_file) as f:
#     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

prof = Image.open(prof_pic)


# Header section

col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(prof, width=220)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📩", EMAIL)

st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write('\n')

