---
title: "Immich 1.90.x 安装方法"
description: "Docker 部署的相册管理软件 1.90.x 安装方法"
tags: [Win,Docker,]
categories: "Docker"
date: 2023-12-23T16:47:59+09:00
image: "https://rashida.cab:5065/i/2023/12/23/pa4lk.jpg"
---

# 群晖 Container Manager（下面简称 CM） 部署教程。
> [immich 项目官方地址](https://immich.app/)。

> 1.90.x 后 compose 文件内容有了较大变化，之前的升级后可能会导致数据丢失，请谨慎升级。
## 准备工作
### 方法一
首先打开群晖的文件管理在 docker 目录下 创建 immich-app 文件夹。
再用 SSH 工具链接群晖 DSM 系统 。
cd 到 immich-app 文件夹。
运行下面两串命令，下载 docker compose 和 .env 文件。
```
wget https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml
```
```
wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env
```
修改 .env 文件中的 
```
UPLOAD_LOCATION=./library #替换成你的实际路径
```
修改 compose 文件中的映射端口。

### 方法二
去项目官网下载 docker compose 和 .env 文件，放到 immich-app 文件夹内。
修改 .env 文件中的 
```
UPLOAD_LOCATION=./library #替换成你的实际路径
```
修改 compose 文件中的映射端口。

## 部署阶段
打开群晖 CM 选择项目选项。
选择新建项目。
填写好项目名称以及项目地址（immich-app），提示使用已有 compose 文件，选择直接使用，开始部署。



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

