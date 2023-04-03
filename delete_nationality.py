import pandas as pd
import streamlit as st
from database import view_all_data_nationality, view_only_nationality, delete_nationality_db
def delete_nationality():
    list_of_pp_no = [i[0] for i in view_only_nationality()]
    list_of_nationality = [i[1] for i in view_only_nationality()]
    selected_pp_no = st.selectbox("Passport Number to Delete", list_of_pp_no)
    selected_nationality = st.selectbox("Nationality to Delete", list_of_nationality)
    if selected_pp_no and selected_nationality:
        st.warning("Do you want to delete ::{}, {}".format(selected_pp_no, selected_nationality))
    if st.button("Delete Nationality"):
        delete_nationality_db(selected_pp_no, selected_nationality)
        st.success("Success!")
    result = view_all_data_nationality()
    df = pd.DataFrame(result, columns=['Passport', 'Nationality'])
    with st.expander("View all Nationalities"):
        st.dataframe(df)