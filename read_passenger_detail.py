import pandas as pd
import streamlit as st
from database import view_all_data_passenger_detail
def read_passenger_detail():
    result = view_all_data_passenger_detail()
    df = pd.DataFrame(result, columns=['Passport Number', 'First Name', 'Middle Initial', 'Last Name', 'Sex', 'Visa Number', 'Date of Birth', 'Minor Accompanier', 'Relation to the Minor', 'Age'])
    with st.expander("View all Passengers"):
        st.dataframe(df)