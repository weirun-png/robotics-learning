# Linux 命令行学习笔记

**学习时间：** 2026-03-04  
**主题：** Linux 基础命令系统学习  
**状态：** ✅ 已完成

---

## 📚 1. 文件查看与操作

### 1.1 查看文件内容

| 命令 | 说明 | 示例 |
|------|------|------|
| `cat` | 显示文件全部内容 | `cat README.md` |
| `head -n N` | 显示文件前 N 行 | `head -n 3 README.md` |
| `tail -n N` | 显示文件最后 N 行 | `tail -n 3 README.md` |
| `tail -f` | 实时监控文件新增内容 | `tail -f logfile.log` |

**注意事项：**
- `tail -f` 用于查看日志，按 `Ctrl+C` 退出
- 大文件建议用 `less` 分页查看

---

### 1.2 复制、移动、删除

| 命令 | 说明 | 示例 |
|------|------|------|
| `cp` | 复制文件 | `cp file1 file2` |
| `mv` | 移动/重命名文件 | `mv old.txt new.txt` |
| `rm` | 删除文件 | `rm file.txt` |
| `rm -f` | 强制删除（不提示） | `rm -f file.txt` |

**常见错误与解决：**

```bash
# 错误 1：源文件不存在
cp file1 file2
# 报错：cannot stat 'file1': No such file or directory
# 解决：先确认文件存在 ls file1

# 错误 2：源文件和目标文件相同
mv ~/robotics-plc-learning /home/xiaoweirun/
# 报错：'...' and '...' are the same file
# 解决：无需移动，或指定新名称

# 错误 3：路径错误
mv /file3.txt /home/xiaoweirun/
# 报错：cannot stat '/file3.txt': No such file or directory
# 解决：检查路径，文件可能在当前目录而非根目录
```

---

## 📁 2. 目录操作

### 2.1 创建目录

```bash
# 创建单个目录
mkdir new_folder

# 递归创建多级目录（常用）
mkdir -p linux_practice/sub1/sub2

# 显示创建过程（加 -v 选项）
mkdir -pv linux_practice/sub1/sub2

# 利用花括号扩展一次性创建复杂结构
mkdir -p challenge/{src,docs,tests}/{module1,module2}
```

**生成的目录结构：**
```
challenge/
├── src/
│   ├── module1/
│   └── module2/
├── docs/
│   ├── module1/
│   └── module2/
└── tests/
    ├── module1/
    └── module2/
```

---

### 2.2 列出目录内容

| 命令 | 说明 | 示例 |
|------|------|------|
| `ls` | 简单列出 | `ls` |
| `ls -l` | 详细信息 | `ls -l` |
| `ls -a` | 包括隐藏文件 | `ls -a` |
| `ls -la` | 组合使用（最常用） | `ls -la` |
| `ls -lh` | 人类可读大小 | `ls -lh` |
| `ls -R` | 递归列出 | `ls -R xiaoweirun` |

**常见错误：**

```bash
# 错误：路径理解错误
ls ~/*.txt
# 报错：No such file or directory
# 原因：~ 是主目录 (/home/xiaoweirun)，不是当前目录

# 正确做法：
ls *.txt                              # 当前目录
ls ~/robotics-plc-learning/*.txt      # 指定完整路径
```

---

### 2.3 删除目录

```bash
# 删除空目录
rmdir empty_dir

# 递归删除非空目录（慎用！）
rm -r dir_name

# 强制删除（不提示，危险！）
rm -rf dir_name

# 交互确认（安全）
rm -ri dir_name
```

⚠️ **警告：** `rm -rf` 删除的文件无法恢复！

---

## 🔍 3. 查找与过滤

### 3.1 查找文件

```bash
# 按名称查找
find . -name "*.py"                   # 查找所有.py 文件
find . -name "day*.md"                # 查找 day 开头的 md 文件

# 按类型查找
find . -type f                        # 只查找文件
find . -type d                        # 只查找目录

# 组合使用
find . -type f -name "*.txt"          # 查找所有.txt 文件

# 查找并执行命令
find logs/ -name "*.md" -exec cat {} \;  # 查找并显示内容

# 统计文件数量
find . -name "*.md" | wc -l           # 统计 md 文件数量
```

---

### 3.2 过滤输出

```bash
# grep 过滤
ls -la | grep "txt"                   # 筛选包含 txt 的行
grep -r "Python" logs/                # 递归搜索

# head/tail 过滤
cat README.md | head -n 5             # 显示前 5 行
cat README.md | tail -n 5             # 显示最后 5 行

# wc 统计
find . -name "*.py" | wc -l           # 统计.py 文件数量
```

---

## 🔗 4. 管道与重定向

### 4.1 管道 `|`

**作用：** 将前一个命令的输出作为后一个命令的输入

```bash
# 示例 1：统计文件数
find . -name "*.md" | wc -l

# 示例 2：过滤列表
ls -la | grep "txt"

# 示例 3：查看前 N 行
cat README.md | head -n 5
```

