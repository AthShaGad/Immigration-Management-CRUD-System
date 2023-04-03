from create_arrival import create_arrival
from create_officer_detail import create_officer_detail
from create_passenger_detail import create_passenger_detail
from create_travel_history import create_travel_history
from create_crime import create_crime
from create_nationality import create_nationality

def create(selected_table):
    if selected_table == 'Arrival':
        create_arrival()
    elif selected_table == 'Officer Details':
        create_officer_detail()
    elif selected_table == 'Passenger Details':
        create_passenger_detail()
    elif selected_table == 'Travel History':
        create_travel_history()
    elif selected_table == 'Crimes':
        create_crime()
    elif selected_table == 'Nationalities':
        create_nationality()