# Essential Git Commands
[git book](https://git-scm.com/book/en/v2)

## General
- **`git --version`**: show current git version

## Setup and Configuration
- **`git init`**: Initialize a new Git repository in the current directory.
- **`git clone <repository-url>`**: Clone a remote repository to your local machine.
- **`git remote add origin <url>`**: Link a remote repository (usually named `origin`) to your local repository.

## Working with Files
- **`git add <file>`**: Stage changes in a specific file for the next commit.
- **`git add .`**: Stage all changes in the current directory.
- **`git commit -m "message"`**: Commit staged changes with a brief message describing the changes.
- **`git status`**: Show the current status of your repository (e.g., staged, unstaged, and untracked files).
- **`git diff`**: View unstaged changes in tracked files.
- **`git diff --staged`**: View staged changes ready to be committed.

## Branching and Merging
- **`git branch`**: List all branches in the repository.
- **`git branch <branch-name>`**: Create a new branch with the specified name.
- **`git checkout <branch-name>`**: Switch to the specified branch.
- **`git checkout -b <branch-name>`**: Create and switch to a new branch.
- **`git merge <branch-name>`**: Merge the specified branch into the current branch.

## Remote Repositories
- **`git push origin <branch-name>`**: Push commits from the local branch to the remote repository.
- **`git pull origin <branch-name>`**: Fetch and merge changes from the remote branch to your local branch.
- **`git fetch`**: Download objects and refs from another repository without merging.
- **`git fetch --prune`**: Removes any references to branches that have been deleted from the remote.
- **`git remote -v`**: List all configured remotes and their URLs.
- **`git remote remove <name>`**: Remove a remote from your configuration.

## Undoing Changes
- **`git reset <file>`**: Unstage a file, keeping changes in the working directory.
- **`git reset --hard`**: Discard all changes in the working directory and reset to the latest commit.
- **`git checkout -- <file>`**: Discard changes in a specific file, restoring it to the last commit.
- **`git revert <commit-hash>`**: Create a new commit that undoes the specified commit.

## Tagging and Versioning
- **`git tag <tag-name>`**: Create a lightweight tag with the specified name.
- **`git tag -a <tag-name> -m "message"`**: Create an annotated tag with a message.

## Viewing History
- **`git log`**: Show the commit history for the current branch.
- **`git log --oneline`**: Display a simplified commit history.
- **`git show <commit-hash>`**: Display detailed information about a specific commit.

## Cleaning Up
- **`git branch -d <branch-name>`**: Delete a local branch.
- **`git branch -D <branch-name>`**: Force delete a local branch.
- **`git remote prune origin`**: Remove references to deleted branches in the remote repository.
- **`git clean -f`**: Remove untracked files from the working directory.

## Useful Shortcuts
- **`git stash`**: Save uncommitted changes for later, removing them from the working directory.
- **`git stash pop`**: Reapply stashed changes and remove the stash entry.
- **`git rebase <branch-name>`**: Move or combine a series of commits onto another branch.

---
