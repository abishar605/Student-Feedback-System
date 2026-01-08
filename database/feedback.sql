CREATE DATABASE feedback_db;
USE feedback_db;

CREATE TABLE student_feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100),
    class VARCHAR(20),
    subject VARCHAR(100),
    rating INT,
    comments TEXT
);
