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

    # 1. Sample Dataset (download (4).png)
    st.header("Sample Dataset")
    image_path = "download (4).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="Sample of the Dataset", use_column_width=True)
    else:
        st.write("Image not found. The Sample Dataset image is currently unavailable.")

    st.write('''
    This image shows a snapshot of our dataset. It gives an idea of the structure 
    and content of our data, including columns for Date, Town, State/Province, Latitude, Longitude, and Number of sightings.
    This raw data view helps illustrate the type of information we're working with in our analysis.
    ''')

    # 2. Geographic Distribution (image.webp)
    st.header("Geographic Distribution of Monarch Butterfly Sightings")
    image_path = "image.webp"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="Heatmap of Monarch Butterfly Sightings Distribution", use_column_width=True)
    else:
        st.write("Image not found. The geographic distribution heatmap is currently unavailable.")

    st.write('''
    This heatmap provides a detailed view of monarch butterfly sighting distributions across North America. 
    The red areas indicate higher concentrations of sightings, while blue areas show lower concentrations. 
    This visualization helps identify key regions for monarch butterfly populations and migration routes.
    ''')

    # 3. Top 30 States/Provinces (download(9).png)
    st.header("Top 30 States/Provinces for Monarch Butterfly Sightings")
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

    # 4. Top 50 Towns (download(10).png)
    st.header("Top 50 Towns in Top 10 States (2017-2024)")
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

    # 5. Yearly Sightings (download(11).png)
    st.header("Yearly Sightings in Top 10 States (2017-2024)")
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

    # 6. Top 10 States Population Trend (line_slope.png)
    st.header("Top 10 States and Monarch Population Sightings from 2017-2024")
    image_path = "line_slope.png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="Top 10 States and Monarch Population Sightings from 2017-2024", use_column_width=True)
    else:
        st.write("Image not found. The Top 10 States and Monarch Population Sightings graph is currently unavailable.")

    # 7. Overall Pollutant Distribution (download(6).png)
    st.header("Overall Pollutant Distribution in Selected States")
    image_path = "download (6).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="Overall Pollutant Distribution in Selected States", use_column_width=True)
    else:
        st.write("Image not found. The Overall Pollutant Distribution graph is currently unavailable.")

    st.write('''
    This bar chart shows the overall distribution of different pollutants in selected states. 
    Understanding the prevalence of various pollutants can help in assessing their potential impact on monarch butterfly populations.
    ''')

    # 8. Pollutant Distribution by Year (Bar Chart) (download(7).png)
    st.header("Pollutant Distribution by Year in Selected States")
    image_path = "download (7).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="Pollutant Distribution by Year in Selected States (Bar Chart)", use_column_width=True)
    else:
        st.write("Image not found. The Pollutant Distribution by Year (Bar Chart) is currently unavailable.")

    st.write('''
    This bar chart illustrates the distribution of different pollutants over the years in selected states. 
    It allows us to observe changes in pollutant levels over time, which may correlate with changes in monarch butterfly populations.
    ''')

    # 9. Pollutant Distribution by Year (Line Chart) (download(8).png)
    st.header("Pollutant Distribution Trends")
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

    # 10. Monarch Butterfly Population Trend (download.png)
    st.header("Monarch Butterfly Population Trend")
    image_path = "download.png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="Monarch Butterfly Population Trend", use_column_width=True)
    else:
        st.write("Image not found. The Monarch Butterfly Population Trend graph is currently unavailable.")

    # 11. Pesticide Usage (download(1).png)
    st.header("Pesticide Usage and Monarch Butterfly Sightings")
    image_path = "download (1).png"
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
