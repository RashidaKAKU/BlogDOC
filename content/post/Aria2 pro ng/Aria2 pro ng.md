
---
title: "Aria2 下载器部署"
description: "Aria2 下载器 群晖Docker部署，带 UI 界面"
tags: [群晖,Docker, 教程, 下载]
categories: "Docker"
date: 2023-06-27T05:53:11+09:00
image: "https://photo-1307600264.cos.ap-hongkong.myqcloud.com/Bing/2023-06/wallpaper_20230628.jpg"
---
# Aria2 Pro Docker Cli 部署
需要修改用户路径，其余可不修改。

```
docker run -d \
    --name Aria2 \
    --restart unless-stopped \
    --log-opt max-size=1m \
    --network host \
    -e PUID=$UID \
    -e PGID=$GID \
    -e RPC_SECRET=<TOKEN> \
    -e RPC_PORT=6800 \
    -e LISTEN_PORT=6888 \
    -v $PWD/aria2-config:/config \
    -v $PWD/aria2-downloads:/downloads \
    p3terx/aria2-pro
```

# AriaNG Docker Cli 部署
可以修改用户端口
可以在 Docker 面板中设置关联容器 Aria2

```
docker run -d \
    --name AriaNG \
    --restart unless-stopped \
    --log-opt max-size=1m \
    -p 6880:6880 \
    p3terx/ariang
```

# 群晖使用 Docker Cli 方法

1. 打开群晖控制面板
2. 找到任务计划
3. 新增计划任务-用户脚本
4. 随意填写任务名称
5. 用户角色选 Root
6. 在脚本处粘贴 Docker Cli 并保存
7. 运行脚本后删除
8. 等待部署完成