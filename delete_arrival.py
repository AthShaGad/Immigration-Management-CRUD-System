import pandas as pd
import streamlit as st
from database import view_all_data_arrival, view_only_arrival_passport_no, delete_arrival_db
def delete_arrival():
    list_of_arrival = [i[0] for i in view_only_arrival_passport_no()]
    selected_arrival = st.selectbox("Arrival to Delete", list_of_arrival)
    if selected_arrival:
        st.warning("Do you want to delete ::{}".format(selected_arrival))
    if st.button("Delete Arrival"):
        delete_arrival_db(selected_arrival)
        st.success("Success!")
    result = view_all_data_arrival()
    df = pd.DataFrame(result, columns=['Passport Number', 'Flight Number', 'Date of Arrival', 'Immigration Officer',
                                       'Travel ID', 'Source', 'Officer ID'])
    with st.expander("Updated Arrivals"):
        st.dataframe(df)