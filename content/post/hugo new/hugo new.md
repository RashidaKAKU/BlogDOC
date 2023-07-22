---
title: "Hugo 新建文章"
description: "利用 Python 新建文章到指定文件夹"
tags: [Win,Python,Hugo]
categories: "脚本"
date: 2023-05-09T04:53:11+09:00
image: "https://photo-1307600264.cos.ap-hongkong.myqcloud.com/Bing/2023-06/wallpaper_20230607.jpg"
---

> 利用 Python 新建 Hugo 文章到指定文件夹

# 使用方式

## 1. 设置文章的元数据

## 2. 指定 Hugo 的文章目录路径

## 3. 创建新的 Markdown 文件

Hugo 的文章目录路径默认为 Content 文件夹

文件名默认为元数据中的 Title

替换代码中的 % 占位符

```python
在代码 --- 之后 """ 之上添加你文章的内容
```

```python
import os
from datetime import datetime

# 设置文章的元数据
title = "%" # 文章标题
description = "%" # 文章描述
tags = [%] # 文章标签
categories = "%" # 文章分类
date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+09:00") # 文章创建时间
featured_image = "%" # 文章特色图片

# 生成Markdown内容
content = f"""---
title: "{title}"
description: "{description}"
tags: {tags}
categories: "{categories}"
date: "{date}"
featured_image: "{featured_image}"
---
%%%%%%%%%%%%%
"""
# 在上方 --- 之后 """ 之上添加你文章的内容

# 指定Hugo的文章目录路径
hugo_content_dir = r"%%%%%%%完整路径%%%%%%"

# 创建新的Markdown文件
slug = title.lower().replace(" ", "-")
file_path = os.path.join(hugo_content_dir, f"{slug}.md")
with open(file_path, "w") as f:
    f.write(content)

print(f"成功创建新的Hugo文章：{file_path}")

```
