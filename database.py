import mariadb
mydb = mariadb.connect(
user="atharva",
password="my_password",
host="127.0.0.1",
port=3306,
database="airport_immi_man"
)
c = mydb.cursor()
def create_tables():
    # c.execute('source c:/users/shaileshgadad/desktop/dbms lab/project/tables creation/tablesCreation.sql')
    pass

def add_data_arrival(pp_no, flight_no, date_of_arrival, immigration_officer, travel_id, source, officer_id):
    c.execute("insert into arrival (pp_no, flight_no, date_of_arrival, immigration_officer, travel_id, source, officer_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", (pp_no, flight_no, date_of_arrival, immigration_officer, travel_id, source, officer_id))
    mydb.commit()

def add_data_officer_detail(officer_id, name, sex, join_date):
    c.execute("insert into officer_details (officer_id, name, sex, join_date) VALUES (%s, %s, %s, %s)", (officer_id, name, sex, join_date))
    mydb.commit()

def add_data_passenger_detail(pp_no, fname, minit, lname, sex, visa_no, dob, minor_accompanier, relaion_to_minor, age):
    c.execute("insert into passenger_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %d)", (pp_no, fname, minit, lname, sex, visa_no, dob, minor_accompanier, relaion_to_minor, age))
    mydb.commit()

def add_data_travel_history(travel_id, date_of_arrival, date_of_departure, source, destination, pp_no):
    c.execute("insert into travel_history (travel_id, date_of_arrival, date_of_departure, source, destination, pp_no) VALUES (%s, %s, %s, %s, %s, %s)", (travel_id, date_of_arrival, date_of_departure, source, destination, pp_no))
    mydb.commit()

def add_data_crime(fir_no, police_station, nature_of_crime, conviction_status, pp_no):
    c.execute("insert into crime VALUES (%s, %s, %s, %s, %s)", (fir_no, police_station, nature_of_crime, conviction_status, pp_no))
    mydb.commit()

def add_data_nationality(pp_no, nationality):
    c.execute("insert into nationalities (pp_no, nationality) VALUES (%s, %s)", (pp_no, nationality))
    mydb.commit()

def view_all_data_arrival():
    c.execute('SELECT * FROM arrival')
    data = c.fetchall()
    return data

def view_all_data_officer_detail():
    c.execute('SELECT * FROM officer_details')
    data = c.fetchall()
    return data

def view_all_data_passenger_detail():
    c.execute('SELECT * FROM passenger_details')
    data = c.fetchall()
    return data

def view_all_data_travel_history():
    c.execute('SELECT * FROM travel_history')
    data = c.fetchall()
    return data

def view_all_data_crime():
    c.execute('SELECT * FROM crime')
    data = c.fetchall()
    return data

def view_all_data_nationality():
    c.execute('SELECT * FROM nationalities')
    data = c.fetchall()
    return data

def view_only_arrival_passport_no():
    c.execute('SELECT pp_no FROM arrival')
    data = c.fetchall()
    return data

def view_only_officer_id():
    c.execute('SELECT officer_id FROM officer_details')
    data = c.fetchall()
    return data

def view_only_passenger_id():
    c.execute('SELECT pp_no FROM passenger_details')
    data = c.fetchall()
    return data

def view_only_travel_id():
    c.execute('SELECT travel_id FROM travel_history')
    data = c.fetchall()
    return data

def view_only_fir_no():
    c.execute('SELECT fir_no FROM crime')
    data = c.fetchall()
    return data

def view_only_nationality():
    c.execute('SELECT * FROM nationalities')
    data = c.fetchall()
    return data

def get_arrival(pp_no):
    c.execute('SELECT * FROM arrival WHERE pp_no="{}"'.format(pp_no))
    data = c.fetchall()
    return data

def get_officer(selected_officer):
    c.execute('SELECT * FROM officer_details WHERE officer_id="{}"'.format(selected_officer))
    data = c.fetchall()
    return data

def get_passenger(selected_passenger):
    c.execute('SELECT * FROM passenger_details WHERE pp_no="{}"'.format(selected_passenger))
    data = c.fetchall()
    return data

def get_travel_history(selected_travel_history):
    c.execute('SELECT * FROM travel_history WHERE travel_id="{}"'.format(selected_travel_history))
    data = c.fetchall()
    return data

def get_crime(selected_crime):
    c.execute('SELECT * FROM crime WHERE fir_no="{}"'.format(selected_crime))
    data = c.fetchall()
    return data

def get_nationality(selected_pp_no, selected_nationality):
    c.execute('SELECT * FROM nationalities WHERE pp_no=%s and nationality=%s',(selected_pp_no, selected_nationality))
    data = c.fetchall()
    return data

