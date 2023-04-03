import streamlit as st
from database import add_data_crime

def create_crime():
    col1, col2 = st.columns(2)
    with col1:
        fir_no = st.text_input("FIR Number:")
        police_station = st.text_input("Name of the Police Station:")
        nature_of_crime = st.text_input("Nature of Crime:")
    with col2:
        conviction_status = st.text_input("Conviction Status:")
        pp_no = st.text_input("Passport Number:")
    if st.button("Add Crime"):
        if not police_station:
            police_station = None
        add_data_crime(fir_no, police_station, nature_of_crime, conviction_status, pp_no)
        st.success("Successfully added Crime: {}".format(fir_no))