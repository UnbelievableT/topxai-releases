# Install TopxAI Desktop 1.52.3 on macOS

Download the application from [TopxAI Releases](https://github.com/UnbelievableT/topxai-releases/releases/tag/v1.52.3-macos.20261002). This release improves diagram navigation, skill selection and subagent identities. Updates use a **manual DMG upgrade**. It does not automatically download or install an update.

## Requirements and signing

- **Apple Silicon (M series), macOS 15 or later.** This installer does not support Intel Macs or Windows.
- Native verification was performed on **macOS 27 Apple Silicon**. The minimum version is a build requirement; macOS 15 and every supported Mac model have not been tested on physical devices.
- The application is **ad-hoc signed, not signed with an Apple Developer ID, and not notarized by Apple**. You may need to approve it in macOS before opening it for the first time.
- The installer is about **1.7 GB** because it includes the runtime for built-in tools. External applications, service accounts, and operating-system permissions may still be required for specific features.

## Install or update

1. Download `TopxAI-1.52.3-macOS-arm64.dmg` from the release page. Do not use GitHub's automatically generated “Source code” archives; those contain the download repository's documentation, not the application.
2. Quit any running version of TopxAI. Open the DMG and drag `TopxAI Desktop.app` into **Applications**. Replace the older application if updating, then launch it from Applications. Avoid running multiple copies at once.
3. If macOS blocks the application because the developer cannot be verified, dismiss the message and open **System Settings → Privacy & Security**. Find the message about TopxAI and select **Open Anyway**.
4. Complete the system's password or Touch ID confirmation and choose **Open** when prompted. This grants an exception for this application; do not disable Gatekeeper globally and do not run `sudo xattr` commands. See [Apple's official instructions](https://support.apple.com/en-us/102445).

If “Open Anyway” is not present, first confirm that you tried to launch the application. A managed Mac may require help from your administrator. If macOS says the app is damaged or will harm your computer, stop, verify the download source and checksum, and report the message.

**Users of 1.52.0 or 1.52.1 need to download 1.52.3 manually to receive the update-check fix.** In 1.52.2 and later, Settings can check the official public release and open its download link. Installation still requires quitting the old version and replacing the application manually.

## First launch and language

A fresh installation starts with an **English** language-selection screen, regardless of the system language. Choose from 5 languages: English, Simplified Chinese, Japanese, Russian, and Spanish. Select **Continue** to save your choice and reach sign-in. Your confirmed choice is retained after restart and can be changed later in Settings. Existing users keep a supported saved language and skip the first-launch selection. Previously confirmed languages that are no longer supported, including the old system-language option, fall back to English without repeating setup.

## Permissions for computer control

Allowing the app to open **does not grant computer-control permissions**. For computer-control tasks, use **System Settings → Privacy & Security** to allow:

- **Accessibility:** permits clicks, typing, and interaction with applications. If TopxAI is missing from the list, use **+** to add the copy in Applications.
- **Screen Recording / Screen & System Audio Recording:** permits reading screen content. The exact label varies by macOS version.

Microphone and project-folder access are requested separately when needed. If macOS asks you to quit and reopen the app after a permission change, follow that prompt, then recheck permissions in TopxAI.

## Verify the download

Download this release's `SHA256SUMS` file into the same folder as the DMG. In Terminal, open that folder and run:

```sh
shasum -a 256 -c SHA256SUMS
```

The result should include `TopxAI-1.52.3-macOS-arm64.dmg: OK`. This command only reads and verifies the file; it does not change security settings. Do not use another release's checksum file.

Third-party license and source notices are provided in `THIRD-PARTY-NOTICES.txt` and retained inside the application.

When reporting an installation problem, include your macOS version, chip type, app version, and error message. Do not include passwords, API keys, or private conversations.
