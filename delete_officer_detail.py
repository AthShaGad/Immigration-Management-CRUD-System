import pandas as pd
import streamlit as st
from database import view_all_data_officer_detail, view_only_officer_id, delete_officer_db
def delete_officer_detail():
    list_of_officer = [i[0] for i in view_only_officer_id()]
    selected_officer = st.selectbox("Officer to Delete", list_of_officer)
    if selected_officer:
        st.warning("Do you want to delete ::{}".format(selected_officer))
    if st.button("Delete Officer"):
        delete_officer_db(selected_officer)
        st.success("Success!")
    result = view_all_data_officer_detail()
    df = pd.DataFrame(result, columns=['Officer ID', 'Name', 'Sex', 'Joining Date'])
    with st.expander("Updated Officers"):
        st.dataframe(df)