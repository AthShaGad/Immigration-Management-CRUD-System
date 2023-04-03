import pandas as pd
import streamlit as st
from database import view_all_data_arrival, view_only_arrival_passport_no, get_arrival, edit_arrival_data
def update_arrival():
    list_of_arrival = [i[0] for i in view_only_arrival_passport_no()]
    selected_arrival = st.selectbox("Arrival to Edit", list_of_arrival)
    selected_result = get_arrival(selected_arrival)
    if selected_result:
        pp_no = selected_result[0][0]
        flight_no = selected_result[0][1]
        date_of_arrival = selected_result[0][2]
        immigration_officer = selected_result[0][3]
        travel_id = selected_result[0][4]
        source = selected_result[0][5]
        officer_id = selected_result[0][6]
    col1, col2 = st.columns(2)
    with col1:
        new_pp_no = st.text_input("Passport Number:")
        new_flight_no = st.text_input("Flight Number:")
        new_date_of_arrival = st.date_input("Date of Arrival:")
        new_immigration_officer = st.text_input("Immigration Officer:")
    with col2:
        new_travel_id = st.text_input("Travel ID:")
        new_source = st.text_input("Source:")
        new_officer_id = st.text_input("Officer ID:")
    if st.button("Update Arrival"):
        if not new_flight_no:
            new_flight_no = None
        if not new_date_of_arrival:
            new_date_of_arrival = None
        if not new_immigration_officer:
            new_immigration_officer = None
        if not new_travel_id:
            new_travel_id = None
        if not new_source:
            new_source = None
        if not new_officer_id:
            new_officer_id = None
        edit_arrival_data(new_pp_no, new_flight_no, new_date_of_arrival, new_immigration_officer, new_travel_id,new_source, new_officer_id, pp_no, flight_no, date_of_arrival, immigration_officer, travel_id, source, officer_id)
        st.success("Successfully updated:: {} to ::{}".format(pp_no, new_pp_no))
    result = view_all_data_arrival()
    df = pd.DataFrame(result, columns=['Passport Number', 'Flight Number', 'Date of Arrival', 'Immigration Officer', 'Travel ID', 'Source', 'Officer ID'])
    with st.expander("Updated Arrivals"):
        st.dataframe(df)