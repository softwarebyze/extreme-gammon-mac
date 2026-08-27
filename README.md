# Extreme Gammon for Mac

[![e2e](https://github.com/softwarebyze/extreme-gammon-mac/actions/workflows/e2e.yml/badge.svg)](https://github.com/softwarebyze/extreme-gammon-mac/actions/workflows/e2e.yml)

eXtreme Gammon (XG) is the backgammon program serious players use. It only ships for Windows. This project wraps it so a Mac user can **double-click one app** and play.

**Site:** https://softwarebyze.github.io/extreme-gammon-mac/

**Download:** [latest release](https://github.com/softwarebyze/extreme-gammon-mac/releases/latest)

## What you send people

The zip from Releases. They unzip, double-click **Extreme Gammon**, and wait. No Terminal, no Homebrew, no Windows license.

First launch downloads Wine (Sikarugir) and the official XG trial from [extremegammon.com](https://www.extremegammon.com/). After that, double-clicking starts the game.

If macOS says it cannot verify the developer: right-click the app → Open → Open.

## What this is not

We do **not** ship Extreme Gammon itself. The installer fetches the official 14-day trial. XG is commercial software; a license is about $60 after the trial.

This project is not affiliated with eXtreme Gammon or Gamesite 2000.

## Requirements

- Mac with macOS 14 (Sonoma) or later
- Apple Silicon (M1 and later) or Intel
- Internet, first launch only
- ~3 GB free disk

## Development

```bash
python3 scripts/pack-zip.py
```

Writes `dist/Extreme-Gammon-for-Mac.zip` with the execute bit preserved (macOS needs that).

Tag `vX.Y.Z` to cut a GitHub Release. The release workflow packs the zip and uploads it.

## Credits

- [Sikarugir](https://github.com/Sikarugir-App/Sikarugir) (Wine wrapper, successor to Wineskin/Kegworks)
- [eXtreme Gammon](https://www.extremegammon.com/) by Xavier Dufaure de Citres
