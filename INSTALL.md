# Installing TopxAI Desktop 1.57.0 on macOS

Release: `v1.57.0-macos.20261113`. Download it from [TopxAI Releases](https://github.com/UnbelievableT/topxai-releases/releases).

1.57.0 moves TopxAI Desktop to its new address. The app signs in and sends requests through `api.topxai.xyz`, its links go to `topxai.xyz`, and its macOS identifier is now `com.topxai.desktop`. From this version on it also updates itself.

Because the identifier changed, macOS treats 1.57.0 as a different app from 1.56.0. Chats, settings and memory stay, but you sign in once more and grant the system permissions again. "Upgrading from 1.56.0" below lists each step.

## Requirements

- Apple Silicon (arm64) with macOS 15.0 or later. This package does not run on Intel Macs or Windows.
- The download is about 1.7 GB and the installed app about 4.2 GB, mostly the bundled tool runtime (Python, Node.js, LibreOffice, Blender, Chromium and others), so most built-in tools need no separate install.
- This build was made to carry the new address and identifier. Its package, signature and notarization were checked on macOS 27.0.1 (Apple M4 Max); it did not go through the hands-on feature testing that 1.56.0 had. The macOS 15 minimum comes from the build settings and has not been checked on a macOS 15 machine.
- The app is signed with an Apple Developer ID (YULUN XUE, ADZG57QP62) and notarized by Apple.

## Install and first launch

1. Download `TopxAI-1.57.0-macOS-arm64.dmg`.
2. Quit any older TopxAI completely, open the DMG, drag `TopxAI Desktop.app` into Applications, and start it from Applications. Don't run two versions at once.
3. On first launch macOS asks whether to open an app downloaded from the Internet. Check that it names TopxAI Desktop and click **Open**.

If macOS says it cannot verify the developer, cannot check the app for malware, or that the app is damaged, don't work around it: stop, check the download against the checksum below, and report it. A Mac managed by an organization may need its administrator.

The first launch asks for a display language: English by default, or 简体中文, 日本語, Русский, Español. You can change it later in Settings. A language chosen in an earlier version is kept.

## Upgrading from 1.56.0

1.56.0 does not install updates by itself. It tells you that 1.57.0 is available and opens the download in your browser. Quit TopxAI, then replace the app in Applications with the new one.

After the first launch of 1.57.0:

- **Sign in again.** The account 1.56.0 stored belongs to the old address, so 1.57.0 starts signed out. Your balance, keys and purchases are on the account and are there once you sign in.
- **Grant Accessibility and Screen Recording again** if you use computer control, as described under "Permissions for computer control". The entry left by 1.56.0 no longer applies to the new app.
- **Allow notifications again** when macOS asks.
- **Turn "Start in the background at login" on again** in Settings if you had it on for on-duty Agents, and allow TopxAI under Login Items in System Settings.
- **Choose TopxAI as the default browser again** if you had done so in 1.56.0.

Chats, settings, memory, projects and learned rules are kept: they live in `~/.config/topxai-desktop`, `~/.local/share/topxai-desktop` and `~/Library/Application Support/TopxAI Desktop`, which the new app reads as before. A phone paired under 1.56.0 is expected to stay paired, but this was not tried on a real phone; if the phone stops receiving status, pair it again in Settings > Connect a phone.

## Upgrading from 1.55.0 or earlier

Follow the steps for 1.56.0 above. In addition, the first launch merges the chat database and the memory database into one file, `~/.local/share/topxai-desktop/sessions/topxai.db`, as 1.56.0 did. **1.55.0 and earlier cannot open the merged database.** The files the merge replaced stay in `~/.local/share/topxai-desktop/sessions/before-merge/` for 7 days. If you may need to go back, copy `~/.local/share/topxai-desktop` somewhere safe before installing.

An upgrade straight from 1.52.x has not been tried; chats from 1.52.x may not appear.

## Updates from now on

1.57.0 checks `api.topxai.xyz` for a newer version when it starts and every four hours. A new version downloads in the background and installs when you next quit, or after five minutes of inactivity when no chat or scheduled work needs the app. Settings has **Download updates automatically** to turn the background download off, and **Install & restart** to install at once.

If the update address cannot be reached, the app offers the DMG from the latest GitHub release instead, to be installed by hand as above.

## Permissions for computer control

Opening the app does not grant computer control. When you want TopxAI to operate your Mac, allow it in **System Settings**, **Privacy & Security**:

- **Accessibility**, for clicking and typing. If TopxAI isn't listed, add it from Applications with the + button.
- **Screen Recording** (named Screen & System Audio Recording on newer systems), for reading the screen.

After upgrading from any earlier version, grant these two once more: if a TopxAI entry is already in a list, remove it with the − button and add the app again from Applications. Later updates keep the grants, because every version from 1.57.0 on carries the same identifier and signature.

Project folder access is requested when a feature needs it. If macOS asks you to quit and reopen the app, do so, then check the permissions again in TopxAI. Apple explains [Accessibility](https://support.apple.com/guide/mac-help/mh43185/mac) and [Screen Recording](https://support.apple.com/guide/mac-help/mchl592e5686/mac) access.

## Checking the download

Put the release's `SHA256SUMS` file in the same folder as the DMG, open Terminal in that folder and run:

```sh
shasum -a 256 -c SHA256SUMS
```

`TopxAI-1.57.0-macOS-arm64.dmg: OK` means the file is intact. The command only reads files. Don't use a checksum file from another version.

When reporting an installation problem, write to support@topxai.xyz with your macOS version, chip, app version and the error message. Never include passwords, API keys or private chat content.
