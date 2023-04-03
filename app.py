import streamlit as st
from create import create
from database import create_tables
from delete import delete
from read import read
from update import update
from custom import custom
from cal_age import cal_age

def main():
    st.title("AIRPORT IMMIGRATION MANAGEMENT")
    st.subheader("By Atharva S Gadad - PES1UG20CS088")
    menu = ["Create", "Read", "Update", "Delete", "Calculate Age", "Custom Query"]
    list_of_tables=['Arrival', 'Passenger Details', 'Travel History', 'Crimes', 'Officer Details', 'Nationalities']
    choice = st.sidebar.selectbox("Menu", menu)
    create_tables()
    if choice == "Create":
        st.subheader("Choose the Table: ")
        selected_table = st.selectbox("Table to Create", list_of_tables)
        create(selected_table)
    elif choice == "Read":
        st.subheader("Choose the Table: ")
        selected_table = st.selectbox("Table to Read", list_of_tables)
        read(selected_table)
    elif choice == "Update":
        st.subheader("Choose the Table: ")
        selected_table = st.selectbox("Table to Update", list_of_tables)
        update(selected_table)
    elif choice == "Delete":
        st.subheader("Choose the Table: ")
        selected_table = st.selectbox("Table to Delete", list_of_tables)
        delete(selected_table)
    elif choice == "Calculate Age":
        cal_age()
    elif choice == "Custom Query":
        custom()
    else:
        st.subheader("About Immigration")
if __name__ == '__main__':
    main()