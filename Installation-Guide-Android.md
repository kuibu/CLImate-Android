# Android 安装指南 📱

详细的 Android / Termux 安装步骤

## 📋 前置要求

- Android 7.0+ (推荐 Android 10+)
- 至少 500MB 可用存储空间
- 稳定的网络连接

## 📥 第一步：安装 Termux

### 方法 1：F-Droid（推荐）⭐

1. 访问 [F-Droid 官网](https://f-droid.org/)
2. 下载并安装 F-Droid App
3. 在 F-Droid 中搜索 "Termux"
4. 安装 Termux

**为什么不用 Google Play？**
- Google Play 版本已过时（2020 年停更）
- F-Droid 是最新版本

### 方法 2：直接下载 APK

1. 访问 [Termux GitHub Releases](https://github.com/termux/termux-app/releases)
2. 下载最新的 `termux-app_*.apk`
3. 安装 APK（需允许"未知来源"）

## 🔧 第二步：配置 Termux

### 1. 更新软件包

打开 Termux，输入：

```bash
pkg update && pkg upgrade
```

遇到提示按 `Y` 确认。

### 2. 授予存储权限

```bash
termux-setup-storage
```

会弹出权限请求，点击"允许"。

### 3. 安装基础工具

```bash
pkg install python git curl wget vim
```

### 4. 更换国内镜像（可选，加速下载）

```bash
# 清华镜像
sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-main stable main@' $PREFIX/etc/apt/sources.list

pkg update
```

## 📦 第三步：安装 CLImate-Android

### 方法 1：手动创建文件（推荐）

因为你可能没有 GitHub 访问，直接创建项目：

```bash
# 创建项目目录
mkdir -p ~/climate-android
cd ~/climate-android

# 创建目录结构
mkdir -p tools llm

# 接下来复制代码文件...
```

然后按照以下步骤创建每个文件：

#### 1. 创建 requirements.txt

```bash
cat > requirements.txt << 'EOF'
anthropic>=0.40.0
psutil>=5.9.0
EOF
```

#### 2. 创建 config.py

```bash
# 文件太长，建议使用 vim 或传输文件
vim config.py
# 然后粘贴代码
```

**或者使用文件传输：**

```bash
# 在电脑上准备好所有文件
# 通过以下方式传输到手机：

# 方法 1：通过 Python HTTP 服务器
# 电脑上：
cd climate-android
python3 -m http.server 8000

# 手机上（确保同一 WiFi）：
cd ~/climate-android
wget http://电脑IP:8000/config.py
wget http://电脑IP:8000/agent.py
# ... 下载所有文件
```

#### 3. 安装 Python 依赖

```bash
pip install -r requirements.txt
```

如果遇到错误，尝试：

```bash
pip install --upgrade pip
pip install anthropic psutil
```

## ⚙️ 第四步：配置

```bash
python agent.py --setup
```

按照提示输入：
1. 选择 LLM 提供商（输入 `1` 选择 Claude）
2. 输入你的 Claude API Key
3. 配置安全选项（建议选 `Y`）

### 获取 Claude API Key

1. 访问 [Claude Console](https://console.anthropic.com/)
2. 注册/登录账号
3. 进入 API Keys 页面
4. 创建新的 API Key
5. 复制 Key（形如 `sk-ant-...`）

## 🚀 第五步：运行

```bash
python agent.py
```

看到这个界面就成功了：

```
🤖 CLImate-Android 已启动！
💡 输入你的需求，我会帮你执行。输入 'exit' 退出。

👤 你:
```

## 🎯 快速测试

试试这些命令：

```
列出当前目录的文件
查看系统信息
帮我创建一个 hello.py 文件
运行 hello.py
```

## 🔧 常见问题

### 1. 提示 "No module named 'anthropic'"

```bash
pip install anthropic
```

### 2. 权限错误

```bash
# 授予存储权限
termux-setup-storage

# 检查权限
ls ~/storage
```

### 3. 网络连接失败

```bash
# 测试网络
ping google.com

# 检查 API Key
cat ~/.climate-android/config.json
```

### 4. Python 版本过低

```bash
# 查看版本
python --version

# 应该是 3.8+，如果不是：
pkg upgrade python
```

### 5. 内存不足

```bash
# 查看内存
free -h

# 关闭其他应用释放内存
```

## 💡 优化建议

### 1. 安装 Termux:API（增强功能）

```bash
# 在 F-Droid 安装 Termux:API
# 然后在 Termux 中：
pkg install termux-api
```

可以使用：
- `termux-battery-status` - 电池状态
- `termux-notification` - 发送通知
- `termux-clipboard-get` - 剪贴板
- `termux-location` - GPS 定位

### 2. 安装 Termux:Widget（快捷启动）

在桌面添加 Agent 启动快捷方式。

### 3. 安装 tmux（后台运行）

```bash
pkg install tmux

# 创建会话
tmux new -s agent

# 运行 Agent
python agent.py

# 分离会话：Ctrl+B 然后按 D
# 重新连接：
tmux attach -t agent
```

### 4. 创建启动别名

```bash
echo 'alias agent="cd ~/climate-android && python agent.py"' >> ~/.bashrc
source ~/.bashrc

# 以后直接输入：
agent
```

### 5. 外接键盘

连接蓝牙键盘，体验更佳：
- Tab 键自动补全
- Ctrl+C 中断命令
- 方向键历史记录

## 🔋 省电技巧

1. **不用时退出** - 输入 `exit` 退出 Agent
2. **限制后台** - 不需要时不要让 Termux 后台运行
3. **降低轮询频率** - 如果有定时任务，增加间隔
4. **使用 WiFi** - 避免用移动数据

## 📱 推荐硬件

- **外接键盘** - 蓝牙键盘，提升输入体验
- **手机支架** - 解放双手
- **移动电源** - 长时间使用必备
- **Type-C Hub** - 有线键盘 + 充电

## 🎓 学习资源

- [Termux Wiki](https://wiki.termux.com/)
- [Python 官方文档](https://docs.python.org/3/)
- [Claude API 文档](https://docs.anthropic.com/)

## 🆘 获取帮助

遇到问题？

1. 查看 README.md
2. 运行 `python agent.py --help`
3. 提交 GitHub Issue
4. 加入社区讨论

---

**安装完成！开始你的移动 CLI Agent 之旅！** 🚀
