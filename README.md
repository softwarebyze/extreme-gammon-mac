# Extreme Gammon for Mac and Linux

[![e2e](https://github.com/softwarebyze/extreme-gammon-mac/actions/workflows/e2e.yml/badge.svg)](https://github.com/softwarebyze/extreme-gammon-mac/actions/workflows/e2e.yml)

eXtreme Gammon (XG) is the backgammon program serious players use. It only ships for Windows. This project wraps it so a Mac or Linux user can **double-click one app** and play.

**Site:** https://softwarebyze.github.io/extreme-gammon-mac/

**Download:** [latest release](https://github.com/softwarebyze/extreme-gammon-mac/releases/latest)

## What you send people

The zip from Releases. Mac users unzip and double-click **Extreme Gammon**. Linux users unzip and run **play-extreme-gammon**. No Windows license.

First launch downloads Wine and the official XG trial from [extremegammon.com](https://www.extremegammon.com/). After that, double-clicking starts the game.

The Mac app is signed and notarized by Zachary Ebenfeld, so macOS should open it without an Apple malware warning. In the Dock and Command-Tab it shows as **macxg**.

On Linux, first launch may ask for your password so it can install Wine.

## What this is not

We do **not** ship Extreme Gammon itself. The installer fetches the official 14-day trial. XG is commercial software; a license is about $60 after the trial.

This project is not affiliated with eXtreme Gammon or Gamesite 2000.

## Requirements

- Mac: macOS 10.15.4 Catalina or later on Intel, macOS 11 Big Sur or later on Apple silicon. macOS 14 Sonoma or later is what has been tested; older versions are best-effort.
- Linux: Ubuntu/Debian, Fedora, or Arch, with a desktop
- Internet, first launch only
- ~3 GB free disk

## Development

```bash
python3 scripts/pack-zip.py
```

Writes `dist/Extreme-Gammon-for-Mac.zip` and `dist/Extreme-Gammon-for-Linux.zip` with execute bits preserved. The Mac zip from this script (and from the GitHub Actions release workflow) is unsigned. CI cannot sign.

The download on [Releases](https://github.com/softwarebyze/extreme-gammon-mac/releases) is signed and notarized locally by Zachary Ebenfeld (`Developer ID Application: Zachary Ebenfeld (75M38Z9JBF)`), then uploaded in place of the CI zip once that workflow finishes. On a Mac with the Developer ID certificate and a `notarytool` keychain profile named `macxg`:

```bash
# Sign the stub and the shipped macxg-wine trampoline
codesign --force --options runtime --timestamp \
  --entitlements scripts/macxg-wine.entitlements \
  --sign "Developer ID Application: Zachary Ebenfeld (75M38Z9JBF)" \
  "app/Extreme Gammon.app/Contents/Resources/macxg-wine"
codesign --force --options runtime --timestamp \
  --sign "Developer ID Application: Zachary Ebenfeld (75M38Z9JBF)" \
  "Extreme Gammon.app"

# Zip just the app, submit, staple, then pack the folder users download
ditto -c -k --keepParent "Extreme Gammon.app" submit.zip
xcrun notarytool submit submit.zip --wait --keychain-profile macxg
xcrun stapler staple "Extreme Gammon.app"
ditto -c -k --keepParent "Extreme Gammon for Mac" Extreme-Gammon-for-Mac.zip
```

Confirm `spctl -a -vv -t exec "Extreme Gammon.app"` says `accepted` / `Notarized Developer ID`, and `xcrun stapler validate` passes.

Tag `vX.Y.Z` to cut a GitHub Release. The release workflow packs both zips and uploads them; replace the Mac zip afterward as above.

## Credits

- [Sikarugir](https://github.com/Sikarugir-App/Sikarugir) (Wine wrapper on Mac, successor to Wineskin/Kegworks)
- [Wine](https://www.winehq.org/) on Linux
- [eXtreme Gammon](https://www.extremegammon.com/) by Xavier Dufaure de Citres
