-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 02, 2023 at 08:37 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `carobar`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(10) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'abhishek', '123@#890'),
(2, 'gurnoor', '12345'),
(3, 'admin', 'admin'),
(4, 'admin', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `brand_new_cars_data`
--

CREATE TABLE `brand_new_cars_data` (
  `id` int(10) NOT NULL,
  `car_type` varchar(20) NOT NULL,
  `car_brand` varchar(500) NOT NULL,
  `car_model` varchar(500) NOT NULL,
  `car_variant` varchar(500) NOT NULL,
  `car_mileage` varchar(500) NOT NULL,
  `car_price` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `brand_new_cars_data`
--

INSERT INTO `brand_new_cars_data` (`id`, `car_type`, `car_brand`, `car_model`, `car_variant`, `car_mileage`, `car_price`) VALUES
(1, 'new', 'Honda', 'Amaze', 'Petrol', '18.4 KM/H', 'Rs. 750000'),
(2, 'new', 'Mahindra', 'Scorpio', 'Petrol', '18.6 KM/H', 'Rs. 1150000'),
(3, 'new', 'Honda', 'Civic', 'Diesel', '18.6 KM/H', 'Rs. 599000'),
(4, 'new', 'Kia', 'Seltos', 'Petrol', '18.6 KM/H', 'Rs. 850000'),
(5, 'new', 'Maruti Suzuki', 'Swift', 'Diesel', '15 KM/H', 'Rs. 600000');

-- --------------------------------------------------------

--
-- Table structure for table `car_services`
--

CREATE TABLE `car_services` (
  `id` int(20) NOT NULL,
  `service_type` varchar(20) NOT NULL,
  `service_time` varchar(20) NOT NULL,
  `service_date` varchar(20) NOT NULL,
  `customer_name` varchar(20) NOT NULL,
  `customer_contact` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car_services`
--

INSERT INTO `car_services` (`id`, `service_type`, `service_time`, `service_date`, `customer_name`, `customer_contact`) VALUES
(1, ' Full Car Service', '11:00 am - 1:00 pm', '26/7/23', 'Gurnoor Singh Saini', '9465301124'),
(2, ' Repair', '11:00 am - 1:00 pm', '12/11/23', 'Ayush Rawat', '9784562347');

-- --------------------------------------------------------

--
-- Table structure for table `instock_cars_data`
--

CREATE TABLE `instock_cars_data` (
  `id` int(20) NOT NULL,
  `car_type` varchar(20) NOT NULL,
  `car_brand` varchar(20) NOT NULL,
  `car_model` varchar(20) NOT NULL,
  `car_variant` varchar(20) NOT NULL,
  `car_mileage` varchar(20) NOT NULL,
  `car_km_driven` varchar(20) NOT NULL,
  `car_registration_year` varchar(20) NOT NULL,
  `car_ownership` varchar(20) NOT NULL,
  `car_price` varchar(20) NOT NULL,
  `is_sold` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `instock_cars_data`
--

INSERT INTO `instock_cars_data` (`id`, `car_type`, `car_brand`, `car_model`, `car_variant`, `car_mileage`, `car_km_driven`, `car_registration_year`, `car_ownership`, `car_price`, `is_sold`) VALUES
(1, 'used', 'Maruti', 'Dzire', 'Diesel', '17.6 KM/H', '20,000 KM', '2018', '1st Owner', 'Rs. 17,00,000', 'NO'),
(2, 'new', 'Kia', 'Seltos', 'Petrol', '18.6 KM/H', 'N/A', 'XXXX', 'N/A', 'Rs. 7850000', 'YES');

-- --------------------------------------------------------

--
-- Table structure for table `secondhand_cars_bought_data`
--

CREATE TABLE `secondhand_cars_bought_data` (
  `id` int(10) NOT NULL,
  `car_type` varchar(11) NOT NULL,
  `car_brand` varchar(20) NOT NULL,
  `car_model` varchar(20) NOT NULL,
  `car_variant` varchar(20) NOT NULL,
  `car_km_driven` varchar(30) NOT NULL,
  `car_registration_year` varchar(20) NOT NULL,
  `car_ownership` varchar(20) NOT NULL,
  `seller_name` varchar(20) NOT NULL,
  `seller_contact` varchar(20) NOT NULL,
  `seller_address` varchar(50) NOT NULL,
  `car_price` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `secondhand_cars_bought_data`
--

INSERT INTO `secondhand_cars_bought_data` (`id`, `car_type`, `car_brand`, `car_model`, `car_variant`, `car_km_driven`, `car_registration_year`, `car_ownership`, `seller_name`, `seller_contact`, `seller_address`, `car_price`) VALUES
(1, 'used', 'Ford', 'Mustang GT 1990', 'Petrol', '1,00,000 km - 1,10,000 km', '1990', '4th owner', 'Vin Diesel', '787569874', 'North Carilona, st 24, Los Angeles', 'Rs. 9000000'),
(2, 'used', 'Honda', 'Civic', 'Electric', '10,000 km - 20,000 km', '2021', '2nd owner', 'Vivek', '487845451', '23, st 4 hello road ', 'Rs. 840000'),
(3, 'Used', 'Tesla', 'S1', 'Electric', '10,000 km - 20,000 km', '2022', '1st owner', 'Elon Musk', '+1 1234567890', 'St2, Los Angeles, H23', 'Rs. 15,00,000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `brand_new_cars_data`
--
ALTER TABLE `brand_new_cars_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `car_services`
--
ALTER TABLE `car_services`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `instock_cars_data`
--
ALTER TABLE `instock_cars_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `secondhand_cars_bought_data`
--
ALTER TABLE `secondhand_cars_bought_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `brand_new_cars_data`
--
ALTER TABLE `brand_new_cars_data`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `car_services`
--
ALTER TABLE `car_services`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `instock_cars_data`
--
ALTER TABLE `instock_cars_data`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `secondhand_cars_bought_data`
--
ALTER TABLE `secondhand_cars_bought_data`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
