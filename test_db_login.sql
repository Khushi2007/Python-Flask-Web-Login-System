-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2021 at 08:35 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test_db_login`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL DEFAULT 'User',
  `password` varchar(255) NOT NULL,
  `profile_image` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `first_name`, `last_name`, `username`, `email`, `type`, `password`, `profile_image`) VALUES
(1, 'Test', 'User', 'tess usher', 'test.user@gmail.com', 'User', 'sha256$vD2M0HGO$2c9caf793316e5365ca43399aaae22de96c2f940eb0ee9e353004159311f1f1c', 'tess_usher.jpg'),
(2, 'Khushi', 'Gandhi', 'cookie', 'khushi_gandhi@outlook.com', 'User', 'sha256$l5HjWhKU$59541e161a3072a160411093b4fc728f0c5000720038258140f90dd828061a9e', 'profile.jpg'),
(3, 'Alexander', 'Lightwood', 'alec lightwood', 'alec.lightwood@gmail.com', 'User', 'sha256$KkRiqfS6$16711c8fc500f77c79cd625384f8f5bb713903c1737f67def3ae7cc906f0ace6', 'alec_lightwood.png'),
(4, 'Cole', 'Sprouse', 'cody martin', 'cole.sprouse@gmail.com', 'User', 'sha256$VGDW954X$ce5868e25bf0fe3e03ebf1001940ff1856593a93a4fe8c1a5a4d50835b0eafeb', 'cole_sprouse_wallpaper.jpg'),
(5, 'Niall', 'Horan', 'nialler', 'da_pimp_is_ere@gmail.com', 'Admin', 'sha256$9Ivenr39$158facb418f6533ff21dfd502b3d30f3bb6bea73b99a46ccbedb2fcd8fcbff02', 'Niall_Horan.jpg'),
(6, 'Harry', 'Styles', 'hazza stiles', 'i_work_in_a_bakery@gmail.com', 'Admin', 'sha256$4XPjTG8V$b6615fc76467fa1cd4609deb63a6daa26e6b991a590e8b59aac6c2f645deea27', 'harry_styles.jpg'),
(7, 'Liam', 'Payne', 'payno', 'liam.payne@gmail.com', 'Admin', 'sha256$OnXmQx4B$54c32afcb8c527fa57f2c9f349a06f1207f6866ee3fc1575d505091d8a993ec9', 'Liam_Payne.jpg'),
(8, 'Louis', 'Tomlinson', 'tommo', 'louis.tommo@gmail.com', 'Super', 'sha256$Fa5qWMDg$80d753f420168e635f6baa16afbf21508a6c20a0473674053d919f31af8ca10a', 'Louis_Tomlinson.jpg'),
(9, 'Zayn', 'Malik', 'dj malik', 'zayn.malik@gmail.com', 'Admin', 'sha256$sp6W0VN0$53f925cbe69aa9d7a1506915e65f9a24df3c36e65757d0eeeeff6e0d6d4c7550', 'Zayn_Malik.jpg'),
(10, 'Robert', 'Downey Jr', 'tony stark', 'robert.downey.jr@gmail.com', 'Super', 'sha256$OkMAHMKn$f2050ecfef08af937dd956cc25fe619db1bcd4b48ad92cac9a13d7baecb2ff67', 'Robert_Downey_Jr.jpg'),
(11, 'Chris', 'Evans', 'steve rogers', 'chris.evans@gmail.com', 'User', 'sha256$OHPqqXPA$f6444d89abe602d33ff5f7729efb048de38f7e6473599af69b62d9451d90d6c0', 'Chris_Evans.webp'),
(12, 'Chris', 'Hemsworth', 'thor odinson', 'chris.hemsworth@gmail.com', 'User', 'sha256$rBopDIJw$009d33115c339c20f6f749ebbd605975e5d38946a65446ee3accff386ae64239', 'Chris_Hemsworth.jpg'),
(13, 'Scarlett', 'Johansson', 'natasha romanoff', 'scarlett.johansson@gmail.com', 'User', 'sha256$0MW4v4vE$c32d1a3350b5d136e44b2111f08dd87a69de5c11ca4c743ea9218907068fe40a', 'Scarlett_Johansson.jpg'),
(14, 'Jeremy', 'Renner', 'barton clint', 'jeremy.renner@gmail.com', 'User', 'sha256$EZXvybO8$71ae1f1fc685ed834f5333fe01cd6f2a31201ec0006fe4c4adca195117d6d268', 'Jeremy_Renner.jpg'),
(15, 'Mark', 'Ruffalo', 'bruce banner', 'mark.ruffalo@gmail.com', 'User', 'sha256$GfzVhGcd$57268d9d5222e122e2a91151e3407acac3599c51653731dde04cc036e7482a30', 'Mark_Ruffalo.jpg'),
(16, 'Admin name', 'Admin surname', 'admin', 'admin@gmail.com', 'Admin', 'sha256$oB46VpjQ$9945deec916d52b6b28f59a7e2e868c2ee3cc27a3f7ce645e03c8edcf5bfd21e', 'admin.png'),
(17, 'Magnus', 'Bane', 'magnus bane', 'magnus.bane@gmail.com', 'User', 'sha256$6Ik5DD44$071047ebc18c8e65eb25586b53ffea0c66588362dd69c830f080413c50d28f60', 'magnus_bane.jpg'),
(20, 'Super name', 'Super surname', 'super user', 'super.user@gmail.com', 'Super', 'sha256$xHWTlslO$96c5ab8859e27eb91f51b45bcc975c0aba6bba7da30c573984bc233a30c342e9', 'super_user.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
