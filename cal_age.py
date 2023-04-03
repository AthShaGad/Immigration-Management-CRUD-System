import pandas as pd
import streamlit as st
from database import get_passenger, view_only_passenger_id, calc_age_pass

def cal_age():
    list_of_passenger = [i[0] for i in view_only_passenger_id()]
    selected_passenger = st.selectbox("Passenger to Calculate Age for", list_of_passenger)
    if selected_passenger:
        st.warning("Do you want to calculate age for ::{}".format(selected_passenger))
    if st.button("Calculate Age for Selected Passenger"):
        calc_age_pass(selected_passenger)
    result = get_passenger(selected_passenger)
    df = pd.DataFrame(result,
                      columns=['Passport Number', 'First Name', 'Middle Initial', 'Last Name', 'Sex', 'Visa Number',
                               'Date of Birth', 'Minor Accompanier', 'Relation to the Minor', 'Age'])
    with st.expander("View Updated Passenger"):
        st.dataframe(df)