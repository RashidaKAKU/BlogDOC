import os
from datetime import datetime

# 设置文章的元数据
title = " " # 文章标题
description = " " # 文章描述
tags = [" "," "] # 文章标签
categories = " " # 文章分类
date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+09:00") # 文章创建时间
featured_image = " g" # 文章特色图片

# 生成Markdown内容
content = f"""---
title: "{title}"
description: "{description}"
tags: {tags}
categories: "{categories}"
date: "{date}"
featured_image: "{featured_image}"
---

"""
# 在上方 --- 之后 """ 之上添加你文章的内容

# 指定Hugo的文章目录路径
hugo_content_dir = r"D:\Code\BlogDoc\content\Windows"

# 创建新的Markdown文件
slug = title.lower().replace(" ", "-")
file_path = os.path.join(hugo_content_dir, f"{slug}.md")
with open(file_path, "w") as f:
    f.write(content)

print(f"成功创建新的Hugo文章：{file_path}")
