-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: pruebatienda
-- ------------------------------------------------------
-- Server version	8.0.28-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `idproducto` char(10) NOT NULL,
  `nombre` char(200) NOT NULL,
  `cantidad` int NOT NULL,
  `precio` int NOT NULL,
  `imagen` char(50) DEFAULT NULL,
  PRIMARY KEY (`idproducto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES ('E018','hp portatil',21,2000000,'equipo1.jpg'),('E019','azus verde',4,3500000,'equipo2.jpg'),('E020','Computador Gamer',5,4000000,'equipo3.jpg'),('E021','Computador Gamer Pro',15,1200000,'equipo4.jpg'),('E022','Computador Portatil',20,4000000,'equipo5.jpg'),('E024','Computador Protatil HP',2,3500000,'equipo6.jpg'),('P006','impresora Hp laser',5,250000,'periferico2.jpg'),('P023','Procesador Intel7',45,2000000,'repuesto4.png'),('P051','Impresora Epson',20,800000,'periferico1.jpg'),('P052','memoria usb',54,50000,'periferico3.jpg'),('P056','Monitor CX',12,900000,'periferico5.jpg'),('P059','memoria usb HP',20,60000,'periferico4.jpg'),('P067','Mouse skymars',4,70000,'periferico7.jpg'),('P074','Teclado',8,90000,'periferico9.jpg'),('P089','Mouse Blanco',8,78000,'periferio8.jpg'),('P090','Teclado Gamer',9,600000,'periferico10.jpg'),('P098','Monitor',34,1100000,'periferico6.jpg'),('R001','Tarjeta wifi',20,89000,'repuesto1.png'),('R017','Disco duro',4,250000,'repuesto2.png'),('R020','Memoria RAM',10,190000,'repuesto3.png'),('R068','Disco solido',34,250000,'repuesto5.png'),('R078','Tarjeta de video',3,1000000,'repuesto6.png');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-04 13:50:04
