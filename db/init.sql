CREATE DATABASE MainTruckDB;
USE MainTruckDB;

CREATE TABLE users (
  id VARCHAR(255) NOT NULL DEFAULT (UUID()),
  firstName VARCHAR(100) DEFAULT NULL,
  lastName VARCHAR(100) DEFAULT NULL,
  phone VARCHAR(50) DEFAULT NULL,
  email VARCHAR(50) DEFAULT NULL,
  username VARCHAR(50) DEFAULT NULL,
  password VARCHAR(255) DEFAULT NULL,
  role VARCHAR(50) DEFAULT NULL,
  createdByID VARCHAR(255) DEFAULT (ID),
  createdDateTime DATETIME DEFAULT NOW(),
  lastModifiedByID VARCHAR(255) DEFAULT (ID),
  lastModifiedDateTime DATETIME DEFAULT NOW(),
  isAdmin INT DEFAULT (1),
  PRIMARY KEY(id),
  UNIQUE KEY `username` (`username`)
);

INSERT INTO users
  (firstName, lastName, phone, email, username, password, role)
VALUES
  ("Administrator", "", NULL, NULL, "admin", "setup", "Administrator");