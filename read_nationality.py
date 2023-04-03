import pandas as pd
import streamlit as st
from database import view_all_data_nationality
def read_nationality():
    result = view_all_data_nationality()
    df = pd.DataFrame(result, columns=['Passport', 'Nationality'])
    with st.expander("View all Nationalities"):
        st.dataframe(df)