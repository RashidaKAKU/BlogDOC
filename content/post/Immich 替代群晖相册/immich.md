---
title: "Immich 群晖相册替代"
description: "Docker 部署的相册管理软件 网页 移动APP"
tags: [Win,Docker,]
categories: "Docker"
date: 2023-12-03T16:47:59+09:00
image: "https://rashida.cab:5065/i/2023/12/03/pambft.jpg"
---

# 群晖 Container Manager（下面简称 CM） 部署教程。
> [immich 项目官方地址](https://immich.app/)。

打开群晖 CM 选择项目选项。
选择新建项目。
填写好项目名称以及项目地址。

创建 Docker compose 代码如下
```yaml
version: "2.1"
services:
  immich:
    image: ghcr.io/imagegenius/immich:latest
    container_name: immich
    environment:
      - PUID=0
      - PGID=0
      - TZ=Asia/Shanghai
      - DB_HOSTNAME=填写你自己的 localhost 地址
      - DB_USERNAME=postgres
      - DB_PASSWORD=postgres
      - DB_DATABASE_NAME=immich
      - REDIS_HOSTNAME=填写你自己的 localhost 地址
      - DISABLE_MACHINE_LEANRNING=false
      - DISABLE_TYPESENSE=false
      - DB_PORT=5668 
      - REDIS_PORT=6332
      - REDIS_PASSWORD=
      - CUDA_ACCELERATION=false
    volumes:
      - 实际存储地址/config:/config
      - 实际存储地址/Photo:/photos
      - 实际存储地址/machine:/config/machine-learning
    ports:
      - 端口号:8080
    restart: unless-stopped
  redis:
    image: redis
    ports:
	- 6332（上方变量 REDIS_PORT=6332 保持一致）:6379
    container_name: redis
  postgres14:
    image: postgres:14
    ports:
	- 5668（上方变量 DB_PORT=5668 保持一致）:5432
    container_name: postgres14
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: immich
    volumes:
      - /volume1/docker/immich/db:/var/lib/postgresql/data
```

# 更新 Immich
> 注意服务器版本和 APP 版本要保持一致！！否则无法使用 APP。

先在项目中停用 Immich。
打开群晖 SSH。
使用链接工具链接后 sudo -i 获取管理员权限。
cd 命令跳转到你 compose yaml 文件存储位置。
使用命令开始更新
```
docker-compose pull
```
更新后回到群晖 CM 找到容器 之前创建的 Immich容器。
右键复制设置然后清除就容器的端口号，在复制后的新容器中填写。
启动 CM 项目，打开Immich 网页端。
如果没有问题且更新到最新版，就可以删除旧容器正常使用了。