def edit_arrival_data(new_pp_no, new_flight_no, new_date_of_arrival, new_immigration_officer, new_travel_id,new_source, new_officer_id, pp_no, flight_no, date_of_arrival, immigration_officer, travel_id, source, officer_id):
    c.execute("UPDATE arrival set pp_no = %s, flight_no=%s, date_of_arrival=%s, immigration_officer=%s, travel_id=%s, source=%s, officer_id=%s where pp_no=%s and flight_no=%s and  date_of_arrival=%s and immigration_officer=%s and travel_id=%s and source=%s and officer_id=%s", (new_pp_no, new_flight_no, new_date_of_arrival, new_immigration_officer, new_travel_id,new_source, new_officer_id, pp_no, flight_no, date_of_arrival, immigration_officer, travel_id, source, officer_id))
    mydb.commit()
    return

def edit_officer_data(new_officer_id, new_name, new_sex, new_join_date,officer_id, name, sex, join_date):
    c.execute("UPDATE officer_details set officer_id=%s, name=%s, sex=%s, join_date=%s where officer_id=%s and name=%s and sex=%s and join_date=%s", (new_officer_id, new_name, new_sex, new_join_date,officer_id, name, sex, join_date))
    mydb.commit()
    return

def edit_passenger_data(new_pp_no, new_fname, new_minit, new_lname, new_sex, new_visa_no, new_dob, new_minor_accompanier, new_relaion_to_minor, pp_no, fname, minit, lname, sex, visa_no, dob, minor_accompanier, relaion_to_minor):
    c.execute("UPDATE passenger_details set pp_no=%s, fname=%s, minit=%s, lname=%s, sex=%s, visa_no=%s, dob=%s, minor_accompanier=%s, relation_to_minor=%s where pp_no=%s", (new_pp_no, new_fname, new_minit, new_lname, new_sex, new_visa_no, new_dob, new_minor_accompanier, new_relaion_to_minor, pp_no))
    mydb.commit()
    return

def edit_travel_history(new_travel_id, new_date_of_arrival, new_date_of_departure, new_source, new_destination, new_pp_no, travel_id, date_of_arrival, date_of_departure, source, destination, pp_no):
    c.execute("UPDATE travel_history set travel_id=%s, date_of_arrival=%s, date_of_departure=%s, source=%s, destination=%s, pp_no=%s where travel_id=%s and date_of_arrival=%s and date_of_departure=%s and source=%s and destination=%s and pp_no=%s", (new_travel_id, new_date_of_arrival, new_date_of_departure, new_source, new_destination, new_pp_no, travel_id, date_of_arrival, date_of_departure, source, destination, pp_no))
    mydb.commit()
    return

def edit_crime(new_fir_no, new_police_station, new_nature_of_crime, new_conviction_status, new_pp_no, fir_no, police_station, nature_of_crime, conviction_status, pp_no):
    c.execute("UPDATE crime set fir_no=%s, police_station=%s, nature_of_crime=%s, conviction_status=%s, pp_no=%s where fir_no=%s and police_station=%s and nature_of_crime=%s and conviction_status=%s and pp_no=%s", (new_fir_no, new_police_station, new_nature_of_crime, new_conviction_status, new_pp_no, fir_no, police_station, nature_of_crime, conviction_status, pp_no))
    mydb.commit()
    return

def edit_nationality(new_pp_no, new_nationality, pp_no, nationality):
    c.execute("UPDATE nationalities set pp_no=%s, nationality=%s where pp_no=%s and nationality=%s", (new_pp_no, new_nationality, pp_no, nationality))
    mydb.commit()
    return

def delete_arrival_db(selected_arrival):
    c.execute('DELETE FROM arrival WHERE pp_no="{}"'.format(selected_arrival))
    mydb.commit()

def delete_officer_db(selected_officer):
    c.execute('DELETE FROM officer_details WHERE officer_id="{}"'.format(selected_officer))
    mydb.commit()

def delete_passenger_db(selected_passenger):
    c.execute('DELETE FROM passenger_details WHERE pp_no="{}"'.format(selected_passenger))
    mydb.commit()

def delete_traveller_db(selected_traveller):
    c.execute('DELETE FROM travel_history WHERE travel_id="{}"'.format(selected_traveller))
    mydb.commit()

def delete_crime_db(selected_crime):
    c.execute('DELETE FROM crime WHERE fir_no="{}"'.format(selected_crime))
    mydb.commit()

def delete_nationality_db(selected_pp_no, selected_nationality):
    c.execute('DELETE FROM nationalities WHERE pp_no="{}" and nationality="{}"'.format(selected_pp_no, selected_nationality))
    mydb.commit()

def custom_query(query):
    c.execute(query)
    data = c.fetchall()
    return data

def calc_age_pass(selected_passenger):
    # c.execute('''set @p0=%s;
    # set @p1=(select passenger_details.dob from passenger_details where passenger_details.pp_no=@p0);
    # set @p2=0;
    # call dob_age(@p0, @p1, @p2);''', (selected_passenger,))
    age = get_passenger(selected_passenger)[0][6]
    c.execute('call dob_age(%s, %s, %s)', (selected_passenger, age, ' '))