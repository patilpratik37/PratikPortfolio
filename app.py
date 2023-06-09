from pathlib import Path

import streamlit as st 
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "Madara.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Pratik Patil | Digital CV"
PAGE_ICON = ":wave:"
NAME = "Pratik Patil"
DESCRIPTION = """
Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "patilpratik37@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Expense Manager - Tool for tracking user expenses",
    "🏆 Netflix Data Analysis and Visualization -  Insights into current market patterns",
    "🏆 Twitlytics - Determined the level of employee attrition in Indian I.T industry",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    
    
    # --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ As a final year engineering student seeking an internship in data analysis
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Completed several data analysis projects, including sentiment analysis and data visualization
- ✔️ Highly motivated, a quick learner, and eager to contribute to the success of the team
- ✔️ Seeking an opportunity to enhance my skills and gain practical experience in a professional setting
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, Linear regression, Decision trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- ACADEMIC PROJECTS ---
st.write('\n')
st.subheader("ACADEMIC PROJECTS")
st.write("---")

# --- PROJECT 1
st.write("🚧", "**Twitlytics | Focus was on determining the attrition rate in Indian IT companies**")
st.write("Jun 2022 - June 2023")
st.write(
    """
- ► Mined Twitter data using the snsscraping Python module for performing Sentiment Analysis
- ► Led a team of 2 analysts to brainstorm XGBoost model on the processed Twitter data
- ► With the accuracy of 86.1%, combined approach of utilizing the NLTK library and the XGBoost algorithm allowed me to efficiently analyze sentiments of the large volumes of Twitter data. 
"""
)

# --- PROJECT 2
st.write('\n')
st.write("🚧", "**Netflix Data Analysis and Visualization |  Insights into current market patterns**")
st.write("Jan 2022- Jun 2022")
st.write(
    """
- ► Developed a sophisticated web-based software application for Netflix using Python, Numpy, Pandas, Plotly, Textblob and leveraged data analysis and visualization technique
- ► Identified and displayed trends in the movie and television industry, provided valuable insights into current market patterns
- ► Compiled, studied, and inferred large amounts of data, to make informed business decisions.
"""
)

# --- PROJECT 3
st.write('\n')
st.write("🚧", "**Expense Manager | User Expense Management Tool**")
st.write("June 2021- Dec 2021")
st.write(
    """
- ► Designed and developed a Java-based web application for efficient user expense management.
- ► Provided real-time insights into financial trends of user through the application.
- ► Enabled users to make informed decisions based on the valuable insights provided.
"""
)