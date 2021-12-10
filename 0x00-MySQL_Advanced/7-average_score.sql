-- creates a stored procedure that computes and store average for a student

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INTEGER)
BEGIN
	UPDATE users SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id GROUP BY corrections.user_id ) WHERE id = user_id;
END $$
DELIMITER ;
