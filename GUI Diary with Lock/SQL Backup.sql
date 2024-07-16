DROP database if EXISTS `user_pass`;
CREATE database `user_pass`;
use `user_pass`;


DROP TABLE IF EXISTS `data`;
CREATE TABLE `data` (
  `code` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`code`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



DROP TABLE IF EXISTS `notepad`;
CREATE TABLE `notepad` (
  `name` varchar(45) NOT NULL,
  `code` int DEFAULT NULL,
  `content` text,
  PRIMARY KEY (`name`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  KEY `code_idx` (`code`),
  CONSTRAINT `code` FOREIGN KEY (`code`) REFERENCES `data` (`code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;