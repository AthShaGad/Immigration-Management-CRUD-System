import pandas as pd
import streamlit as st
from database import view_all_data_arrival
def read_arrival():
    result = view_all_data_arrival()
    df = pd.DataFrame(result, columns=['Passport Number', 'Flight Number', 'Date of Arrival', 'Immigration Officer', 'Travel ID', 'Source', 'Officer ID'])
    with st.expander("View all Arrivals"):
        st.dataframe(df)