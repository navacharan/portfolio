import streamlit as st
import base64
from pathlib import Path

# --- Configuration ---
st.set_page_config(
    page_title="Venkata Nava Charan Grandhi - Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="auto"
)

# --- Helper Function for Local Files ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- General Settings ---
NAME = "VENKATA NAVA CHARAN GRANDHI"
PROFESSION_ROLE = "Software Engineer | AI/ML Engineer"
EMAIL = "navacharangrandhi@gmail.com"
PHONE = "6300868164"
LINKEDIN_URL = "https://www.linkedin.com/in/grandhi-venkata-nava-charan-5405b3210/"
GITHUB_URL = "https://github.com/navacharan"
RESUME_PDF_PATH = "Navacharan.pdf"

# --- Custom CSS for Styling ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

try:
    local_css("style.css")
except FileNotFoundError:
    st.warning("`style.css` not found. Some custom styling may not be applied. Please create the `style.css` file as instructed.")

# --- Navigation ---
st.sidebar.image("RAJ_0081-.jpg", width=200)
st.sidebar.title("Portfolio Navigation")
page = st.sidebar.radio("📂 Menu",
    [
        "👤 About Me",
        "🎓 Education",
        "🛠️ Skills",
        "💼 Work Experience",
        "📁 Projects",
        "📜 Certifications",
        "📬 Contact"
    ],
    label_visibility="visible"
)

# --- Page Content ---
if page == "👤 About Me":
    st.title(f"Hi, I'm {NAME}! 👋")
    st.write(f"## {PROFESSION_ROLE}")
    with st.container():
        st.markdown("## 👨‍💻 About Me")
        st.markdown("""
Hi, I'm **Venkata Nava Charan Grandhi** — a dedicated software engineer and AI/ML enthusiast committed to transforming complex challenges into impactful, real-world solutions.

With practical experience in **Java Full Stack Development** and AI/ML domains like **pneumonia detection** and **paddy disease classification**, I blend curiosity, technical expertise, and a deep desire to learn into everything I build.

🔍 **What drives me:**
- Building clean, efficient, and meaningful software  
- Exploring data to uncover valuable insights  
- Solving real problems with purposeful technology  

💡 I believe in continuous learning, collaborative development, and staying ahead of the curve in this rapidly evolving tech world.

When I’m not coding, I enjoy diving into emerging tools, engaging in virtual internships, and exploring new opportunities to sharpen my skills and grow as a developer.
""")

    

elif page == "🛠️ Skills":
    st.markdown("---")
    st.header("My Core Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Programming Languages 🧑‍💻")
        st.markdown("""
        - ![Python](https://img.icons8.com/color/24/000000/python--v1.png) Python (Proficient)  
        - ![Java](https://img.icons8.com/color/24/000000/java-coffee-cup-logo--v1.png) Java  
        - ![HTML](https://img.icons8.com/color/24/000000/html-5--v1.png) HTML  
        - ![SQL](https://img.icons8.com/color/24/000000/sql.png) SQL
        """)

        st.subheader("Frameworks & Libraries 📚")
        st.markdown("""
        - Scikit-learn  
        - TensorFlow  
        - Keras  
        - PyTorch (familiarity)  
        - Matplotlib, Seaborn
        """)

        st.subheader("Concepts")
        st.markdown(""" 
        - Object-Oriented Programming (OOP)
        """)

    with col2:
        st.subheader("AI/ML & Deep Learning 🤖")
        st.markdown("""
        - Machine Learning Algorithms (SVM, Regression, Classification)  
        - Deep Learning (CNNs, RNNs)  
        - Natural Language Processing (NLP)  
        - Computer Vision  
        - Data Preprocessing & Feature Engineering  
        - Model Evaluation & Optimization
        """)

        st.subheader("Tools & Platforms 🛠️")
        st.markdown("""
        - Git  
        - GitHub  
        - Streamlit  
        - Jupyter Notebooks
        """)


elif page == "🎓 Education":
    st.markdown("---")
    st.header("Education")
    st.subheader("🎓 B.Tech in Computer Science and Engineering")
    st.write("**Kalasalingam Academy of Research and Education**")
    st.write("*April 2020 - May 2024* | **CGPA: 8.1**")

    st.subheader("🏫 Intermediate (MPC)")
    st.write("**Vignana Bharathi Junior College**")
    st.write("*June 2018 - June 2020* | **CGPA: 8.2**")

