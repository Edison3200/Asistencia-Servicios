-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.5.9-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Volcando estructura para tabla sesiones.estudiantes
CREATE TABLE IF NOT EXISTS `estudiantes` (
  `id_es` int(11) NOT NULL AUTO_INCREMENT,
  `iden` int(10) NOT NULL DEFAULT 0,
  `nom_es` varchar(50) NOT NULL DEFAULT '0',
  `apellidos` varchar(50) NOT NULL DEFAULT '0',
  `celular` varchar(50) NOT NULL DEFAULT '0',
  `email` varchar(50) NOT NULL DEFAULT '0',
  `semestre` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id_es`),
  KEY `FK_estudiantes_semestres` (`semestre`),
  CONSTRAINT `FK_estudiantes_semestres` FOREIGN KEY (`semestre`) REFERENCES `semestres` (`id_se`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla sesiones.estudiantes: ~4 rows (aproximadamente)
DELETE FROM `estudiantes`;
/*!40000 ALTER TABLE `estudiantes` DISABLE KEYS */;
INSERT INTO `estudiantes` (`id_es`, `iden`, `nom_es`, `apellidos`, `celular`, `email`, `semestre`) VALUES
	(2, 456424, 'Marcos', 'Asencio', '3232161213', 'marcos23@gmail.com', 4),
	(3, 1232451456, 'Andres Marcial', 'Martinez', '321234567', 'marcial@gmail.com', 4),
	(4, 478545345, 'Daniel A', 'Enriquez', '3432556232', 'daniel@gmail.com', 4),
	(5, 135417899, 'Juan', 'Perez', '32145614', 'juano@gmail.com', 4);
/*!40000 ALTER TABLE `estudiantes` ENABLE KEYS */;

-- Volcando estructura para tabla sesiones.semestres
CREATE TABLE IF NOT EXISTS `semestres` (
  `id_se` int(11) NOT NULL AUTO_INCREMENT,
  `nom_se` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_se`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla sesiones.semestres: ~1 rows (aproximadamente)
DELETE FROM `semestres`;
/*!40000 ALTER TABLE `semestres` DISABLE KEYS */;
INSERT INTO `semestres` (`id_se`, `nom_se`) VALUES
	(4, '5 semestre de Ingeniería Civil');
/*!40000 ALTER TABLE `semestres` ENABLE KEYS */;

-- Volcando estructura para tabla sesiones.sesion
CREATE TABLE IF NOT EXISTS `sesion` (
  `id_se` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL DEFAULT '0',
  `descripcion` varchar(50) NOT NULL,
  `semestre` int(11) NOT NULL,
  `fecha_ini` date NOT NULL,
  `hora_ini` time NOT NULL,
  `hora_fin` time NOT NULL,
  PRIMARY KEY (`id_se`),
  KEY `FK_sesion_semestres` (`semestre`),
  CONSTRAINT `FK_sesion_semestres` FOREIGN KEY (`semestre`) REFERENCES `semestres` (`id_se`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla sesiones.sesion: ~2 rows (aproximadamente)
DELETE FROM `sesion`;
/*!40000 ALTER TABLE `sesion` DISABLE KEYS */;
INSERT INTO `sesion` (`id_se`, `nom`, `descripcion`, `semestre`, `fecha_ini`, `hora_ini`, `hora_fin`) VALUES
	(1, 'Estructura de datos', 'Sesion en la noche', 4, '2021-04-30', '15:25:32', '04:21:00');
/*!40000 ALTER TABLE `sesion` ENABLE KEYS */;

-- Volcando estructura para tabla sesiones.sesion_es
CREATE TABLE IF NOT EXISTS `sesion_es` (
  `id_se_es` int(11) NOT NULL AUTO_INCREMENT,
  `id_se` int(11) NOT NULL DEFAULT 0,
  `id_es` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id_se_es`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla sesiones.sesion_es: ~2 rows (aproximadamente)
DELETE FROM `sesion_es`;
/*!40000 ALTER TABLE `sesion_es` DISABLE KEYS */;
INSERT INTO `sesion_es` (`id_se_es`, `id_se`, `id_es`) VALUES
	(19, 1, 3),
	(20, 1, 4);
/*!40000 ALTER TABLE `sesion_es` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
