# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations
import plotly.express as px

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

if os.path.exists("data.csv"):
    df_csv = pd.read_csv("data.csv")
    st.success("Successfully loaded data.csv")
else:
   
    df_csv = pd.DataFrame(columns=["Category", "Value"])
    st.error("data.csv not found! Please submit data on the Survey page.")
    st.info("TODO: Add your data loading logic here.")

try:
    with open("data.json", "r") as json_file:
        json_dict = json.load(json_file) 
    df_json = pd.DataFrame(json_dict["data_points"])
    st.success("Successfully loaded data.json")
except Exception as e:
    st.error(f"Error loading JSON file: {e}")
# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
# TO DO:
st.subheader("Graph 1: Baseline Activities (Static)")
fig1 = px.bar(df_json, x="label", y="value", title="Data from JSON") # #NEW
st.plotly_chart(fig1) 
st.write("This is a static graph. It shows the data we manually typed into the JSON file.")

# GRAPH 2: DYNAMIC GRAPH
st.subheader("Graph 2: Survey Trends (Dynamic)")
if "line_color" not in st.session_state:
    st.session_state.line_color = "Blue" 
user_color = st.selectbox("Pick a line color:", ["Blue", "Red", "Green"]) 
st.session_state.line_color = user_color
line_style = st.radio("Pick a line style:", ["solid", "dot"]) 

fig2 = px.line(df_csv, x="Category", y="Value", title="Dynamic CSV Line Chart")
fig2.update_traces(line=dict(color=st.session_state.line_color.lower(), dash=line_style))
st.plotly_chart(fig2)


# GRAPH 3: DYNAMIC GRAPH
st.subheader("Graph 3: Data Composition (Dynamic)")
opacity_val = st.slider("Adjust Transparency:", 0.1, 1.0, 0.7)
show_legend = st.checkbox("Show Chart Legend", value=True) 
fig3 = px.pie(df_csv, values='Value', names='Category', title="Activity Distribution")
fig3.update_traces(opacity=opacity_val) 
fig3.update_layout(showlegend=show_legend)
st.plotly_chart(fig3)
