# TopxAI Desktop downloads

English · [简体中文](README.zh-CN.md)

Public installers and installation instructions for TopxAI Desktop. This repository distributes the desktop app; it does not contain the product's source code.

## Download for macOS

**[Download TopxAI Desktop 1.57.0 (Apple silicon)](https://github.com/UnbelievableT/topxai-releases/releases/latest/download/TopxAI-1.57.0-macOS-arm64.dmg)**

[Release notes and all files](https://github.com/UnbelievableT/topxai-releases/releases/latest)

The link above always points to the latest version. Earlier versions keep their release pages.

- For Apple silicon Macs (M series) with macOS 15 or later. The package was checked on macOS 27.
- The download is about 1.7 GB, including the bundled tool runtime. It does not run on Intel Macs or Windows.
- From 1.54.0 on, the app is signed with an Apple Developer ID and notarized by Apple.

Open the DMG and drag TopxAI Desktop into Applications. The first time you open it, macOS asks whether to open an app downloaded from the Internet; choose Open. Step-by-step instructions, permissions and how to check the download are in `INSTALL.md`, attached to each release.

Every release includes a `SHA256SUMS` file. Don't install from the "Source code" archives GitHub adds to each release; they only contain this repository's documents.

[English installation instructions](INSTALL.md) · [中文安装说明](INSTALL.zh-CN.md)

## Updates and feedback

From 1.57.0 on, the app updates itself: it checks for a newer version at launch and every four hours, downloads it in the background and installs it when you quit. 1.56.0 and earlier only open the download link, so the update to 1.57.0 is done by hand: quit the old version, then replace the app with the one in the new DMG.

1.57.0 uses TopxAI's new address, `api.topxai.xyz`, and a new macOS identifier. After installing it, sign in again and grant Screen Recording and Accessibility once more; chats, settings and memory stay, and later updates keep these grants. Upgrading from 1.55.0 or earlier also merges the chat and memory databases into one, which those versions cannot open afterwards: going back needs the original files, kept in `sessions/before-merge/` for 7 days, or a backup made before installing (see the installation instructions).

When reporting a problem, write to support@topxai.xyz with the app version, macOS version, chip and the error message. Never post passwords, API keys or private chat content.
