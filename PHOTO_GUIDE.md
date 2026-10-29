# 照片与平台更新指南

## 当前个人照片：assets/liang.jpg

主页已使用你提供的 `assets/liang.jpg`，居中显示，宽度 180px，保留原始 2:3 比例，不裁切、不拉伸。替换这张照片时可直接更新同名文件。

`assets/portrait.jpg` 仍作为日后可选路径预留；只有实际放入文件后才切换引用：

1. 选择你愿意公开、有权使用的真人照片，建议正方形或 4:5，300–800 KB。
2. 发布前移除 EXIF/GPS，并检查背景中的个人信息。
3. 保存到 `assets/portrait.jpg`。
4. 将 README 顶部头像标签替换为：

```html
<img src="assets/portrait.jpg" width="180" alt="Portrait of Ziyang Liang" />
```

## 音乐、创作与生活：2–3 张

README 的 `PHOTO_GALLERY_START` 注释中已预留三个位置：

- `assets/photos/music-studio.jpg`：音乐制作或舞台。
- `assets/photos/creative-work.jpg`：写作、创作过程或作品。
- `assets/photos/everyday.jpg`：愿意公开的生活片段。

放入真实文件后，移除对应展示区的外层注释及说明文字，并删除未使用的图片标签。建议保持单列、`width="560"`，由 GitHub 在窄屏上自动缩小。图片描述应与实际内容一致。

## 作品与平台

- 音乐：补充代表作标题、官方播放链接，以及有权公开的封面。
- 社交：在 Elsewhere 折叠区填入抖音、B 站、知乎、其他音乐平台和个人网站的公开个人主页地址。
- 不用 `#`、示例域名或猜测的用户 ID 占位；缺链接时保留纯文字。

更新后运行 `python3 scripts/check_profile.py`；发布操作见 [MAINTENANCE.md](MAINTENANCE.md)。
