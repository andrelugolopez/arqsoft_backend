-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-05-2022 a las 00:36:21
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.0.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `database_user`
--
CREATE DATABASE IF NOT EXISTS `database_user` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `database_user`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios` (
  `Documento` varchar(100) CHARACTER SET utf16 COLLATE utf16_spanish_ci NOT NULL,
  `Nombres` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish_ci NOT NULL,
  `Apellidos` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish2_ci NOT NULL,
  `Password` varchar(250) CHARACTER SET utf16 COLLATE utf16_spanish2_ci NOT NULL,
  `Rol` varchar(10) CHARACTER SET utf16 COLLATE utf16_spanish2_ci NOT NULL,
  `Direccion` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish2_ci DEFAULT NULL,
  `Telefono` varchar(12) CHARACTER SET utf16 COLLATE utf16_spanish_ci DEFAULT NULL,
  `Email` varchar(50) CHARACTER SET utf16 COLLATE utf16_spanish2_ci NOT NULL,
  `id_carrito` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`Documento`, `Nombres`, `Apellidos`, `Password`, `Rol`, `Direccion`, `Telefono`, `Email`, `id_carrito`) VALUES
('98765432', 'Oscar A.', 'Henao', '$2b$12$s8vXDkdpAT1bOPrY57XLB.Dd7tjeXlQLPs.83.490r9mRGdOrbnUe', 'admin', NULL, NULL, 'oscarhenao3600@gmail.com', NULL),
('98765432', 'Oscar Alexander.', 'Henao Hernandez', '$2b$12$AibLDktZ5Y401Pomr0YDCeyUaYVFKe8g7r9d65QxQNjAvDJw4BiqW', 'user', NULL, NULL, 'oscarhenao3600@hotmail.com', NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`Email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
