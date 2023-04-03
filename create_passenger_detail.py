import streamlit as st
from database import add_data_passenger_detail

def create_passenger_detail():
    col1, col2 = st.columns(2)
    with col1:
        pp_no = st.text_input("Passport Number:")
        fname = st.text_input("First Name:")
        minit = st.text_input("Middle Initial:")
        lname = st.text_input("Last Name:")
        sex = st.text_input("Sex:")
    with col2:
        visa_no = st.text_input("Visa Number:")
        dob = st.date_input("Date of Birth:")
        minor_accompanier = st.text_input("Minor Accompanier:")
        relaion_to_minor = st.text_input("Relation to Minor:")
    if st.button("Add Passenger"):
        if not minit:
            minit = None
        if not sex:
            sex = None
        if not visa_no:
            visa_no = None
        if not dob:
            dob = None
        if not minor_accompanier:
            minor_accompanier = None
        if not relaion_to_minor:
            relaion_to_minor = None
        age = None
        add_data_passenger_detail(pp_no, fname, minit, lname, sex, visa_no, dob, minor_accompanier, relaion_to_minor, age)
        st.success("Successfully added Passenger: {}".format(pp_no))