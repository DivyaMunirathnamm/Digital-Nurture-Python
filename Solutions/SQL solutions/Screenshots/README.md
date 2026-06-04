# SQL Output Screenshots

This folder contains selected output screenshots from the SQL exercises completed as part of the Cognizant Digital Nurture 5.0 training program.

Due to the large number of SQL queries and database operations, only a representative set of screenshots has been included. These screenshots demonstrate the successful execution of database creation, schema design, data insertion, joins, aggregate functions, grouping operations, and analytical SQL queries.

The screenshots are provided for demonstration and verification purposes and do not include outputs from every individual SQL exercise.

## Sample Queries Included

### Database Creation

Demonstrates the creation of the Event Management database.

#### CODE

```sql
CREATE DATABASE event_management;

USE event_management;
```

#### OUTPUT

<img width="1213" height="1079" alt="image" src="https://github.com/user-attachments/assets/ac8acf64-1c77-41a2-8fcc-2539f0fabc10" />

### Schema Creation

Demonstrates table creation using primary keys, foreign keys, constraints, and relationships.

#### CODE

```sql
USE event_management;

CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    city VARCHAR(100) NOT NULL,
    registration_date DATE NOT NULL
);

CREATE TABLE Events (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    city VARCHAR(100) NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    status ENUM('upcoming','completed','cancelled'),
    organizer_id INT,
    FOREIGN KEY (organizer_id) REFERENCES Users(user_id)
);

CREATE TABLE Sessions (
    session_id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT,
    title VARCHAR(200) NOT NULL,
    speaker_name VARCHAR(100) NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    FOREIGN KEY (event_id) REFERENCES Events(event_id)
);

CREATE TABLE Registrations (
    registration_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    event_id INT,
    registration_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (event_id) REFERENCES Events(event_id)
);

CREATE TABLE Feedback (
    feedback_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    event_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comments TEXT,
    feedback_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (event_id) REFERENCES Events(event_id)
);

CREATE TABLE Resources (
    resource_id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT,
    resource_type ENUM('pdf','image','link'),
    resource_url VARCHAR(255) NOT NULL,
    uploaded_at DATETIME NOT NULL,
    FOREIGN KEY (event_id) REFERENCES Events(event_id)
);
);
```

#### OUTPUT

<img width="1210" height="1078" alt="image" src="https://github.com/user-attachments/assets/f5015af6-bf4a-4d2a-987c-27dc8e70843c" />



### Sample Data Insertion

Demonstrates inserting records into database tables.

#### CODE

```sql
INSERT INTO Users (user_id, full_name, email, city, registration_date)
VALUES
(1, 'Alice Johnson', 'alice@example.com', 'New York', '2024-12-01'),
(2, 'Bob Smith', 'bob@example.com', 'Los Angeles', '2024-12-05'),
(3, 'Charlie Lee', 'charlie@example.com', 'Chicago', '2024-12-10'),
(4, 'Diana King', 'diana@example.com', 'New York', '2025-01-15'),
(5, 'Ethan Hunt', 'ethan@example.com', 'Los Angeles', '2025-02-01');

INSERT INTO Events
(event_id, title, description, city, start_date, end_date, status, organizer_id)
VALUES
(1, 'Tech Innovators Meetup',
'A meetup for tech enthusiasts.',
'New York',
'2025-06-10 10:00:00',
'2025-06-10 16:00:00',
'upcoming',
1),

(2, 'AI & ML Conference',
'Conference on AI and ML advancements.',
'Chicago',
'2025-05-15 09:00:00',
'2025-05-15 17:00:00',
'completed',
3),

(3, 'Frontend Development Bootcamp',
'Hands-on training on frontend tech.',
'Los Angeles',
'2025-07-01 10:00:00',
'2025-07-03 16:00:00',
'upcoming',
2);

INSERT INTO Sessions
(session_id, event_id, title, speaker_name, start_time, end_time)
VALUES
(1, 1, 'Opening Keynote', 'Dr. Tech',
'2025-06-10 10:00:00',
'2025-06-10 11:00:00'),

(2, 1, 'Future of Web Dev', 'Alice Johnson',
'2025-06-10 11:15:00',
'2025-06-10 12:30:00'),

(3, 2, 'AI in Healthcare', 'Charlie Lee',
'2025-05-15 09:30:00',
'2025-05-15 11:00:00'),

(4, 3, 'Intro to HTML5', 'Bob Smith',
'2025-07-01 10:00:00',
'2025-07-01 12:00:00');

INSERT INTO Registrations
(registration_id, user_id, event_id, registration_date)
VALUES
(1, 1, 1, '2025-05-01'),
(2, 2, 1, '2025-05-02'),
(3, 3, 2, '2025-04-30'),
(4, 4, 2, '2025-04-28'),
(5, 5, 3, '2025-06-15');

INSERT INTO Feedback
(feedback_id, user_id, event_id, rating, comments, feedback_date)
VALUES
(1, 3, 2, 4, 'Great insights!', '2025-05-16'),
(2, 4, 2, 5, 'Very informative.', '2025-05-16'),
(3, 2, 1, 3, 'Could be better.', '2025-06-11');

INSERT INTO Resources
(resource_id, event_id, resource_type, resource_url, uploaded_at)
VALUES
(1, 1, 'pdf',
'https://portal.com/resources/tech_meetup_agenda.pdf',
'2025-05-01 10:00:00'),

(2, 2, 'image',
'https://portal.com/resources/ai_poster.jpg',
'2025-04-20 09:00:00'),

(3, 3, 'link',
'https://portal.com/resources/html5_docs',
'2025-06-25 15:00:00');
```

#### OUTPUT


<img width="1211" height="1075" alt="image" src="https://github.com/user-attachments/assets/32b500f9-4136-4d5d-9fd6-7d914dc0e57a" />

### Question 1 - User Upcoming Events

Show a list of all upcoming events a user is registered for in their city, sorted by date.

#### CODE
```sql
SELECT u.full_name, e.title, e.city, e.start_date
FROM Users u
JOIN Registrations r ON u.user_id = r.user_id
JOIN Events e ON r.event_id = e.event_id
WHERE e.status = 'upcoming'
AND u.city = e.city
ORDER BY e.start_date;
```

#### OUTPUT

<img width="1208" height="1075" alt="image" src="https://github.com/user-attachments/assets/45843283-743f-4731-94f2-f8713808230a" />

### Question 24 - Average Session Duration per Event

Compute the average duration (in minutes) of sessions in each event.

#### CODE
```sql
SELECT event_id,
AVG(TIMESTAMPDIFF(MINUTE,start_time,end_time))
AS avg_duration_minutes
FROM Sessions
GROUP BY event_id;
```
## OUTPUT

<img width="1211" height="1076" alt="image" src="https://github.com/user-attachments/assets/e51b4a2b-1654-42ee-9433-4f1d34a6e90c" />



## SQL Concepts Demonstrated

* CREATE DATABASE
* CREATE TABLE
* INSERT INTO
* SELECT
* WHERE
* ORDER BY
* GROUP BY
* HAVING
* INNER JOIN
* LEFT JOIN
* Aggregate Functions
* Subqueries
* Foreign Key Relationships

## Note

Only selected screenshots have been uploaded to maintain repository clarity and organization. The complete SQL scripts, schema definitions, sample data, and query solutions are available in the SQL Solutions folder.

For complete implementations and additional SQL exercises, please refer to the corresponding SQL files.
