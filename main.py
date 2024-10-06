import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os


def main():
    st.set_page_config(page_title="Monarch Butterfly Sightings Analysis",
                       layout="wide")
    st.title("Monarch Butterfly Sightings Analysis")

    # Project Origin
    st.header("Project Origin")
    st.write("""
    This project began with the ambitious task of scraping data from the Journey North website, 
    a comprehensive resource for tracking monarch butterfly migrations. Our initial dataset combined 
    spring and fall data, resulting in approximately 166,000 observations of monarch butterfly sightings.
    """)

    # Include download (4).png after Project Origin
    image_path = "download (4).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image,
                 caption="Top 10 Locations in Cleaned Data from Approach 2",
                 use_column_width=True)
    else:
        st.write(
            "Image not found. The Top 10 Locations graph is currently unavailable."
        )

    st.write("""
    The data collection process evolved as follows:
    1. Initially, we scraped both "Monarch (Other)" and adult monarch butterfly data from Journey North.
    2. Upon analysis, we realized the need to focus specifically on adult monarch butterflies for more accurate migration patterns.
    3. We then refined our scraping process to collect adult monarch butterfly data from 2017-2024.
    """)

    # Include image.webp
    image_path = "image.webp"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(
            image,
            caption="Geographic Distribution of Monarch Butterfly Sightings",
            use_column_width=True)
    else:
        st.write(
            "Image not found. The geographic distribution heatmap is currently unavailable."
        )

    # Hypothesis
    st.header("Hypothesis")
    st.write("""
    We initially hypothesized that the reduction in monarch butterfly populations is due to environmental factors such as air quality (AQI) and pesticide usage from 2017 to 2024. Our challenge was to predict the decline in monarch butterfly sightings using these various factors.
    """)

    # Include download(9).png
    image_path = "download (9).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(
            image,
            caption="Top 30 States/Provinces by Monarch Butterfly Sightings",
            use_column_width=True)
    else:
        st.write(
            "Image not found. The Top 30 States/Provinces graph is currently unavailable."
        )

    # Data Collection and Cleaning
    st.header("Data Collection and Cleaning")
    st.write("""
    We started by scraping data from the Journey North website for each year from 2017 to 2024, focusing on adult monarch butterflies as they would be most spotted and provide bulk data. This resulted in approximately 166,000 rows of data.

    During the data cleaning process, we faced several challenges:
    - We removed data that had missing values and images, which reduced the dataset to about 111,000 data points.
    - We checked the mean and standard deviation to understand how these removals affected our dataset.
    - We attempted geocoding this data using longitude and latitude, but the estimated completion time was about 16 hours, so we decided not to pursue that.
    """)

    # Include download(10).png
    image_path = "download (10).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(
            image,
            caption=
            "Top 50 Towns in Top 10 States for Monarch Butterfly Sightings (2017-2024)",
            use_column_width=True)
    else:
        st.write(
            "Image not found. The Top 50 Towns in Top 10 States graph is currently unavailable."
        )

    # Include download(11).png
    image_path = "download (11).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(
            image,
            caption=
            "Yearly Monarch Butterfly Sightings in Top 10 States (2017-2024)",
            use_column_width=True)
    else:
        st.write(
            "Image not found. The Yearly Sightings in Top 10 States graph is currently unavailable."
        )

    # Include line_slope.png
    image_path = "line_slope.png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(
            image,
            caption=
            "Top 10 States and Monarch Population Sightings from 2017-2024",
            use_column_width=True)
    else:
        st.write(
            "Image not found. The Top 10 States and Monarch Population Sightings graph is currently unavailable."
        )

    # Challenges and Approaches
    st.header("Challenges and Approaches")
    st.write("""
    We attempted to incorporate additional environmental factors such as pesticide usage and air quality index (AQI) into our analysis. However, we faced several challenges:

    - **Pesticide Data**: We had limited pesticide usage data from 2017 to 2022, and only four of the states we initially focused on had matching data. Due to the insufficient data, we decided to discard pesticide usage from our analysis.
    - **Air Quality Data**: We noticed trends when plotting AQI data but found that the correlation was not strong enough at the state level. We decided to analyze county-wise data to test our hypothesis further.

    To enrich our dataset with county information, we explored several approaches:

    1. **Using Language Models (LLMs)**: We attempted to use the OpenAI API to process 51,000 data entries. However, the estimated completion time was around 18.79 hours, which was impractical.
    2. **Triangulation Method**: We tried to achieve 90% accuracy by triangulating data based on state, latitude and longitude, and the top 500 cities. We used the `BallTree` model from `sklearn.neighbors` to match coordinates to the nearest city.
    3. **Geopy Library**: We attempted to obtain county data using the Geopy library, but the process was estimated to take around 8 hours, and system limitations prevented us from completing it.

    Ultimately, we conducted a small-scale test with 2,000 entries using the OpenAI API and performed statistical analysis. However, we found that the results were too fuzzy and not particularly useful.
    """)

    # Include download(6).png
    st.header("Overall Pollutant Distribution in Selected States")
    image_path = "download (6).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image,
                 caption="Overall Pollutant Distribution in Selected States",
                 use_column_width=True)
    else:
        st.write(
            "Image not found. The Overall Pollutant Distribution graph is currently unavailable."
        )

    st.write('''
    This bar chart shows the overall distribution of different pollutants in selected states. 
    Understanding the prevalence of various pollutants can help in assessing their potential impact on monarch butterfly populations.
    ''')

    # Include download(7).png
    st.header("Pollutant Distribution by Year in Selected States")
    image_path = "download (7).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(
            image,
            caption=
            "Pollutant Distribution by Year in Selected States (Bar Chart)",
            use_column_width=True)
    else:
        st.write(
            "Image not found. The Pollutant Distribution by Year (Bar Chart) is currently unavailable."
        )

    st.write('''
    This bar chart illustrates the distribution of different pollutants over the years in selected states. 
    It allows us to observe changes in pollutant levels over time, which may correlate with changes in monarch butterfly populations.
    ''')

    # Include download(8).png
    st.header("Pollutant Distribution Trends")
    image_path = "download (8).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(
            image,
            caption=
            "Pollutant Distribution by Year in Selected States (Line Chart)",
            use_column_width=True)
    else:
        st.write(
            "Image not found. The Pollutant Distribution by Year (Line Chart) is currently unavailable."
        )

    st.write('''
    This line chart shows the trends in pollutant distribution over the years in selected states. 
    These trends can help us understand long-term changes in air quality that might affect monarch butterflies. 
    For instance, a consistent increase in ozone levels over the years could potentially be linked to changes 
    in monarch population sizes or shifts in their migration patterns.
    ''')

    # Include download.png
    st.header("Monarch Butterfly Population Trend")
    image_path = "download.png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image,
                 caption="Monarch Butterfly Population Trend",
                 use_column_width=True)
    else:
        st.write(
            "Image not found. The Monarch Butterfly Population Trend graph is currently unavailable."
        )

    # Include download(1).png
    st.header("Pesticide Usage and Monarch Butterfly Sightings")
    image_path = "download (1).png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(
            image,
            caption=
            "States and their Total Pesticide Usage based on Concentration (2017-2022)",
            use_column_width=True)
    else:
        st.write(
            "Image not found. The Pesticide Usage graph is currently unavailable."
        )

    st.write('''
    These graphs show the total pesticide usage based on concentration in selected states from 2017 to 2022. 
    Pesticide use can have significant impacts on monarch butterfly populations by affecting their food sources 
    and habitats. Comparing these trends with monarch sightings data could reveal potential correlations between 
    pesticide use and monarch population changes.
    ''')

    # Conclusion
    st.header("Conclusion")
    st.write("""
    Throughout this project, we learned a great deal about data collection, cleaning, and analysis. We faced several challenges, including dealing with large datasets, time-consuming geocoding processes, and limited data availability for certain environmental factors.

    Despite these challenges, we gained valuable experience in using APIs, working with large datasets, and data visualization. Our analysis suggests that there is a correlation between air quality and monarch butterfly sightings, although further research with more granular data (e.g., county-level data) would be necessary to strengthen this conclusion.

    This project highlighted the importance of careful planning, teamwork, and adaptability when working with complex data analysis tasks. While we faced obstacles, the experience reinforced the idea that humans can achieve remarkable things when united for a cause.
    """)


if __name__ == "__main__":
    main()
