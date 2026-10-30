# TopxAI Desktop downloads

English · [简体中文](README.zh-CN.md)

Public installers and installation instructions for TopxAI Desktop. This repository distributes the desktop app; it does not contain the product's source code.

## Download for macOS

**[Download TopxAI Desktop 1.54.1 (Apple silicon)](https://github.com/UnbelievableT/topxai-releases/releases/latest/download/TopxAI-1.54.1-macOS-arm64.dmg)**

[Release notes and all files](https://github.com/UnbelievableT/topxai-releases/releases/latest)

The link above always points to the latest version. Earlier versions keep their release pages.

- For Apple silicon Macs (M series) with macOS 15 or later. Hands-on testing was done on macOS 27.
- The download is about 1.7 GB, including the bundled tool runtime. It does not run on Intel Macs or Windows.
- From 1.54.0 on, the app is signed with an Apple Developer ID and notarized by Apple.

Open the DMG and drag TopxAI Desktop into Applications. The first time you open it, macOS asks whether to open an app downloaded from the Internet; choose Open. Step-by-step instructions, permissions and how to check the download are in `INSTALL.md`, attached to each release.

Every release includes a `SHA256SUMS` file. Don't install from the "Source code" archives GitHub adds to each release; they only contain this repository's documents.

[English installation instructions](INSTALL.md) · [中文安装说明](INSTALL.zh-CN.md)

## Updates and feedback

Settings can check for the latest official version and open its download link. For now, update by installing the new DMG: quit the old version first, then replace the app. Chats from 1.52.x do not appear in 1.54.x; the old chat database is first copied in full on your Mac (see the installation instructions). After upgrading from an earlier version, grant Screen Recording and Accessibility once more; later updates keep these grants.

When reporting a problem, include the app version, macOS version, chip and the error message. Never post passwords, API keys or private chat content.
