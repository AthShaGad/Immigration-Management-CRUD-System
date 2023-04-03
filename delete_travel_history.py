import pandas as pd
import streamlit as st
from database import view_all_data_travel_history, view_only_travel_id, delete_traveller_db
def delete_travel_history():
    list_of_traveller = [i[0] for i in view_only_travel_id()]
    selected_traveller = st.selectbox("Travel History to Delete", list_of_traveller)
    if selected_traveller:
        st.warning("Do you want to delete ::{}".format(selected_traveller))
    if st.button("Delete Travel History"):
        delete_traveller_db(selected_traveller)
        st.success("Success!")
    result = view_all_data_travel_history()
    df = pd.DataFrame(result, columns=['Travel ID', 'Date of Arrival', 'Date of Departure', 'Source', 'Destination',
                                       'Passport Number'])
    with st.expander("View all Travel History"):
        st.dataframe(df)