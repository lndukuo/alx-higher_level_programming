#!/bin/bash

# Assuming you are in the root directory of your Git repository
git add .

read -p "Enter your commit message: " commit_message

# Commit changes
git commit -m "$commit_message"

# Push changes to the default branch (e.g., main or master)
git push origin HEAD
