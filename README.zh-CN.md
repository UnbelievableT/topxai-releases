# TopxAI Desktop 下载

[English](README.md) · 简体中文

TopxAI 的公开安装包与安装说明。此仓库用于分发桌面客户端，不包含产品源码。

## 下载 macOS 版

**[下载 TopxAI Desktop 1.57.0（Apple Silicon）](https://github.com/UnbelievableT/topxai-releases/releases/latest/download/TopxAI-1.57.0-macOS-arm64.dmg)**

[查看发布说明与全部附件](https://github.com/UnbelievableT/topxai-releases/releases/latest)

上面的链接始终指向最新版。历史版本的发布记录仍在 Releases 页面。

- 适用于 Apple Silicon（M 系列），要求 macOS 15 或更高版本；安装包在 macOS 27 上核对过。
- 下载约 1.7 GB，包含内置工具运行环境。此包不适用于 Intel Mac 或 Windows。
- 从 1.54.0 起，安装包使用 Apple Developer ID 签名并通过 Apple 公证。

打开 DMG，将 TopxAI 拖入“应用程序”。第一次打开时，macOS 会询问是否打开从互联网下载的应用，点“打开”。详细步骤、权限说明和校验方法见发布附件 `INSTALL.zh-CN.md`。

每次发布提供 `SHA256SUMS` 校验文件。不要下载 GitHub 自动生成的 “Source code” 压缩包来安装应用；它仅包含本下载仓库的说明文件。

[中文安装说明](INSTALL.zh-CN.md) · [English installation instructions](INSTALL.md)

## 更新与反馈

从 1.57.0 起应用会自己更新：启动时查一次新版本，之后每四小时查一次，在后台下载，下次退出时安装。1.56.0 和更早的版本只会打开下载链接，所以升到 1.57.0 这一步要手动做：先退出旧版，再用新 DMG 里的应用替换它。

1.57.0 用的是 TopxAI 的新地址 `api.topxai.xyz`，macOS 上的应用标识也换了。装好后要再登录一次，屏幕录制和辅助功能也要重新授权一次；会话、设置和记忆都会保留，以后的更新不用再授权。从 1.55.0 或更早的版本升级时，还会把会话库和记忆库合并成一个，旧版本打不开合并后的库。要退回旧版，得用 `sessions/before-merge/` 里保留 7 天的原文件，或者安装前做的备份，详见安装说明。

遇到问题时，请发邮件到 support@topxai.xyz，写明应用版本、macOS 版本、芯片型号和错误提示；不要公开密码、API 密钥或私人会话内容。
