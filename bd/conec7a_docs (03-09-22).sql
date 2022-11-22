-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3308
-- Tiempo de generación: 03-09-2022 a las 17:27:16
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `conec7a_docs`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carpeta`
--

CREATE TABLE `carpeta` (
  `idcarpeta` int(11) NOT NULL,
  `nombre_carpeta` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `descripcion_carpeta` text COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `carpeta`
--

INSERT INTO `carpeta` (`idcarpeta`, `nombre_carpeta`, `descripcion_carpeta`) VALUES
(1, 'PROCESO DE APOYO', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
(2, 'PROCESO ESTRATÉGICO', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
(3, 'PROCESO MISIONAL', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
(4, 'PROCESO DE EVALUACIÓN', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
(5, 'CONTROL INTERNO', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `documento`
--

CREATE TABLE `documento` (
  `iddocumento` int(11) NOT NULL,
  `carpeta` int(11) DEFAULT NULL,
  `subcarpeta` int(11) DEFAULT NULL,
  `nombre_documento` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `fecha_documento` date DEFAULT NULL,
  `version_documento` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `estado_documento` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `documento`
--

INSERT INTO `documento` (`iddocumento`, `carpeta`, `subcarpeta`, `nombre_documento`, `fecha_documento`, `version_documento`, `estado_documento`) VALUES
(1, 1, 2, 'favicon_io_1.zip', '2022-07-13', '1', 0),
(3, 3, 11, 'formato-evaluacion-docente23423324.pdf', '2022-06-13', '1', 1),
(4, 1, 2, 'CertificadoMIPG.pdf', '2022-04-05', '3', 1),
(5, 4, 14, 'resolucion-documento-procesoev00234.pdf', '2022-02-02', '1', 0),
(6, 4, 14, 'documento de prueba.pdf', '2022-03-18', '1', 1),
(12, 2, 8, 'prueba_2.sql', '2022-07-20', '1', 1),
(14, 2, 9, 'Articulo_Uso_de_robotica_en_los_procesos_educativos_1.pdf', '2022-07-23', '1', 1),
(17, 3, 11, 'ACTUALIZACION_HOJA_DE_VIDA_SIGEP_II.pdf', '2022-07-08', '2', 0);

--
-- Disparadores `documento`
--
DELIMITER $$
CREATE TRIGGER `insertarHistorial` AFTER UPDATE ON `documento` FOR EACH ROW BEGIN 
   INSERT INTO historial_documento(documento_id, carpeta, subcarpeta, nombre_documento, fecha_documento, version_documento, estado_documento, fecha_cambio)
   VALUES (OLD.iddocumento, OLD.carpeta, OLD.subcarpeta, OLD.nombre_documento, OLD.fecha_documento, OLD.version_documento, OLD.estado_documento, CURRENT_TIMESTAMP);
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_documento`
--

