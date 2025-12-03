
CREATE TABLE IF NOT EXISTS students (
    -- Unique student identifier (primary key)
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- Student's full name
    full_name TEXT NOT NULL,  
    -- Student's year of birth
    birth_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS grades (
    -- Unique grade identifier (primary key)
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- Foreign key referencing student's id in students table
    student_id INTEGER NOT NULL,
    -- Name of the subject for which the grade is given
    subject TEXT NOT NULL,
    -- Grade for the subject (must be between 1 and 100)
    grade INTEGER NOT NULL CHECK (grade >= 1 AND grade <= 100),
    -- Foreign key constraint linking to students table
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_students_name ON students(full_name);
CREATE INDEX IF NOT EXISTS idx_students_birth_year ON students(birth_year);
CREATE INDEX IF NOT EXISTS idx_grades_student ON grades(student_id);
CREATE INDEX IF NOT EXISTS idx_grades_subject ON grades(subject);
CREATE INDEX IF NOT EXISTS idx_grades_student_grade ON grades(student_id, grade);


INSERT INTO students (full_name, birth_year) VALUES
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

INSERT INTO grades (student_id, subject, grade) VALUES
(1, 'Math', 88),
(1, 'English', 92),
(1, 'Science', 85),
(2, 'Math', 75),
(2, 'History', 83),
(2, 'English', 79),
(3, 'Science', 95),
(3, 'Math', 91),
(3, 'Art', 89),
(4, 'Math', 84),
(4, 'Science', 88),
(4, 'Physical Education', 93),
(5, 'English', 90),
(5, 'History', 85),
(5, 'Math', 88),
(6, 'Science', 72),
(6, 'Math', 78),
(6, 'English', 81),
(7, 'Art', 94),
(7, 'Science', 87),
(7, 'Math', 90),
(8, 'History', 77),
(8, 'Math', 83),
(8, 'Science', 80),
(9, 'English', 96),
(9, 'Math', 89),
(9, 'Art', 92);


SELECT s.full_name, g.subject, g.grade
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.full_name = 'Alice Johnson'
ORDER BY g.subject;


SELECT 
    s.id,
    s.full_name,
    ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC;


SELECT id, full_name, birth_year
FROM students
WHERE birth_year > 2004
ORDER BY birth_year, full_name;


SELECT 
    subject,
    ROUND(AVG(grade), 2) as average_grade
FROM grades
GROUP BY subject
ORDER BY average_grade DESC;

SELECT 
    s.id,
    s.full_name,
    ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC
LIMIT 3;


SELECT DISTINCT
    s.id,
    s.full_name,
    g.subject,
    g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80
ORDER BY s.full_name, g.subject;
