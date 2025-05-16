# OpenHarmony Mirror Sync Workflows 

This repository mirrors all repositories from [the OpenHarmony organization on Gitee](https://gitee.com/openharmony/docs). These mirrored repositories are **read-only** and are consumed by the Eclipse Oniro build system.

## Objective

The purpose of this mirroring is to:
1. Enhance the speed and reliability of accessing OpenHarmony repositories.
2. Simplify the process of forking and integration with GitHub.
3. Maintain up-to-date synchronization through a CI workflow executed every 24 hours.

If you are interested in contributing to active development, please visit [Eclipse Oniro for OpenHarmony](https://github.com/eclipse-oniro4openharmony).

## Repository Contents

### Scripts

#### `mirror-repo-list-generator.sh`
A script to generate a list of unique repositories required by the OpenHarmony build system across multiple release branches:
- Outputs: A consolidated list of unique repositories (`repo-list.txt`).

### Workflows

#### `.github/workflows/mirror_large_repos.yml`
A GitHub Actions workflow that:
- Mirrors large Gitee repositories with shallow cloning.
- Tracks files exceeding GitHub's 100MB limit using Git LFS.

#### `.github/workflows/split-list.py`
A Python script that:
- Divides a list of repositories into smaller chunks for parallel processing.
- Filters out problematic repositories to improve mirroring reliability.

#### `.github/workflows/main.yml`
The main CI workflow that:
1. Retrieves and processes the list of repositories to be mirrored.
2. Splits the workload into chunks for parallel execution.
3. Mirrors repositories from Gitee to GitHub.

## Key Features

- **CI-Driven Mirroring**: Automates the synchronization process to ensure repositories are always up-to-date.
- **Parallel Processing**: Speeds up mirroring by handling multiple repositories simultaneously.
- **Error Handling**: Excludes problematic repositories and leverages Git LFS for large files.

## Contributions

Contributions are welcome to improve the mirroring scripts or workflows. For development-related contributions, please refer to [Eclipse Oniro for OpenHarmony](https://github.com/eclipse-oniro4openharmony).

---

### License

This repository is licensed under the [Apache License 2.0](LICENSE).
