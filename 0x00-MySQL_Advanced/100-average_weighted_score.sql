-- Creates a stored procedure 'ComputeAverageWeightedScoreForUser'
-- that calculates and stores the average weighted score for a specified student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    DECLARE tot_weighted_score INT DEFAULT 0;
    DECLARE tot_weight INT DEFAULT 0;

    -- Calculate the total weighted score for the specified user.
    SELECT SUM(corrections.score * projects.weight) INTO tot_weighted_score
    FROM corrections 
    INNER JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Calculate the total weight for the specified user.
    SELECT SUM(projects.weight) INTO tot_weight 
    FROM corrections
    INNER JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- If total weight is zero, set the average score to zero for the user.
    IF tot_weight = 0 THEN
        UPDATE users
        SET users.average_score = 0
        WHERE users.id = user_id;
    ELSE
        -- Otherwise, calculate the average weighted score for the user.
        UPDATE users
        SET users.average_score = tot_weighted_score / tot_weight
        WHERE users.id = user_id;
    END IF;
END //
DELIMITER ;
