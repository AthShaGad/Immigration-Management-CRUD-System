from read_arrival import read_arrival
from read_officer_detail import read_officer_detail
from read_passenger_detail import read_passenger_detail
from read_travel_history import read_travel_history
from read_crime import read_crime
from read_nationality import read_nationality

def read(selected_table):
    if selected_table == 'Arrival':
        read_arrival()
    elif selected_table == 'Officer Details':
        read_officer_detail()
    elif selected_table == 'Passenger Details':
        read_passenger_detail()
    elif selected_table == 'Travel History':
        read_travel_history()
    elif selected_table == 'Crimes':
        read_crime()
    elif selected_table == 'Nationalities':
        read_nationality()