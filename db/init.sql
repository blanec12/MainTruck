CREATE DATABASE test;
USE test;

CREATE TABLE Users (
  ID INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  Username VARCHAR(255) DEFAULT NULL,
  Password VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY(ID),
  UNIQUE KEY `Username` (`Username`)
);

INSERT INTO Users
  (Username, Password)
VALUES
  ('test', 'test');