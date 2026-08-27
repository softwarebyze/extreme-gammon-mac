# Extreme Gammon for Mac and Linux

[![e2e](https://github.com/softwarebyze/extreme-gammon-mac/actions/workflows/e2e.yml/badge.svg)](https://github.com/softwarebyze/extreme-gammon-mac/actions/workflows/e2e.yml)

eXtreme Gammon (XG) is the backgammon program serious players use. It only ships for Windows. This project wraps it so a Mac or Linux user can **double-click one app** and play.

**Site:** https://softwarebyze.github.io/extreme-gammon-mac/

**Download:** [latest release](https://github.com/softwarebyze/extreme-gammon-mac/releases/latest)

## What you send people

The zip from Releases. Mac users unzip and double-click **Extreme Gammon**. Linux users unzip and run **play-extreme-gammon**. No Windows license.

First launch downloads Wine and the official XG trial from [extremegammon.com](https://www.extremegammon.com/). After that, double-clicking starts the game.

If macOS says it cannot verify the developer: right-click the app → Open → Open.

On Linux, first launch may ask for your password so it can install Wine.

## What this is not

We do **not** ship Extreme Gammon itself. The installer fetches the official 14-day trial. XG is commercial software; a license is about $60 after the trial.

This project is not affiliated with eXtreme Gammon or Gamesite 2000.

## Requirements

- Mac: macOS 14 (Sonoma) or later, Apple Silicon or Intel
- Linux: Ubuntu/Debian, Fedora, or Arch, with a desktop
- Internet, first launch only
- ~3 GB free disk

## Development

```bash
python3 scripts/pack-zip.py
```

Writes `dist/Extreme-Gammon-for-Mac.zip` and `dist/Extreme-Gammon-for-Linux.zip` with execute bits preserved.

Tag `vX.Y.Z` to cut a GitHub Release. The release workflow packs both zips and uploads them.

## Credits

- [Sikarugir](https://github.com/Sikarugir-App/Sikarugir) (Wine wrapper on Mac, successor to Wineskin/Kegworks)
- [Wine](https://www.winehq.org/) on Linux
- [eXtreme Gammon](https://www.extremegammon.com/) by Xavier Dufaure de Citres
