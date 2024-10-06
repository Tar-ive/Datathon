import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

def main():
    st.set_page_config(page_title="Monarch Butterfly Sightings Analysis", layout="wide")
    st.title("Monarch Butterfly Sightings Analysis")

    # Project Origin
    st.header("Project Origin")
    st.write("""
    This project began with the ambitious task of scraping data from the Journey North website, 
    a comprehensive resource for tracking monarch butterfly migrations. Our initial dataset combined 
    spring and fall data, resulting in approximately 166,000 observations of monarch butterfly sightings.

    The data collection process evolved as follows:
    1. Initially, we scraped both "Monarch (Other)" and adult monarch butterfly data from Journey North.
    2. Upon analysis, we realized the need to focus specifically on adult monarch butterflies for more accurate migration patterns.
    3. We then refined our scraping process to collect adult monarch butterfly data from 2017-2024.

    During the data cleaning process, we faced several challenges:
    - Due to an error in our scraping process, the data was initially formatted incorrectly, which took several hours to identify and resolve.
    - We reduced the dataset to about 111,000 observations after cleaning and dropping missing columns.
    - We standardized date formats, corrected inconsistencies in location names, and converted coordinates to a uniform format.

    These challenges highlight the importance of careful data collection and cleaning in ensuring the accuracy of our analysis.
    """)

    # Load and display basic statistics
    st.header("Dataset Overview")
    df = pd.read_csv("cleaned_merged.csv")
    df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime
    st.write(f"Total number of observations: {len(df):,}")
    st.write(f"Date range of observations: from {df['Date'].min().strftime('%m/%d/%Y')} to {df['Date'].max().strftime('%m/%d/%Y')}")
    st.write(f"Number of unique locations: {df['Town'].nunique():,}")

    # Geographic Distribution of Monarch Butterfly Sightings
    st.header("Geographic Distribution of Monarch Butterfly Sightings")
    image_path = "Screenshot 2024-10-06 at 9.46.19 AM.png"
    if os.path.exists(image_path):
        image_geo = Image.open(image_path)
        st.image(image_geo, caption="Heatmap of Monarch Butterfly Sightings Across the United States", use_column_width=True)
    else:
        st.write("Image not found. The geographic distribution map is currently unavailable.")

    # Add the new heatmap image
    image_path_heatmap = "image.webp"
    if os.path.exists(image_path_heatmap):
        image_heatmap = Image.open(image_path_heatmap)
        st.image(image_heatmap, caption="Heatmap of Monarch Butterfly Sightings Distribution", use_column_width=True)
    else:
        st.write("Heatmap image not found. The detailed distribution map is currently unavailable.")

    # Add explanation for the heatmap
    st.write('''
    This heatmap provides a more detailed view of monarch butterfly sighting distributions across North America. 
    The red areas indicate higher concentrations of sightings, while blue areas show lower concentrations. 
    This visualization helps identify key regions for monarch butterfly populations and migration routes.
    ''')

    # Visualizations
    st.header("Visualizations")

    # Monarch Butterfly Population Trend
    st.subheader("Monarch Butterfly Population Trend")
    image_path = "download.png"
    if os.path.exists(image_path):
        image1 = Image.open(image_path)
        st.image(image1, caption="Monarch Butterfly Population Trend", use_column_width=True)
    else:
        st.write("Image not found. The Monarch Butterfly Population Trend graph is currently unavailable.")

    # Top 10 States and Monarch Population Sightings from 2017-2024
    st.subheader("Top 10 States and Monarch Population Sightings from 2017-2024")
    
    # Calculate and display top 10 states
    top_10_states = df.groupby('State/Province')['State/Province'].count().nlargest(10)
    st.write("Top 10 states with the highest number of observations:")
    st.table(top_10_states.reset_index(name='Count'))

    image_path = "line_slope.png"
    if os.path.exists(image_path):
        image4 = Image.open(image_path)
        st.image(image4, caption="Top 10 States and Monarch Population Sightings from 2017-2024", use_column_width=True)
    else:
        st.write("Image not found. The Top 10 States and Monarch Population Sightings graph is currently unavailable.")

    # 15k Sample Data Analysis
    st.subheader("15k Sample Data Analysis")
    st.write('''
    To gain initial insights and test our data processing methods, we took a 15,000 observation sample from our larger dataset. 
    This sample allowed us to quickly iterate on our analysis techniques and identify potential patterns or issues in the data 
    before scaling up to the full dataset.
    ''')

    image_path_3 = "download (3).png"
    if os.path.exists(image_path_3):
        image5 = Image.open(image_path_3)
        st.image(image5, caption="Distribution of Spring and Fall Data in 15k Sample", use_column_width=True)
    else:
        st.write("Image not found. The Distribution of Spring and Fall Data graph is currently unavailable.")

    # Add the new image and explanation
    image_path_4 = "download (4).png"
    if os.path.exists(image_path_4):
        image6 = Image.open(image_path_4)
        st.image(image6, caption="Sample of the 15k Dataset", use_column_width=True)
    else:
        st.write("Image not found. The Sample of 15k Dataset image is currently unavailable.")

    st.write('''
    This image shows a snapshot of our 15,000 observation sample dataset. It gives an idea of the structure 
    and content of our data, including columns for Date, Town, State/Province, Latitude, Longitude, and Number of sightings.
    This raw data view helps illustrate the type of information we're working with in our analysis.
    ''')

    # Air Quality and Pollutant Analysis
    st.subheader("Air Quality and Pollutant Analysis")
    st.write('''
    Air quality and pollutant levels can significantly impact monarch butterfly populations and their habitats. 
    The following visualizations provide insights into various pollutant distributions and air quality metrics 
    that may influence monarch butterfly migration patterns and overall health.
    ''')

    # Top 10 Counties with Unhealthy Air Quality
    image_path = "download (5).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="Top 10 Counties with Most Occurrences of Unhealthy Air Quality Categories", use_column_width=True)
    else:
        st.write("Image not found. The Top 10 Counties with Unhealthy Air Quality graph is currently unavailable.")

    # Pollutant Distribution Trends
    st.subheader("Pollutant Distribution Trends")
    image_path = "download (8).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="Pollutant Distribution by Year in Selected States (Line Chart)", use_column_width=True)
    else:
        st.write("Image not found. The Pollutant Distribution by Year (Line Chart) is currently unavailable.")
    
    st.write('''
    This line chart shows the trends in pollutant distribution over the years in selected states. 
    These trends can help us understand long-term changes in air quality that might affect monarch butterflies. 
    For instance, a consistent increase in ozone levels over the years could potentially be linked to changes 
    in monarch population sizes or shifts in their migration patterns.
    ''')

    # Top 30 States/Provinces for Monarch Butterfly Sightings
    st.subheader("Top 30 States/Provinces for Monarch Butterfly Sightings")
    image_path = "download (9).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="Top 30 States/Provinces by Monarch Butterfly Sightings", use_column_width=True)
    else:
        st.write("Image not found. The Top 30 States/Provinces graph is currently unavailable.")
    
    st.write('''
    This bar chart shows the top 30 states or provinces with the highest number of monarch butterfly sightings. 
    This distribution provides valuable insights into the monarch butterfly's preferred habitats and migration routes. 
    States with higher sighting numbers may be critical for conservation efforts.
    ''')

    # Top 50 Towns in Top 10 States (2017-2024)
    st.subheader("Top 50 Towns in Top 10 States (2017-2024)")
    image_path = "download (10).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="Top 50 Towns in Top 10 States for Monarch Butterfly Sightings (2017-2024)", use_column_width=True)
    else:
        st.write("Image not found. The Top 50 Towns in Top 10 States graph is currently unavailable.")
    
    st.write('''
    This visualization shows the top 50 towns within the top 10 states for monarch butterfly sightings from 2017 to 2024. 
    It helps identify specific localities that are particularly important for monarch butterflies, which could be 
    crucial for targeted conservation efforts.
    ''')

    # Yearly Sightings in Top 10 States (2017-2024)
    st.subheader("Yearly Sightings in Top 10 States (2017-2024)")
    image_path = "download (11).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="Yearly Monarch Butterfly Sightings in Top 10 States (2017-2024)", use_column_width=True)
    else:
        st.write("Image not found. The Yearly Sightings in Top 10 States graph is currently unavailable.")
    
    st.write('''
    This set of graphs shows the yearly trends of monarch butterfly sightings in the top 10 states from 2017 to 2024. 
    These trends can help identify patterns in monarch populations over time and across different regions, 
    which could be influenced by factors such as climate change, habitat loss, or conservation efforts.
    ''')

    # Pesticide Usage and Monarch Butterfly Sightings
    st.subheader("Pesticide Usage and Monarch Butterfly Sightings")
    image_path = "download (12).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="States and their Total Pesticide Usage based on Concentration (2017-2022)", use_column_width=True)
    else:
        st.write("Image not found. The Pesticide Usage graph is currently unavailable.")
    
    st.write('''
    These graphs show the total pesticide usage based on concentration in selected states from 2017 to 2022. 
    Pesticide use can have significant impacts on monarch butterfly populations by affecting their food sources 
    and habitats. Comparing these trends with monarch sightings data could reveal potential correlations between 
    pesticide use and monarch population changes.
    ''')

if __name__ == "__main__":
    main()
