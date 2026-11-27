# Git Guide

This guide helps beginners learn basic Git operations and understand how to contribute to open-source projects with Git. It starts with installation and configuration, then introduces local repository management and remote collaboration.

---

## Introduction

Git is a distributed version-control system widely used for code management and team collaboration. It lets you track a file's change history and allows multiple people to work on different branches at the same time.

---

## Installing and Configuring Git

### Install Git

- **Windows**: Visit [git-scm.com](https://git-scm.com/), download the installer, and run it.
- **macOS**:

  ```bash
  brew install git
  ```

- **Linux (Ubuntu/Debian)**:

  ```bash
  sudo apt update
  sudo apt install git
  ```

### Configure User Information

Set your user name and email address before using Git for the first time:

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

View the current configuration:

```bash
git config --list
```

---

## Creating a Local Repository

After entering the project directory, initialize a Git repository with:

```bash
cd your_project_folder
git init
```

Add files to the staging area and commit the first change:

```bash
git add .
git commit -m "Initial commit"
```

---

## Daily Development Operations

### View Status

```bash
git status
```

### Add Files to the Staging Area

Add a single file or all modified files:

```bash
git add filename.txt
# Or stage all modified files
git add .
```

### Commit Changes

```bash
git commit -m "Describe what you did"
```

### View Commit History

```bash
git log
```

Or display a more compact one-line summary for each commit:

```bash
git log --oneline
```

---

## Branch Management

### List All Branches

```bash
git branch
```

The branch marked with an asterisk (`*`) is the current branch.

### Create a Branch

```bash
git checkout -b feature_branch_name
```

This creates and switches to the new branch.

### Switch Branches

```bash
git checkout main
```

This switches back to the `main` branch or another existing branch.

### Merge a Branch

Merge `feature_branch_name` into the current branch (usually `main`):

```bash
git merge feature_branch_name
```

If conflicts occur, edit the affected files manually before continuing the merge.

### Delete a Branch

Delete a completed local feature branch:

```bash
git branch -d feature_branch_name
```

To force deletion of a branch that has not been fully merged, use `-D` instead of `-d`.

---

## Connecting to a Remote Repository

To push a local project to a hosting service such as GitHub or GitLab, first add the remote repository URL:

```bash
git remote add origin https://github.com/username/repository.git
```

Push the local content to the remote server:

```bash
git push -u origin main
```

Afterward, simply run `git push` to synchronize later updates.

---

## Cloning Another Project to Contribute

To contribute to someone else's open-source project, the usual workflow is to fork the original project to your account, then clone the fork to your computer and modify it.

### Click the "Fork" Button on the Website to Create a Copy

Then clone your fork to your computer:

```bash
git clone https://github.com/yourusername/forked-repo-name.git
cd forked-repo-name
```

Configure the upstream remote so that you can fetch changes from the original project:

```bash
git remote add upstream https://github.com/original-owner/original-repo-name.git
```

Regularly fetch upstream changes to stay synchronized:

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

---

## Frequently Asked Questions and Best Practices

### How Do I Undo a Commit?

Undo only the commit without affecting working-tree files:

```bash
git reset --soft HEAD~1
```

Discard the commit and restore the file changes completely:

```bash
git reset --hard HEAD~1
```

### How Do I Keep Sensitive Files from Being Tracked?

Create a `.gitignore` file and list the name patterns of objects that should not be included in version control, for example:

```text
node_modules/
.env
*.log
build/
dist/
```

### How Do I Share SSH Keys Safely?

Never disclose a private key. Each person should generate a separate key pair and upload only the public-key portion to the relevant platform's authentication system.
