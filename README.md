# 🍗 astrbot_plugin_legs (看看腿插件)

一个轻量级的 [AstrBot](https://github.com/Soulter/AstrBot) 插件，支持通过指令随机获取黑丝或白丝图片，并可在 WebUI 自由配置触发概率。

![AstrBot Version](https://img.shields.io/badge/AstrBot-v4.0%2B-blue)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-green)

---

## ✨ 功能特性

* 🎨 **精准触发**：支持单独获取白丝或黑丝图片。
* 🎲 **随机概率**：支持通过 `看看腿` 指令随机掉落，概率可随时在 WebUI 拖拽调节。
* ⚡ **防重复/防缓存**：内置时间戳请求机制，避免微信、QQ 等平台因图片 URL 重复而触发本地缓存。

---

## 📌 指令列表

| 指令 | 说明 | 示例 |
| :--- | :--- | :--- |
| `白丝` | 直接获取一张白丝图片 | `白丝` |
| `黑丝` | 直接获取一张黑丝图片 | `黑丝` |
| `看看腿` | 根据设置的概率随机掉落黑丝或白丝 | `看看腿` |

---

## ⚙️ 插件配置

在 AstrBot 管理面板的 **设置 -> 插件配置 -> 看看腿插件** 中，你可以调整以下参数：

| 配置项 | 类型 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- |
| **黑丝出现概率 (%)** | `int` | `50` | 触发 `看看腿` 时掉落黑丝的概率（0~100）。白丝概率将自动为 100 - 黑丝概率。 |

---

## 📦 安装方法

### 方法一：通过 WebUI 安装（推荐）

1. 打开 AstrBot 管理面板，进入 **插件管理**。
2. 点击 **安装插件**，在 URL 框中填入本仓库地址：
   ```text
   https://github.com/ALpapam/astrbot_plugin_legs
   ```
3. 点击确定安装，安装完成后**重启 AstrBot** 或**重新加载插件**即可。

### 方法二：手动安装

1. 下载本仓库 Zip 压缩包或使用 Git 克隆：
   ```bash
   git clone https://github.com/ALpapam/astrbot_plugin_legs.git
   ```
2. 将文件夹放入 AstrBot 的 `data/plugins/` 目录下（最终路径为 `data/plugins/astrbot_plugin_legs/`）。
3. 重启 AstrBot 即可生效。

---

## 🙏 致谢

* API 提供：[nycnm API](https://api.nycnm.cn/)
* 机器人框架：[AstrBot](https://github.com/Soulter/AstrBot)