CREATE TABLE `historial_documento` (
  `idhist_documento` int(11) NOT NULL,
  `documento_id` int(11) NOT NULL,
  `carpeta` int(11) DEFAULT NULL,
  `subcarpeta` int(11) DEFAULT NULL,
  `nombre_documento` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `fecha_documento` date DEFAULT NULL,
  `version_documento` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `estado_documento` int(1) DEFAULT NULL,
  `fecha_cambio` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `historial_documento`
--

INSERT INTO `historial_documento` (`idhist_documento`, `documento_id`, `carpeta`, `subcarpeta`, `nombre_documento`, `fecha_documento`, `version_documento`, `estado_documento`, `fecha_cambio`) VALUES
(16, 2, 1, 7, 'archivo nuevo 3.pdf', '2022-06-21', '1', 0, '2022-07-23 10:55:26'),
(17, 2, 1, 7, 'archivo nuevo 3.pdf', '2022-06-21', '1', 1, '2022-07-23 10:55:52'),
(18, 6, 4, 14, 'documento de prueba.pdf', '2022-03-14', '1', 1, '2022-07-23 10:57:15'),
(19, 4, 1, 2, 'ComprobantePSE20220706224902.pdf', '2022-04-07', '1', 1, '2022-07-23 12:26:37'),
(20, 14, 2, 9, 'CERTIFICACION-EPS.pdf', '2022-07-23', '1', 1, '2022-07-23 12:50:58'),
(21, 15, 1, 5, 'CORRECCIONES_GENERALES-MODELOS3D.pdf', '2022-07-27', '1', 1, '2022-07-27 19:08:43'),
(22, 13, 3, 12, '2022-080_JEFFERSON_LEONARDO_ALVAREZ_ZAMBRANO.pdf', '2022-07-20', '1', 1, '2022-07-29 12:45:20'),
(23, 4, 1, 2, 'ComprobantePSE20220706224902.pdf', '2022-04-07', '1', 1, '2022-08-04 10:01:47'),
(24, 4, 1, 2, 'ComprobantePSE20220706224902.pdf', '2022-04-07', '1', 1, '2022-08-04 10:01:58'),
(25, 4, 1, 2, 'ComprobantePSE20220706224902.pdf', '2022-04-07', '1', 1, '2022-08-04 10:02:45'),
(26, 4, 1, 2, 'ComprobantePSE20220706224902.pdf', '2022-04-05', '1', 1, '2022-08-04 10:02:55'),
(27, 1, 1, 2, 'favicon_io_1.zip', '2022-07-13', '1', 1, '2022-08-04 10:07:28'),
(28, 2, 1, 7, 'Tipos_de_Computadoras.jpg', '2022-06-21', '1', 1, '2022-08-04 10:07:28'),
(29, 3, 3, 11, 'formato-evaluacion-docente23423324.pdf', '2022-06-13', '1', 1, '2022-08-04 10:07:28'),
(30, 4, 1, 2, 'ComprobantePSE20220706224902.pdf', '2022-04-05', '1', 1, '2022-08-04 10:07:28'),
(31, 5, 4, 14, 'resolucion-documento-procesoev00234.pdf', '2022-02-02', '1', 0, '2022-08-04 10:07:28'),
(32, 6, 4, 14, 'documento de prueba.pdf', '2022-03-18', '1', 1, '2022-08-04 10:07:28'),
(33, 12, 2, 8, 'prueba_2.sql', '2022-07-20', '1', 1, '2022-08-04 10:07:28'),
(34, 14, 2, 9, 'Articulo_Uso_de_robotica_en_los_procesos_educativos_1.pdf', '2022-07-23', '1', 1, '2022-08-04 10:07:28'),
(35, 1, 1, 2, 'favicon_io_1.zip', '2022-07-13', '1', 1, '2022-08-04 10:11:17'),
(36, 4, 1, 2, 'ComprobantePSE20220706224902.pdf', '2022-04-05', '1', 1, '2022-08-04 10:29:30'),
(37, 4, 1, 2, 'ComprobantePSE20220706224902.pdf', '2022-04-05', '1', 1, '2022-08-04 10:29:36'),
(38, 4, 1, 2, 'ComprobantePSE20220706224902.pdf', '2022-04-05', '1', 0, '2022-08-04 10:48:48'),
(39, 4, 1, 2, 'ComprobantePSE20220706224902.pdf', '2022-04-05', '1', 1, '2022-08-04 10:50:34'),
(40, 4, 1, 2, 'certi_Afil.pdf', '2022-04-05', '2', 1, '2022-08-04 11:05:54'),
(41, 17, 3, 11, 'EPIF001_V6.pdf', '2022-08-08', '1', 1, '2022-08-08 17:28:14'),
(42, 17, 3, 11, 'ACTUALIZACION_HOJA_DE_VIDA_SIGEP_II.pdf', '2022-07-08', '2', 1, '2022-08-08 17:31:35');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `subcarpeta`
--

CREATE TABLE `subcarpeta` (
  `idsubcarpeta` int(11) NOT NULL,
  `carpeta_id` int(11) DEFAULT NULL,
  `nombre_subcarpeta` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `descripcion_subcarpeta` text COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `subcarpeta`
--

INSERT INTO `subcarpeta` (`idsubcarpeta`, `carpeta_id`, `nombre_subcarpeta`, `descripcion_subcarpeta`) VALUES
(1, 1, 'GESTIÓN TALENTO HUMANO', 'Maecenas blandit in odio sed mattis. In in interdum felis. Donec id mattis ligula. Nullam tempor metus dolor, non cursus nisl dignissim in. Sed vehicula massa elit, sit amet feugiat leo dignissim in. Aliquam vel pulvinar nulla. Nunc sit amet odio odio. Maecenas malesuada aliquam turpis, non pellentesque ex vehicula id. Quisque interdum odio a est accumsan malesuada. Suspendisse suscipit aliquam odio et venenatis. Quisque orci nisl, cursus et lacus sit amet, aliquet rhoncus risus. Sed viverra eu.'),
(2, 1, 'GESTIÓN FINANCIERA', 'Maecenas blandit in odio sed mattis. In in interdum felis. Donec id mattis ligula. Nullam tempor metus dolor, non cursus nisl dignissim in. Sed vehicula massa elit, sit amet feugiat leo dignissim in. Aliquam vel pulvinar nulla. Nunc sit amet odio odio. Maecenas malesuada aliquam turpis, non pellentesque ex vehicula id. Quisque interdum odio a est accumsan malesuada. Suspendisse suscipit aliquam odio et venenatis. Quisque orci nisl, cursus et lacus sit amet, aliquet rhoncus risus. Sed viverra eu.'),
(3, 1, 'GESTIÓN CONTRACTUAL', 'Maecenas blandit in odio sed mattis. In in interdum felis. Donec id mattis ligula. Nullam tempor metus dolor, non cursus nisl dignissim in. Sed vehicula massa elit, sit amet feugiat leo dignissim in. Aliquam vel pulvinar nulla. Nunc sit amet odio odio. Maecenas malesuada aliquam turpis, non pellentesque ex vehicula id. Quisque interdum odio a est accumsan malesuada. Suspendisse suscipit aliquam odio et venenatis. Quisque orci nisl, cursus et lacus sit amet, aliquet rhoncus risus. Sed viverra eu.'),
(4, 1, 'GESTIÓN DOCUMENTAL', 'Maecenas blandit in odio sed mattis. In in interdum felis. Donec id mattis ligula. Nullam tempor metus dolor, non cursus nisl dignissim in. Sed vehicula massa elit, sit amet feugiat leo dignissim in. Aliquam vel pulvinar nulla. Nunc sit amet odio odio. Maecenas malesuada aliquam turpis, non pellentesque ex vehicula id. Quisque interdum odio a est accumsan malesuada. Suspendisse suscipit aliquam odio et venenatis. Quisque orci nisl, cursus et lacus sit amet, aliquet rhoncus risus. Sed viverra eu.'),
(5, 1, 'GESTIÓN ADMINISTRATIVA', 'Maecenas blandit in odio sed mattis. In in interdum felis. Donec id mattis ligula. Nullam tempor metus dolor, non cursus nisl dignissim in. Sed vehicula massa elit, sit amet feugiat leo dignissim in. Aliquam vel pulvinar nulla. Nunc sit amet odio odio. Maecenas malesuada aliquam turpis, non pellentesque ex vehicula id. Quisque interdum odio a est accumsan malesuada. Suspendisse suscipit aliquam odio et venenatis. Quisque orci nisl, cursus et lacus sit amet, aliquet rhoncus risus. Sed viverra eu.'),
(6, 1, 'GESTIÓN JURÍDICA', 'Maecenas blandit in odio sed mattis. In in interdum felis. Donec id mattis ligula. Nullam tempor metus dolor, non cursus nisl dignissim in. Sed vehicula massa elit, sit amet feugiat leo dignissim in. Aliquam vel pulvinar nulla. Nunc sit amet odio odio. Maecenas malesuada aliquam turpis, non pellentesque ex vehicula id. Quisque interdum odio a est accumsan malesuada. Suspendisse suscipit aliquam odio et venenatis. Quisque orci nisl, cursus et lacus sit amet, aliquet rhoncus risus. Sed viverra eu.'),
(7, 1, 'GESTIÓN TIC - COMUNICACIONES', 'Maecenas blandit in odio sed mattis. In in interdum felis. Donec id mattis ligula. Nullam tempor metus dolor, non cursus nisl dignissim in. Sed vehicula massa elit, sit amet feugiat leo dignissim in. Aliquam vel pulvinar nulla. Nunc sit amet odio odio. Maecenas malesuada aliquam turpis, non pellentesque ex vehicula id. Quisque interdum odio a est accumsan malesuada. Suspendisse suscipit aliquam odio et venenatis. Quisque orci nisl, cursus et lacus sit amet, aliquet rhoncus risus. Sed viverra eu.'),
(8, 2, 'DIRECCIONAMIENTO ESTRATÉGICO', 'Maecenas blandit in odio sed mattis. In in interdum felis. Donec id mattis ligula. Nullam tempor metus dolor, non cursus nisl dignissim in. Sed vehicula massa elit, sit amet feugiat leo dignissim in. Aliquam vel pulvinar nulla. Nunc sit amet odio odio. Maecenas malesuada aliquam turpis, non pellentesque ex vehicula id. Quisque interdum odio a est accumsan malesuada. Suspendisse suscipit aliquam odio et venenatis. Quisque orci nisl, cursus et lacus sit amet, aliquet rhoncus risus. Sed viverra eu.'),
(9, 2, 'SISTEMA DE GESTIÓN DE CALIDAD', 'Maecenas blandit in odio sed mattis. In in interdum felis. Donec id mattis ligula. Nullam tempor metus dolor, non cursus nisl dignissim in. Sed vehicula massa elit, sit amet feugiat leo dignissim in. Aliquam vel pulvinar nulla. Nunc sit amet odio odio. Maecenas malesuada aliquam turpis, non pellentesque ex vehicula id. Quisque interdum odio a est accumsan malesuada. Suspendisse suscipit aliquam odio et venenatis. Quisque orci nisl, cursus et lacus sit amet, aliquet rhoncus risus. Sed viverra eu.'),
(10, 3, 'PROMOCIÓN DERECHOS HUMANOS', 'Maecenas blandit in odio sed mattis. In in interdum felis. Donec id mattis ligula. Nullam tempor metus dolor, non cursus nisl dignissim in. Sed vehicula massa elit, sit amet feugiat leo dignissim in. Aliquam vel pulvinar nulla. Nunc sit amet odio odio. Maecenas malesuada aliquam turpis, non pellentesque ex vehicula id. Quisque interdum odio a est accumsan malesuada. Suspendisse suscipit aliquam odio et venenatis. Quisque orci nisl, cursus et lacus sit amet, aliquet rhoncus risus. Sed viverra eu.'),
(11, 3, 'FUNCIÓN DISCIPLINARIA', 'Maecenas blandit in odio sed mattis. In in interdum felis. Donec id mattis ligula. Nullam tempor metus dolor, non cursus nisl dignissim in. Sed vehicula massa elit, sit amet feugiat leo dignissim in. Aliquam vel pulvinar nulla. Nunc sit amet odio odio. Maecenas malesuada aliquam turpis, non pellentesque ex vehicula id. Quisque interdum odio a est accumsan malesuada. Suspendisse suscipit aliquam odio et venenatis. Quisque orci nisl, cursus et lacus sit amet, aliquet rhoncus risus. Sed viverra eu.'),
(12, 3, 'SERVICIO CIUDADANO', 'Maecenas blandit in odio sed mattis. In in interdum felis. Donec id mattis ligula. Nullam tempor metus dolor, non cursus nisl dignissim in. Sed vehicula massa elit, sit amet feugiat leo dignissim in. Aliquam vel pulvinar nulla. Nunc sit amet odio odio. Maecenas malesuada aliquam turpis, non pellentesque ex vehicula id. Quisque interdum odio a est accumsan malesuada. Suspendisse suscipit aliquam odio et venenatis. Quisque orci nisl, cursus et lacus sit amet, aliquet rhoncus risus. Sed viverra eu.'),
(13, 3, 'ATENCIÓN VICTIMA CONFLICTO ARMADO', 'Maecenas blandit in odio sed mattis. In in interdum felis. Donec id mattis ligula. Nullam tempor metus dolor, non cursus nisl dignissim in. Sed vehicula massa elit, sit amet feugiat leo dignissim in. Aliquam vel pulvinar nulla. Nunc sit amet odio odio. Maecenas malesuada aliquam turpis, non pellentesque ex vehicula id. Quisque interdum odio a est accumsan malesuada. Suspendisse suscipit aliquam odio et venenatis. Quisque orci nisl, cursus et lacus sit amet, aliquet rhoncus risus. Sed viverra eu.'),
(14, 4, 'PROCESO DE EVALUACIÓN', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris volutpat nulla id volutpat cursus. Donec laoreet quam et tincidunt consectetur. Sed egestas nisl sit amet erat posuere, facilisis elementum nulla sodales. Donec luctus ornare dolor sit amet viverra. Nulla lectus justo, lobortis in lorem eget, congue sagittis libero. Vestibulum ut magna tortor. Curabitur non ex nibh. Nam ac aliquet purus. Nulla fringilla, quam fringilla finibus accumsan, eros odio aliquet nisl, vitae porttitor fusce.'),
(15, 5, 'CONTROL INTERNO', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris volutpat nulla id volutpat cursus. Donec laoreet quam et tincidunt consectetur. Sed egestas nisl sit amet erat posuere, facilisis elementum nulla sodales. Donec luctus ornare dolor sit amet viverra. Nulla lectus justo, lobortis in lorem eget, congue sagittis libero. Vestibulum ut magna tortor. Curabitur non ex nibh. Nam ac aliquet purus. Nulla fringilla, quam fringilla finibus accumsan, eros odio aliquet nisl, vitae porttitor fusce.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `idusuario` int(11) NOT NULL,
  `username` varchar(15) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `nombre_usuario` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `correo_usuario` varchar(60) COLLATE utf8_unicode_ci DEFAULT NULL,
  `telefono_usuario` varchar(11) COLLATE utf8_unicode_ci DEFAULT NULL,
  `estado_usuario` int(1) DEFAULT NULL,
  `rol_usuario` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idusuario`, `username`, `password`, `nombre_usuario`, `correo_usuario`, `telefono_usuario`, `estado_usuario`, `rol_usuario`) VALUES
(1, '1053332958', 'pbkdf2:sha256:260000$C2LkpYD4Ju9kHSjH$a52f469dd14b7a7a808663e575dd2b8c9dd8de53a666ff5f030f4f55f8396d3c', 'Leonardo Alvarez', 'leoalvarez@gmail.com', '3112653180', 1, 1),
(6, '987654321', 'pbkdf2:sha256:260000$f26gXwDXrGhxA0Wr$233eb5c20933b1cd3f597cad9a1b74dd376b5961201d83976747fecd65ee442a', 'Samuel Duran', '', '', 1, 2),
(7, '123456789', 'pbkdf2:sha256:260000$q9gLJqUZTJoezUHE$1f01ccf5ef22a236b108c4b9b1287ba5f7c96e393324a248f0bba528e49706bb', 'Laura Maria Parra', 'laura@correo.com', '3111200943', 0, 2),
(8, '55555', 'pbkdf2:sha256:260000$bsr7gZrtE752Q9J5$193009f62bf951bfd9eae5a8839e44362455596c60d73e83725b64ec60b8c7b0', 'Eduard Rafael Caicedo', 'erafaelcaicedo@gmail.com', '23423423', 1, 2),
(9, '999999999', 'pbkdf2:sha256:260000$dgZKKlI1cCNdhAEy$90102fe40560b05bc189647cf38522a08c143c98aed8e50d850e6f5028985ef4', '99999999999', '9999@9999999', '999999', 1, 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carpeta`
--
ALTER TABLE `carpeta`
  ADD PRIMARY KEY (`idcarpeta`);

--
-- Indices de la tabla `documento`
--
ALTER TABLE `documento`
  ADD PRIMARY KEY (`iddocumento`);

--
-- Indices de la tabla `historial_documento`
--
ALTER TABLE `historial_documento`
  ADD PRIMARY KEY (`idhist_documento`);

--
-- Indices de la tabla `subcarpeta`
--
ALTER TABLE `subcarpeta`
  ADD PRIMARY KEY (`idsubcarpeta`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idusuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `carpeta`
--
ALTER TABLE `carpeta`
  MODIFY `idcarpeta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `documento`
--
ALTER TABLE `documento`
  MODIFY `iddocumento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `historial_documento`
--
ALTER TABLE `historial_documento`
  MODIFY `idhist_documento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT de la tabla `subcarpeta`
--
ALTER TABLE `subcarpeta`
  MODIFY `idsubcarpeta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idusuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
