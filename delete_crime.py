import pandas as pd
import streamlit as st
from database import view_all_data_crime, view_only_fir_no, delete_crime_db
def delete_crime():
    list_of_crime = [i[0] for i in view_only_fir_no()]
    selected_crime = st.selectbox("Crime to Delete", list_of_crime)
    if selected_crime:
        st.warning("Do you want to delete ::{}".format(selected_crime))
    if st.button("Delete Crime"):
        delete_crime_db(selected_crime)
        st.success("Success!")
    result = view_all_data_crime()
    df = pd.DataFrame(result,
                      columns=['FIR Number', 'Name of the Police Station', 'Nature of Crime', 'Conviction Status',
                               'Passport Number'])
    with st.expander("View all Crimes"):
        st.dataframe(df)