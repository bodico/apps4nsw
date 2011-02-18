create database animals;
use animals;

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

DROP TABLE IF EXISTS `animals`;
CREATE TABLE `animals` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `colour` varchar(100) NOT NULL,
  `suburb` varchar(10) NOT NULL,
  `flavour` varchar(100) NOT NULL,
  `other` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2094867 ;

load data local infile '~/animals.csv' into table animals
fields terminated by '	'
enclosed by '"'
lines terminated by '\n'
(`name`, `type`, `colour`, `suburb`, `flavour`, `other`);