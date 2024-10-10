-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 10, 2024 at 01:22 PM
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
(1, 'Aldren', 'Female', '8000', '09088184444', 'lanoy@gmail.com', 'Filipino', 'Driving License', '12345', 'Lanoy St. Toril Davao City'),
(2, 'Cyprus', 'Male', '8000', '12345', 'Cyprus@gmail.com', 'African American', 'Passport', '12345', 'Mintal DC'),
(3, 'Pamela Mendoza', 'Female', '8000', '090912345', 'Pam@gmail.com', 'Filipino', 'National ID', '123456', 'Landmark Davao City'),
(4, 'Kaye', 'Other', '9000', '0922165216', 'kaye@gmail.com', 'British', 'National ID', '1928109232', 'Bankerohan Davao City');

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
(1, 25, 'Single'),
(2, 21, 'Single'),
(3, 12, 'Single'),
(3, 15, 'Deluxe');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `contact_number` varchar(15) NOT NULL,
  `email` varchar(255) NOT NULL,
  `security_question` varchar(255) NOT NULL,
  `security_answer` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`first_name`, `last_name`, `contact_number`, `email`, `security_question`, `security_answer`, `password`) VALUES
('John Benedic', 'Dutaro', '09088184444', 'dots@gmail.com', 'Your Best Friend Name', 'russel', '1234'),
('Aldren', 'Reyes', '09088184444', 'lanoy@gmail.com', 'Your Pet Name', 'Bella', '12345');

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
(1, 'fdd', 'asfd', 'adaf', 'asdfa', 'Your Pet Name', 'asd', 'asdasd'),
(2, 'Aldren Louie', 'Reyes', '090988811231', 'Lanoy@gmail.com', 'Your Pet Name', 'cookie', '1234'),
(3, 'John', 'Dots', '1234', 'john@gmail.com', 'Your Pet Name', 'dog', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`ref`);

--
-- Indexes for table `details`
--
ALTER TABLE `details`
  ADD PRIMARY KEY (`floor`,`roomno`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`email`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`contact`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
