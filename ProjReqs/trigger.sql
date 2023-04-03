DELIMITER $$
CREATE TRIGGER check_join_date
BEFORE INSERT
ON officer_details FOR EACH ROW
BEGIN
DECLARE error_msg VARCHAR(255);
SET error_msg = ('The join date is invalid');
IF (new.join_date>(select GETDATE())) THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = error_msg;
END IF;
END $$
DELIMITER ;