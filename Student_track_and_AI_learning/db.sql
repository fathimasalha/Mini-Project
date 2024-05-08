/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - student
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`student` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `student`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add dataset',7,'add_dataset'),
(26,'Can change dataset',7,'change_dataset'),
(27,'Can delete dataset',7,'delete_dataset'),
(28,'Can view dataset',7,'view_dataset'),
(29,'Can add expert_table',8,'add_expert_table'),
(30,'Can change expert_table',8,'change_expert_table'),
(31,'Can delete expert_table',8,'delete_expert_table'),
(32,'Can view expert_table',8,'view_expert_table'),
(33,'Can add login_table',9,'add_login_table'),
(34,'Can change login_table',9,'change_login_table'),
(35,'Can delete login_table',9,'delete_login_table'),
(36,'Can view login_table',9,'view_login_table'),
(37,'Can add suggestion_table',10,'add_suggestion_table'),
(38,'Can change suggestion_table',10,'change_suggestion_table'),
(39,'Can delete suggestion_table',10,'delete_suggestion_table'),
(40,'Can view suggestion_table',10,'view_suggestion_table'),
(41,'Can add study_material',11,'add_study_material'),
(42,'Can change study_material',11,'change_study_material'),
(43,'Can delete study_material',11,'delete_study_material'),
(44,'Can view study_material',11,'view_study_material'),
(45,'Can add staff_table',12,'add_staff_table'),
(46,'Can change staff_table',12,'change_staff_table'),
(47,'Can delete staff_table',12,'delete_staff_table'),
(48,'Can view staff_table',12,'view_staff_table'),
(49,'Can add parent_table',13,'add_parent_table'),
(50,'Can change parent_table',13,'change_parent_table'),
(51,'Can delete parent_table',13,'delete_parent_table'),
(52,'Can view parent_table',13,'view_parent_table'),
(53,'Can add leave',14,'add_leave'),
(54,'Can change leave',14,'change_leave'),
(55,'Can delete leave',14,'delete_leave'),
(56,'Can view leave',14,'view_leave'),
(57,'Can add doubt_table',15,'add_doubt_table'),
(58,'Can change doubt_table',15,'change_doubt_table'),
(59,'Can delete doubt_table',15,'delete_doubt_table'),
(60,'Can view doubt_table',15,'view_doubt_table'),
(61,'Can add daily_activities',16,'add_daily_activities'),
(62,'Can change daily_activities',16,'change_daily_activities'),
(63,'Can delete daily_activities',16,'delete_daily_activities'),
(64,'Can view daily_activities',16,'view_daily_activities'),
(65,'Can add chatbot',17,'add_chatbot'),
(66,'Can change chatbot',17,'change_chatbot'),
(67,'Can delete chatbot',17,'delete_chatbot'),
(68,'Can view chatbot',17,'view_chatbot'),
(69,'Can add chat_table',18,'add_chat_table'),
(70,'Can change chat_table',18,'change_chat_table'),
(71,'Can delete chat_table',18,'delete_chat_table'),
(72,'Can view chat_table',18,'view_chat_table'),
(73,'Can add attendence_table',19,'add_attendence_table'),
(74,'Can change attendence_table',19,'change_attendence_table'),
(75,'Can delete attendence_table',19,'delete_attendence_table'),
(76,'Can view attendence_table',19,'view_attendence_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$FnZzjiH1AuRiVK1xcGVESY$ihRKfMVknEjsPED4HwQG+zipxYwlIIFC8lKMe/iXwG4=','2023-11-22 11:38:00.650818',1,'admin','','','admin@gmail.com',1,1,'2023-11-19 10:54:48.163373');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(19,'studentapp','attendence_table'),
(18,'studentapp','chat_table'),
(17,'studentapp','chatbot'),
(16,'studentapp','daily_activities'),
(7,'studentapp','dataset'),
(15,'studentapp','doubt_table'),
(8,'studentapp','expert_table'),
(14,'studentapp','leave'),
(9,'studentapp','login_table'),
(13,'studentapp','parent_table'),
(12,'studentapp','staff_table'),
(11,'studentapp','study_material'),
(10,'studentapp','suggestion_table');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-09-21 00:09:16.639252'),
(2,'auth','0001_initial','2023-09-21 00:09:17.071321'),
(3,'admin','0001_initial','2023-09-21 00:09:17.160221'),
(4,'admin','0002_logentry_remove_auto_add','2023-09-21 00:09:17.174850'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-09-21 00:09:17.179272'),
(6,'contenttypes','0002_remove_content_type_name','2023-09-21 00:09:17.250000'),
(7,'auth','0002_alter_permission_name_max_length','2023-09-21 00:09:17.296072'),
(8,'auth','0003_alter_user_email_max_length','2023-09-21 00:09:17.320701'),
(9,'auth','0004_alter_user_username_opts','2023-09-21 00:09:17.327495'),
(10,'auth','0005_alter_user_last_login_null','2023-09-21 00:09:17.376175'),
(11,'auth','0006_require_contenttypes_0002','2023-09-21 00:09:17.379209'),
(12,'auth','0007_alter_validators_add_error_messages','2023-09-21 00:09:17.394221'),
(13,'auth','0008_alter_user_username_max_length','2023-09-21 00:09:17.459286'),
(14,'auth','0009_alter_user_last_name_max_length','2023-09-21 00:09:17.500158'),
(15,'auth','0010_alter_group_name_max_length','2023-09-21 00:09:17.527914'),
(16,'auth','0011_update_proxy_permissions','2023-09-21 00:09:17.540564'),
(17,'auth','0012_alter_user_first_name_max_length','2023-09-21 00:09:17.594269'),
(18,'sessions','0001_initial','2023-09-21 00:09:17.628175'),
(19,'studentapp','0001_initial','2023-09-21 00:09:18.425587'),
(20,'studentapp','0002_alter_attendence_table_attendence','2023-09-21 23:25:09.622950'),
(21,'studentapp','0003_auto_20230923_1225','2023-09-23 19:26:01.607117'),
(22,'studentapp','0004_rename_student_name_parent_table_parent_name','2023-10-14 05:20:12.562511'),
(23,'studentapp','0005_auto_20231103_0908','2023-11-03 03:38:27.527713'),
(24,'studentapp','0006_auto_20231103_1115','2023-11-03 05:46:03.564025'),
(25,'studentapp','0007_auto_20231103_1554','2023-11-03 10:24:59.984452'),
(26,'studentapp','0008_auto_20231105_1242','2023-11-05 07:13:00.915972'),
(27,'studentapp','0009_chatbot_dataset','2023-11-05 07:13:20.827851'),
(28,'studentapp','0010_auto_20231111_1101','2023-11-11 05:31:53.036801'),
(29,'studentapp','0011_auto_20231111_1224','2023-11-11 06:55:10.682361'),
(30,'studentapp','0012_suggestion_table_type','2023-11-22 04:39:34.421924'),
(31,'studentapp','0013_alter_suggestion_table_mark','2023-11-22 07:00:45.559552'),
(32,'studentapp','0014_auto_20231122_1539','2023-11-22 10:09:25.893688');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('0w3f58jovhkqwi5l4cfykffjw9qevgug','.eJyrVkrOTFGyMtdRygHRRhY6SsVghpGOUiqIYaqjlJyTWFysZGWso1QAEjE01FFKATPMawEkThEJ:1qzapm:ykCZwIj-0oVGl7ixvCjLrud2gjQZiO9n95gt3MTJgyQ','2023-11-19 10:58:26.822225'),
('2lzdr3k8rolqxseazbfdzh8b4wxlok4q','eyJsaWQiOjF9:1qryNj:qLZOrNbDYgKR-fS3tZJ5C5-SKSPbswnb-DQUfSANWlM','2023-10-29 10:29:59.747408'),
('6tf5q3jy0homatt7shppvce4vuhqs8sg','.eJyrVsrJTFGyMrXQUSoGMcx1lJJzEouLlayMdZQKQCKGljpKqWA1QCW5MDV5JUpWBjpKJZVKVkquicWVSkAxqFwKWJdFLQCGghkC:1r4d0D:ipUIbH83kSE1zW2nnTpo_8hBo--M3qz1JI30Rv4HyKY','2023-12-03 08:18:01.261026'),
('8mxb5ecamtwnfnq67rsdhk2uc4l4dbfe','.eJxVjsEOgjAQRP-lZ9O0W1oXj975hmbb3QpKIKFwMv67kHDQ67yZl3mrSNvax63KEgdWN2XV5TdLlF8yHYCfND1mnedpXYakj4o-adXdzDLez-6foKfa72vMDZhCNjAah42U1pfCgEItZ8IAVDwam1gCOJLgSa7OJoAAYKXALh2Pfx4_X_aLOnw:1r50ae:Nv2_NIECmHggizSD7IwsKu2AquqTRVIWfGYT16EbrlY','2023-12-04 09:29:12.421212'),
('8tsh6edgfv6ksqu10pop6xeato1kk76c','.eJxVjsEOgyAQRP-FsyGwCEWPvfsNZGGXams0ET01_fdK4qG9zpt5mbcIeOxjOApvYSLRCy2a3yxievFSAT1xeawyrcu-TVHWirxokcNKPN-v7p9gxDKea59aUBm1I6-Mbzl3NmcCz9hRQu8As_VKR2IHBtlZ5JvREcABaM5wSuf6z9pGpBlLEb35fAFN0T1s:1r5lYO:4xxv46pxfe5dcnV-ul2a9-WZCkUVmAkpZrnRA0AVXNI','2023-12-06 11:38:00.653610'),
('8uqcg7xl4mvm70kprkym1pi1c1eysknw','eyJsaWQiOjU4fQ:1r3Y6i:zHv2ECc_d5EVRhLUt5BkpZoGu-Q48pj0pPJg3VT5aGg','2023-11-30 08:52:16.800680'),
('985bru13n5bpiusdxncgotiisbfell0n','.eJxVjjsOwyAQRO9CHSFYG4JTpvcZ0MIuwYkFkj9VlLvHSC6Sdt7M07yFx33Lfl958ROJm9Di8psFjC8uDdATy6PKWMu2TEG2ijzpKsdKPN_P7p8g45qPtYs9qITaklOd6zkNJiUCxzhQRGcBk3FKB2ILHbI1yNdOBwALoDnBIZ3bPzN8vvaNOn0:1r4zhG:v5ox1N7In0UnwLc6kdl-c4sTobtBNerIUsl9OVEPkr0','2023-12-04 08:31:58.102224'),
('a4ghj14qqb15umi8nt7df47woxx4u88a','.eJyrVsrJTFGyMrXQUSrOBbHMdZSS80qUrAx0lEoqlayUXBOLK5WAYjmJxcVKVsY6SgUgVYYmOkopYAZII1hfLQAhdhTb:1r4eHY:1UzC9qUAYnVc_YlBYMs_WSEOgBlSgpMcW9Qn6-Zu1zw','2023-12-03 09:40:00.627772'),
('acvdja0b9hw6z1mt8e72kmtc3qpv1h3p','eyJsaWQiOjI2fQ:1qrvhH:f-SVcJnQtbj898UzF4IdVmnHgf-jQtRhjXE9CptH-dM','2023-10-29 07:37:59.646965'),
('aimn4lw290tlzo62ozrd5kxuw2koatd7','.eJxVjsEOgyAQRP-FsyGwCEWPvfsNZGGXams0ET01_fdK4qG9zpt5mbcIeOxjOApvYSLRCy2a3yxievFSAT1xeawyrcu-TVHWirxokcNKPN-v7p9gxDKea59aUBm1I6-Mbzl3NmcCz9hRQu8As_VKR2IHBtlZ5JvREcABaM5wSuf6z9pGpBlLEb35fAFN0T1s:1r5egk:M43-CHbmCLtjz7fd0ILSGmlD2wm2Noa7SNA4qA4UB4o','2023-12-06 04:18:10.573339'),
('alw2w2ukchbsrpngakzjocl4zeingrkg','.eJyrVirITFGystBRygHRRkBGCohhaKqjVAxmGOgoJYMYprUADkIL1A:1qx0Hc:GqcZW4QR05yG0ajTwUAUCkyLQ4ZvBu_5JVaWZt4eoqw','2023-11-12 07:32:28.988660'),
('bsgtt8vq8rmf58jpi4fs10ly9ha78xhe','.eJyrVsrJTFGyMtRRSgXRRjpKxSDaVEcpBSxupqNUAGJY6iglg2iTWgBa_g1-:1qrYG3:J-omufgiuLzfQimO9cgom5vTEuficQdYPcYbG-LbidY','2023-10-28 06:36:19.037828'),
('d4pnh9qcjqgk8pr3delo9p0q8gf5f4bq','.eJyrVsrJTFGyMrLQUSoGMYzNdJSScxKLi4FMHaUCkJChCVAIxDAHqsmFMpLzSpSsDHSUSiqVrJR8U1MyS3OVdJRSQbKmtQDx2xe3:1r3YCB:IAfIBa8DKEGPlDflO_UjzjGX6RTY2VXdN1nHXpuViKA','2023-11-30 08:57:55.058895'),
('dfbf3zx3895l3iutkxey6ntzboqbjcyk','eyJsaWQiOjEsImNsYXNzIjozfQ:1qzgFj:nWZ_Gi28368mPTnQL38rYzyxH7ueElZfp33j20yVN_c','2023-11-19 16:45:35.564661'),
('dwpc2wgf7ttepc2nj4hjnelooqyo9rxf','eyJsaWQiOjF9:1qry89:tkSjgT_utvHzg_6XItaHC6emhLyNInrZiNDPbpUmpCc','2023-10-29 10:13:53.153282'),
('eh7lt4pzaik9kaaafcho5a2rq445bi5o','.eJxVjsEOgjAQRP-lZ9O0W1oXj975hmbb3QpKIKFwMv67kHDQ67yZl3mrSNvax63KEgdWN2XV5TdLlF8yHYCfND1mnedpXYakj4o-adXdzDLez-6foKfa72vMDZhCNjAah42U1pfCgEItZ8IAVDwam1gCOJLgSa7OJoAAYKXALh2Pfx4_X_aLOnw:1r4zi2:rnZ3SS64ufHK-UzXzX7dpv1VMxRQ2yn7GGnu1VnyMic','2023-12-04 08:32:46.798296'),
('emsa3ehlnroy8eze3hrys16is6qz4244','eyJsaWQiOjI2LCJzaWQiOjgsImVpZCI6NCwicGlkIjo4fQ:1qrzuZ:_TE8v1SRLGF8SK6FpMc5JinOqyNBUFKdx7nsv0fdasI','2023-10-29 12:07:59.369565'),
('jyj864tujiffadax55y20799clm4sybx','.eJxVjsEOgjAQRP-lZ9O0W1oXj975hmbb3QpKIKFwMv67kHDQ67yZl3mrSNvax63KEgdWN2XV5TdLlF8yHYCfND1mnedpXYakj4o-adXdzDLez-6foKfa72vMDZhCNjAah42U1pfCgEItZ8IAVDwam1gCOJLgSa7OJoAAYKXALh2Pfx4_X_aLOnw:1r4zbM:XSqQV7M6QMMr-GM_nidbjmUrwsdvxIlPCzTwJvx8WRM','2023-12-04 08:25:52.420258'),
('k75811t4krld3obysmhht6rvnn7mj8zi','.eJxVjjsOwyAQRO9CHSFYG4JTpvcZ0MIuwYkFkj9VlLvHSC6Sdt7M07yFx33Lfl958ROJm9Di8psFjC8uDdATy6PKWMu2TEG2ijzpKsdKPN_P7p8g45qPtYs9qITaklOd6zkNJiUCxzhQRGcBk3FKB2ILHbI1yNdOBwALoDnBIZ3bPzN8vvaNOn0:1r4zhH:uNe6xBhx0DdLL8zoUarFE6RhkSnwbxVkFnOddvuV-cY','2023-12-04 08:31:59.080783'),
('kssvvybr2vr46iukvhali2hgsm967kvx','eyJsaWQiOjF9:1qra25:yuHI8ZqFF2IAeQ7eAs0JJEZDR7LDNr80OcWO7R4vkAE','2023-10-28 08:30:01.180134'),
('lb22lyx75g7elqj08vpofatqzgs32e26','eyJsaWQiOjI2fQ:1qraYY:hSviHWcMDu0U7K_f3M0yulbZjeB_8v66fIv_ZZgzjlE','2023-10-28 09:03:34.293842'),
('m1m0mtdpbisvdmgdpzpfzy2q4zq3ki4x','.eJxVjsEOgyAQRP-FsyGwCEWPvfsNZGGXams0ET01_fdK4qG9zpt5mbcIeOxjOApvYSLRCy2a3yxievFSAT1xeawyrcu-TVHWirxokcNKPN-v7p9gxDKea59aUBm1I6-Mbzl3NmcCz9hRQu8As_VKR2IHBtlZ5JvREcABaM5wSuf6z9pGpBlLEb35fAFN0T1s:1r5egk:M43-CHbmCLtjz7fd0ILSGmlD2wm2Noa7SNA4qA4UB4o','2023-12-06 04:18:10.570193'),
('o1d9a7p898bqo4x95yukwvejhtwdu4uz','.eJxVjjsOwyAQRO9CHSFYG4JTpvcZ0MIuwYkFkj9VlLvHSC6Sdt7M07yFx33Lfl958ROJm9Di8psFjC8uDdATy6PKWMu2TEG2ijzpKsdKPN_P7p8g45qPtYs9qITaklOd6zkNJiUCxzhQRGcBk3FKB2ILHbI1yNdOBwALoDnBIZ3bPzN8vvaNOn0:1r4zhB:YbbjXbWCXeLz00WMwIVvvatqvCaM-P0g15YrkP0RDIg','2023-12-04 08:31:53.586638'),
('q41ag8ou2pmoi67dv6mji9g6kjouv140','eyJsaWQiOjI2LCJwaWQiOjh9:1qrZSq:8e6X82M-smJvlscycb9VFpvEPkZwdG3vbedWJVfoSh4','2023-10-28 07:53:36.771634'),
('s40ki0ypkdz3tybh6victkx2l3sf2gig','eyJsaWQiOjI4LCJjbGFzcyI6M30:1r3Ylw:qxgtzrp421B3LhMCKGJ2tYAPlc7yEvbUIxd3svBLvCU','2023-11-30 09:34:52.700587'),
('t2sdpzd3m0jsxq4u9mvkzzglmw1wcadv','eyJsaWQiOjI2fQ:1qraeK:Q5csqmWjmWw2vRnQiuQuz89RQRT7_-0GKPTvYVq8mDg','2023-10-28 09:09:32.999202'),
('w9l0xp87hi5phe499u0x4jbb20uxh04c','.eJxVjsEOgyAQRP-FsyGwCEWPvfsNZGGXams0ET01_fdK4qG9zpt5mbcIeOxjOApvYSLRCy2a3yxievFSAT1xeawyrcu-TVHWirxokcNKPN-v7p9gxDKea59aUBm1I6-Mbzl3NmcCz9hRQu8As_VKR2IHBtlZ5JvREcABaM5wSuf6z9pGpBlLEb35fAFN0T1s:1r50KQ:r4QSCQyOVsNh2fwOshp5tZ7TGR_q9k3r-n9NM4_2HoI','2023-12-04 09:12:26.292244'),
('zzwahpignyz9rhuvobnmcolo33hsc4wv','eyJsaWQiOjU4LCJzbWlkIjo3LCJjbnQiOjAsInR5IjoiRWFzeSIsInNpZCI6MzN9:1r4dET:IfC6S06vrnyiZdSFWzF1OO0L-lIVepWcmOiQvmRRwLc','2023-12-03 08:32:45.624859');

/*Table structure for table `studentapp_attendence_table` */

DROP TABLE IF EXISTS `studentapp_attendence_table`;

CREATE TABLE `studentapp_attendence_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `attendence` bigint NOT NULL,
  `PARENT_id` bigint NOT NULL,
  `STAFF_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `studentapp_attendenc_PARENT_id_b631e02b_fk_studentap` (`PARENT_id`),
  KEY `studentapp_attendenc_STAFF_id_a7f195f4_fk_studentap` (`STAFF_id`),
  CONSTRAINT `studentapp_attendenc_PARENT_id_b631e02b_fk_studentap` FOREIGN KEY (`PARENT_id`) REFERENCES `studentapp_parent_table` (`id`),
  CONSTRAINT `studentapp_attendenc_STAFF_id_a7f195f4_fk_studentap` FOREIGN KEY (`STAFF_id`) REFERENCES `studentapp_staff_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `studentapp_attendence_table` */

insert  into `studentapp_attendence_table`(`id`,`date`,`attendence`,`PARENT_id`,`STAFF_id`) values 
(50,'2023-10-30',1,13,17),
(51,'2023-10-30',0,14,17),
(52,'2023-11-02',0,13,17),
(53,'2023-11-02',1,14,17),
(54,'2023-11-03',1,13,17),
(55,'2023-11-03',1,14,17),
(56,'2023-11-04',0,13,17),
(57,'2023-11-04',1,14,17),
(58,'2023-11-06',0,13,17),
(59,'2023-11-06',1,14,17),
(60,'2023-11-09',0,13,17),
(61,'2023-11-09',0,14,17),
(62,'2023-11-15',1,13,17),
(63,'2023-11-15',1,14,17),
(64,'2023-11-18',1,13,17),
(65,'2023-11-18',0,14,17);

/*Table structure for table `studentapp_chat_table` */

DROP TABLE IF EXISTS `studentapp_chat_table`;

CREATE TABLE `studentapp_chat_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `message` varchar(100) NOT NULL,
  `from_id_id` bigint NOT NULL,
  `to_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `studentapp_chat_tabl_from_id_id_74a0ae3f_fk_studentap` (`from_id_id`),
  KEY `studentapp_chat_tabl_to_id_id_fe0e43f4_fk_studentap` (`to_id_id`),
  CONSTRAINT `studentapp_chat_tabl_from_id_id_74a0ae3f_fk_studentap` FOREIGN KEY (`from_id_id`) REFERENCES `studentapp_login_table` (`id`),
  CONSTRAINT `studentapp_chat_tabl_to_id_id_fe0e43f4_fk_studentap` FOREIGN KEY (`to_id_id`) REFERENCES `studentapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `studentapp_chat_table` */

insert  into `studentapp_chat_table`(`id`,`date`,`message`,`from_id_id`,`to_id_id`) values 
(15,'2023-11-03','hlo',55,58),
(16,'2023-11-05','hi',58,55),
(21,'2023-11-11','how are you',55,58),
(22,'2023-11-11','i am fine thanku',58,55),
(29,'2023-11-20','hii',55,58),
(30,'2023-11-20','hjkl',58,55);

/*Table structure for table `studentapp_chatbot` */

DROP TABLE IF EXISTS `studentapp_chatbot`;

CREATE TABLE `studentapp_chatbot` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `answer` varchar(1000) NOT NULL,
  `date` date NOT NULL,
  `PARENT_id` bigint NOT NULL,
  `DATASET_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `studentapp_chatbot_PARENT_id_9480d718_fk_studentap` (`PARENT_id`),
  KEY `studentapp_chatbot_DATASET_id_d2dda8f9_fk_studentapp_dataset_id` (`DATASET_id`),
  CONSTRAINT `studentapp_chatbot_DATASET_id_d2dda8f9_fk_studentapp_dataset_id` FOREIGN KEY (`DATASET_id`) REFERENCES `studentapp_dataset` (`id`),
  CONSTRAINT `studentapp_chatbot_PARENT_id_9480d718_fk_studentap` FOREIGN KEY (`PARENT_id`) REFERENCES `studentapp_parent_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=136 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `studentapp_chatbot` */

insert  into `studentapp_chatbot`(`id`,`answer`,`date`,`PARENT_id`,`DATASET_id`) values 
(68,'6','2023-11-18',13,9),
(69,'7','2023-11-18',13,10),
(70,'6','2023-11-18',13,11),
(71,'7','2023-11-18',13,13),
(72,'16','2023-11-18',13,8),
(73,'3','2023-11-19',13,8),
(74,'12','2023-11-19',13,9),
(75,'7','2023-11-19',13,10),
(76,'3','2023-11-19',13,11),
(77,'3','2023-11-19',13,13),
(78,'34','2023-11-20',13,8),
(79,'23','2023-11-20',13,9),
(80,'7','2023-11-20',13,10),
(81,'5','2023-11-20',13,11),
(82,'23','2023-11-20',13,13),
(83,'15','2023-11-21',13,8),
(84,'12','2023-11-21',13,9),
(85,'7','2023-11-21',13,10),
(86,'56','2023-11-21',13,11),
(87,'34','2023-11-21',13,13),
(93,'16','2023-11-22',13,8),
(94,'6','2023-11-22',13,9),
(95,'7','2023-11-22',13,10),
(96,'5','2023-11-22',13,11),
(97,'6','2023-11-22',13,13),
(121,'CPU','2023-11-20',13,26),
(122,'scanner','2023-11-20',13,27),
(123,'computer is a device','2023-11-20',13,28),
(124,'information entered in the computer input','2023-11-20',13,29),
(125,'set of insruction','2023-11-20',13,30),
(126,'cpu','2023-11-21',13,26),
(127,'dgh','2023-11-21',13,27),
(128,'fgjl','2023-11-21',13,28),
(129,'input','2023-11-21',13,29),
(130,'sjklfjk','2023-11-21',13,30),
(131,'cpu','2023-11-22',13,26),
(132,'dfg','2023-11-22',13,27),
(133,'ghj','2023-11-22',13,28),
(134,'input','2023-11-22',13,29),
(135,'ghk','2023-11-22',13,30);

/*Table structure for table `studentapp_daily_activities` */

DROP TABLE IF EXISTS `studentapp_daily_activities`;

CREATE TABLE `studentapp_daily_activities` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `activity` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `STAFF_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `studentapp_daily_act_STAFF_id_4e48b523_fk_studentap` (`STAFF_id`),
  CONSTRAINT `studentapp_daily_act_STAFF_id_4e48b523_fk_studentap` FOREIGN KEY (`STAFF_id`) REFERENCES `studentapp_staff_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `studentapp_daily_activities` */

insert  into `studentapp_daily_activities`(`id`,`date`,`activity`,`details`,`STAFF_id`) values 
(18,'2023-11-02','Maths','Homework2',17),
(19,'2023-11-22','dfsff','ferfe',17);

/*Table structure for table `studentapp_dataset` */

DROP TABLE IF EXISTS `studentapp_dataset`;

CREATE TABLE `studentapp_dataset` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `question` varchar(1000) NOT NULL,
  `answer` varchar(1000) NOT NULL,
  `type` varchar(100) NOT NULL,
  `STUDYMATERIAL_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `studentapp_dataset_STUDYMATERIAL_id_015ee09d_fk_studentap` (`STUDYMATERIAL_id`),
  CONSTRAINT `studentapp_dataset_STUDYMATERIAL_id_015ee09d_fk_studentap` FOREIGN KEY (`STUDYMATERIAL_id`) REFERENCES `studentapp_study_material` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `studentapp_dataset` */

insert  into `studentapp_dataset`(`id`,`question`,`answer`,`type`,`STUDYMATERIAL_id`) values 
(8,'9+7','16','Easy',7),
(9,'6+6','12','Easy',7),
(10,'3+4','7','Easy',7),
(11,'2+3','5','Easy',7),
(13,'3+6','9','Easy',7),
(14,'9+10','19','Medium',7),
(15,'7+11','18','Medium',7),
(16,'3+12','15','Medium',7),
(17,'5+15','20','Medium',7),
(18,'7+17','24','Medium',7),
(19,'24+36','60','Hard',7),
(20,'67+55','122','Hard',7),
(21,'34+87','121','Hard',7),
(22,'68+12','80','Hard',7),
(23,'45+56','101','Hard',7),
(26,'Name the device that is known as the brain of the computer.',' CPU (Central Processing Unit)','Easy',13),
(27,'Which hardware device is used to read words, numbers or pictures printed on a paper? ','Scanner is used to read words, numbers or pictures printed on a paper. ','Easy',13),
(28,'What is a computer?','Computer is a machine that works with the data and instructions given by the user.','Easy',13),
(29,'What do you call the information that you enter into a computer?','The information that we enter into computer is called Input.','Easy',13),
(30,'Define the term software','A group of instructions given to the computer to do a particular work is called software.','Easy',13);

/*Table structure for table `studentapp_doubt_table` */

DROP TABLE IF EXISTS `studentapp_doubt_table`;

CREATE TABLE `studentapp_doubt_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `doubt` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `EXPERT_id` bigint NOT NULL,
  `PARENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `studentapp_doubt_tab_EXPERT_id_2113cff7_fk_studentap` (`EXPERT_id`),
  KEY `studentapp_doubt_tab_PARENT_id_b7b494d1_fk_studentap` (`PARENT_id`),
  CONSTRAINT `studentapp_doubt_tab_EXPERT_id_2113cff7_fk_studentap` FOREIGN KEY (`EXPERT_id`) REFERENCES `studentapp_expert_table` (`id`),
  CONSTRAINT `studentapp_doubt_tab_PARENT_id_b7b494d1_fk_studentap` FOREIGN KEY (`PARENT_id`) REFERENCES `studentapp_parent_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `studentapp_doubt_table` */

insert  into `studentapp_doubt_table`(`id`,`date`,`doubt`,`reply`,`EXPERT_id`,`PARENT_id`) values 
(6,'2023-11-03','what is sqrt','square root',4,13),
(7,'2023-11-05','DBMA','data',4,13),
(9,'2023-11-22','fgh','pending',4,13);

/*Table structure for table `studentapp_expert_table` */

DROP TABLE IF EXISTS `studentapp_expert_table`;

CREATE TABLE `studentapp_expert_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `post` varchar(20) NOT NULL,
  `pin` bigint NOT NULL,
  `ph_no` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `studentapp_expert_ta_LOGIN_id_5b78ba81_fk_studentap` (`LOGIN_id`),
  CONSTRAINT `studentapp_expert_ta_LOGIN_id_5b78ba81_fk_studentap` FOREIGN KEY (`LOGIN_id`) REFERENCES `studentapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `studentapp_expert_table` */

insert  into `studentapp_expert_table`(`id`,`fname`,`lname`,`place`,`post`,`pin`,`ph_no`,`photo`,`LOGIN_id`,`email`) values 
(4,'Ravi','Kumar','KKD','CKL',674561,9847438967,'img7_xxhVfWa.jpg',28,'ravi@gmail.com'),
(5,'Sera','Joseph','PKD','PDL',456770,8547344533,'img9.webp',29,'sara@gmail.com');

/*Table structure for table `studentapp_leave` */

DROP TABLE IF EXISTS `studentapp_leave`;

CREATE TABLE `studentapp_leave` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `reason` varchar(100) NOT NULL,
  `PARENT_id` bigint NOT NULL,
  `STAFF_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `studentapp_leave_PARENT_id_da7f22f1_fk_studentap` (`PARENT_id`),
  KEY `studentapp_leave_STAFF_id_c366e533_fk_studentapp_staff_table_id` (`STAFF_id`),
  CONSTRAINT `studentapp_leave_PARENT_id_da7f22f1_fk_studentap` FOREIGN KEY (`PARENT_id`) REFERENCES `studentapp_parent_table` (`id`),
  CONSTRAINT `studentapp_leave_STAFF_id_c366e533_fk_studentapp_staff_table_id` FOREIGN KEY (`STAFF_id`) REFERENCES `studentapp_staff_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `studentapp_leave` */

insert  into `studentapp_leave`(`id`,`date`,`reason`,`PARENT_id`,`STAFF_id`) values 
(7,'2023-11-02','Fever',13,17),
(10,'2023-11-16','cold',13,17);

/*Table structure for table `studentapp_login_table` */

DROP TABLE IF EXISTS `studentapp_login_table`;

CREATE TABLE `studentapp_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `studentapp_login_table` */

insert  into `studentapp_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','Admin@123','admin'),
(28,'expert','Expert@123','expert'),
(29,'expert1','123','expert'),
(55,'staff','Staff@1234','staff'),
(58,'parent','Parent@123','parent'),
(59,'parent1','Parent1@123','parent'),
(84,'salha','Salha@123','staff'),
(112,'manu','Manu@123','staff'),
(120,'Shafi','Shafi@123','parent'),
(121,'nizu','Nizu@123','parent'),
(122,'nizu','Nizu@123','parent'),
(123,'nizu','Nizu@123','parent'),
(124,'nizu','Nizu@123','parent'),
(125,'nizu','Nizu@123','parent');

/*Table structure for table `studentapp_parent_table` */

DROP TABLE IF EXISTS `studentapp_parent_table`;

CREATE TABLE `studentapp_parent_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `ph_no` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `parent_name` varchar(20) NOT NULL,
  `Class` int NOT NULL,
  `DOB` date NOT NULL,
  `gender` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `post` varchar(20) NOT NULL,
  `pin` bigint NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `studentapp_parent_ta_LOGIN_id_eec94d0d_fk_studentap` (`LOGIN_id`),
  CONSTRAINT `studentapp_parent_ta_LOGIN_id_eec94d0d_fk_studentap` FOREIGN KEY (`LOGIN_id`) REFERENCES `studentapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `studentapp_parent_table` */

insert  into `studentapp_parent_table`(`id`,`fname`,`lname`,`ph_no`,`email`,`parent_name`,`Class`,`DOB`,`gender`,`place`,`post`,`pin`,`photo`,`LOGIN_id`) values 
(13,'Ahmad','Nizu',9567453456,'jaslank@gmail.com','Jasla',3,'2016-06-28','Male','kkl','KGM',676789,'b3,png_hF7yRqL.png',58),
(14,'Sheza','Rahman',9544358026,'jasnank@gmail.com','Jasna',3,'2016-06-18','Female','kdvly','KGM',676780,'g1.png_2TFJ61i.jpg',59),
(21,'Diya','Sherin',9544358026,'fathimasalhank@gmail.com','Shafi',1,'2012-01-10','Female','pakl','pppl',345678,'g3_Tircijh.jpg',120);

/*Table structure for table `studentapp_staff_table` */

DROP TABLE IF EXISTS `studentapp_staff_table`;

CREATE TABLE `studentapp_staff_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `place` varchar(20) NOT NULL,
  `post` varchar(20) NOT NULL,
  `pin` bigint NOT NULL,
  `ph_no` bigint NOT NULL,
  `Class` int NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `studentapp_staff_tab_LOGIN_id_39bb8342_fk_studentap` (`LOGIN_id`),
  CONSTRAINT `studentapp_staff_tab_LOGIN_id_39bb8342_fk_studentap` FOREIGN KEY (`LOGIN_id`) REFERENCES `studentapp_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `studentapp_staff_table` */

insert  into `studentapp_staff_table`(`id`,`fname`,`lname`,`gender`,`place`,`post`,`pin`,`ph_no`,`Class`,`photo`,`LOGIN_id`,`email`) values 
(17,'Ravi','Kumar','Male','madavoor','padanilam',673571,9847432367,3,'b1.png_p1RNCJb.jpg',55,'ravi@gmail.com'),
(33,'Fathima','Salha','Female','CKL','PDL',673576,9544358026,4,'g1_y7NzCxU.jpg',84,'fathimasalhank62@gmail.com'),
(36,'Manu','Das','Male','madavoor','PDLK',789058,9544358020,0,'b2,png_l5ML7xF.png',112,'manudas@gmail.com');

/*Table structure for table `studentapp_study_material` */

DROP TABLE IF EXISTS `studentapp_study_material`;

CREATE TABLE `studentapp_study_material` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `name` varchar(20) NOT NULL,
  `study_material` varchar(100) NOT NULL,
  `EXPERT_id` bigint NOT NULL,
  `Class` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `studentapp_study_mat_EXPERT_id_53c3522d_fk_studentap` (`EXPERT_id`),
  CONSTRAINT `studentapp_study_mat_EXPERT_id_53c3522d_fk_studentap` FOREIGN KEY (`EXPERT_id`) REFERENCES `studentapp_expert_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `studentapp_study_material` */

insert  into `studentapp_study_material`(`id`,`date`,`name`,`study_material`,`EXPERT_id`,`Class`) values 
(7,'2023-11-05','Addition','Maths-addition.pdf',4,'3'),
(13,'2023-11-22','computer','Computer.pdf',4,'3');

/*Table structure for table `studentapp_suggestion_table` */

DROP TABLE IF EXISTS `studentapp_suggestion_table`;

CREATE TABLE `studentapp_suggestion_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mark` int NOT NULL,
  `suggestion` varchar(500) NOT NULL,
  `EXPERT_id` bigint NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `studentapp_suggestio_EXPERT_id_3ddd4a08_fk_studentap` (`EXPERT_id`),
  CONSTRAINT `studentapp_suggestio_EXPERT_id_3ddd4a08_fk_studentap` FOREIGN KEY (`EXPERT_id`) REFERENCES `studentapp_expert_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `studentapp_suggestion_table` */

insert  into `studentapp_suggestion_table`(`id`,`mark`,`suggestion`,`EXPERT_id`,`type`) values 
(6,40,'improve',4,'Easy'),
(7,60,'good',4,'Easy');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
