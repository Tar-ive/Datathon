import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(page_title="Monarch Butterfly Sightings Analysis", layout="wide")

def main():
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

    The web scraping process, detailed in the MonarchWebScrapper.ipynb file, utilized Python libraries such as requests, 
    BeautifulSoup, and pandas to efficiently collect and organize the data.

    We chose to focus on adult butterflies because they are easier to spot and potentially represent the highest numbers 
    in migration patterns, providing a more accurate representation of monarch movement.

    This cleaned and focused dataset forms the foundation of our analysis and visualizations presented in this application.
    """)

    # Display the new screenshot
    image_path = "Screenshot 2024-10-06 at 9.57.25 AM.png"
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption="Sample of the combined spring and fall data from our initial scraping", use_column_width=True)
    else:
        st.write("Image not found. The sample data screenshot is currently unavailable.")

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
    st.write("""
    This heatmap illustrates the geographic distribution of monarch butterfly sightings across the United States. 
    The color intensity represents the concentration of sightings, with darker colors indicating a higher number of observations. 
    This visualization helps identify key areas of monarch butterfly activity and potential migration routes.

    Key observations from the map:
    - California and Texas show the highest concentration of sightings, likely due to their importance in the monarch's migration patterns.
    - There's a notable presence along the East Coast, particularly in the Northeast.
    - The Midwest also shows significant activity, aligning with known monarch habitats and migration routes.

    This distribution provides valuable insights into the monarch butterfly's preferred habitats and migration patterns across the country.
    """)

    st.header("Visualizations")

    # Display and explain the first image
    st.subheader("Monarch Butterfly Population Trend")
    image_path = "download.png"
    if os.path.exists(image_path):
        image1 = Image.open(image_path)
        st.image(image1, caption="Monarch Butterfly Population Trend", use_column_width=True)
    else:
        st.write("Image not found. The Monarch Butterfly Population Trend graph is currently unavailable.")
    st.write("""
    This graph shows the trend of Monarch Butterfly population over time. The x-axis represents years, 
    while the y-axis shows the population count. The line graph illustrates fluctuations in the butterfly 
    population, helping us identify any long-term trends or significant changes over the years.
    
    Code used to generate this plot:
    ```python
    import matplotlib.pyplot as plt
    import pandas as pd

    # Assuming 'df' is your DataFrame with 'Date' and population count columns
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Population'], marker='o')
    plt.title('Monarch Butterfly Population Trend')
    plt.xlabel('Year')
    plt.ylabel('Population Count')
    plt.grid(True)
    plt.savefig('download.png')
    plt.close()
    ```
    """)

    # Display and explain the second image
    st.subheader("Geographical Distribution of Monarch Butterfly Sightings")
    image_path = "download (1).png"
    if os.path.exists(image_path):
        image2 = Image.open(image_path)
        st.image(image2, caption="Geographical Distribution of Monarch Butterfly Sightings", use_column_width=True)
    else:
        st.write("Image not found. The Geographical Distribution of Monarch Butterfly Sightings map is currently unavailable.")
    st.write("""
    This map visualization shows the geographical distribution of Monarch Butterfly sightings. 
    Each point on the map represents a location where butterflies were observed. The color intensity 
    might indicate the frequency of sightings in each area.

    Code used to generate this plot:
    ```python
    import plotly.express as px

    # Assuming 'df' is your DataFrame with 'Latitude', 'Longitude', and 'Count' columns
    fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', size='Count',
                            color='Count', hover_name='Location', zoom=3,
                            mapbox_style="carto-positron")
    fig.write_image("download (1).png")
    ```
    """)

    # Display and explain the third image
    st.subheader("Seasonal Pattern of Monarch Butterfly Sightings")
    image_path = "download (2).png"
    if os.path.exists(image_path):
        image3 = Image.open(image_path)
        st.image(image3, caption="Seasonal Pattern of Monarch Butterfly Sightings", use_column_width=True)
    else:
        st.write("Image not found. The Seasonal Pattern of Monarch Butterfly Sightings graph is currently unavailable.")
    st.write("""
    This bar chart illustrates the seasonal pattern of Monarch Butterfly sightings. The x-axis represents 
    months, while the y-axis shows the number of sightings. This visualization helps us understand 
    the peak seasons for butterfly activity and migration patterns.

    Code used to generate this plot:
    ```python
    import matplotlib.pyplot as plt
    import pandas as pd

    # Assuming 'df' is your DataFrame with a 'Date' column
    monthly_counts = df.groupby(df['Date'].dt.month)['Date'].count()
    
    plt.figure(figsize=(12, 6))
    monthly_counts.plot(kind='bar')
    plt.title('Seasonal Pattern of Monarch Butterfly Sightings')
    plt.xlabel('Month')
    plt.ylabel('Number of Sightings')
    plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.savefig('download (2).png')
    plt.close()
    ```
    """)

    # Display and explain the fourth image
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
    st.write("""
    This multi-line graph shows the Monarch Butterfly sightings for the top 10 states from 2017 to 2024. 
    Each line represents a different state, allowing for easy comparison of sighting trends across states over time. 
    The varying slopes indicate different rates of change in sightings for each state.

    This visualization was created after identifying the top 10 states with the highest number of observations, 
    as shown in the table above.

    Code used to generate this plot:
    ```python
    import matplotlib.pyplot as plt
    import pandas as pd

    # Assuming 'df' is your DataFrame with 'Date', 'State', and 'Count' columns
    top_10_states = df.groupby('State')['Count'].sum().nlargest(10).index
    df_top_10 = df[df['State'].isin(top_10_states)]

    fig, ax = plt.subplots(2, 5, figsize=(20, 10), sharex=True)
    fig.suptitle('Top 10 States and Monarch Population Sightings from 2017-2024')

    for i, state in enumerate(top_10_states):
        row = i // 5
        col = i % 5
        state_data = df_top_10[df_top_10['State'] == state]
        ax[row, col].plot(state_data['Date'], state_data['Count'])
        ax[row, col].set_title(f"{state} Monarch Butterfly Sightings")
        ax[row, col].set_xlabel('Year')
        ax[row, col].set_ylabel('Count')

    plt.tight_layout()
    plt.savefig('line_slope.png')
    plt.close()
    ```
    """)

if __name__ == "__main__":
    main()
