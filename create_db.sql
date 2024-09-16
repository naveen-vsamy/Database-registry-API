DROP DATABASE  IF EXISTS `registry`;
CREATE DATABASE `registry`;
USE `registry`;
CREATE TABLE `client_registry`( `reg_no` int(5) NOT NULL AUTO_INCREMENT PRIMARY KEY);
ALTER TABLE `client_registry` ADD COLUMN `name` VARCHAR(50) NOT NULL;
ALTER TABLE `client_registry` ADD COLUMN `phone` VARCHAR(10) NOT null;