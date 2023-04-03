import streamlit as st
from database import add_data_arrival

def create_arrival():
    col1, col2 = st.columns(2)
    with col1:
        pp_no = st.text_input("Passport Number:")
        flight_no = st.text_input("Flight Number:")
        date_of_arrival=st.date_input("Date of Arrival:")
        immigration_officer=st.text_input("Immigration Officer:")
    with col2:
        travel_id = st.text_input("Travel ID:")
        source = st.text_input("Source:")
        officer_id = st.text_input("Officer ID:")
    if st.button("Add Arrival"):
        if not flight_no:
            flight_no = None
        if not date_of_arrival:
            date_of_arrival = None
        if not immigration_officer:
            immigration_officer = None
        if not travel_id:
            travel_id = None
        if not source:
            source = None
        if not officer_id:
            officer_id = None
        add_data_arrival(pp_no, flight_no, date_of_arrival, immigration_officer, travel_id, source, officer_id)
        st.success("Successfully added Arrival: {}".format(pp_no))