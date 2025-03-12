-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: telecom_db
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `cidades`
--

DROP TABLE IF EXISTS `cidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cidades` (
  `codigo_ibge` int NOT NULL,
  `nome` varchar(50) NOT NULL,
  `uf` char(2) NOT NULL,
  PRIMARY KEY (`codigo_ibge`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cidades`
--

LOCK TABLES `cidades` WRITE;
/*!40000 ALTER TABLE `cidades` DISABLE KEYS */;
/*!40000 ALTER TABLE `cidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empresas`
--

DROP TABLE IF EXISTS `empresas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empresas` (
  `cnpj` varchar(14) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `porte` varchar(50) NOT NULL,
  `grupos_economicos_id` int NOT NULL,
  PRIMARY KEY (`cnpj`,`grupos_economicos_id`),
  KEY `fk_empresas_grupos_economicos_idx` (`grupos_economicos_id`),
  CONSTRAINT `fk_empresas_grupos_economicos` FOREIGN KEY (`grupos_economicos_id`) REFERENCES `grupos_economicos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresas`
--

LOCK TABLES `empresas` WRITE;
/*!40000 ALTER TABLE `empresas` DISABLE KEYS */;
/*!40000 ALTER TABLE `empresas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `empresas_porte`
--

DROP TABLE IF EXISTS `empresas_porte`;
/*!50001 DROP VIEW IF EXISTS `empresas_porte`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `empresas_porte` AS SELECT 
 1 AS `cnpj`,
 1 AS `porte`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `empresas_porte_grande`
--

DROP TABLE IF EXISTS `empresas_porte_grande`;
/*!50001 DROP VIEW IF EXISTS `empresas_porte_grande`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `empresas_porte_grande` AS SELECT 
 1 AS `cnpj`,
 1 AS `porte`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `empresas_porte_media`
--

DROP TABLE IF EXISTS `empresas_porte_media`;
/*!50001 DROP VIEW IF EXISTS `empresas_porte_media`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `empresas_porte_media` AS SELECT 
 1 AS `cnpj`,
 1 AS `porte`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `empresas_porte_pequena`
--

DROP TABLE IF EXISTS `empresas_porte_pequena`;
/*!50001 DROP VIEW IF EXISTS `empresas_porte_pequena`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `empresas_porte_pequena` AS SELECT 
 1 AS `cnpj`,
 1 AS `porte`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `grupos_economicos`
--

DROP TABLE IF EXISTS `grupos_economicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grupos_economicos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupos_economicos`
--

LOCK TABLES `grupos_economicos` WRITE;
/*!40000 ALTER TABLE `grupos_economicos` DISABLE KEYS */;
/*!40000 ALTER TABLE `grupos_economicos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operacoes`
--

DROP TABLE IF EXISTS `operacoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `operacoes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cidades_codigo_ibge` int NOT NULL,
  `empresas_cnpj` varchar(14) NOT NULL,
  `faixa_velocidade` varchar(50) DEFAULT NULL,
  `velocidade` decimal(10,2) DEFAULT NULL,
  `tecnologia` varchar(50) DEFAULT NULL,
  `meio_acesso` varchar(50) DEFAULT NULL,
  `tipo_pessoa` varchar(50) DEFAULT NULL,
  `tipo_produto` varchar(50) DEFAULT NULL,
  `acessos` int DEFAULT NULL,
  PRIMARY KEY (`id`,`cidades_codigo_ibge`,`empresas_cnpj`),
  KEY `fk_operacoes_empresas1_idx` (`empresas_cnpj`),
  KEY `fk_operacoes_cidades1_idx` (`cidades_codigo_ibge`),
  CONSTRAINT `fk_operacoes_cidades1` FOREIGN KEY (`cidades_codigo_ibge`) REFERENCES `cidades` (`codigo_ibge`) ON DELETE CASCADE,
  CONSTRAINT `fk_operacoes_empresas1` FOREIGN KEY (`empresas_cnpj`) REFERENCES `empresas` (`cnpj`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operacoes`
--

LOCK TABLES `operacoes` WRITE;
/*!40000 ALTER TABLE `operacoes` DISABLE KEYS */;
/*!40000 ALTER TABLE `operacoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `velocidade_maior_50`
--

DROP TABLE IF EXISTS `velocidade_maior_50`;
/*!50001 DROP VIEW IF EXISTS `velocidade_maior_50`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `velocidade_maior_50` AS SELECT 
 1 AS `id`,
 1 AS `cidades_codigo_ibge`,
 1 AS `empresas_cnpj`,
 1 AS `velocidade`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `velocidade_menor_50`
--

DROP TABLE IF EXISTS `velocidade_menor_50`;
/*!50001 DROP VIEW IF EXISTS `velocidade_menor_50`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `velocidade_menor_50` AS SELECT 
 1 AS `id`,
 1 AS `cidades_codigo_ibge`,
 1 AS `empresas_cnpj`,
 1 AS `velocidade`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `empresas_porte`
--

/*!50001 DROP VIEW IF EXISTS `empresas_porte`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `empresas_porte` AS select `empresas`.`cnpj` AS `cnpj`,`empresas`.`porte` AS `porte` from `empresas` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `empresas_porte_grande`
--

/*!50001 DROP VIEW IF EXISTS `empresas_porte_grande`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `empresas_porte_grande` AS select `empresas`.`cnpj` AS `cnpj`,`empresas`.`porte` AS `porte` from `empresas` where (upper(`empresas`.`porte`) = 'GRANDE') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `empresas_porte_media`
--

/*!50001 DROP VIEW IF EXISTS `empresas_porte_media`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `empresas_porte_media` AS select `empresas`.`cnpj` AS `cnpj`,`empresas`.`porte` AS `porte` from `empresas` where (upper(`empresas`.`porte`) = 'MEDIA') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `empresas_porte_pequena`
--

/*!50001 DROP VIEW IF EXISTS `empresas_porte_pequena`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `empresas_porte_pequena` AS select `empresas`.`cnpj` AS `cnpj`,`empresas`.`porte` AS `porte` from `empresas` where (upper(`empresas`.`porte`) = 'PEQUENA') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `velocidade_maior_50`
--

/*!50001 DROP VIEW IF EXISTS `velocidade_maior_50`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `velocidade_maior_50` AS select `operacoes`.`id` AS `id`,`operacoes`.`cidades_codigo_ibge` AS `cidades_codigo_ibge`,`operacoes`.`empresas_cnpj` AS `empresas_cnpj`,`operacoes`.`velocidade` AS `velocidade` from `operacoes` where (`operacoes`.`velocidade` > 50.00) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `velocidade_menor_50`
--

/*!50001 DROP VIEW IF EXISTS `velocidade_menor_50`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `velocidade_menor_50` AS select `operacoes`.`id` AS `id`,`operacoes`.`cidades_codigo_ibge` AS `cidades_codigo_ibge`,`operacoes`.`empresas_cnpj` AS `empresas_cnpj`,`operacoes`.`velocidade` AS `velocidade` from `operacoes` where (`operacoes`.`velocidade` < 50.00) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-10 19:21:57
