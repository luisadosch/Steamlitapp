import streamlit as st
from PIL import Image
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Load CSS for styling
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="/">Luisa Dosch</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#cv">CV<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Header
st.write('''
# Luisa Dosch
##### *Resume* 
''')

# Display profile image
image = Image.open('ld.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Strong communication and interpersonal skills developed through various internships and freelance positions.
- Passionate about data science and machine learning with hands-on experience in predictive modeling.
''')

#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)

def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)

#####################
# CV Section
st.markdown('<a id="cv"></a>', unsafe_allow_html=True)
st.markdown('''
## Personal Information
''')
st.markdown('''
- **Address:** Neydeckgasse 6, 97082 Würzburg
- **Contact:** +49 1758175688
- **Email:** [luisadosch@gmx.de](mailto:luisadosch@gmx.de)
''')

#####################
# Work Experience Section
st.markdown('''
## Work Experience
''')
txt('**Data Engineer, Working Student, BDS - Business Data Solutions, Rimpar**', '11/2024 - Present')
st.markdown('''
- Handling multiple stages of the **data analysis pipeline**, including **data collection, cleaning, and evaluation**.  
- Working with **Python** and **SQL** to process, transform, and analyze data efficiently.  
- Cleaning and preprocessing web-scraped data using **regular expressions (regex)**.  
- Managing databases using **PostgreSQL** and **MongoDB**, ensuring structured and unstructured data are optimized for analysis.  
- **Prompt Engineering:** Optimizing input prompts for **LLMs**, preparing and structuring data before passing it to AI models, and testing different **LLM APIs** for cost-effectiveness and performance evaluation.  
- Documenting workflows and processes in **Confluence** for knowledge sharing and reproducibility.  
- Using **JIRA** for project management, task tracking, and agile development.  
- Utilizing **Git** for version control, ensuring efficient collaboration, and tracking changes across multiple data processing scripts and models.  
''')

txt('**Teaching Assistant, University of Würzburg - Data Driven Decisions Group**', '06/2024 - 08/2024')
st.markdown('''
- Assisted in the development of the course "Data Driven Supply Chain Management".
- Prepared exercises in python building on the machine learning packages Scikit-learn and PyTorch.
''')
txt('**Change Management, Working Student, Bosch Rexroth, Lohr**', '08/2023 - 01/2024')
st.markdown('''
- Conducted data analysis using Power BI.
- Prepared presentations for optimizing workflows.
''')
txt('**Business Excellence, Working Student, Siemens, Frankfurt**', '12/2022 - 06/2023')
st.markdown('''
- Maintained data in Salesforce and SAP.
- Conducted data analysis using Excel.
- Created sales pitches in Highspot.
- Performed market analysis to identify potential customers.
''')
txt('**Financial Services Consulting, Intern, PwC, Frankfurt**', '08/2022 - 11/2022')
st.markdown('''
- Developed new reporting processes using Power BI and Excel.
- Prepared presentations for clients.
''')
txt('**Social Business Development, Freelance, Up4distribution**', '06/2021 – 11/2022')
st.markdown('''
- Created customized website and social media content, blogs, campaigns, and pitch documents for various clients of an international startup accelerator.
- Scheduled meetings with investors for various international startups.
''')


# Education Section
st.markdown('''
## Education
''')

# Master's Degree
txt('**M.Sc in Information Systems, Julius-Maximilians-University Würzburg**', '04/2025 - 04/2027')
st.markdown('''
- **Seminar-Thesis:** 'AI-Driven Image Inpainting, implemented with Python'
''')

# Bachelor's Degree
txt('**B.Sc in Information Systems, Julius-Maximilians-University Würzburg**', '10/2021 - 03/2025')
st.markdown('''
- **Bachelor-Thesis:** 'Probabilistic Forecasting Of Pedestrian Flow Using Machine Learning, implemented with Python'
- **Seminar Thesis:** "Predicting Airbnb Prices with Machine Learning, implemented with Python"
- **Courses:** Statistics, Database Systems, Software Engineering, Applied Econometrics, Programming, Web Programming
''')

#####################
# Extracurricular Activities Section
st.markdown('''
## Extracurricular Activities
''')
txt('**Buddy for International Students, Würzburg**', '10/2022 – 08/2023')
st.markdown('''
- Planned events and acted as a point of contact for international students.
''')
txt('**Tutor, AuxiliO Würzburg**', '01/2021 – 06/2021')
st.markdown('''
- Provided tutoring in mathematics and English for students in grades 5 to 10.
- Offered tutoring sessions for children with dyslexia.
''')

#####################
# Skills Section
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `Java`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`, `pytorch`')
txt3('Web development', '`HTML`, `CSS`, `JavaScript`')
txt3('Model deployment', '`streamlit`')

#####################
# Projects Section
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.markdown('''
## Projects
''')





st.markdown('### Project 1: AI-Driven Image Inpainting')
st.markdown('''
- **Description:** Explores how modern generative AI transforms image inpainting compared to classic techniques by benchmarking **LaMa** and **Stable Diffusion** against the traditional **Telea** method.
- **Technologies Used:** Python, PyTorch, Stable Diffusion, LaMa, OpenCV, Pandas
- **Challenges:** Image preparation, mask improvement, model evaluation, bootstrapping, significance testing.
- **Models Used:** LaMa, Stable Diffusion (Hugging Face), Telea (OpenCV)
- **Findings:** AI-based models outperform traditional inpainting methods. Mask size is a critical factor influencing model performance and model selection.
''')
if st.button('View Project 1 Details'):
    st.markdown('''
    - **Code Repository:** [https://github.com/luisadosch/MaSeInpaint](https://github.com/luisadosch/MaSeInpaint)
    ''')

    st.markdown('### Inpainting Results')
    st.image('viswithtitle1.png', width=700)

    
    
    # Display title and description
    st.markdown('### Results and Model Comparison')
    
     # Data for tables
    small_mask_data = pd.DataFrame({
        "Model": ["LaMa", "Telea (Baseline)", "Stable Diffusion"],
        "Improvement to Baseline (%)": ["+0.17%", "0%", "-21.48%"],
        "Ranking": ["1", "2", "3*"]
    })
    
    medium_mask_data = pd.DataFrame({
        "Model": ["LaMa", "Telea (Baseline)", "Stable Diffusion"],
        "Improvement to Baseline (%)": ["+11.67%", "0%", "+3.83%"],
        "Ranking": ["1*", "3*", "2*"]
    })
    
    large_mask_data = pd.DataFrame({
        "Model": ["LaMa", "Telea (Baseline)", "Stable Diffusion"],
        "Improvement to Baseline (%)": ["+14.27%", "0%", "+18.78%"],
        "Ranking": ["2*", "3*", "1*"]
    })
    
    overall_data = pd.DataFrame({
        "Model": ["LaMa", "Telea (Baseline)", "Stable Diffusion"],
        "Improvement to Baseline (%)": ["+14.64%", "0%", "+13.40%"],
        "Ranking": ["1*", "3*", "2*"]
    })
    
    # Display tables
    st.markdown('#### Small Mask')
    st.dataframe(small_mask_data)
    
    st.markdown('#### Medium Mask')
    st.dataframe(medium_mask_data)
    
    st.markdown('#### Large Mask')
    st.dataframe(large_mask_data)
    
    st.markdown('#### Overall')
    st.dataframe(overall_data)
 
    # Subtitle "Key Findings"
    st.markdown('##### Key Findings')
    
    # Display text
    st.markdown('''
    - AI-based models outperform Telea by approximately 14%.
    - Mask size is a critical factor; **Stable Diffusion** excels with large masks (despite potential hallucinations), while **LaMa** performs best for small-to-medium masks.
    - Future work focuses on improving model efficiency and reducing unwanted object generation.
    ''')


st.markdown('### Project 2: Probabilistic Forecasting Of Pedestrian Flow Using Machine Learning')


st.markdown('### Project 3: Predicting Airbnb Prices with Machine Learning')
st.markdown('''
- **Description:** Developed a predictive model using machine learning algorithms to forecast Airbnb prices based on various features such as location, amenities, and property type.
- **Technologies Used:** Python, scikit-learn, pandas, osmnx, geopandas
- **Challenges:** Handling missing data, feature engineering, model evaluation
- **Models Used:** Random Forest Regressor, Linear Regression, Geospatial Models like SLX and SAR
- **Findings:** Key factors influencing property prices include location, property size, and proximity to attractions. Spatial influences also play a role.
''')
if st.button('View Project 3 Details'):
    st.markdown('''
    - **Code Repository:** [https://github.com/luisadosch/Seminar_Airbnb](https://github.com/luisadosch/Seminar_Airbnb)
    ''')


    # Display the html map

   # show the html airbnb_prices.html

   # Display title and description
    st.markdown('### Map of Airbnb Prices in Prague')

    # Read the HTML file and display it in Streamlit
    with open('airbnb_prices.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Embed the HTML map in Streamlit
    st.components.v1.html(html_content, width=700, height=500)

    st.markdown('''
    - The dots represent Airbnb listings in Prague. Brighter colors indicate higher prices.
    - As expected, the highest prices are concentrated in the Old Town of Prague.
    ''')



    # Display title and description
    st.markdown('### Results and Model Comparison')
    # Daten erstellen
    data = {
        "Model": ["Ordinary Least Squares Regression", "Geospatial Regression", "Random Forest", "Random Forest (with POIs)"],
        "Property Features": ["x", "x", "x", "x"],
        "POI Features": ["", "x", "", "x"],
        "Spatial Lag": ["", "x", "", ""],
        "Spatial Cross Correlation": ["", "x", "", ""],
        "Relative Improvement RMSE": ["0%", "8%", "-2%", "14%"]
    }

    # DataFrame erstellen
    df = pd.DataFrame(data)

    # Setze die Spalte "Model" als Index
    df.set_index("Model", inplace=True)

    # Tabelle anzeigen
    st.table(df)

    # Subtitel "Was sind Points of Interest (POIs)?"
    st.markdown('##### What are Points of Interest (POIs)?')

    # Text anzeigen
    st.markdown('''
    - Points of Interest (POIs) are locations that may attract people, such as restaurants, bars, and public transportation.
                ''')
    
    # Subtitel "Was ist ein Spatial Lag? Was ist eine Spatial Cross Correlation?"
    st.markdown('##### What are Spatial Lags and Spatial Cross Correlation?')

    # Text anzeigen
    st.markdown('''
    - **Spatial Lag:** The spatial lag measures the influence of neighboring properties' prices on the price of a property. It captures the spatial autocorrelation of property prices.
    - **Spatial Cross Correlation:** The spatial cross correlation measures the relationship between the spatial distribution of different variables. It captures the spatial dependence between different features.
    ''')

    # Subtitel "Key Findings"
    st.markdown('##### Key Findings')

    # Text anzeigen
    st.markdown('''
                - **Effect of Space:** Considering the influence of space can improve price predictions.
                - **Best Models:** The best models are either linear models with complex features (spatial regression)
                 or non-linear models (random forest) with simpler geospatial features (POIs).
                ''')

 

st.markdown('### Project 4: Simulation Study on an Ice Cream Shop')
st.markdown('''
- **Description:** Conducted a simulation study to optimize the throughput of an ice cream shop.
- **Technologies Used:** Python, simpy
- **Challenges:** Designing the simulation model, validating the model, analyzing the results
- **Outcome:** Provided insights into the optimal number of employees and reduced waiting times for customers by over 60%.
''')
if st.button('View Project 4 Details'):
    st.markdown('''
    - **Code Repository:** [https://github.com/luisadosch/A-Simulation-Study](https://github.com/luisadosch/A-Simulation-Study)
    ''')
    st.image('simulation_project.jpeg', width=700)



#####################
# Personal Interests Section
st.markdown('''
## Personal Interests
''')
st.markdown('''
- Traveling, Outdoors, Coffee, Sports (Crossfit, Running, Hiking, Cycling, Swimming)
''')

#####################
# Footer
st.markdown('''
<nav class="navbar fixed-bottom navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="/">Luisa Dosch</a>
</nav>
''', unsafe_allow_html=True)
