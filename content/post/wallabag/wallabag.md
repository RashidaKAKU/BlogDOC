---
title: "Wallabag 安装方法"
description: "Docker 部署网页存档工具"
tags: [Docker,]
categories: "Docker"
date: 2023-12-25T06:30:59+09:00
image: "https://rashida.cab:5065/i/2023/12/25/8vv12i.jpg"
---

# 群晖 Container Manager（下面简称 CM） 部署教程。
> [Wallabag 项目官方地址](https://wallabag.org/)。

## 准备工作
首先打开群晖的文件管理在 docker 目录下 创建 wallabag 与 wallabagdb 文件夹。

```
version: '3.9'
services:
  wallabag:
    image: wallabag/wallabag
    container_name: Wallabag
    restart: on-failure:5
    environment:
      - MYSQL_ROOT_PASSWORD=wallaroot
      - SYMFONY__ENV__DATABASE_DRIVER=pdo_mysql
      - SYMFONY__ENV__DATABASE_HOST=db
      - SYMFONY__ENV__DATABASE_PORT=3306
      - SYMFONY__ENV__DATABASE_NAME=wallabag
      - SYMFONY__ENV__DATABASE_USER=wallabag
      - SYMFONY__ENV__DATABASE_PASSWORD=wallapass
      - SYMFONY__ENV__DATABASE_CHARSET=utf8mb4
      - SYMFONY__ENV__DOMAIN_NAME=xxxxxx # 修改为你反代之后的 https 地址，否则可能会出现加载错误。
      - SYMFONY__ENV__SERVER_NAME=mariushosting
      - SYMFONY__ENV__FOSUSER_CONFIRMATION=false
      - SYMFONY__ENV__TWOFACTOR_AUTH=true
    ports:
      - 6749:80
    volumes:
      - /volume1/docker/wallabag/images:/var/www/wallabag/web/assets/images:rw
      - /volume1/docker/wallabag/data:/var/www/wallabag/data:rw
     
    depends_on:
     - db
     - redis
  db:
    image: mariadb
    container_name: Wallabag-DB
    restart: always
    environment:
      - MYSQL_ROOT_PASSWORD=wallaroot
      - TZ=Asia/Tokyo
    volumes:
      - /volume1/docker/wallabagdb:/var/lib/mysql:rw
  redis:
    image: redis:alpine
    container_name: Wallabag-REDIS
    restart: on-failure:5
```
修改 compose 文件中的映射端口。

修改 db 中的文件映射本地路径，如果按照准备阶段创建文件夹，可以不用修改。

修改 wallabag 中的文件映射本地路径，如果按照准备阶段创建文件夹，可以不用修改。

修改 SYMFONY__ENV__DOMAIN_NAME=xxxxxx 中的xxxxxx 为你反代之后的 https 地址，否则可能会出现加载错误。

## 部署阶段
打开群晖 CM 选择项目选项。
选择新建项目。
填写好项目名称以及项目地址（wallabag），创建新的 compose 文件，开始部署。

