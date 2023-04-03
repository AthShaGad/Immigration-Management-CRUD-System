import pandas as pd
import streamlit as st
from database import view_all_data_officer_detail
def read_officer_detail():
    result = view_all_data_officer_detail()
    df = pd.DataFrame(result, columns=['Officer ID', 'Name', 'Sex', 'Joining Date'])
    with st.expander("View all Officers"):
        st.dataframe(df)