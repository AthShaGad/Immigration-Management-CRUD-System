import pandas as pd
import streamlit as st
from database import view_all_data_crime, view_only_fir_no, get_crime, edit_crime
def update_crime():
    list_of_crime = [i[0] for i in view_only_fir_no()]
    selected_crime = st.selectbox("Crime to Edit", list_of_crime)
    selected_result = get_crime(selected_crime)
    if selected_result:
        fir_no = selected_result[0][0]
        police_station = selected_result[0][1]
        nature_of_crime = selected_result[0][2]
        conviction_status = selected_result[0][3]
        pp_no = selected_result[0][4]
    col1, col2 = st.columns(2)
    with col1:
        new_fir_no = st.text_input("FIR Number:")
        new_police_station = st.text_input("Name of the Police Station:")
        new_nature_of_crime = st.text_input("Nature of Crime:")
    with col2:
        new_conviction_status = st.text_input("Conviction Status:")
        new_pp_no = st.text_input("Passport Number:")
    if st.button("Update Crime"):
        if not new_police_station:
            new_police_station = None
        edit_crime(new_fir_no, new_police_station, new_nature_of_crime, new_conviction_status, new_pp_no, fir_no, police_station, nature_of_crime, conviction_status, pp_no)
        st.success("Successfully updated:: {} to ::{}".format(fir_no, new_fir_no))
    result = view_all_data_crime()
    df = pd.DataFrame(result,
                      columns=['FIR Number', 'Name of the Police Station', 'Nature of Crime', 'Conviction Status',
                               'Passport Number'])
    with st.expander("View all Crimes"):
        st.dataframe(df)