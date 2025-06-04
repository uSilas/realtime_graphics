import streamlit as st
import pandas as pd
import altair as alt
from streamlit_autorefresh import st_autorefresh

DATA_FILE = 'data.csv'

st.title("Player Performance Visualization")

refresh_interval = 5000
st_autorefresh(interval=refresh_interval, key="datarefresh")

try:
    data = pd.read_csv(DATA_FILE)
except FileNotFoundError:
    st.warning("No data available yet.")
    st.stop()

st.subheader("Raw Data")
st.dataframe(data)

st.subheader("Points vs Time Without Dying")

chart = alt.Chart(data).mark_line(point=True).encode(
    x='time_without_dying:Q',
    y='points:Q',
    tooltip=['points', 'time_without_dying']
).properties(
    width=600,
    height=400
)

st.altair_chart(chart, use_container_width=True)

st.subheader("Distribution of Points")
st.bar_chart(data['points'])

st.subheader("Distribution of Time Without Dying")
st.bar_chart(data['time_without_dying'])

st.write(f"Auto-refreshing every {refresh_interval // 1000} seconds...")
