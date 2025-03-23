import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from streamlit_pdf_viewer import pdf_viewer


# Set page configuration
st.set_page_config(page_title="Naziya Mahimkar's Portfolio", layout="wide")

# Sidebar
with st.sidebar:
     # Skills Buttons
    st.write("### Skills")
    def display_buttons(skills, columns=4):
            cols = st.columns(columns)
            for i, skill in enumerate(skills):
                cols[i % columns].button(skill)

    # Programming Languages
    st.subheader("Programming Languages")
    display_buttons(["C", "C++", "Python", "Java", "HTML", "CSS"], columns=3)

    # AI & Machine Learning
    st.subheader("AI & Machine Learning")
    display_buttons([
        "LLM Training", "vLLM Deployment", "ONNX Optimization", "RAG (Retrieval-Augmented Generation)",
        "Multi-Agent Systems", "Deep Learning", "NLP", "Transformers"
    ], columns=2)

    # Databases
    st.subheader("Databases")
    display_buttons(["MySQL", "MongoDB", "Azure Blob Storage", "SQL Server"], columns=2)

    # Cloud Computing
    st.subheader("Cloud Computing")
    display_buttons(["Microsoft Azure"], columns=1)

    # DevOps & Version Control
    st.subheader("DevOps & Version Control")
    display_buttons(["Docker", "Kubernetes", "Git"], columns=3)

    # Data Visualization
    st.subheader("Data Visualization")
    display_buttons(["Power BI", "Tableau", "Microsoft Excel"], columns=3)

    

# Main Page
st.markdown("# 🎉 Naziya Mahimkar's Portfolio")

# Intro Section
intro_col1,intro_col2 = st.columns(2)
with intro_col2:
    st.header(' ')
    st.image(r'images\final image.png', width=300)

with intro_col1:
    st.markdown("### Hi, I'm Naziya Mahimkar!")
    st.write("## Aspiring Data Scientist tuning complex data into solution. ")
    st.write("I am a final-year B. Tech student at Savitribai Phule Pune University, deeply passionate about Artificial Intelligence and Machine Learning. I thrive on turning innovative ideas into practical solutions and am always eager to collaborate on exciting AI/ML projects that push the boundaries of what's possible. *Always eager to create something extraordinary!* ")
    st.write("📫 Reach me at: [naziyamahimkar13@gmail.com](mailto:naziyamahimkar13@gmail.com)")
    st.write("🌐 [GitHub-Old](https://github.com/naziya-19) | [GitHub-New](https://github.com/naziya-22) | [LinkedIn](https://www.linkedin.com/in/naziya-mahimkar-29526122a/) | [Kaggle](https://www.kaggle.com/naziyamahimkar19)") 

# Resume Viewer - With Close Button
if 'show_resume' not in st.session_state:
    st.session_state.show_resume = False

if st.button("📄 View Resume"):
    st.session_state.show_resume = True

if st.session_state.show_resume:
    c1, c2 = st.columns(2)
    
    if st.button("❌ Close Resume Preview"):
        st.session_state.show_resume = False
        st.rerun()
    else:
        with open('Naziya_Mahimkar_resume.pdf', 'rb') as pdf_file:
            pdf_data = pdf_file.read()
            st.download_button(label="Download Resume", data=pdf_data, file_name="Naziya_Mahimkar_resume.pdf")
            st.markdown("---")
            st.write("### Resume Preview")
            pdf_viewer(pdf_data)


# Projects Section
st.markdown("## 💼 Projects")
proj_col1, proj_col2, proj_col3 = st.columns(3)

# Creating cards for projects with different background colors
with proj_col1:
    with st.container():
        st.markdown("<div style='background-color: #FFC1C1; padding: 10px; border-radius: 10px;'>", unsafe_allow_html=True)
        st.markdown("### Covid-19 Detection using X-rays")
        st.write("Developed a novel lightweight model for detection of covid 19.")
        st.markdown("[GitHub Link](https://github.com/naziya-19/Detection-of-Covid-19-and-Viral-Pneumonia-Using-X-rays-Images)")
        st.markdown("</div>", unsafe_allow_html=True)

        st.header(" ")
        st.markdown("<div style='background-color: #FFC1C1; padding: 10px; border-radius: 10px;'>", unsafe_allow_html=True)
        st.markdown("### Object Detection using AI")
        st.write("Detect some basic day to day life objects.")
        st.markdown("[GitHub Link](https://github.com/naziya-19/Colour-and-Object-Detection)")
        st.markdown("</div>", unsafe_allow_html=True)
        

with proj_col2:
    with st.container():
        st.markdown("<div style='background-color: #C1FFC1; padding: 10px; border-radius: 10px;'>", unsafe_allow_html=True)
        st.markdown("### Stock Market Prediction")
        st.write("Predicting stock prices using LSTM and sentiment analysis.")
        st.markdown("[GitHub Link](https://github.com/naziya-19/Stock-Market-Prediction)")
        st.markdown("</div>", unsafe_allow_html=True)

        st.header(" ")
        st.markdown("<div style='background-color: #C1FFC1; padding: 10px; border-radius: 10px;'>", unsafe_allow_html=True)
        st.markdown("### AI Tic - Tac - Toe")
        st.write("A simple application of AI in Tic Tac Toe Game using Minimax Algorithm using python turtle libirary.")
        st.markdown("[GitHub Link](https://github.com/naziya-19/AI-Tic-Tac-Toe?tab=readme-ov-file)")
        st.markdown("</div>", unsafe_allow_html=True)

with proj_col3:
    with st.container():
        st.markdown("<div style='background-color: #C1C1FF; padding: 10px; border-radius: 10px;'>", unsafe_allow_html=True)
        st.markdown("### OptiTrip - Tourist Path Optimization Website")
        st.write("Offer's optimal tourist paths for visiting places of interest using the Travelling Salesman Problem Algorithm.")
        st.markdown("[GitHub Link](https://github.com/naziya-19/optimal-path-finder)")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div style='background-color: #C1C1FF; padding: 10px; border-radius: 10px;'>", unsafe_allow_html=True)
        st.markdown("### File upload delete view in-mongo")
        st.write("CRUD operations app using MongoDB, Express, nodeJS.")
        st.markdown("[GitHub Link](https://github.com/naziya-19/image-upload-delete-view-in-mongo)")
        st.markdown("</div>", unsafe_allow_html=True)

# Articles Section
st.markdown("## 📝 Articles")
st.image(r'images\blog.png')
st.write("[Read my articles on Medium](https://medium.com/@naziyamahimkar13)")

# Footer
st.markdown("---")
st.write("⚡ Fun fact: I think I am funny 😄")
