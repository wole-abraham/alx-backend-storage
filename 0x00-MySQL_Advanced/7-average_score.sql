-- Calculate the average score for the specified user


DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average_score DECIMAL(5, 2);

    -- Calculate the average score for the specified user
    SELECT AVG(score) INTO average_score
    FROM scores
    WHERE user_id = user_id;

    -- Store the average score in a new table (you may need to create this table first)
    INSERT INTO user_average_scores (user_id, average_score)
    VALUES (user_id, average_score)
    ON DUPLICATE KEY UPDATE average_score = average_score; -- Update if the record exists
END$$

DELIMITER ;
