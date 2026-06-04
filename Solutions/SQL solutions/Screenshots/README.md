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
CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    city VARCHAR(100) NOT NULL,
    registration_date DATE NOT NULL
);
```

#### OUTPUT

<img width="1210" height="1078" alt="image" src="https://github.com/user-attachments/assets/f5015af6-bf4a-4d2a-987c-27dc8e70843c" />



### Sample Data Insertion

Demonstrates inserting records into database tables.

#### CODE

```sql
INSERT INTO Users
(user_id, full_name, email, city, registration_date)
VALUES
(1, 'Alice Johnson', 'alice@example.com', 'New York', '2024-12-01');
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
