#!/bin/bash

# This script retrieves all Gitee repositories required by the OpenHarmony repo manifest 
# across multiple release branches. Specifically, it initializes the `repo` environment 
# for each specified release branch (OpenHarmony-3.2-Release, OpenHarmony-4.0-Release, 
# OpenHarmony-4.1-Release, and OpenHarmony-5.0.0-Release), lists the repositories for 
# each, and consolidates them into a single file containing a unique list of 
# repositories without duplicates.

# Define branch names and output file
branches=("OpenHarmony-3.2-Release" "OpenHarmony-4.0-Release" "OpenHarmony-4.1-Release" "OpenHarmony-5.0.0-Release")
output_file="repo-list.txt"

# Create a new directory for the repository initialization
mkdir -p openharmony_repos
cd openharmony_repos || exit

# Initialize an empty output file
> "$output_file"

# Loop through each branch and initialize, list, and store repositories
for branch_name in "${branches[@]}"; do
    # Initialize repo for the current branch
    mkdir -p "$branch_name"
    cd "$branch_name" || exit
    repo init -u https://gitee.com/openharmony/manifest.git -b "$branch_name" --no-repo-verify

    # List repositories and append to a temporary file
    repo list -a -n >> "../temp_repos.txt"

    # Go back to the base directory
    cd ..
done

# Remove duplicates and save to the output file
sort -u temp_repos.txt | paste -sd, - > $output_file

# Cleanup temporary file
rm temp_repos.txt

echo "The unique list of repositories has been saved to $output_file."
