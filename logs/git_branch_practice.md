# Git 分支操作实践笔记

**时间：** 2026-03-04  
**主题：** Git 分支操作  
**状态：** ✅ 已完成

---

## 📚 核心概念

### 什么是分支？
- 分支是 Git 的"平行宇宙"
- 可以在分支上随意实验，不影响主分支
- 实验完成后合并到主分支

### 分支策略
- `master`：主分支，保持稳定
- `feature-xxx`：功能分支，开发新功能
- `bugfix-xxx`：修复分支，修复 bug

---

## 🎯 常用命令

### 1. 查看分支
```bash
git branch              # 查看所有分支
git branch --show-current  # 显示当前分支
```

### 2. 创建分支
```bash
git branch feature-name     # 创建分支
git checkout -b feature-name # 创建并切换
```

### 3. 切换分支
```bash
git checkout master         # 切换到 master
git checkout feature-name   # 切换到功能分支
```

### 4. 合并分支
```bash
git checkout master         # 先切换到目标分支
git merge feature-name      # 合并功能分支
```

### 5. 推送分支
```bash
git push origin feature-name  # 推送分支到远程
```

---

## 💡 实践记录

### 第一次分支操作
- **分支名：** feature-git-practice
- **目的：** 学习 Git 分支操作
- **操作：**
  1. 创建分支：`git checkout -b feature-git-practice`
  2. 创建学习笔记
  3. 提交并合并到 master

---

## ✅ 关键要点
1. master 分支保持稳定
2. 新功能在 feature 分支开发
3. 开发完成后合并到 master
4. 推送时也要推送分支

---

## ❓ 常见问题

### Q1: 合并冲突怎么办？
A: Git 会标记冲突文件，手动编辑解决后重新提交

### Q2: 如何删除分支？
A: `git branch -d feature-name`（已合并）或 `git branch -D`（强制）

### Q3: 如何回退到之前的版本？
A: `git reset --hard commit_id`（慎用！）
