import streamlit as st
import pandas as pd
import streamlit.components.v1 as components  # Für HTML-Komponente

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# --- Home Page ---
if page == "Home":
    st.image("ld.png", width=200)
    st.title("Welcome to My Portfolio")
    st.write("I am an information systems student passionate about machine learning, data science, and AI research.")
    st.write("Feel free to explore my projects and get in touch!")
   



# --- Projects Page ---
if page == "Projects":
    st.title("My Projects")
    tabs = st.tabs(["Image Inpainting", "Pedestrian Flow Forecasting", "Airbnb Pricing", "Ice Cream Shop Simulation"])
    
    # --- Project 1 ---
    with tabs[0]:
        st.header("AI-Driven Image Inpainting")
        # here picture object_removal_comparison.jpg
        st.image("object_removal_comparison.jpg", width=700)
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
            
            # --- Project 1 Tables (Fixed) ---

            # Small Mask Data (Convert percentages to floats and rankings to integers)
            small_mask_data = pd.DataFrame({
                "Model": ["LaMa", "Telea (Baseline)", "Stable Diffusion"],
                "Improvement (%)": [0.17, 0.0, -21.48],  # Store as floats
                "Ranking": ["1", "2", "3"]  # Remove asterisks for clean display
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
            
            # Key Findings
            st.markdown('##### Key Findings')
            st.markdown('''
            - AI-based models outperform Telea by approximately 14%.
            - Mask size is a critical factor; **Stable Diffusion** excels with large masks (despite potential hallucinations), while **LaMa** performs best for small-to-medium masks. **Telea** stays relevant for small masks.
            - Future work focuses on improving model efficiency and reducing unwanted object generation.
            ''')

    # --- Project 2 ---
    with tabs[1]:
        st.image("Würzburg.jpg", width=200)
        st.header("Machine Learning and Deep Learning-Based Time Series Probabilistic Forecasting of Pedestrian Movement")
        # Here you can add an image related to the project if available
        # st.image("pedestrian_forecasting.jpg", width=700)
        st.markdown('''
- **Description:** Developed probabilistic time series forecasting models to predict pedestrian flow in Würzburg using advanced Machine Learning (ML) and Deep Learning (DL) techniques. The goal was to generate accurate foot traffic predictions across different time horizons (2-day and 7-day) to support data-driven retail operations, including optimized staffing and inventory management.
- **Technologies Used:** Python, PyTorch, Neuralforecast, Scikit-learn
- **Challenges:** Dataset preparation for time series forecasting, feature engineering (holidays, special events, lag features, weather comparisons), probabilistic forecasting, model evaluation using Multi-Quantile Loss (MQL) and Mean Absolute Error (MAE).
- **Models Used:** Long Short-Term Memory (LSTM), LightGBM, CatBoost, Quantile Random Forest, Quantile Regression.
- **Findings:** CatBoost and LightGBM outperformed other models in accuracy for both short-term (2-day) and long-term (7-day) forecasts. Key factors influencing pedestrian flow include day of the week, seasonal trends, and time of day. 
        ''')
        
        if st.button('View Project 2 Details'):
            st.markdown('''
            - **Code Repository:** https://github.com/luisadosch/Code---BA
            ''')
            st.markdown('### Forecasting Results')
            
            # Data for forecasting performance
  
            forecast_data = pd.DataFrame({
                'Method': ['CatBoost', 'LightGBM', 'LSTM', 'RandomForest', 'Quantile Regression', 'Empirical Quantiles'],
                'Improvement_MAE_2d': ['68.90%', '69.17%', '68.08%', '68.34%', '62.54%', '0.00%'],
                'Improvement_MAE_7d': ['67.95%', '68.83%', '67.44%', '67.48%', '62.22%', '0.00%'],
                'Improvement_MAE_48h': ['76.90%', '74.01%', '76.93%', '72.66%', '68.04%', '0.00%'],
                'Improvement_MAE_168h': ['77.68%', '75.15%', '75.59%', '73.25%', '70.06%', '0.00%']
            })
            
            st.dataframe(forecast_data)

            st.markdown('''
            - **Daily Data:** The MAE values, ranging from 2594 to 3252, represent a relatively small percentage of the average daily pedestrian count, approximately 20,525. For instance, an MAE of 2677 equates to an average error of around 13%, which indicates a reasonable level of accuracy.
            - **Hourly Data:** Considering the average hourly pedestrian count is approximately 797.78, an MAE of 163.07 translates to an error of about 20.44%. This indicates that these models can provide relatively accurate forecasts, with error rates just above 20% of the hourly average.
            ''')

            st.image("day_results_without_weather.png", width=700)
            st.markdown('- Average performance improvement in MQL of best performing models of daily data')
            st.image("hour_results_without_weather.png", width=700)
            st.markdown('- Average performance improvement in MQL of best performing models of hourly data')


            
            # Key Findings
            st.markdown('##### Key Findings')
            st.markdown('''
            - **Temporal Factors:** Foot traffic peaks on Saturdays and drops on Sundays, necessitating dynamic staffing and inventory strategies.
            - **Weather Influence:** Extreme temperatures impact foot traffic, but overall weather effects are minor.
            - **Seasonal Trends:** Higher foot traffic in May, June, July, and December requires seasonal adjustments in operations.
            - **Hourly Trends:** Peak pedestrian activity occurs between 11:00 AM and 1:00 PM, guiding optimal shift scheduling.
            - **Model Performance:** CatBoost and LightGBM delivered the best accuracy.
            - **Key Predictive Drivers:** 7-day lag of pedestrian counts, day of the week, and location-specific factors played a crucial role.
            ''')
            st.image("locations.jpg", width=700)
            st.markdown('''By leveraging these models, retailers can optimize resource allocation, improve forecasting accuracy, and enhance decision-making for better operational efficiency.''')

                      
          
    
    # --- Project 3 ---
    with tabs[2]:
        st.header("Predicting Airbnb Prices with Machine Learning")
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
            st.markdown('### Map of Airbnb Prices in Prague')
            with open('airbnb_prices.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            components.html(html_content, width=700, height=500)

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

 
    
    # --- Project 4 ---
    with tabs[3]:
        st.header("Ice Cream Shop Simulation Study")
        st.markdown('''
        - **Description:** Conducted a simulation study to optimize the throughput of an ice cream shop.
        - **Technologies Used:** Python, simpy
        - **Challenges:** Designing the simulation model, validating the model, analyzing the results
        - **Outcome:** Provided insights into the optimal number of employees and reduced waiting times for customers by over 60%.
        ''')
        st.image('simulation_project.jpeg', width=700)
        
        if st.button('View Project 4 Details'):
            st.markdown('''
            - **Code Repository:** [https://github.com/luisadosch/A-Simulation-Study](https://github.com/luisadosch/A-Simulation-Study)
            ''')
            st.markdown('### Simulation Model Flowchart')
            st.image('Flowchart.jpeg', width=700)

            st.markdown('### Best Model Configuration')
            # Daten
            data = {
                'Configuration': ['Ice Cream Shop', 'Best Dynamic', 'Second Best Static', 'Best Static'],
                'Threshold 2 Cashiers': ["5", "3", "2", "3"],
                'Threshold 3 Cashiers': ["9", "5", " ", " "],
                'Mean Waiting Time (seconds)': ["175", "133", "63", "49"]
            }

            # DataFrame erstellen
            df = pd.DataFrame(data)

            # Setze die Spalte "Model" als Index
            df.set_index("Configuration", inplace=True)

            # Tabelle anzeigen
            st.table(df)


            # Subtitel "Key Findings"
            st.markdown('##### Data & Decision')
            # Text anzeigen
            st.markdown('''
                        - Recommendation: Maintain a minimum of two cashiers at all times for the ice cream shop.
                        ''')


# --- Contact Page ---
elif page == "Contact":
    st.title("Get in Touch")
    st.write("📧 Email: [luisadosch@gmx.de](luisadosch@gmx.de)")
    st.write("🔗 LinkedIn: [Luisa Dosch](https://www.linkedin.com/in/luisadosch/)")
