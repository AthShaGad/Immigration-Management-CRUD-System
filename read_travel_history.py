import pandas as pd
import streamlit as st
from database import view_all_data_travel_history
def read_travel_history():
    result = view_all_data_travel_history()
    df = pd.DataFrame(result, columns=['Travel ID', 'Date of Arrival', 'Date of Departure', 'Source', 'Destination', 'Passport Number'])
    with st.expander("View all Travel History"):
        st.dataframe(df)