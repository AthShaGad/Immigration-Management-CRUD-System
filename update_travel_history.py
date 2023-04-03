import pandas as pd
import streamlit as st
from database import view_all_data_travel_history, view_only_travel_id, get_travel_history, edit_travel_history
def update_travel_history():
    list_of_traveller = [i[0] for i in view_only_travel_id()]
    selected_traveller = st.selectbox("Travel History to Edit", list_of_traveller)
    selected_result = get_travel_history(selected_traveller)
    if selected_result:
        travel_id = selected_result[0][0]
        date_of_arrival = selected_result[0][1]
        date_of_departure = selected_result[0][2]
        source = selected_result[0][3]
        destination = selected_result[0][4]
        pp_no = selected_result[0][5]
    col1, col2 = st.columns(2)
    with col1:
        new_travel_id = st.text_input("Travel ID:")
        new_date_of_arrival = st.date_input("Date of Arrival:")
        new_date_of_departure = st.date_input("Date of Departure:")
    with col2:
        new_source = st.text_input("Source:")
        new_destination = st.text_input("Destination:")
        new_pp_no = st.text_input("Passport Number:")
    if st.button("Update Travel History"):
        edit_travel_history(new_travel_id, new_date_of_arrival, new_date_of_departure, new_source, new_destination, new_pp_no, travel_id, date_of_arrival, date_of_departure, source, destination, pp_no)
        st.success("Successfully updated:: {} to ::{}".format(travel_id, new_travel_id))
    result = view_all_data_travel_history()
    df = pd.DataFrame(result, columns=['Travel ID', 'Date of Arrival', 'Date of Departure', 'Source', 'Destination',
                                       'Passport Number'])
    with st.expander("View all Travel History"):
        st.dataframe(df)