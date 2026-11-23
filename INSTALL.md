# Installing TopxAI Desktop 1.66.2 on macOS

Release: `v1.66.2-macos.20261123`. Download the DMG from `https://dl.topxai.xyz/desktop/updates/darwin/arm64/TopxAI-1.66.2-macOS-arm64.dmg` or from https://topxai.xyz. The release on [TopxAI Releases](https://github.com/UnbelievableT/topxai-releases/releases) carries the notes and these guides only, not the installer.

1.57.0 to 1.66.1 update themselves to 1.66.2 ("Upgrading from 1.57.0 to 1.66.1" below); everyone else installs it from the DMG as described here. Coming from 1.56.0 or earlier, whose app had another macOS identifier, you also sign in once more and grant the system permissions again. "Upgrading from 1.56.0" below lists each step.

## Requirements

- Apple Silicon (arm64) with macOS 15.0 or later. This package does not run on Intel Macs or Windows.
- The DMG is about 780 MB and the installed app about 1.17 GB. The tool runtime (Python, Node.js, LibreOffice, Blender, Chromium and others) is not inside the app: TopxAI downloads it from `dl.topxai.xyz`, about 1.32 GB, and unpacks it to about 3.19 GB in `~/.local/share/topxai-desktop/runtimes/`. Keep about 5 GB free for that; the download is deleted once it is unpacked. Chats work meanwhile. Documents, browser tasks, computer control and 3D work start once the tools are installed, and Skills shows how far the download is. A download cut off by quitting or by losing the network continues where it stopped.
- 1.66.2 uses the same runtime as 1.63.0 to 1.66.1 (2026.11.20.1). A Mac that already runs one of them keeps the runtime it downloaded and downloads nothing more after the update.
- Its package, signature and notarization were checked on 2026-11-23. The macOS 15 minimum comes from the build settings and has not been checked on a macOS 15 machine.
- The app is signed with an Apple Developer ID (YULUN XUE, ADZG57QP62) and notarized by Apple.

## Install and first launch

1. Download `TopxAI-1.66.2-macOS-arm64.dmg`.
2. Quit any older TopxAI completely, open the DMG, drag `TopxAI Desktop.app` into Applications, and start it from Applications. Don't run two versions at once.
3. On first launch macOS asks whether to open an app downloaded from the Internet. Check that it names TopxAI Desktop and click **Open**.

If macOS says it cannot verify the developer, cannot check the app for malware, or that the app is damaged, don't work around it: stop, check the download against the checksum below, and report it. A Mac managed by an organization may need its administrator.

The first launch asks for a display language: English by default, or 简体中文, 日本語, Русский, Español. You can change it later in Settings. A language chosen in an earlier version is kept.

## Upgrading from 1.57.0 to 1.66.1

These versions are offered 1.66.2 when they check for updates, at start and every four hours. They download it in the background (471 MB) and install it when you quit TopxAI, or at once with **Install & restart** in Settings. On 1.64.0 to 1.66.1 the row above your account in the sidebar shows the download and the preparation, then that 1.66.2 is ready, with **Restart now**. You can also quit TopxAI and replace the app in Applications with the one in the DMG, as above. Either way your sign-in and the permissions you granted stay, because these versions carry the same identifier and signature.

A 1.66.1 updated itself to 1.66.2 in a test, through a local copy of the update address: it downloaded the whole update, macOS prepared it, and after the restart 1.66.2 ran with the tool runtime 1.66.1 had downloaded. 1.57.0 to 1.66.0 were not tried with 1.66.2.

If macOS asks for an administrator's password while TopxAI installs an update, your account cannot change the app where it is. Enter the password, or quit TopxAI and replace the app with the one in the DMG.

On 1.63.0, the update is not ready the moment its download ends: macOS takes a few more minutes to unpack and check it. During that time **Install & restart** shows nothing, and quitting leaves 1.66.2 to install only when you click **Install & restart** again. 1.64.0 and later fix this, but the update from 1.63.0 still runs 1.63.0's updater. If 1.66.2 does not install, quit TopxAI and replace the app with the one in the DMG.

Coming from 1.57.0, 1.58.0 or 1.59.0, 1.66.2 downloads its tool runtime after the update, as described under "Requirements": the old runtime was inside the old app. The update-related notes of the 1.63.0 guide apply to them too: phones pair from the web edition, your own computers reach each other without approval, and Grok's command-line tool is no longer an Agent.

## Upgrading from 1.56.0

1.56.0 does not install updates by itself. It tells you that a new version is available and opens the download in your browser. Quit TopxAI, then replace the app in Applications with the new one.

