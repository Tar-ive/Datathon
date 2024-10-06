import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
from data_processing import load_data, filter_data, get_top_towns
from visualizations import plot_sightings_over_time, plot_top_towns

st.set_page_config(page_title="Monarch Butterfly Sightings Analysis", layout="wide")

def main():
    st.title("Monarch Butterfly Sightings Analysis")

    # Sidebar for data upload and filtering
    st.sidebar.header("Data Upload and Filtering")
    uploaded_file = st.sidebar.file_uploader("Upload CSV file", type="csv")

    if uploaded_file is not None:
        df = load_data(uploaded_file)
    else:
        st.warning("Please upload a CSV file to begin analysis.")
        return

    # Date range filter
    min_date = df['Date'].min().date()
    max_date = df['Date'].max().date()
    start_date, end_date = st.sidebar.date_input(
        "Select date range",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    # State/Province filter
    states = sorted(df['State/Province'].unique())
    selected_states = st.sidebar.multiselect("Select States/Provinces", states, default=states)

    # Filter data based on user selection
    filtered_df = filter_data(df, start_date, end_date, selected_states)

    # Display basic statistics
    st.header("Basic Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sightings", len(filtered_df))
    col2.metric("Unique Locations", filtered_df['Town'].nunique())
    col3.metric("Date Range", f"{start_date} to {end_date}")

    # Visualizations
    st.header("Visualizations")

    # Sightings over time
    st.subheader("Monarch Butterfly Sightings Over Time")
    fig_time = plot_sightings_over_time(filtered_df)
    st.plotly_chart(fig_time, use_container_width=True)

    # Top towns
    st.subheader("Top 10 Towns with Most Sightings")
    top_towns = get_top_towns(filtered_df, n=10)
    fig_towns = plot_top_towns(top_towns)
    st.plotly_chart(fig_towns, use_container_width=True)

    # Display uploaded image
    st.header("Additional Visualization")
    image = Image.open("assets/line_slope.png")
    st.image(image, caption="Top 10 States and Monarch Population Sightings from 2017-2024", use_column_width=True)

    # Display raw data
    st.header("Raw Data")
    st.dataframe(filtered_df)

if __name__ == "__main__":
    main()
