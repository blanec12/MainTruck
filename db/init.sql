CREATE DATABASE MainTruckDB;
USE MainTruckDB;

CREATE TABLE Users (
  ID VARCHAR(255) NOT NULL DEFAULT (UUID()),
  FirstName VARCHAR(50) DEFAULT NULL,
  LastName VARCHAR(50) DEFAULT NULL,
  Phone VARCHAR(50) DEFAULT NULL,
  Email VARCHAR(50) DEFAULT NULL,
  Username VARCHAR(50) DEFAULT NULL,
  Password VARCHAR(255) DEFAULT NULL,
  Role VARCHAR(50) DEFAULT NULL,
  CreatedByID VARCHAR(255) DEFAULT (ID),
  CreatedDateTime DATETIME DEFAULT NOW(),
  LastModifiedByID VARCHAR(255) DEFAULT (ID),
  LastModifiedDateTime DATETIME DEFAULT NOW(),
  PRIMARY KEY(ID),
  UNIQUE KEY `Username` (`Username`)
);

INSERT INTO Users
  (FirstName, LastName, Phone, Email, Username, Password, Role)
VALUES
  ("Administrator", NULL, NULL, NULL, "admin", "setup", "Administrator");