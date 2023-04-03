DELIMITER $$
CREATE FUNCTION no_of_males(males int)
returns varchar(50)
deterministic
begin
declare return_value varchar(50);
if males>1 then
    set return_value="Males have come to India";
else
    set return_value="Males have not come to India";
end if;
return return_value;
end $$
DELIMITER ;

with numbs as (select count(*) as cnt from passenger_details where sex="M") 
select no_of_males(cnt) as male_count from numbs;




select fname, lname, pp_no from passenger_details where pp_no in (select pp_no from passenger_details except select pp_no from nationalities);