# Installing TopxAI Desktop 1.55.0 on macOS

Release: `v1.55.0-macos.20261031`. Download it from [TopxAI Releases](https://github.com/UnbelievableT/topxai-releases/releases).

1.55.0 redraws the whole app on a warm paper palette. Hard requests are planned and handed to several models, a chat can start sessions of its own, each chat can show which models ran and what they cost, and the Design canvas builds screens beside the chat. Reloading the window no longer ends a chat turn running on a TopxAI model.

Since 1.54.0 the app has two built-in capabilities. Coding workflows come from ECC and are managed under Settings, Advanced. Memory is based on claude-mem and is stored on this Mac; every TopxAI account signed in on the same Mac uses the same memory. Automatic capture is off until you turn it on in Settings, Memory, where you can also review and delete what was saved.

## Requirements

- Apple Silicon (arm64) with macOS 15.0 or later. This package does not run on Intel Macs or Windows.
- The download is about 1.7 GB and the installed app about 4.2 GB, mostly the bundled tool runtime (Python, Node.js, LibreOffice, Blender, Chromium and others), so most built-in tools need no separate install.
- Hands-on testing was done on macOS 27.0.1 (Apple M4 Max) only. The macOS 15 minimum comes from the build settings and has not been checked on a macOS 15 machine.
- The app is signed with an Apple Developer ID (YULUN XUE, ADZG57QP62) and notarized by Apple.

## Install and first launch

1. Download `TopxAI-1.55.0-macOS-arm64.dmg`.
2. Quit any older TopxAI completely, open the DMG, drag `TopxAI Desktop.app` into Applications, and start it from Applications. Don't run two versions at once.
3. On first launch macOS asks whether to open an app downloaded from the Internet. Check that it names TopxAI Desktop and click **Open**.

If macOS says it cannot verify the developer, cannot check the app for malware, or that the app is damaged, don't work around it: stop, check the download against the checksum below, and report it. A Mac managed by an organization may need its administrator.

The first launch asks for a display language: English by default, or 简体中文, 日本語, Русский, Español. You can change it later in Settings. A language chosen in an earlier version is kept.

## Upgrading from 1.54.x

Quit TopxAI, then replace the app in Applications with the new one. Chats, settings, memory and the Screen Recording and Accessibility grants carry over, because these versions carry the same signature.

## Upgrading from 1.52.x

Chats from 1.52.x do not appear in 1.54.0 or later: the chat database has a new structure and is not converted. On first launch the new version copies the old database in full to `~/.local/share/topxai-desktop/sessions/sessions-v21-<time>.db` and then starts a new one. The copy is never deleted automatically.

Settings such as the default model may return to their defaults. If you see the sign-in page after upgrading, sign in again. Memory saved per account in the old version is merged into this Mac's memory, and the original files stay untouched.

## Permissions for computer control

Opening the app does not grant computer control. When you want TopxAI to operate your Mac, allow it in **System Settings**, **Privacy & Security**:

- **Accessibility**, for clicking and typing. If TopxAI isn't listed, add it from Applications with the + button.
- **Screen Recording** (named Screen & System Audio Recording on newer systems), for reading the screen.

Earlier versions had no stable signature, so after upgrading from 1.52.x or 1.53.x grant these two once more: if TopxAI is already switched on in a list, remove it with the − button and add it again. From 1.54.0 on, every version carries the same signature, so updates keep these grants.

Microphone and project folder access are requested when a feature needs them. If macOS asks you to quit and reopen the app, do so, then check the permissions again in TopxAI. Apple explains [Accessibility](https://support.apple.com/guide/mac-help/mh43185/mac) and [Screen Recording](https://support.apple.com/guide/mac-help/mchl592e5686/mac) access.

## Checking the download

Put the release's `SHA256SUMS` file in the same folder as the DMG, open Terminal in that folder and run:

```sh
shasum -a 256 -c SHA256SUMS
```

`TopxAI-1.55.0-macOS-arm64.dmg: OK` means the file is intact. The command only reads files. Don't use a checksum file from another version.

When reporting an installation problem, include your macOS version, chip, app version and the error message. Never include passwords, API keys or private chat content.