elif page == "💼 Work Experience":
    st.markdown("---")
    st.header("💼 Work Experience")
    st.subheader("Software Engineer Trainee")
    st.write("**Lyros Technologies Private Limited** | Hyderabad")
    st.write("*February 2025 - Present*")
    st.markdown("""
        - Actively participating in a structured training program focused on **Artificial Intelligence and Machine Learning (AI/ML)**, gaining hands-on experience with cutting-edge technologies.
        - **Assisted in data collection, cleaning, and structuring datasets** for AI/ML training and analysis, ensuring data integrity for project success.
        - **Supported in designing, training, and evaluating machine learning models**, conducting performance testing, and suggesting improvements for accuracy and efficiency.
        - **Analyzed AI applications to propose optimization strategies**, focusing on improving computational efficiency and enhancing model scalability.
        - Engaged in **research and experimentation**, staying updated with the latest AI/ML advancements and contributing to innovative solutions.
        - Developed **basic scripts to automate repetitive tasks** and improve AI development workflows.
        - **Maintained clear and concise documentation** of AI/ML experiments, model performance, and project progress.
        - **Collaborated closely with experienced industry professionals and mentors** to enhance technical skills, problem-solving abilities, and overall professional competencies in the dynamic field of AI/ML
    """)

elif page == "📁 Projects":
    st.markdown("---")
    st.header("Projects Showcase")
    project_types = ["Academic", "Personal", "Professional"]
    selected_type = st.selectbox("Select Project Type", project_types)

    if selected_type == "Personal":
        with st.expander("💻 Bank Management System"):
            st.markdown("""
            **Objective:** To build a basic bank system that handles account operations using object-oriented programming.

            **Overview:** Java-based console application managing deposits, withdrawals, and transaction history.

            **Features:**
            - Account creation & management
            - Balance inquiry
            - Transaction logs
            - User-friendly interface for CLI operations
            - Efficient handling of invalid entries and exceptions
            """)

    elif selected_type == "Professional":
        with st.expander("📊 Student Grading System"):
            st.markdown("""
            **Objective:** To automate student performance tracking within the training team.

            **Overview:** Python and SQL-powered system for recording grades and attendance.

            **Features:**
            - Grade entry interface
            - Analytics for performance tracking
            - Admin and student portals
            - Dynamic reports generation
            - Visual dashboards for insights
            - Export functionality for grade reports
            - Integration with email notifications
            """)
            st.markdown("#### 📸 Sample Output")
            st.image("Screenshot 2025-06-12 170601.png", caption="Student grading system- Streamlit App Output")

        with st.expander("🚗 Used Car Price Calculator"):
            st.markdown("""
            **Objective:** To predict the price of a used car based on its features.

            **Overview:** A user-friendly Streamlit app that estimates the value of a car using multiple parameters like year, mileage, model, and drivetrain.

            **Tech Stack:** Streamlit, Python

            **Features:**
            - Interactive form for input
            - Price prediction using regression
            - JSON-style result display for transparency
            """)

            st.markdown("#### 📸 Sample Output")
            st.image("Screenshot 2025-06-12 162056.png", caption="Used Car Price Calculator - Streamlit App Output")

            st.markdown("#### 🎯 Example Price Estimation:")
            year = st.number_input("Year", min_value=1900, max_value=2025, value=2001)
            mileage = st.number_input("Mileage", min_value=0, max_value=1000000, value=86132)
            predicted_price = 10000 - (year - 2000) * 500 - mileage * 0.1
            st.success(f"Predicted Price: ${predicted_price:.2f}")

    elif selected_type == "Academic":
        with st.expander("🌾 Paddy Crop Disease Detection"):
            st.markdown("""
            **Objective:** Early detection of crop disease using image processing techniques.

            **Overview:** CNN and SVM used for classifying infected rice leaves from custom datasets.

            **Tech Stack:** OpenCV, TensorFlow, Streamlit

            **Highlights:**
            - Achieved over 90% accuracy
            - Streamlit app with disease prediction results
            - Real-time detection and classification
            - User feedback-based iterative model improvement
            """)

        with st.expander("🩺 Pneumonia Detection from X-ray"):
            st.markdown("""
            **Objective:** To assist diagnosis through chest X-ray image classification using deep learning.

            **Overview:** CNN model with Flask backend serving inference for uploaded X-ray images.

            **Tech Stack:** Flask, TensorFlow, Keras

            **Features:**
            - Real-time classification with diagnostic output
            - Simple frontend for X-ray upload
            - Evaluation using precision-recall metrics
            - ROC analysis and threshold tuning
            """)
            st.markdown("#### Sample Chest X-ray Input")
            st.image("person260_bacteria_1222.jpeg", caption="X-ray Sample")

            st.markdown("#### Model Output:")
            st.success("Prediction: **Pneumonia Detected**")

            st.markdown("#### Model Accuracy:")
            st.metric(label="Accuracy", value="93.7%")

        with st.expander("🗣️ Sentiment Analysis of Reviews"):
            st.markdown("""
            **Objective:** Predict the sentiment of restaurant reviews using NLP.

            **Overview:** Preprocessing of user reviews with sentiment classification using multiple models.

            **Tools Used:** NLTK, Scikit-learn, Streamlit

            **Features:**
            - TF-IDF vectorization
            - Multi-model evaluation
            - Interactive GUI for review input
            - Model comparison and error visualization
            """)

