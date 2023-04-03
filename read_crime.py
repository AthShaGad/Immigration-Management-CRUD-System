import pandas as pd
import streamlit as st
from database import view_all_data_crime
def read_crime():
    result = view_all_data_crime()
    df = pd.DataFrame(result, columns=['FIR Number', 'Name of the Police Station', 'Nature of Crime', 'Conviction Status', 'Passport Number'])
    with st.expander("View all Crimes"):
        st.dataframe(df)