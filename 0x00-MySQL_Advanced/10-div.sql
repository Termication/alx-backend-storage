-- Creates a function 'SafeDiv' that performs division of two numbers.
-- It returns the result of 'a' divided by 'b', or returns 0 if 'b' equals 0.
DELIMITER $$ ;
CREATE FUNCTION SafeDiv(
    a INT,
    b INT
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE result FLOAT;
    IF b = 0 THEN
        RETURN 0;
    END IF;
    SET result = (a * 1.0) / b;
    RETURN result;
END;$$
DELIMITER ;
