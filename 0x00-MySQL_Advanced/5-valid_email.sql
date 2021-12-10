-- create trigger that resets the attribute valid_mail only when email has been changed

DELIMITER $$
CREATE TRIGGER validate BEFORE UPDATE ON users FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email THEN
		SET NEW.valid_email = 0;
	END IF;
END$$
DELIMITER ;
