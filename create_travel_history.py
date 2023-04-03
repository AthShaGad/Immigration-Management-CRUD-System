import streamlit as st
from database import add_data_travel_history

def create_travel_history():
    col1, col2 = st.columns(2)
    with col1:
        travel_id = st.text_input("Travel ID:")
        date_of_arrival = st.date_input("Date of Arrival:")
        date_of_departure = st.date_input("Date of Departure:")
    with col2:
        source = st.text_input("Source:")
        destination = st.text_input("Destination:")
        pp_no = st.text_input("Passport Number:")
    if st.button("Add Travel History"):
        add_data_travel_history(travel_id, date_of_arrival, date_of_departure, source, destination, pp_no)
        st.success("Successfully added Travel History: {}".format(travel_id))