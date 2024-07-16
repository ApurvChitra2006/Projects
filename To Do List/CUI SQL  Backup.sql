DROP database if EXISTS todolist;
create database todolist;
use todolist;

DROP TABLE IF EXISTS `project`;
CREATE TABLE `project` (
  `ProjectCode` int NOT NULL,
  `ProjectName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ProjectCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `tasks`;
CREATE TABLE `tasks` (
  `TaskID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `Completed` int DEFAULT '0',
  `Project_ID` int DEFAULT NULL,
  PRIMARY KEY (`TaskID`),
  KEY `ProjectCode_idx` (`Project_ID`),
  CONSTRAINT `ProjectCode` FOREIGN KEY (`Project_ID`) REFERENCES `project` (`ProjectCode`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;taskstasks