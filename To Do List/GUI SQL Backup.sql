drop database if exists `todolistgui`;
create database `todolistgui`;
use `todolistgui`;

DROP TABLE IF EXISTS `task`;
CREATE TABLE `task` (
  `code` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) DEFAULT NULL,
  `Deadline` date DEFAULT NULL,
  `Completed` bit(1) DEFAULT b'0',
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
