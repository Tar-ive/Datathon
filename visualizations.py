import plotly.express as px
import plotly.graph_objects as go

def plot_sightings_over_time(df):
    daily_counts = df.groupby('Date').size().reset_index(name='Count')
    fig = px.line(daily_counts, x='Date', y='Count', title='Monarch Butterfly Sightings Over Time')
    fig.update_layout(xaxis_title='Date', yaxis_title='Number of Sightings')
    return fig

def plot_top_towns(top_towns):
    fig = go.Figure(data=[go.Bar(x=top_towns.index, y=top_towns.values)])
    fig.update_layout(
        title='Top 10 Towns with Most Sightings',
        xaxis_title='Town',
        yaxis_title='Number of Sightings',
        xaxis_tickangle=-45
    )
    return fig
