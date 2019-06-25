-- MySQL dump 10.13  Distrib 5.7.26, for Win64 (x86_64)
--
-- Host: localhost    Database: shopdb
-- ------------------------------------------------------
-- Server version	5.7.26

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add users',7,'add_users'),(20,'Can change users',7,'change_users'),(21,'Can delete users',7,'delete_users'),(22,'Can add types',8,'add_types'),(23,'Can change types',8,'change_types'),(24,'Can delete types',8,'delete_types'),(25,'Can add goods',9,'add_goods'),(26,'Can change goods',9,'change_goods'),(27,'Can delete goods',9,'delete_goods'),(28,'Can add detail',10,'add_detail'),(29,'Can change detail',10,'change_detail'),(30,'Can delete detail',10,'delete_detail'),(31,'Can add orders',11,'add_orders'),(32,'Can change orders',11,'change_orders'),(33,'Can delete orders',11,'delete_orders');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detail`
--

DROP TABLE IF EXISTS `detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderid` int(11) NOT NULL,
  `goodsid` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `price` double NOT NULL,
  `num` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detail`
--

LOCK TABLES `detail` WRITE;
/*!40000 ALTER TABLE `detail` DISABLE KEYS */;
INSERT INTO `detail` VALUES (6,20190003,5,'虾',3.5,3),(7,20190004,8,'戴尔5000',4980,2),(8,20190005,12,'睡衣',100,4),(9,20190005,6,'联想5000',5000,1),(10,20190006,12,'睡衣',100,2),(11,20190007,4,'康师傅红烧牛肉面2',3.5,4),(12,20190008,5,'虾',3.5,4),(13,20190009,8,'戴尔5000',4980,3);
/*!40000 ALTER TABLE `detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(10,'common','detail'),(9,'common','goods'),(11,'common','orders'),(8,'common','types'),(7,'common','users'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-05-30 15:31:29.211456'),(2,'auth','0001_initial','2019-05-30 15:31:30.707542'),(3,'admin','0001_initial','2019-05-30 15:31:30.934555'),(4,'admin','0002_logentry_remove_auto_add','2019-05-30 15:31:30.948556'),(5,'contenttypes','0002_remove_content_type_name','2019-05-30 15:31:31.180569'),(6,'auth','0002_alter_permission_name_max_length','2019-05-30 15:31:31.278574'),(7,'auth','0003_alter_user_email_max_length','2019-05-30 15:31:31.351579'),(8,'auth','0004_alter_user_username_opts','2019-05-30 15:31:31.367580'),(9,'auth','0005_alter_user_last_login_null','2019-05-30 15:31:31.429583'),(10,'auth','0006_require_contenttypes_0002','2019-05-30 15:31:31.438584'),(11,'auth','0007_alter_validators_add_error_messages','2019-05-30 15:31:31.455585'),(12,'auth','0008_alter_user_username_max_length','2019-05-30 15:31:31.648596'),(13,'common','0001_initial','2019-05-30 15:31:31.731600'),(14,'sessions','0001_initial','2019-05-30 15:31:31.889609'),(15,'common','0002_types','2019-06-01 12:24:53.955511'),(16,'common','0003_auto_20190603_1544','2019-06-03 07:45:11.809544'),(17,'common','0004_goods','2019-06-04 03:17:50.575064'),(18,'common','0005_detail_orders','2019-06-10 15:29:28.160885');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('if19ihm7y2zwry1rfts818sey5mm11zg','NWM5MDQxOTVjMDAyM2FiNThiNjM3MmQyZmY0ZWE1YzQxN2UwODhlNzp7InNob3BsaXN0Ijp7IjgiOnsiaWQiOjgsInR5cGVpZCI6NywiZ29vZHMiOiJcdTYyMzRcdTVjMTQ1MDAwIiwiY29tcGFueSI6Ilx1NjIzNFx1NWMxNCIsImNvbnRlbnQiOiI8cD5cdTZjMzRcdTc1MzVcdThkMzk8L3A+IiwicHJpY2UiOjQ5ODAuMCwicGljbmFtZSI6IjE1NTk3MDk4NTQuOTU0ODk2NS5qcGciLCJudW0iOjAsImNsaWNrbnVtIjo4LCJzdGF0ZSI6MSwic3RvcmUiOjEwMCwibSI6MX19LCJ2aXB1c2VyIjp7ImNvZGUiOiIiLCJzZXgiOjAsImlkIjoyMCwidXNlcm5hbWUiOiJsa2JqaGcxIiwibmFtZSI6IiIsInBhc3N3b3JkIjoiMjAyY2I5NjJhYzU5MDc1Yjk2NGIwNzE1MmQyMzRiNzAiLCJhZGRyZXNzIjoiXHU1MzE3XHU0ZWFjXHU1ZTAyXHU3M2FmXHU1N2NlXHU1MzE3XHU4ZGVmODlcdTUzZjciLCJwaG9uZSI6IiIsImVtYWlsIjoia2xxX25jZXB1QDEyNi5jb20iLCJzdGF0ZSI6MX0sImFkbWludXNlciI6eyJjb2RlIjoiMTIzNDUiLCJzZXgiOjAsImlkIjoyLCJ1c2VybmFtZSI6ImNoYXJnZXJLb25nIiwibmFtZSI6Ilx1NWYyMFx1NGUwOSIsInBhc3N3b3JkIjoiMjAyY2I5NjJhYzU5MDc1Yjk2NGIwNzE1MmQyMzRiNzAiLCJhZGRyZXNzIjoiXHU0ZjNjXHU2MWMyXHU5NzVlXHU2MWMyXHU0ZjViXHU2MzIxXHU2NzQwXHU0ZjViIiwicGhvbmUiOiIxMjM0MzU0MzUiLCJlbWFpbCI6ImtscV9uY2VwdUAxMjYuY29tIiwic3RhdGUiOjB9LCJ0b3RhbCI6NDk4MC4wLCJvcmRlcmxpc3QiOnsiOCI6eyJpZCI6OCwidHlwZWlkIjo3LCJnb29kcyI6Ilx1NjIzNFx1NWMxNDUwMDAiLCJjb21wYW55IjoiXHU2MjM0XHU1YzE0IiwiY29udGVudCI6IjxwPlx1NmMzNFx1NzUzNVx1OGQzOTwvcD4iLCJwcmljZSI6NDk4MC4wLCJwaWNuYW1lIjoiMTU1OTcwOTg1NC45NTQ4OTY1LmpwZyIsIm51bSI6MCwiY2xpY2tudW0iOjgsInN0YXRlIjoxLCJzdG9yZSI6MTAwLCJtIjoxfX19','2019-06-27 16:49:11.354466');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `typeid` int(11) NOT NULL,
  `goods` varchar(32) NOT NULL,
  `company` varchar(50) NOT NULL,
  `content` longtext NOT NULL,
  `price` double NOT NULL,
  `picname` varchar(255) NOT NULL,
  `store` int(11) NOT NULL,
  `num` int(11) NOT NULL,
  `clicknum` int(11) NOT NULL,
  `state` smallint(6) NOT NULL,
  `addtime` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES (4,11,'康师傅红烧牛肉面2','康师傅','<p>哎哎哎</p>',3.5,'1559711831.1814847.jpg',1000,0,7,0,'2019-06-04 23:58:12.534139'),(5,12,'虾','不知道','<p>奥德赛</p>',3.5,'1559667350.6809337.jpg',100,0,9,1,'2019-06-05 00:55:50.680933'),(6,13,'联想5000','联想','<p>阿斯顿</p>',5000,'1559704639.123148.jpg',10,0,4,1,'2019-06-05 11:17:19.123148'),(7,10,'盐','盐','<p>阿道夫</p>',2,'1559705936.0108783.jpg',200,0,0,1,'2019-06-05 11:38:56.010878'),(8,7,'戴尔5000','戴尔','<p>水电费</p>',4980,'1559709854.9548965.jpg',100,0,8,1,'2019-06-05 12:44:14.954896'),(9,7,'戴尔5002','戴尔','<p>电饭锅</p>',14980,'1559710202.236662.jpg',10,0,1,1,'2019-06-05 12:50:02.236662'),(10,8,'牛仔裤','鳄鱼','<p>fghf</p>',100,'1559795390.952269.jpg',200,0,4,1,'2019-06-06 12:29:50.952269'),(12,14,'睡衣','不详','<p>寄顾客</p>',100,'1559795566.686773.jpg',200,0,12,1,'2019-06-06 12:32:46.686773'),(13,14,'连衣裙','不详','<p>123</p>',200,'1559795645.3842742.jpeg',1000,0,1,1,'2019-06-06 12:34:05.384274');
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `linkman` varchar(32) NOT NULL,
  `address` varchar(255) NOT NULL,
  `code` varchar(6) NOT NULL,
  `phone` varchar(16) NOT NULL,
  `addtime` datetime(6) NOT NULL,
  `total` double NOT NULL,
  `state` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20190010 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (20190003,20,'KLQ','北京市昌平区华北电力大学','','18802136666','2019-06-11 14:29:08.000000',10.5,0),(20190004,20,'KLQ','','','','2019-06-11 14:44:16.000000',9960,1),(20190005,20,'XL','北京市昌平区华北电力大学','','18802136666','2019-06-11 14:45:49.000000',5400,2),(20190006,20,'KLQ','北京市昌平区华北电力大学','123456','18802136666','2019-06-12 16:25:25.000000',200,1),(20190007,20,'KLQ','北京市昌平区华北电力大学','123456','18802136666','2019-06-12 16:25:41.000000',14,1),(20190008,20,'KLQ','北京市昌平区华北电力大学','123456','18802136666','2019-06-12 16:30:58.000000',14,2),(20190009,20,'XL','北京市昌平区华北电力大学','123456','123456','2019-06-14 00:47:21.000000',14940,0);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type`
--

DROP TABLE IF EXISTS `type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `pid` int(11) NOT NULL,
  `path` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type`
--

LOCK TABLES `type` WRITE;
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
INSERT INTO `type` VALUES (1,'服装',0,'0,'),(2,'数码',0,'0,'),(6,'电脑',2,'0,2,'),(7,'戴尔',6,'0,2,6,'),(8,'男装',1,'0,1,'),(9,'食品',0,'0,'),(10,'生活食品',9,'0,9,'),(11,'零食',9,'0,9,'),(12,'生鲜',9,'0,9,'),(13,'联想',6,'0,2,6,'),(14,'女装',1,'0,1,');
/*!40000 ALTER TABLE `type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `name` varchar(16) NOT NULL,
  `password` varchar(32) NOT NULL,
  `sex` int(11) NOT NULL,
  `address` varchar(255) NOT NULL,
  `code` varchar(6) NOT NULL,
  `phone` varchar(16) NOT NULL,
  `email` varchar(50) NOT NULL,
  `state` int(11) NOT NULL,
  `addtime` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_username_e8658fc8_uniq` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'chargerKong','张三','202cb962ac59075b964b07152d234b70',0,'似懂非懂佛挡杀佛','12345','123435435','klq_ncepu@126.com',0,'2019-05-31 14:09:28.346806'),(5,'1161080102','张三','7815696ecbf1c96e6894b779456d330e',1,'北京市环城北路87号','123123','12345123','klq_ncepu@126.com',2,'2019-05-31 15:25:28.224942'),(6,'lkbjhgwoaiqylkb1','天空2号','202cb962ac59075b964b07152d234b70',0,'北京市环城北路89号','123123','12345123','klq_ncepu@126.com',1,'2019-06-01 01:36:09.077008'),(7,'abc','NPC','202cb962ac59075b964b07152d234b70',0,'北京市环城北路89号','123123','12345123','klq_ncepu@126.com',1,'2019-06-02 19:37:48.970223'),(8,'chargerKong3','工程师','202cb962ac59075b964b07152d234b70',1,'似懂非懂佛挡杀佛1号','123123','12345123','klq_ncepu@126.com',1,'2019-06-03 13:57:50.352170'),(17,'fgh','菜鸟','250cf8b51c773f3f8dc8b4be867a9a02',1,'天空之城','00000','8123456','cainiao@123.com',0,'2019-06-03 16:02:53.219254'),(18,'lkbjhg','chargerKong','202cb962ac59075b964b07152d234b70',0,'北京市环城北路88号','123123','123456','klq_ncepu@126.com',1,'2019-06-03 17:09:26.729669'),(19,'asf','','202cb962ac59075b964b07152d234b70',-1,'','','','',1,'2019-06-05 19:23:18.571967'),(20,'lkbjhg1','','202cb962ac59075b964b07152d234b70',0,'北京市环城北路89号','','','klq_ncepu@126.com',1,'2019-06-05 19:31:00.608394'),(21,'123','请问','76d80224611fc919a5d54f0ff9fba446',-1,'','','','',1,'2019-06-06 16:12:47.350373'),(28,'dadada1263970138','asd','81dc9bdb52d04dc20036dbd8313ed055',-1,'北京市昌平区华北电力大学','330124','18801326548','',1,'2019-06-07 00:15:56.149174'),(30,'admin','asdfsd','21232f297a57a5a743894a0e4a801fc3',1,'北京市环城北路88号','123123','12345123','cainiao@123.com',0,'2019-06-14 00:16:33.898506');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-14  0:50:50
