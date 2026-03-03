import streamlit as st
import pandas as pd
import json
import os
import plotly.express as px
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

st.title("Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")
st.divider()
st.header("Load Data")
if os.path.exists("data.csv") and os.path.getsize("data.csv") > 0:
    df_csv = pd.read_csv("data.csv")
    st.success("Successfully loaded data.csv")
else:
    df_csv = pd.DataFrame(columns=["Category", "Value"])
    st.warning("data.csv is empty or not found. Submit data on the Survey page first!")


try:
    if os.path.exists("data.json"):
        with open("data.json", "r") as json_file:
            json_dict = json.load(json_file) 
        df_json = pd.DataFrame(json_dict["data_points"])
        st.success("Successfully loaded data.json")
    else:
        st.error("data.json not found!")
        df_json = pd.DataFrame(columns=["label", "value"])
except Exception as e:
    st.error(f"Error loading JSON file: {e}")
    df_json = pd.DataFrame(columns=["label", "value"])

st.divider()
st.header("Graphs")

st.subheader("Graph 1: Baseline Activities (Static)")
if not df_json.empty:
    fig1 = px.bar(df_json, x="label", y="value", title="Data from JSON")
    st.plotly_chart(fig1) 
    st.write("This is a static graph showing the data from your JSON file.")
st.subheader("Graph 2: Survey Trends (Dynamic)")
if not df_csv.empty:
    user_color = st.selectbox("Pick a line color:", ["Blue", "Red", "Green"]) 
    line_style = st.radio("Pick a line style:", ["solid", "dot"]) 

    fig2 = px.line(df_csv, x="Category", y="Value", title="Dynamic CSV Line Chart")
    fig2.update_traces(line=dict(color=user_color.lower(), dash=line_style))
    st.plotly_chart(fig2)
else:
    st.info("Add data in the Survey to see the Line Chart.")

st.subheader("Graph 3: Data Composition (Dynamic)")
if not df_csv.empty:
    opacity_val = st.slider("Adjust Transparency:", 0.1, 1.0, 0.7)
    show_legend = st.checkbox("Show Chart Legend", value=True) 
    fig3 = px.pie(df_csv, values='Value', names='Category', title="Activity Distribution")
    fig3.update_traces(opacity=opacity_val) 
    fig3.update_layout(showlegend
