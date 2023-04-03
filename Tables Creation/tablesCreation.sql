-- Table Creation
create table IF NOT EXISTS passenger_details(pp_no varchar(8) not null primary key, fname varchar(255) not null, minit varchar(1),
lname varchar(255) not null, sex varchar(1), visa_no varchar(8), dob date, 
minor_accompanier varchar(8), relation_to_minor varchar(255), foreign key (minor_accompanier) 
references passenger_details(pp_no));

create table IF NOT EXISTS travel_history(travel_id varchar(5) primary key not null, date_of_arrival date not null,
date_of_departure date not null, source varchar(255) not null, destination varchar(255) not null, 
pp_no varchar(8) not null, foreign key (pp_no) references passenger_details(pp_no));

create table IF NOT EXISTS crime (fir_no varchar(6) not null primary key, police_station varchar(255), nature_of_crime varchar(255) not null,
conviction_status varchar(255) not null, pp_no varchar(8) not null, foreign key (pp_no) references passenger_details(pp_no));

create table IF NOT EXISTS officer_details(officer_id varchar(4) not null primary key, name varchar(255) not null, sex varchar(1),
join_date date not null);

create table IF NOT EXISTS arrival(pp_no varchar(8) not null primary key, flight_no varchar(4), date_of_arrival date,
immigration_officer varchar(255), travel_id varchar(5), source varchar(255), officer_id varchar(4), 
foreign key (pp_no) references passenger_details(pp_no), foreign key (officer_id) references officer_details(officer_id));

create table IF NOT EXISTS nationalities(pp_no varchar(8) not null, nationality varchar(100) not null,
foreign key (pp_no) references passenger_details(pp_no), primary key(pp_no, nationality));

-- -- Trigger
--  DELIMITER $$
-- CREATE TRIGGER check_birth_date
-- BEFORE INSERT
-- ON passenger_details FOR EACH ROW
-- BEGIN
-- DECLARE error_msg VARCHAR(255);
-- declare age int;
-- set age=DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(),new.dob)), '%Y') + 0;
-- SET error_msg = ('Minor, add a companion');
-- IF (age<3 and new.minor_accompanier is null) THEN
-- SIGNAL SQLSTATE '45000'
-- SET MESSAGE_TEXT = error_msg;
-- END IF;
-- END $$
-- DELIMITER ;

-- -- Function
-- DELIMITER $$
-- CREATE FUNCTION no_of_males(males int)
-- returns varchar(50)
-- deterministic
-- begin
-- declare return_value varchar(50);
-- if males>1 then
--     set return_value="Males have come to India";
-- else
--     set return_value="Males have not come to India";
-- end if;
-- return return_value;
-- end $$
-- DELIMITER ;

-- with numbs as (select count(*) as cnt from passenger_details where sex="M") 
-- select no_of_males(cnt) as male_count from numbs;




-- select fname, lname, pp_no from passenger_details where pp_no in (select pp_no from passenger_details except select pp_no from nationalities);

-- -- Procedure
-- DELIMITER $$
-- create procedure dob_age(in pp_no varchar(20), in dob date, out age int)
-- begin
-- update passenger_details set  
-- passenger_details.age =DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(),dob)), '%Y') + 0
-- where passenger_details.pp_no=pp_no;
-- end;
-- $$
-- DELIMITER ;

-- set @p0='12345678';
-- set @p1=(select passenger_details.dob from passenger_details where passenger_details.pp_no=@p0);
-- set @p2=0;
-- call dob_age(@p0, @p1, @p2);
-- select * from passenger_details where passenger_details.pp_no=@p0;

-- -- CRUD Statements
-- insert into arrival (pp_no, flight_no, date_of_arrival, immigration_officer, travel_id, source, officer_id) VALUES (%s, %s, %s, %s, %s, %s, %s)
-- insert into officer_details (officer_id, name, sex, join_date) VALUES (%s, %s, %s, %s)
-- insert into passenger_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %d)
-- insert into travel_history (travel_id, date_of_arrival, date_of_departure, source, destination, pp_no) VALUES (%s, %s, %s, %s, %s, %s)
-- insert into crime VALUES (%s, %s, %s, %s, %s)
-- insert into nationalities (pp_no, nationality) VALUES (%s, %s)
-- SELECT * FROM arrival
-- SELECT * FROM officer_details
-- SELECT * FROM passenger_details
-- SELECT * FROM travel_history
-- SELECT * FROM crime
-- SELECT * FROM nationalities
-- SELECT pp_no FROM arrival
-- SELECT officer_id FROM officer_details
-- SELECT pp_no FROM passenger_details
-- SELECT travel_id FROM travel_history
-- SELECT fir_no FROM crime
-- SELECT * FROM nationalities
-- SELECT * FROM arrival WHERE pp_no="{}"
-- 'SELECT * FROM officer_details WHERE officer_id="{}"'
-- SELECT * FROM passenger_details WHERE pp_no="{}"
-- SELECT * FROM travel_history WHERE travel_id="{}"
-- SELECT * FROM crime WHERE fir_no="{}"
-- SELECT * FROM nationalities WHERE pp_no=%s and nationality=%s
-- UPDATE arrival set pp_no = %s, flight_no=%s, date_of_arrival=%s, immigration_officer=%s, travel_id=%s, source=%s, officer_id=%s where pp_no=%s and flight_no=%s and  date_of_arrival=%s and immigration_officer=%s and travel_id=%s and source=%s and officer_id=%s
-- UPDATE officer_details set officer_id=%s, name=%s, sex=%s, join_date=%s where officer_id=%s and name=%s and sex=%s and join_date=%s
-- "UPDATE passenger_details set pp_no=%s, fname=%s, minit=%s, lname=%s, sex=%s, visa_no=%s, dob=%s, minor_accompanier=%s, relation_to_minor=%s where pp_no=%s"
-- UPDATE travel_history set travel_id=%s, date_of_arrival=%s, date_of_departure=%s, source=%s, destination=%s, pp_no=%s where travel_id=%s and date_of_arrival=%s and date_of_departure=%s and source=%s and destination=%s and pp_no=%s
-- UPDATE crime set fir_no=%s, police_station=%s, nature_of_crime=%s, conviction_status=%s, pp_no=%s where fir_no=%s and police_station=%s and nature_of_crime=%s and conviction_status=%s and pp_no=%s
-- UPDATE nationalities set pp_no=%s, nationality=%s where pp_no=%s and nationality=%s
-- DELETE FROM arrival WHERE pp_no="{}"
-- DELETE FROM officer_details WHERE officer_id="{}"
-- DELETE FROM passenger_details WHERE pp_no="{}"
-- DELETE FROM travel_history WHERE travel_id="{}"
-- DELETE FROM crime WHERE fir_no="{}"
-- DELETE FROM nationalities WHERE pp_no="{}" and nationality="{}"
-- call dob_age(%s, %s, %s)