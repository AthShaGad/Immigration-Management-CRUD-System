from update_arrival import update_arrival
from update_officer_detail import update_officer_detail
from update_passenger_detail import update_passenger_detail
from update_travel_history import update_travel_history
from update_crime import update_crime
from update_nationality import update_nationality

def update(selected_table):
    if selected_table == 'Arrival':
        update_arrival()
    elif selected_table == 'Officer Details':
        update_officer_detail()
    elif selected_table == 'Passenger Details':
        update_passenger_detail()
    elif selected_table == 'Travel History':
        update_travel_history()
    elif selected_table == 'Crimes':
        update_crime()
    elif selected_table == 'Nationalities':
        update_nationality()