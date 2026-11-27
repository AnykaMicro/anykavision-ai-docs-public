# Git操作指南

本指南旨在帮助初学者掌握 Git 的基本操作，并了解如何通过 Git 参与到开源项目中。我们将从安装配置开始，逐步介绍本地仓库管理、远程协作。

---

## 简介

Git 是一个分布式版本控制系统，广泛用于代码管理和团队协作。它允许你追踪文件的变更历史，并支持多人同时在不同分支上工作。

---

## 安装和配置 Git

### 安装 Git

- **Windows**：访问 [git-scm.com](https://git-scm.com/) 下载安装程序并运行。
- **macOS**：

  ```bash
  brew install git
  ```

- **Linux (Ubuntu/Debian)**：

  ```bash
  sudo apt update
  sudo apt install git
  ```

### 配置用户信息

首次使用前需要设置用户名和邮箱：

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

查看当前配置：

```bash
git config --list
```

---

## 创建本地仓库

进入你的项目目录后执行以下命令初始化 Git 仓库：

```bash
cd your_project_folder
git init
```

添加文件至暂存区并提交第一次更改：

```bash
git add .
git commit -m "Initial commit"
```

---

## 日常开发操作

### 查看状态

```bash
git status
```

### 添加文件到暂存区

添加单个文件或所有修改过的文件：

```bash
git add filename.txt
# 或添加所有修改
git add .
```

### 提交更改

```bash
git commit -m "Describe what you did"
```

### 查看提交历史

```bash
git log
```

或者更简洁地显示每次提交的一行摘要：

```bash
git log --oneline
```

---

## 分支管理

### 列出所有分支

```bash
git branch
```

带星号（`*`）的是当前所在的分支。

### 新建分支

```bash
git checkout -b feature_branch_name
```

这会新建并切换到新的分支。

### 切换分支

```bash
git checkout main
```

切换回主分支或其他已存在的分支。

### 合并分支

将 `feature_branch_name` 合并进当前分支（通常是 `main`）：

```bash
git merge feature_branch_name
```

如果发生冲突，请手动编辑相关文件后再继续合并过程。

### 删除分支

删除本地已完成使命的功能分支：

```bash
git branch -d feature_branch_name
```

要强制删除未完全合并的分支，可使用 `-D` 参数代替 `-d`。

---

## 连接到远程仓库

若你想把本地项目推送到 GitHub/GitLab 等平台托管服务，需先添加远程仓库地址：

```bash
git remote add origin https://github.com/username/repository.git
```

推送本地内容到远程服务器：

```bash
git push -u origin main
```

之后只需简单输入 `git push` 即可同步后续更新。

---

## 克隆他人项目进行贡献

当你要为别人的开源项目做贡献时，通常做法是 Fork 原始项目到自己的账户下，然后 Clone 到本地环境里修改：

### 在网页端点击 "Fork" 按钮生成副本

接着 clone 自己 fork 出来的副本到本地计算机：

```bash
git clone https://github.com/yourusername/forked-repo-name.git
cd forked-repo-name
```

设置上游源以便随时获取原始项目的最新改动：

```bash
git remote add upstream https://github.com/original-owner/original-repo-name.git
```

定期从上游拉取新变化以保持同步：

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

---

## 常见问题与最佳实践

### 如何撤销某个 commit？

只撤销 commit 不影响工作区文件：

```bash
git reset --soft HEAD~1
```

彻底清除 commit 并还原文件变动：

```bash
git reset --hard HEAD~1
```

### 忽略某些敏感文件不被追踪怎么办？

创建 `.gitignore` 文件列出不想纳入版本控制的对象名称模式即可，例如：

```text
node_modules/
.env
*.log
build/
dist/
```

### 怎样安全共享 SSH 密钥？

避免把私钥泄露给他人！应该各自生成独立密钥对并上传公钥部分到对应平台认证系统内。
