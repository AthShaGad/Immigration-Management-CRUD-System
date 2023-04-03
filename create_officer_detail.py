import streamlit as st
from database import add_data_officer_detail

def create_officer_detail():
    col1, col2 = st.columns(2)
    with col1:
        officer_id = st.text_input("Officer ID:")
        name = st.text_input("Name:")
    with col2:
        sex = st.text_input("Sex:")
        join_date = st.date_input("Joining Date:")
    if st.button("Add Officer"):
        if not sex:
            sex = None
        add_data_officer_detail(officer_id, name, sex, join_date)
        st.success("Successfully added Officer: {}".format(officer_id))