---

### 4.2 重定向

| 符号 | 说明 | 示例 |
|------|------|------|
| `>` | 输出重定向（覆盖） | `echo "Hello" > file.txt` |
| `>>` | 输出重定向（追加） | `echo "World" >> file.txt` |
| `2>/dev/null` | 丢弃错误信息 | `ls /nonexistent 2>/dev/null` |

**组合使用：**

```bash
# 优先用 tree，失败则用 ls -R
tree challenge 2>/dev/null || ls -R challenge

# 解释：
# 1. 尝试运行 tree challenge
# 2. 如果失败（tree 未安装），错误被丢弃
# 3. || 表示"或"，执行 ls -R challenge
```

---

## ❌ 5. 常见错误与排查

### 5.1 命令拼写错误

```bash
# 错误 1：中文引号
grep "机器人" README.md          # ❌ 中文引号
grep "机器人" README.md          # ✅ 英文引号

# 错误 2：大小写错误
Is -R challenge                   # ❌ 大写 i
ls -R challenge                   # ✅ 小写 L

# 错误 3：目录名拼写错误
ls -R chanllenge                  # ❌ 拼写错误
ls -R challenge                   # ✅ 正确
```

---

### 5.2 路径理解错误

```bash
# 问题：找不到文件
ls ~/*.txt
# 报错：No such file or directory

# 原因：~ 是主目录，文件可能在当前目录

# 解决：
ls *.txt                              # 当前目录
ls ~/robotics-plc-learning/*.txt      # 明确路径
```

---

### 5.3 移动文件错误

```bash
# 问题：源文件已在目标位置
mv ~/robotics-plc-learning /home/xiaoweirun/
# 报错：'...' and '...' are the same file

# 解决：无需移动，或指定新名称
mv ~/robotics-plc-learning ~/new-name
```

---

## 🔧 6. Git 状态信息

```bash
git status
```

**典型输出：**
```
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

**解读：**
- ✅ 当前在 `master` 分支
- ✅ 本地与远程分支同步
- ✅ 工作目录和暂存区无未提交更改

---

## 📄 7. 特殊文件

### `.hushlogin`

**作用：** 登录时不显示系统欢迎信息（MOTD、上次登录时间等）

```bash
# 创建
touch ~/.hushlogin

# 删除
rm ~/.hushlogin
```

---

## 🎯 8. 组合命令示例

### 示例 1：目录树显示
```bash
tree challenge 2>/dev/null || ls -R challenge
```

### 示例 2：批量创建文件
```bash
touch challenge/src/module1/{file1,file2,file3}.py
```

### 示例 3：查找并统计
```bash
find . -name "*.py" | wc -l
```

### 示例 4：搜索并查看
```bash
grep -r "Python" logs/ | head -n 10
```

---

## 💡 重要概念总结

### 1. 路径概念

| 路径 | 含义 | 示例 |
|------|------|------|
| `~` | 用户主目录 | `/home/xiaoweirun` |
| `.` | 当前目录 | `./file.txt` |
| `..` | 上级目录 | `../file.txt` |
| `/` | 根目录 | `/home/xiaoweirun` |

---

### 2. 通配符

| 符号 | 含义 | 示例 |
|------|------|------|
| `*` | 匹配任意字符 | `*.txt` |
| `?` | 匹配单个字符 | `file?.txt` |
| `[]` | 匹配字符范围 | `file[1-3].txt` |

---

### 3. Unix 哲学

- ✅ **静默原则：** 成功时无输出，错误时有提示
- ✅ **组合使用：** 用小命令组合完成复杂任务
- ✅ **管道思维：** 一个命令的输出是另一个命令的输入

---

## 📝 实践检查清单

- [ ] 能用 `pwd` 显示当前路径
- [ ] 能用 `ls -la` 列出所有文件
- [ ] 能用 `cd` 切换目录
- [ ] 能用 `mkdir -p` 创建多级目录
- [ ] 能用 `touch` 创建文件
- [ ]  复制文件
- [ ] 能用 `mv` 移动/重命名文件
- [ ] 能用 `rm` 删除文件（谨慎）
- [ ] 能用 `cat`、`less`、`head`、`tail` 查看文件
- [ ] 能用 `grep` 搜索文本
- [ ] 能用 `find` 查找文件
- [ ] 理解通配符 `*`、`?`、`[]`
- [ ] 理解重定向 `>`、`>>`、`2>/dev/null`
- [ ] 理解管道 `|` 的用法

---

## 🔗 参考资源

- `man` 命令：`man ls`、`man grep` 等
- GNU Coreutils 文档：https://www.gnu.org/software/coreutils/manual/
- Linux 命令大全：https://wangchujiang.com/linux-command/

---

**下次更新：** 2026-03-05  
**复习计划：** 每周复习一次，直到熟练掌握
