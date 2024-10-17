-- Creates a trigger that resets the 'valid_email' attribute 
-- only when the 'email' field is updated.
DELIMITER $$ 
CREATE TRIGGER validate BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END; $$
DELIMITER ;
