import streamlit as st
from database import add_data_nationality

def create_nationality():
    col1, col2 = st.columns(2)
    with col1:
        pp_no = st.text_input("Passport Number:")
    with col2:
        nationality = st.text_input("Nationality:")
    if st.button("Add Nationality"):
        add_data_nationality(pp_no, nationality)
        st.success("Successfully added Nationality: {}".format(pp_no))