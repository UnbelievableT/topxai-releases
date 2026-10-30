# TopxAI Desktop 下载

[English](README.md) · 简体中文

TopxAI 的公开安装包与安装说明。此仓库用于分发桌面客户端，不包含产品源码。

## 下载 macOS 版

**[下载 TopxAI Desktop 1.54.0（Apple Silicon）](https://github.com/UnbelievableT/topxai-releases/releases/latest/download/TopxAI-1.54.0-macOS-arm64.dmg)**

[查看发布说明与全部附件](https://github.com/UnbelievableT/topxai-releases/releases/latest)

上面的链接始终指向最新版。历史版本的发布记录仍在 Releases 页面。

- 适用于 Apple Silicon（M 系列），要求 macOS 15 或更高版本；当前实机验证环境为 macOS 27。
- 下载约 1.7 GB，包含内置工具运行环境。此包不适用于 Intel Mac 或 Windows。
- 从 1.54.0 起，安装包使用 Apple Developer ID 签名并通过 Apple 公证。

打开 DMG，将 TopxAI 拖入“应用程序”。第一次打开时，macOS 会询问是否打开从互联网下载的应用，点“打开”。详细步骤、权限说明和校验方法见发布附件 `INSTALL.zh-CN.md`。

每次发布提供 `SHA256SUMS` 校验文件。不要下载 GitHub 自动生成的 “Source code” 压缩包来安装应用；它仅包含本下载仓库的说明文件。

[中文安装说明](INSTALL.zh-CN.md) · [English installation instructions](INSTALL.md)

## 更新与反馈

可在设置中检查官方最新版本并打开下载链接，当前通过新版 DMG 手动更新；请先退出旧版再替换应用。1.52.x 的会话记录不会出现在 1.54.0 里，旧会话库会先完整备份在本机，详见安装说明。从旧版升级后，屏幕录制和辅助功能需要重新授权一次，以后的更新会保留这些授权。

遇到问题时，请提供应用版本、macOS 版本、芯片型号和错误提示；不要公开密码、API 密钥或私人会话内容。
