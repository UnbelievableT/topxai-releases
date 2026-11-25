# TopxAI Desktop downloads

English · [简体中文](README.zh-CN.md)

Public installers and installation instructions for TopxAI Desktop. This repository distributes the desktop app; it does not contain the product's source code.

## Download for macOS

**[Download TopxAI Desktop 1.67.0 (Apple silicon)](https://dl.topxai.xyz/desktop/updates/darwin/arm64/TopxAI-1.67.0-macOS-arm64.dmg)**

[Release notes](https://github.com/UnbelievableT/topxai-releases/releases/latest), or download from https://topxai.xyz

The installers are kept on `dl.topxai.xyz`; the releases here carry the notes and installation instructions. Earlier versions keep their release pages.

- For Apple silicon Macs (M series) with macOS 15 or later. The package was checked on macOS 27.
- The DMG is about 790 MB. On first launch the app downloads its tools (Python, LibreOffice, Chromium and others), about 1.32 GB that unpack to about 3.19 GB, so keep about 5 GB free. It does not run on Intel Macs or Windows.
- From 1.54.0 on, the app is signed with an Apple Developer ID and notarized by Apple.

Open the DMG and drag TopxAI Desktop into Applications. The first time you open it, macOS asks whether to open an app downloaded from the Internet; choose Open. Step-by-step instructions, permissions and how to check the download are in `INSTALL.md`, attached to each release.

Each version's checksums are in `SHA256SUMS-<version>` beside its installer, for 1.67.0 `https://dl.topxai.xyz/desktop/updates/darwin/arm64/SHA256SUMS-1.67.0`. Don't install from the "Source code" archives GitHub adds to each release; they only contain this repository's documents.

[English installation instructions](INSTALL.md) · [中文安装说明](INSTALL.zh-CN.md)

## Updates and feedback

From 1.57.0 on, the app updates itself: it checks for a newer version at launch and every four hours, downloads it in the background and installs it when you quit, or at once from Settings. 1.57.0 to 1.66.2 update themselves to 1.67.0, a 471 MB download. From 1.56.0 or earlier, quit the old version, then replace the app with the one in the new DMG.

Since 1.57.0 the app uses TopxAI's new address, `api.topxai.xyz`, and a new macOS identifier. Coming from 1.56.0 or earlier, sign in again and grant Screen Recording and Accessibility once more; chats, settings and memory stay, and later versions keep these grants. Upgrading from 1.55.0 or earlier also merges the chat and memory databases into one, which those versions cannot open afterwards: going back needs the original files, kept in `sessions/before-merge/` for 7 days, or a backup made before installing (see the installation instructions).

1.58.0 removed connections to other computers by address, over SSH or through the coordinator, so computers added that way in 1.57.0 are no longer listed. 1.59.0 turns on the link to TopxAI's relay: other computers signed in to your account and the web edition reach this computer through it. To keep it off, add `TOPXAI_RELAY_LINK: false` to `~/.config/topxai-desktop/config.yaml` and restart the app.

When reporting a problem, write to support@topxai.xyz with the app version, macOS version, chip and the error message. Never post passwords, API keys or private chat content.
