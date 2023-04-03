from delete_arrival import delete_arrival
from delete_officer_detail import delete_officer_detail
from delete_passenger_detail import delete_passenger_detail
from delete_travel_history import delete_travel_history
from delete_crime import delete_crime
from delete_nationality import delete_nationality

def delete(selected_table):
    if selected_table == 'Arrival':
        delete_arrival()
    elif selected_table == 'Officer Details':
        delete_officer_detail()
    elif selected_table == 'Passenger Details':
        delete_passenger_detail()
    elif selected_table == 'Travel History':
        delete_travel_history()
    elif selected_table == 'Crimes':
        delete_crime()
    elif selected_table == 'Nationalities':
        delete_nationality()