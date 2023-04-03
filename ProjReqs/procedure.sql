DELIMITER $$
create procedure dob_age(in pp_no varchar(20), in dob date, out age int)
begin
update passenger_details set  
passenger_details.age =DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(),dob)), '%Y') + 0
where passenger_details.pp_no=pp_no;
end;
$$
DELIMITER ;

set @p0='12345678';
set @p1=(select passenger_details.dob from passenger_details where passenger_details.pp_no=@p0);
set @p2=0;
call dob_age(@p0, @p1, @p2);
select * from passenger_details where passenger_details.pp_no=@p0;