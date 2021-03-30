-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 26, 2020 at 06:18 PM
-- Server version: 5.1.36
-- PHP Version: 5.3.0

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `mobilemis`
--

-- --------------------------------------------------------

--
-- Table structure for table `branddetails`
--

CREATE TABLE IF NOT EXISTS `branddetails` (
  `brandId` varchar(20) NOT NULL,
  `brandName` varchar(50) NOT NULL,
  PRIMARY KEY (`brandId`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `branddetails`
--

INSERT INTO `branddetails` (`brandId`, `brandName`) VALUES
('C001', 'Asus'),
('C002', 'Redmi');

-- --------------------------------------------------------

--
-- Table structure for table `logindetails`
--

CREATE TABLE IF NOT EXISTS `logindetails` (
  `UserId` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Usertype` varchar(20) NOT NULL,
  PRIMARY KEY (`UserId`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `logindetails`
--

INSERT INTO `logindetails` (`UserId`, `Password`, `Usertype`) VALUES
('susheelrastogi1999', 'rastogis2000', 'Admin'),
('rastogi1999', 'harsh2000', 'Console');

-- --------------------------------------------------------

--
-- Table structure for table `modeldetails`
--

CREATE TABLE IF NOT EXISTS `modeldetails` (
  `modelNumber` varchar(50) NOT NULL,
  `brandId` varchar(20) NOT NULL,
  `modelName` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `Features` varchar(100) NOT NULL,
  `Quantity` int(10) NOT NULL,
  PRIMARY KEY (`modelNumber`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `modeldetails`
--

INSERT INTO `modeldetails` (`modelNumber`, `brandId`, `modelName`, `price`, `Features`, `Quantity`) VALUES
('PB20IBM', 'C001', 'Redmi', 9000, 'Smartphone, Fast Charging', 10),
('XT1770', 'C002', 'Motorola', 7500, 'Dolby Atmos features ', 9);

-- --------------------------------------------------------

--
-- Table structure for table `saledetails`
--

CREATE TABLE IF NOT EXISTS `saledetails` (
  `transactionId` int(10) NOT NULL AUTO_INCREMENT,
  `modelNumber` varchar(50) NOT NULL,
  `quantity` int(10) NOT NULL,
  `customerName` varchar(50) NOT NULL,
  `email` varchar(45) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `date` varchar(11) NOT NULL,
  PRIMARY KEY (`transactionId`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `saledetails`
--

INSERT INTO `saledetails` (`transactionId`, `modelNumber`, `quantity`, `customerName`, `email`, `address`, `phone`, `date`) VALUES
(1, 'PB20IBM', 1, 'Harsh', 'harsh@gmail.com', '50,Mahadevan Tola fatehpur', '783498291', '26/07/2020'),
(2, 'XT1770', 1, 'Yash', 'yash@gmail.com', 'kajsdhn hiah', '56789', '26/07/2020');
