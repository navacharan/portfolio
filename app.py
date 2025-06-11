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
    """
    Converts a local file to base64 for embedding (useful for images or PDFs).
    """
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
PROFILE_PIC = "https://via.placeholder.com/150" # Replace with your actual profile picture URL!
RESUME_PDF_PATH = "Navacharan.pdf" # Make sure this PDF exists in the same directory!

# --- Custom CSS for Styling ---
def local_css(file_name):
    """Loads custom CSS from a local file."""
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

try:
    local_css("style.css") # Ensure 'style.css' is in the same directory
except FileNotFoundError:
    st.warning("`style.css` not found. Some custom styling may not be applied. Please create the `style.css` file as instructed.")

# --- Navigation ---
st.sidebar.title("Navigate Through My Portfolio")
# Reordered navigation for a more logical flow
page = st.sidebar.radio("",
    ("About Me", "Education", "Skills", "Work Experience", "Projects", "Certifications", "Contact")
)

# --- Page Content ---
if page == "About Me":
    # --- HEADER SECTION ---

    st.title(f"Hi, I'm {NAME}! 👋")
    st.write(f"## {PROFESSION_ROLE}")

    st.write(
        "A passionate **Software Engineer** with a strong focus on **AI/ML**. "
        "I excel at developing innovative solutions, from **image-based disease detection** "
        "using CNNs to applying NLP for **sentiment analysis**. "
        "I'm eager to leverage my expertise in **Python, deep learning, and related technologies** "
        "to contribute to impactful AI/ML solutions, actively engaging in **research, model development, and optimization**."
    )

    st.markdown("---") # Separator
    st.subheader("Connect with Me:")
    st.markdown(f"- **Email:** [{EMAIL}](mailto:{EMAIL})")
    st.markdown(f"- **Phone:** {PHONE}")

    st.markdown(
        f'<div class="about-links">'
        f'<a href="{LINKEDIN_URL}" target="_blank">LinkedIn</a>'
        f'<a href="{GITHUB_URL}" target="_blank">GitHub</a>'
    , unsafe_allow_html=True)

    if Path(RESUME_PDF_PATH).exists():
        st.markdown(
            f'<a href="data:application/pdf;base64,{get_base64_of_bin_file(RESUME_PDF_PATH)}" download="Venkata_Charan_Grandhi_Resume.pdf" target="_blank">Download Resume</a>'
        , unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) # Close the 'about-links' div


elif page == "Skills":
    # --- SKILLS SECTION ---
    st.markdown("---")
    st.header("My Core Skills")

    # Grouping skills for better readability
    st.subheader("Programming Languages")
    st.markdown("""
        - Python (Proficient)
        - Java
        - HTML
        - SQL
    """)

    st.subheader("AI/ML & Deep Learning")
    st.markdown("""
        - Machine Learning Algorithms (e.g., SVM, Regression, Classification)
        - Deep Learning Architectures (CNNs, RNNs)
        - Natural Language Processing (NLP)
        - Computer Vision
        - Data Preprocessing & Feature Engineering
        - Model Evaluation & Optimization
    """)

    st.subheader("Frameworks & Libraries")
    st.markdown("""
        - Scikit-learn
        - TensorFlow
        - Keras
        - PyTorch (familiarity)
        - Matplotlib, Seaborn (Data Visualization)
    """)

    st.subheader("Tools & Platforms")
    st.markdown("""
        - Git, GitHub (Version Control)
        - Streamlit (Web App Development)
        - Jupyter Notebooks (Interactive Development)
    """)

    st.subheader("Concepts")
    st.markdown("""
        - Data Structures
        - Algorithms
        - Object-Oriented Programming (OOP)
    """)
    
    # --- Skills Visualization ---
    st.markdown("---")
    st.subheader("Skill Proficiency")
    skill_data = {
        "Python": 90, "Java": 80, "SQL": 80,
        "TensorFlow": 75, "Keras": 70, "Scikit-learn": 85,
        "PyTorch": 60, "Matplotlib": 70, "Git": 85
    }
    skills = list(skill_data.keys())
    proficiency = list(skill_data.values())
    st.bar_chart(
        {"Skill": skills, "Proficiency": proficiency},
        x="Skill",
        y="Proficiency",
        x_label="Skill Name", # Added label
        y_label="Proficiency Level (%)" # Added label
    )


elif page == "Education":
    # --- EDUCATION SECTION ---
    st.markdown("---")
    st.header("Education")
    st.subheader("B.Tech in Computer Science and Engineering")
    st.write("**Kalasalingam Academy of Research and Education**")
    st.write("*April 2020 - May 2024* | **CGPA: 8.1**")
    st.write("") # Keep for spacing for visual separation

    st.subheader("Intermediate (MPC)")
    st.write("**Vignana Bharathi Junior College**")
    st.write("*June 2018 - June 2020* | **CGPA: 8.2**")


elif page == "Work Experience":
    # --- WORK EXPERIENCE SECTION ---
    st.markdown("---")
    st.header("Work Experience")
    st.subheader("Software Engineer Trainee")
    st.write("**Lyros Technologies Private Limited** | Hyderabad")
    st.write("*February 2025 - Present*")
    st.markdown(
        """
        - Actively participating in a structured training program focused on **Artificial Intelligence and Machine Learning (AI/ML)**, gaining hands-on experience with cutting-edge technologies.
        - **Assisted in data collection, cleaning, and structuring datasets** for AI/ML training and analysis, ensuring data integrity for project success.
        - **Supported in designing, training, and evaluating machine learning models**, conducting performance testing, and suggesting improvements for accuracy and efficiency.
        - **Analyzed AI applications to propose optimization strategies**, focusing on improving computational efficiency and enhancing model scalability.
        - Engaged in **research and experimentation**, staying updated with the latest AI/ML advancements and contributing to innovative solutions.
        - Developed **basic scripts to automate repetitive tasks** and improve AI development workflows.
        - **Maintained clear and concise documentation** of AI/ML experiments, model performance, and project progress.
        - **Collaborated closely with experienced industry professionals and mentors** to enhance technical skills, problem-solving abilities, and overall professional competencies in the dynamic field of AI/ML.
        """
    )


