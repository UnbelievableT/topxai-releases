# Installing TopxAI Desktop 1.56.0 on macOS

Release: `v1.56.0-macos.20261108`. Download it from [TopxAI Releases](https://github.com/UnbelievableT/topxai-releases/releases).

1.56.0 can learn from your corrections, runs apps from the new store (PDF Reader is the first), shows a quieter chat page with a side panel, takes your own API providers and pairs with the TopxAI phone app.

Everything the app keeps on this Mac is shared by every TopxAI account signed in on it: chats, the sidebar, memory, lessons and learned rules, ECC practices, projects, external Agents, connectors, schedules and media. Keys, the wallet and billing stay with each account.

## Requirements

- Apple Silicon (arm64) with macOS 15.0 or later. This package does not run on Intel Macs or Windows.
- The download is about 1.7 GB and the installed app about 4.3 GB, mostly the bundled tool runtime (Python, Node.js, LibreOffice, Blender, Chromium and others), so most built-in tools need no separate install.
- Hands-on testing was done on macOS 27.0.1 (Apple M4 Max) only. The macOS 15 minimum comes from the build settings and has not been checked on a macOS 15 machine.
- The app is signed with an Apple Developer ID (YULUN XUE, ADZG57QP62) and notarized by Apple.

## Install and first launch

1. Download `TopxAI-1.56.0-macOS-arm64.dmg`.
2. Quit any older TopxAI completely, open the DMG, drag `TopxAI Desktop.app` into Applications, and start it from Applications. Don't run two versions at once.
3. On first launch macOS asks whether to open an app downloaded from the Internet. Check that it names TopxAI Desktop and click **Open**.

If macOS says it cannot verify the developer, cannot check the app for malware, or that the app is damaged, don't work around it: stop, check the download against the checksum below, and report it. A Mac managed by an organization may need its administrator.

The first launch asks for a display language: English by default, or 简体中文, 日本語, Русский, Español. You can change it later in Settings. A language chosen in an earlier version is kept.

TopxAI then asks whether it should learn from how you use it: leave it off, or turn it on for about 70,000 extra tokens a day. Neither is preselected and nothing is recorded until you choose. Settings > Learning changes this later, and also offers a standard tier that writes rules that keep coming up into the prompts. Learning needs a TopxAI account.

## Upgrading from 1.54.x or 1.55.0

Quit TopxAI, then replace the app in Applications with the new one. Chats, settings, memory and the Screen Recording and Accessibility grants carry over, because these versions carry the same signature.

On first launch the chat database and the memory database are merged into one file, `~/.local/share/topxai-desktop/sessions/topxai.db`. This takes a few seconds, during which the chat list waits. If several accounts were used on this Mac, their chats, memory and projects are merged into one copy at the same time. TopxAI also asks the learning question above.

**1.55.0 and earlier cannot open the merged database.** To go back to 1.55.0 you have to restore the data as well as the app: the files the merge replaced stay in `~/.local/share/topxai-desktop/sessions/before-merge/` for 7 days. After that, only a backup you made before installing brings them back, and chats and learning records from after that backup are lost. If you may need to go back, copy `~/.local/share/topxai-desktop` somewhere safe before installing.

From now on the app copies the chat database before each upgrade (the last 3 are kept) and once a day (the last 2 are kept), in the `sessions` folder. An upgrade needs free disk space twice the size of the chat database; without it the database is left as it is.

## Upgrading from 1.52.x

An upgrade straight from 1.52.x has not been tried. The app copies the old chat database before it upgrades it, and upgrades carry rows over instead of starting empty, but chats from 1.52.x may still not appear. Settings such as the default model may return to their defaults; if you see the sign-in page, sign in again. Screen Recording and Accessibility must be granted once more, as described below.

## Permissions for computer control

Opening the app does not grant computer control. When you want TopxAI to operate your Mac, allow it in **System Settings**, **Privacy & Security**:

- **Accessibility**, for clicking and typing. If TopxAI isn't listed, add it from Applications with the + button.
- **Screen Recording** (named Screen & System Audio Recording on newer systems), for reading the screen.

Versions before 1.54.0 had no stable signature, so after upgrading from 1.52.x or 1.53.x grant these two once more: if TopxAI is already switched on in a list, remove it with the − button and add it again. From 1.54.0 on, every version carries the same signature, so updates keep these grants.

Project folder access is requested when a feature needs it. If macOS asks you to quit and reopen the app, do so, then check the permissions again in TopxAI. Apple explains [Accessibility](https://support.apple.com/guide/mac-help/mh43185/mac) and [Screen Recording](https://support.apple.com/guide/mac-help/mchl592e5686/mac) access.

## Checking the download

Put the release's `SHA256SUMS` file in the same folder as the DMG, open Terminal in that folder and run:

```sh
shasum -a 256 -c SHA256SUMS
```

`TopxAI-1.56.0-macOS-arm64.dmg: OK` means the file is intact. The command only reads files. Don't use a checksum file from another version.

When reporting an installation problem, include your macOS version, chip, app version and the error message. Never include passwords, API keys or private chat content.
