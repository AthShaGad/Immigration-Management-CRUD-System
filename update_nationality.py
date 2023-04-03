import pandas as pd
import streamlit as st
from database import view_all_data_nationality, view_only_nationality, get_nationality, edit_nationality
def update_nationality():
    list_of_pp_no = [i[0] for i in view_only_nationality()]
    list_of_nationality = [i[1] for i in view_only_nationality()]
    selected_pp_no = st.selectbox("Passport Number to Edit", list_of_pp_no)
    selected_nationality = st.selectbox("Nationality to Edit", list_of_nationality)
    selected_result = get_nationality(selected_pp_no, selected_nationality)
    if selected_result:
        pp_no = selected_result[0][0]
        nationality = selected_result[0][1]
    col1, col2 = st.columns(2)
    with col1:
        new_pp_no = st.text_input("Passport Number:")
    with col2:
        new_nationality = st.text_input("Nationality:")
    if st.button("Update Nationality"):
        edit_nationality(new_pp_no, new_nationality, pp_no, nationality)
        st.success("Successfully updated:: {} to ::{}".format(pp_no, new_pp_no))
    result = view_all_data_nationality()
    df = pd.DataFrame(result, columns=['Passport', 'Nationality'])
    with st.expander("View all Nationalities"):
        st.dataframe(df)