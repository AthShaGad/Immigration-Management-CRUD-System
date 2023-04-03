import pandas as pd
import streamlit as st
from database import view_all_data_passenger_detail, view_only_passenger_id, delete_passenger_db
def delete_passenger_detail():
    list_of_passenger = [i[0] for i in view_only_passenger_id()]
    selected_passenger = st.selectbox("Passenger to Delete", list_of_passenger)
    if selected_passenger:
        st.warning("Do you want to delete ::{}".format(selected_passenger))
    if st.button("Delete Passenger"):
        delete_passenger_db(selected_passenger)
        st.success("Success!")
    result = view_all_data_passenger_detail()
    df = pd.DataFrame(result,
                      columns=['Passport Number', 'First Name', 'Middle Initial', 'Last Name', 'Sex', 'Visa Number',
                               'Date of Birth', 'Minor Accompanier', 'Relation to the Minor', 'Age'])
    with st.expander("View Updated Passengers"):
        st.dataframe(df)