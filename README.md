# Version Checker

## Overview

The **Version Checker** is a standalone Python script that validates if source and destination versions are listed in `versionlist.txt`. It also calculates the upgrade path and provides suggestions for efficient upgrades.

## Features

- Loads and validates versions from a `versionlist.txt` file.
- Checks if source and destination versions exist in the version list.
- Calculates the upgrade path between the versions.
- Provides recommendations for format installations when necessary.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/version-checker.git
   cd version-checker
   ```
2. Ensure `versionlist.txt` exists in the same directory as the script. This file should contain the list of valid versions, one version per line.

## Usage

Run the script in a terminal:

```bash
python version_checker.py
```

The script will prompt you to enter:

1. **Source Version**: The starting version (e.g., `20.1`).
2. **Destination Version**: The target version (e.g., `21.3`).

### Example Workflow

1. Enter the source version:
   ```
   Enter the source version (e.g., 20.1): 20.1
   ```
2. Enter the destination version:
   ```
   Enter the destination version (e.g., 21.3): 21.3
   ```
3. If valid, the script calculates and displays the upgrade path:
   ```
   Upgrade Path:
   Upgrade 1: From 20.1 to 20.4
   Upgrade 2: From 20.4 to 21.3
   
   Consider a Format-Install via USB. Downtime for more than 2 upgrades may exceed reinstalling and reapplying the configuration.
   ```

## Version List Format

Ensure `versionlist.txt` contains valid versions in ascending order, one per line, e.g.,

```
20.1
20.2
20.3
20.4
21.1
21.2
21.3
```

## Notes

- If a version is not found in `versionlist.txt`, the script will notify the user.
- The script does not support downgrades.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the script.