elif page == "Projects":
    # --- PROJECTS SECTION ---
    st.markdown("---")
    st.header("Projects Showcase")

    # --- Project Type Filter ---
    project_types = ["Academic", "Personal", "Professional"]
    selected_type = st.selectbox("Select Project Type", project_types)

    if selected_type == "Personal":
        st.subheader("Bank Management System")
        st.write("A console-based **Bank Management System** developed using **Java**.")
        st.write("This project provides basic functionalities like creating accounts, depositing/w*ithdrawing funds, checking balances, and viewing transaction history. It demonstrates strong understanding of **Object-Oriented Programming (OOP)** principles and **data structures** for managing bank records effectively.")
        # Add a GitHub link if available: st.markdown("[View on GitHub](YOUR_GITHUB_LINK_HERE)")
        st.markdown("---")

    elif selected_type == "Professional":
        st.subheader("Student Grading System")
        st.write("Developed a comprehensive **Student Grading System** as part of my training at **Lyros Technologies Private Limited**, utilizing **Python** and **SQL** for database management.")
        st.write("This system streamlines the process of managing student grades, attendance, and performance reports. It features functionalities for adding/removing students, updating grades, calculating GPA, and generating performance summaries. This project enhanced my practical skills in **backend development** and **database interaction**.")
        # Add a GitHub link or project demo link if available: st.markdown("[View on GitHub](YOUR_GITHUB_LINK_HERE)")
        st.markdown("---")

    elif selected_type == "Academic":
        st.subheader("Paddy Crop Disease Detection Using SVM and CNN")
        st.success(
            """
            Developed a robust system for **automated paddy crop disease detection** by combining **Support Vector Machines (SVM)**
            and **Convolutional Neural Networks (CNN)**. This solution precisely analyzes images of paddy leaves
            to identify common diseases like blast, brown spot, and leaf smut, enabling farmers to take
            **early intervention measures** and significantly **improve crop yield**. This project showcased
            my ability to apply advanced machine learning techniques to real-world agricultural challenges.
            """
        )
        # Add a GitHub link if available: st.markdown("[View on GitHub](YOUR_GITHUB_LINK_HERE)")
        st.markdown("---") # Separator between academic projects

        st.subheader("Pneumonia Detection Using Chest X-ray")
        st.success(
            """
            Engineered an advanced **deep learning model leveraging CNNs** for the **accurate identification of pneumonia**
            from chest X-ray images, facilitating **prompt and precise diagnosis**. The project involved
            implementing sophisticated **data augmentation and preprocessing methods** to enhance model
            generalization capabilities and maximize diagnostic efficiency. This demonstrates my proficiency
            in medical image analysis and deep learning for critical applications.
            """
        )
        # Add a GitHub link if available: st.markdown("[View on GitHub](YOUR_GITHUB_LINK_HERE)")
        st.markdown("---") # Separator between academic projects

        st.subheader("Restaurant Review Sentiment Analysis")
        st.success(
            """
            Developed a comprehensive **restaurant review analysis system** utilizing **Natural Language Processing (NLP)**
            techniques to accurately analyze and classify customer sentiments. This system provides valuable insights
            that enhance decision-making for both diners and restaurant owners. I employed **advanced text processing
            algorithms** to extract key insights from unstructured review data, ultimately optimizing user experience and satisfaction.
            """
        )
        # Add a GitHub link if available: st.markdown("[View on GitHub](YOUR_GITHUB_LINK_HERE)")


elif page == "Certifications":
    # --- CERTIFICATIONS SECTION ---
    st.markdown("---")
    st.header("Certifications")
    st.markdown(
        """
        - **PROCESS MINING VIRTUAL INTERNSHIP** *(July 2022 - September 2022)*
        - **JAVA FULL STACK DEVELOPMENT** *(May 2024 - December 2024)*
        - **AI-900: MICROSOFT AZURE AI FUNDAMENTALS**
        """
    )

elif page == "Contact":
    # --- CONTACT SECTION ---
    st.markdown("---")
    st.header("Get In Touch!")
    st.write("Feel free to reach out if you have any questions, want to discuss a project, or just want to connect. I'm always open to new opportunities and collaborations!")

    # Formsubmit.co is used here for a simple contact form.
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
    st.write("You can also connect with me directly via:")
    st.markdown(f"- **Email:** [{EMAIL}](mailto:{EMAIL})")
    st.markdown(f"- **Phone:** {PHONE}")
    st.markdown(f"- **LinkedIn:** [My LinkedIn Profile]({LINKEDIN_URL})")
    st.markdown(f"- **GitHub:** [My GitHub Profile]({GITHUB_URL})")

else:
    st.write("Please select a page from the navigation menu to explore my portfolio.")

# --- Footer ---
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: #888; font-size: 0.8em;'>© 2025 {NAME}. All rights reserved. Built with Streamlit.</p>", unsafe_allow_html=True)