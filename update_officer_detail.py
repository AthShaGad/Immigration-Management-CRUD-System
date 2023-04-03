import pandas as pd
import streamlit as st
from database import view_all_data_officer_detail, view_only_officer_id, get_officer, edit_officer_data
def update_officer_detail():
    list_of_officer = [i[0] for i in view_only_officer_id()]
    selected_officer = st.selectbox("Officer to Edit", list_of_officer)
    selected_result = get_officer(selected_officer)
    if selected_result:
        officer_id = selected_result[0][0]
        name = selected_result[0][1]
        sex = selected_result[0][2]
        join_date = selected_result[0][3]
    col1, col2 = st.columns(2)
    with col1:
        new_officer_id = st.text_input("Officer ID:")
        new_name = st.text_input("Name:")
    with col2:
        new_sex = st.text_input("Sex:")
        new_join_date = st.date_input("Joining Date:")
    if st.button("Update Officer"):
        if not new_sex:
            new_sex = None
        edit_officer_data(new_officer_id, new_name, new_sex, new_join_date,officer_id, name, sex, join_date)
        st.success("Successfully updated:: {} to ::{}".format(officer_id, new_officer_id))
    result = view_all_data_officer_detail()
    df = pd.DataFrame(result, columns=['Officer ID', 'Name', 'Sex', 'Joining Date'])
    with st.expander("Updated Officers"):
        st.dataframe(df)