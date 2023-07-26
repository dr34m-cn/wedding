SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for conf
-- ----------------------------
DROP TABLE IF EXISTS `conf`;
CREATE TABLE `conf`  (
  `id` int(11) NOT NULL,
  `status` tinyint(4) NULL DEFAULT 0 COMMENT '状态，0-未开奖，1-开奖中，2-开奖结束',
  `key` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '婚礼当天key',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '配置表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for userList
-- ----------------------------
DROP TABLE IF EXISTS `userList`;
CREATE TABLE `userList`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `openId` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '微信openId',
  `status` tinyint(4) NULL DEFAULT 0 COMMENT '状态，0-暂未中奖，1-中奖',
  `reword` tinyint(4) NULL DEFAULT 0 COMMENT '奖项，0-暂未中奖，1-一等奖，2-二等奖，3-三等奖，4-幸运奖',
  `createTime` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `updateTime` datetime(0) NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '用户信息表' ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