elif page == "📜 Certifications":
    with st.container():
        st.subheader("📜 Certifications")

        st.markdown("""
        ### ✅ JAVA FULL STACK DEVELOPMENT  
        **Duration:** *May 2024 – Dec 2024*  
        - Hands-on training in full-stack development using **Java, Spring Boot, Hibernate**.  
        - Built dynamic web apps with **REST APIs, JSP/Servlets**, and frontend tech like **HTML, CSS, JavaScript**.  
        - Practiced **Agile development**, version control (Git), and deployment strategies.  

        ---

        ### ✅ AI-900: Microsoft Azure AI Fundamentals  
        **Year:** *2023*  
        - Microsoft-certified foundational course in **AI and Machine Learning** concepts.  
        - Explored **Computer Vision, NLP**, and Azure Cognitive Services.  
        - Learned how to **train, test, and deploy AI models** on Microsoft Azure.  
        - Studied **responsible AI** and ethical guidelines.

        ---

        ### ✅ Process Mining Virtual Internship  
        **Duration:** *Jul 2022 – Sep 2022*  
        - Interned virtually with exposure to **process mining techniques** using tools like **Celonis**.  
        - Extracted event logs, analyzed bottlenecks, and optimized workflows.  
        - Developed an understanding of **data-driven decision making** and business process improvement.  
        """)


elif page == "📬 Contact":
    st.markdown("---")
    st.header("Get In Touch!")
    st.write("I'm always open to connecting — feel free to reach out!")

    contact_form = f"""
    <form action="https://formsubmit.co/{EMAIL}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required rows="5"></textarea>
        <button type="submit">Send Message</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    st.write("---")
    st.markdown("### 📬 Connect with me:")
    st.markdown(f"- 📧 **Email:** [{EMAIL}](mailto:{EMAIL})")
    st.markdown(f"- 📱 **Phone:** {PHONE}")
    st.markdown(f"- ![LinkedIn](https://img.icons8.com/ios-filled/20/0e76a8/linkedin.png) [LinkedIn]({LINKEDIN_URL})")
    st.markdown(f"- ![GitHub](https://img.icons8.com/ios-glyphs/20/000000/github.png) [GitHub]({GITHUB_URL})")
    if Path(RESUME_PDF_PATH).exists():
        st.markdown(
            f'<a href="data:application/pdf;base64,{get_base64_of_bin_file(RESUME_PDF_PATH)}" download="Venkata_Charan_Grandhi_Resume.pdf" target="_blank">📄 Download Resume</a>',
            unsafe_allow_html=True
        )

st.markdown("---")
st.markdown(f"<p style='text-align: center; color: #888; font-size: 0.8em;'>© 2025 {NAME}. All rights reserved. Built with Streamlit.</p>", unsafe_allow_html=True)
