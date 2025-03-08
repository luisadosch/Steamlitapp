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
##### *Projects* 
''')

# Display profile image
image = Image.open('ld.png')
st.image(image, width=150)


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
# Footer
st.markdown('''
<nav class="navbar fixed-bottom navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="/">Luisa Dosch</a>
</nav>
''', unsafe_allow_html=True)
