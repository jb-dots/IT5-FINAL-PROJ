-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 11, 2024 at 06:14 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel_management_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `ref` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `postcode` varchar(20) DEFAULT NULL,
  `mobile` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `nationality` varchar(50) DEFAULT NULL,
  `idproof` varchar(50) DEFAULT NULL,
  `idnumber` varchar(50) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`ref`, `name`, `gender`, `postcode`, `mobile`, `email`, `nationality`, `idproof`, `idnumber`, `address`) VALUES
(1, 'John Benedic Dutaro', 'Male', '8000', '9630631699', 'dutaro@gmail.com', 'Filipino', 'Passport', '129711', 'Bangkal Davao City'),
(2, 'Russel Labiaga', 'Other', '8000', '9071772596', 'russel@gmail.com', 'Filipino', 'National ID', '129711100097', 'Deca Tacunan Mintal D.C.');

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `floor` int(10) NOT NULL,
  `roomno` int(200) NOT NULL,
  `roomtype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `details`
--

INSERT INTO `details` (`floor`, `roomno`, `roomtype`) VALUES
(1, 1, 'Luxury');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `contact` varchar(20) NOT NULL,
  `checkin` varchar(10) NOT NULL,
  `checkout` varchar(10) NOT NULL,
  `roomtype` enum('Single','Double','Luxury') NOT NULL,
  `roomavailable` int(11) NOT NULL,
  `meal` varchar(50) DEFAULT NULL,
  `noofdays` int(11) DEFAULT NULL,
  `paidtax` decimal(10,2) DEFAULT NULL,
  `actualtotal` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`contact`, `checkin`, `checkout`, `roomtype`, `roomavailable`, `meal`, `noofdays`, `paidtax`, `actualtotal`, `total`) VALUES
('9630631699', '01/20/2024', '01/25/2024', 'Luxury', 1, 'Dinner', 5, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `securityQ` varchar(50) NOT NULL,
  `securityA` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `fname`, `lname`, `contact`, `email`, `securityQ`, `securityA`, `password`) VALUES
(4, 'John Benedic', 'Dutaro', '9630631699', 'dutaro@gmail.com', 'Your Pet Name', 'Mobidchi', '1234'),
(5, 'Aldren Louie', 'Reyes', '9155127436', 'lanoy@gmail.com', 'Your Pet Name', 'bella', 'aldren');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`ref`),
  ADD UNIQUE KEY `mobile` (`mobile`);

--
-- Indexes for table `details`
--
ALTER TABLE `details`
  ADD PRIMARY KEY (`roomno`) USING BTREE,
  ADD UNIQUE KEY `roomno` (`roomno`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`contact`),
  ADD UNIQUE KEY `roomtype` (`roomtype`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `contact` (`contact`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `ref` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `room`
--
ALTER TABLE `room`
  ADD CONSTRAINT `room_ibfk_1` FOREIGN KEY (`contact`) REFERENCES `customer` (`mobile`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
