import pandas as pd
import streamlit as st
from database import view_all_data_passenger_detail, view_only_passenger_id, get_passenger, edit_passenger_data
def update_passenger_detail():
    list_of_passenger = [i[0] for i in view_only_passenger_id()]
    selected_passenger = st.selectbox("Passenger to Edit", list_of_passenger)
    selected_result = get_passenger(selected_passenger)
    if selected_result:
        pp_no = selected_result[0][0]
        fname = selected_result[0][1]
        minit = selected_result[0][2]
        lname = selected_result[0][3]
        sex = selected_result[0][4]
        visa_no = selected_result[0][5]
        dob = selected_result[0][6]
        minor_accompanier = selected_result[0][7]
        relaion_to_minor = selected_result[0][8]
    col1, col2 = st.columns(2)
    with col1:
        new_pp_no = st.text_input("Passport Number:")
        new_fname = st.text_input("First Name:")
        new_minit = st.text_input("Middle Initial:")
        new_lname = st.text_input("Last Name:")
        new_sex = st.text_input("Sex:")
    with col2:
        new_visa_no = st.text_input("Visa Number:")
        new_dob = st.date_input("Date of Birth:")
        new_minor_accompanier = st.text_input("Minor Accompanier:")
        new_relaion_to_minor = st.text_input("Relation to Minor:")
    if st.button("Update Passenger"):
        if not new_minit:
            new_minit = None
        if not new_sex:
            new_sex = None
        if not new_visa_no:
            new_visa_no = None
        if not new_dob:
            new_dob = None
        if not new_minor_accompanier:
            new_minor_accompanier = None
        if not new_relaion_to_minor:
            new_relaion_to_minor = None
        edit_passenger_data(new_pp_no, new_fname, new_minit, new_lname, new_sex, new_visa_no, new_dob, new_minor_accompanier, new_relaion_to_minor, pp_no, fname, minit, lname, sex, visa_no, dob, minor_accompanier, relaion_to_minor)
        st.success("Successfully updated:: {} to ::{}".format(pp_no, new_pp_no))
    result = view_all_data_passenger_detail()
    df = pd.DataFrame(result,
                      columns=['Passport Number', 'First Name', 'Middle Initial', 'Last Name', 'Sex', 'Visa Number',
                               'Date of Birth', 'Minor Accompanier', 'Relation to the Minor', 'Age'])
    with st.expander("View Updated Passengers"):
        st.dataframe(df)