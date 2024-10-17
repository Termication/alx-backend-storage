-- Creates a view 'need_meeting' that lists all students who meet the following criteria:
-- 1. Have a score strictly less than 80.
-- 2. Have either no record of a last meeting or the last meeting was more than one month ago.

CREATE VIEW need_meeting AS
SELECT name 
FROM students 
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH));
