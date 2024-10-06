import streamlit as st
from PIL import Image

st.set_page_config(page_title="Monarch Butterfly Sightings Analysis", layout="wide")

def main():
    st.title("Monarch Butterfly Sightings Analysis")

    st.header("Visualizations")

    # Display and explain the first image
    st.subheader("Monarch Butterfly Population Trend")
    image1 = Image.open("download.png")
    st.image(image1, caption="Monarch Butterfly Population Trend", use_column_width=True)
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
    image2 = Image.open("download (1).png")
    st.image(image2, caption="Geographical Distribution of Monarch Butterfly Sightings", use_column_width=True)
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
    image3 = Image.open("download (2).png")
    st.image(image3, caption="Seasonal Pattern of Monarch Butterfly Sightings", use_column_width=True)
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
    image4 = Image.open("line_slope.png")
    st.image(image4, caption="Top 10 States and Monarch Population Sightings from 2017-2024", use_column_width=True)
    st.write("""
    This multi-line graph shows the Monarch Butterfly sightings for the top 10 states from 2017 to 2024. 
    Each line represents a different state, allowing for easy comparison of sighting trends across states over time. 
    The varying slopes indicate different rates of change in sightings for each state.

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