After the first launch of 1.66.2:

- **Sign in again.** The account 1.56.0 stored belongs to the old address, so 1.66.2 starts signed out. Your balance, keys and purchases are on the account and are there once you sign in.
- **Grant Accessibility and Screen Recording again** if you use computer control, as described under "System permissions". The entry left by 1.56.0 no longer applies to the new app.
- **Allow notifications again** when macOS asks.
- **Turn "Start in the background at login" on again** in Settings if you had it on, and allow TopxAI under Login Items in System Settings.
- **Choose TopxAI as the default browser again** if you had done so in 1.56.0.

Chats, settings, memory, projects and learned rules are kept: they live in `~/.config/topxai-desktop`, `~/.local/share/topxai-desktop` and `~/Library/Application Support/TopxAI Desktop`, which the new app reads as before. A phone paired with 1.56.0 pairs again from the web edition.

## Upgrading from 1.55.0 or earlier

Follow the steps for 1.56.0 above. In addition, the first launch merges the chat database and the memory database into one file, `~/.local/share/topxai-desktop/sessions/topxai.db`, as 1.56.0 did. **1.55.0 and earlier cannot open the merged database.** The files the merge replaced stay in `~/.local/share/topxai-desktop/sessions/before-merge/` for 7 days. If you may need to go back, copy `~/.local/share/topxai-desktop` somewhere safe before installing.

An upgrade straight from 1.52.x has not been tried; chats from 1.52.x may not appear.

## Updates

1.66.2 checks `https://dl.topxai.xyz/desktop/updates/darwin/arm64/` for a newer version when it starts and every four hours. It downloads a newer version in the background; with **Download updates automatically** off, it downloads only when you choose. A row above your account in the sidebar shows the download and the preparation, then "is ready · Restart now"; one notice tells you once, and the tray menu and Settings › Updates can restart too. A click while the update is being prepared restarts TopxAI as soon as the update is ready. A version goes into the update address only after an update from the version before it has installed itself in a test.

If TopxAI cannot restart into the new version, the window says so at once, with **Try again** and **Download the full installer**, and TopxAI keeps working as before. The install TopxAI makes by itself while you are away waits for a command left running in one of its terminals.

A copy of TopxAI signed with another certificate than the release, such as one built on your own Mac, cannot update itself: macOS refuses the update. TopxAI says so once and offers **Download the full installer**, which opens the DMG, instead of downloading the update again at every start.

If the update address cannot be reached, the app reads the newest version from the macOS releases on GitHub and offers its DMG from `dl.topxai.xyz`, or the download page `https://api.topxai.xyz/downloads` when that DMG is not there. Install it by hand as above.

## System permissions

Opening the app does not grant these. Allow them in **System Settings**, **Privacy & Security**, when you need them; Settings › Permissions in TopxAI shows each one and opens the right page.

- **Accessibility**, for clicking and typing when TopxAI operates your Mac. If TopxAI isn't listed, add it from Applications with the + button.
- **Screen Recording** (named Screen & System Audio Recording on newer systems), for reading the screen.
- **Full Disk Access**, for chats that search or read outside the project folder: Desktop, Documents, Downloads and Library. Without it macOS refuses such commands, and the chat is told that retrying will not help.
- **Automation**, listed since 1.64.0, for controlling other apps through Apple events.

After upgrading from 1.56.0 or earlier, grant Accessibility and Screen Recording once more: if a TopxAI entry is already in a list, remove it with the − button and add the app again from Applications. Replacing 1.57.0 or later keeps the grants, because those versions carry the same identifier and signature.

Project folder access is requested when a feature needs it. If macOS asks you to quit and reopen the app, do so, then check the permissions again in TopxAI. Apple explains [Accessibility](https://support.apple.com/guide/mac-help/mh43185/mac) and [Screen Recording](https://support.apple.com/guide/mac-help/mchl592e5686/mac) access.

## Checking the download

The DMG's SHA-256 is `b91553188e2b42085d6708435eab9104fde3d559f8f18c415a02b6be481a5c67`, also listed in `https://dl.topxai.xyz/desktop/updates/darwin/arm64/SHA256SUMS-1.66.2`. Open Terminal in the folder that holds the DMG and run:

```sh
shasum -a 256 TopxAI-1.66.2-macOS-arm64.dmg
```

The value must equal the DMG's line in `SHA256SUMS-1.66.2`. The command only reads the file. Don't compare with a checksum from another version.

When reporting an installation problem, write to support@topxai.xyz with your macOS version, chip, app version and the error message. Never include passwords, API keys or private chat content.
