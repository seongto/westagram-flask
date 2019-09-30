-- MySQL dump 10.13  Distrib 5.7.25, for osx10.14 (x86_64)
--
-- Host: localhost    Database: westa
-- ------------------------------------------------------
-- Server version	5.7.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img` varchar(1000) NOT NULL DEFAULT 'https://s3.ap-northeast-2.amazonaws.com/cdn.wecode.co.kr/logo/wecode_gray_logo.png',
  `post_text` text,
  `total_like` int(11) NOT NULL DEFAULT '0',
  `author` varchar(20) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (1,'https://scontent-gmp1-1.cdninstagram.com/vp/236ee9845cd1052b5ede2af90689ea8b/5E3D302B/t51.2885-15/sh0.08/e35/s640x640/58410837_2294357490683490_1995145092515161063_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=106 640w,https://scontent-gmp1-1.cdninstagram.com/vp/67b2248b80c42b93605e2aa749ea45af/5E3093EF/t51.2885-15/sh0.08/e35/s750x750/58410837_2294357490683490_1995145092515161063_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=106 750w,https://scontent-gmp1-1.cdninstagram.com/vp/2a10c2eca0b943448a994c7080786e51/5E19C5EF/t51.2885-15/e35/s1080x1080/58410837_2294357490683490_1995145092515161063_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=106 1080w','위코드의 모든 커리큘럼은 글로벌 코워킹 스페이스 #wework 에서 진행됩니다.',0,'wecode_bootcamp','2019-09-30 12:29:05',NULL,0),(2,'https://scontent-gmp1-1.cdninstagram.com/vp/6f773632762191105093909353e83c4b/5E3B5C56/t51.2885-15/sh0.08/e35/s640x640/67415440_525074608253260_6147130801562027883_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=104 640w,https://scontent-gmp1-1.cdninstagram.com/vp/78163ea210d1afea2d3a116d7fff8ebe/5E2E4456/t51.2885-15/sh0.08/e35/s750x750/67415440_525074608253260_6147130801562027883_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=104 750w,https://scontent-gmp1-1.cdninstagram.com/vp/b68e6820398d1c6ee162d016e8da9c66/5E20E2E1/t51.2885-15/e35/s1080x1080/67415440_525074608253260_6147130801562027883_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=104 1080w','위코드 2기 수료식! 모두 수고하셨습니다!',0,'wecode_bootcamp','2019-09-30 12:29:05',NULL,0),(3,'https://scontent-gmp1-1.cdninstagram.com/vp/7e887feffa673df5e0d27bfa90fa6148/5E2A252F/t51.2885-15/sh0.08/e35/p640x640/66710303_674722113002527_2823296399337308947_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=107 640w,https://scontent-gmp1-1.cdninstagram.com/vp/b84c8d804571665579e108cba5a534b2/5E1B372F/t51.2885-15/sh0.08/e35/p750x750/66710303_674722113002527_2823296399337308947_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=107 750w,https://scontent-gmp1-1.cdninstagram.com/vp/4df1fca4a75d6efcf1b2c45e59d92d7c/5E24C8CA/t51.2885-15/e35/p1080x1080/66710303_674722113002527_2823296399337308947_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=107 1080w','코딩 중에 간식 챙기는 것은 기본!',0,'wecode_bootcamp','2019-09-30 12:29:05',NULL,0),(4,'https://scontent-gmp1-1.cdninstagram.com/vp/ba4fcc7c4d4e481ed3e0b64670db41d1/5E222C74/t51.2885-15/sh0.08/e35/s640x640/67752580_2251982321577164_7584410942453240704_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=108 640w,https://scontent-gmp1-1.cdninstagram.com/vp/ebcb4da772e3d3114668d71e3a144596/5E24C9B0/t51.2885-15/sh0.08/e35/s750x750/67752580_2251982321577164_7584410942453240704_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=108 750w,https://scontent-gmp1-1.cdninstagram.com/vp/cc9bd1ff0187fdeda39ab90825f9524b/5E2DC9B0/t51.2885-15/e35/s1080x1080/67752580_2251982321577164_7584410942453240704_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=108 1080w','클라이밍을 비롯한 위워크의 다양한 이벤트를 즐길 수 있어요!',0,'wecode_bootcamp','2019-09-30 12:29:05',NULL,0),(5,'https://scontent-gmp1-1.cdninstagram.com/vp/a6fa26072b6ea9961778bb9d70ed9b87/5E1E8425/t51.2885-15/sh0.08/e35/s640x640/68801638_182495849449265_8439247336083662841_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=105 640w,https://scontent-gmp1-1.cdninstagram.com/vp/8471888c3188ea1bdc176381769bb8dd/5E322825/t51.2885-15/sh0.08/e35/s750x750/68801638_182495849449265_8439247336083662841_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=105 750w,https://scontent-gmp1-1.cdninstagram.com/vp/bd1cd0ab844f96c8d191ffc9d14d0372/5E18A7C0/t51.2885-15/e35/68801638_182495849449265_8439247336083662841_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=105 1080w','위코드 프론트엔드 어벤져스!',0,'wecode_bootcamp','2019-09-30 12:29:05',NULL,0),(6,'https://t1.daumcdn.net/cfile/tistory/99DDFB3B5B42C58522','여기가 그 핫하다는 위코드인가요?',0,'개그맨 황모씨','2019-09-30 12:29:33',NULL,0);
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) NOT NULL,
  `review_text` text,
  `author` varchar(20) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `reviews_post_id_fkey` (`post_id`),
  CONSTRAINT `reviews_post_id_fkey` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,1,'참 좋은 글이네요.','행인','2019-09-30 12:35:11',NULL,0),(2,1,'위워크 넘나 이쁘네요!','위워크 매니저','2019-09-30 12:35:11',NULL,0),(3,1,'맥주 맛있겠다...','그라가스','2019-09-30 12:35:11',NULL,0),(4,2,'동료 개발자가 되신 것을 축하드립니다.','갓예리','2019-09-30 12:35:11',NULL,0),(5,2,'모두 수고많으셨어요~! 축하합니다!','위코드 부트캠프','2019-09-30 12:35:11',NULL,0),(6,3,'당분은 정의다.','당 떨어진 형주','2019-09-30 12:35:11',NULL,0),(7,4,'선릉 2호점만의 특별한 매력!','모 매니저','2019-09-30 12:35:11',NULL,0),(8,5,'재밌엉...','왼쪽 사람','2019-09-30 12:35:11',NULL,0),(9,5,'이게 왜 안되지...','가운데 사람','2019-09-30 12:35:11',NULL,0),(10,5,'이게 왜 안되지...','오른쪽 사람','2019-09-30 12:35:11',NULL,0),(11,6,'하하하하하하하하하하하','관객','2019-09-30 12:35:11',NULL,0);
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-30 21:37:19
