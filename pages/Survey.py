import streamlit as st
import pandas as pd
import os 
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

st.title("Data Collection Survey 📝")
st.write("Please fill out the form below to add your data to the dataset.")

with st.form("survey_form"):
    category_input = st.text_input("Enter a category:")
    value_input = st.text_input("Enter a corresponding value:")
    submitted = st.form_submit_button("Submit Data")
    if submitted:
        file = open("data.csv", "a") 
        file.write(category_input + "," + value_input + "\n")
        file.close()
        st.success("Your data has been submitted!")
        st.write(f"You entered: **Category:** {category_input}, **Value:** {value_input}")
st.divider()
st.header("Current Data in CSV")
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    current_data_df = pd.read_csv('data.csv')
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")

    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")
