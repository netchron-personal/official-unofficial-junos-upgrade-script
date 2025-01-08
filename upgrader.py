import os
import re

def load_version_list(file_path):
    """Load versions from the versionlist.txt file."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []

def get_full_version(version, versionlist):
    """Get the full version from the version list."""
    matching_versions = [v for v in versionlist if v.startswith(version)]
    if matching_versions:
        return matching_versions[-1]
    else:
        lower_versions = [v for v in versionlist if v < version]
        if lower_versions:
            return lower_versions[-1]
        else:
            return None

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'versionlist.txt')

    # Load versions from file
    versionlist_junos = load_version_list(file_path)
    if not versionlist_junos:
        return

    print("Welcome to the Version Checker!")

    # Get input from the user
    start_version = input("Enter the source version (e.g., 20.1): ").strip()
    finish_version = input("Enter the destination version (e.g., 21.3): ").strip()

    try:
        start_major, start_minor = map(int, re.split('[.XRD]', start_version)[:2])
        finish_major, finish_minor = map(int, re.split('[.XRD]', finish_version)[:2])
    except ValueError:
        print("Invalid version format. Please enter versions in the format 'major.minor'.")
        return

    # Check if versions are valid
    if start_version not in versionlist_junos or finish_version not in versionlist_junos:
        print("One or both of the versions are not found in versionlist.txt.")
        return

    # Check if the start version is higher than the finish version
    if (start_major, start_minor) > (finish_major, finish_minor):
        print(f"You want to downgrade from {start_version} to {finish_version}. Downgrades are not supported.")
        return

    # Calculate the upgrade path
    upgrade_path = []
    while (finish_major - start_major) > 3:
        start_major += 3
        upgrade_version = f"{start_major}.{start_minor}"
        upgrade_path.append(upgrade_version)
    upgrade_path.append(finish_version)

    # Get the full versions from the version list
    upgrade_path_full = [get_full_version(version, versionlist_junos) for version in upgrade_path]

    # Print the upgrade path
    print("\nUpgrade Path:")
    for i in range(len(upgrade_path_full)):
        if i == 0:
            print(f"Upgrade {i + 1}: From {start_version} to {upgrade_path_full[i]}")
        else:
            print(f"Upgrade {i + 1}: From {upgrade_path_full[i - 1]} to {upgrade_path_full[i]}")

    # Suggest a Format-Install if more than 2 upgrades are needed
    if len(upgrade_path_full) > 2:
        print("\nConsider a Format-Install via USB. Downtime for more than 2 upgrades may exceed reinstalling and reapplying the configuration.")

if __name__ == "__main__":
    main()
