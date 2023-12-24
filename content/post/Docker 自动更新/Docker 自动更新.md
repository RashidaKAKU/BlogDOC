---
title: "Docker 自动更新"
description: "Watchtower - 自动更新 Docker 镜像与容器"
tags: [群晖,Docker, 教程]
categories: "Docker"
date: 2023-06-29T05:53:11+09:00
image: "https://photo-1307600264.cos.ap-hongkong.myqcloud.com/Bing/2023-06/wallpaper_20230627.jpg"
---

！！！更新 Docker 可能会出现未知问题，请谨慎更新！！！

# 快速启动

执行以下标准命令启动 Watch­tower 容器，并每 5 分钟一次检查所有容器的镜像是否为最新版，如发现镜像更新将会自动停止容器，删除容器，拉取最新镜像，在以之前启动容器的命令启动容器。
```
docker run -d \
    --name watchtower \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower
```

# 清理旧镜像

镜像在更新后旧镜像标签会变为 none，长期自动更新会导致过多的 none 镜像占用空间，加入--cleanup 参数可以在每次更新后自动删除 none 镜像。
```
docker run -d \
    --name watchtower \
    --restart always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower \
    --cleanup
```

# 指定容器更新

如无需自动更新所有稳定运行的容器，可以配置仅更新指定容器，只需要在命令后加上容器名：例如只更新 nginx 和 redis。

注意指定容器需填写 容器名，并非镜像名。由于部分容器启动时可能没有定义 --name 参数，请执行 docker ps 查询核对容器名。
```
docker run -d \
    --name watchtower \
    --restart always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower \
    --cleanup \
    nginx redis
```

# 配置自动更新频率

Watch­tower 

默认每 5 分钟轮询一次，可以使用以下参数配置更新的频率。

* --interval,-i 配置更新周期，默认 300 秒。
* --schedule,-s 配置定时更新，使用 Cron 表达式，例如 "0 0 1 * * *" 即每天凌晨 1 点更新。
！！！当使用 -s 参数来配置定时更新时，由于容器内默认为 UTC 时间，上述设置的 凌晨 1 点 实际上是北京时间早上 9 点，可以通过加上 -e TZ=Asia/Shanghai 环境变量来定义时区，此时配置的时间则为北京时间。

## 每小时更新一次
```
docker run -d \
    --name watchtower \
    --restart always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower \
    --cleanup \
    -i 3600
```

## 每天凌晨 1 点更新（北京时间）
```
docker run -d \
    --name watchtower \
    --restart always \
    -e TZ=Asia/Shanghai \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower \
    --cleanup \
    -s "0 0 1 * * *"
```

# 手动更新
使用手动更新的方式，运行一次 Watch­tower 容器来更新所需的容器，更新后会自动删除本次运行的 Watch­tower 容器：只需要加上--rm 和--run-once 参数即可，同时也可以配合以上指定容器或指定排除容器的参数来使用。

## 手动更新所有容器
```
docker run --rm \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower \
    --cleanup \
    --run-once
```

## 手动更新指定容器
```
docker run --rm \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower \
    --cleanup \
    --run-once \
    nginx redis
```