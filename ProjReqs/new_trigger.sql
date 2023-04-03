 DELIMITER $$
CREATE TRIGGER check_birth_date
BEFORE INSERT
ON passenger_details FOR EACH ROW
BEGIN
DECLARE error_msg VARCHAR(255);
declare age int;
set age=DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(),new.dob)), '%Y') + 0;
SET error_msg = ('Minor, add a companion');
IF (age<3 and new.minor_accompanier is null) THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = error_msg;
END IF;
END $$
DELIMITER ;