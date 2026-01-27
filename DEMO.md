# 演示指南 🎬

## 🚀 快速演示（在电脑上测试）

### 1. 安装依赖

```bash
cd ~/climate-android
pip3 install -r requirements.txt
```

### 2. 配置 API Key

```bash
python3 agent.py --setup
```

按提示输入：
- 选择 `1` (Claude)
- 输入你的 Claude API Key
- 安全确认选 `Y`

### 3. 测试单次命令

```bash
# 列出文件
python3 agent.py --once "列出当前目录的所有文件"

# 系统信息
python3 agent.py --once "查看系统资源使用情况"

# 创建文件
python3 agent.py --once "帮我创建一个 Python 文件 test.py，内容是打印 Hello World"
```

### 4. 交互模式

```bash
python3 agent.py
```

然后输入：

```
你: 帮我查看当前目录
你: 创建一个文件夹叫 demo
你: 在 demo 文件夹中创建一个 hello.py
你: 运行这个 Python 文件
你: exit  # 退出
```

## 📱 在 Android 上测试

### 准备工作

1. 在 F-Droid 安装 Termux
2. 打开 Termux

### 传输文件到 Android

#### 方法 1：通过 HTTP 服务器（推荐）

**在电脑上：**
```bash
cd ~/climate-android
python3 -m http.server 8000
```

**在手机 Termux 中：**
```bash
# 确保手机和电脑在同一 WiFi
pkg update && pkg install python git wget

# 下载项目（替换为你的电脑 IP）
mkdir -p ~/climate-android
cd ~/climate-android

wget http://192.168.1.100:8000/agent.py
wget http://192.168.1.100:8000/config.py
wget http://192.168.1.100:8000/requirements.txt
wget http://192.168.1.100:8000/README.md

# 下载 tools 目录
mkdir -p tools llm
wget http://192.168.1.100:8000/tools/bash.py -O tools/bash.py
wget http://192.168.1.100:8000/tools/file.py -O tools/file.py
wget http://192.168.1.100:8000/tools/system.py -O tools/system.py
wget http://192.168.1.100:8000/llm/claude.py -O llm/claude.py
```

#### 方法 2：通过 USB 传输

1. 将手机连接到电脑
2. 复制 `climate-android` 文件夹到手机
3. 在 Termux 中访问：
   ```bash
   cd ~/storage/shared/Download/climate-android
   ```

#### 方法 3：通过 Git (如果有访问权限)

```bash
cd ~
git clone https://github.com/your-repo/climate-android.git
cd climate-android
```

### 安装和运行

```bash
# 安装依赖
pip install -r requirements.txt

# 配置
python agent.py --setup

# 运行
python agent.py
```

## 🎯 演示场景

### 场景 1：文件管理

```
你: 列出当前目录所有 Python 文件
🤖: [执行 ls *.py]

你: 创建一个备份脚本 backup.sh
🤖: [创建 shell 脚本]

你: 压缩 Documents 目录
🤖: [执行 tar 命令]
```

### 场景 2：系统监控

```
你: 查看 CPU 和内存使用率
🤖: [显示资源使用情况]

你: 检查电池电量
🤖: [显示电池状态]

你: 查看磁盘空间
🤖: [显示磁盘使用]
```

### 场景 3：开发任务

```
你: 初始化一个 Python 项目
🤖: [创建目录、虚拟环境、requirements.txt]

你: 安装 requests 和 beautifulsoup4
🤖: [执行 pip install]

你: 写一个爬虫获取网页标题
🤖: [创建 scraper.py 并运行]
```

### 场景 4：自动化

```
你: 创建一个脚本，每小时检查一次磁盘空间
🤖: [创建定时脚本]

你: 写一个脚本监控日志文件，发现 ERROR 就通知
🤖: [创建监控脚本]
```

## 🎬 录屏演示脚本

### 开场（30秒）

```
[画面：手机屏幕]
旁白：这是一部普通的 Android 手机
[打开 Termux]
旁白：但装了 Termux 和我们的 CLI Agent 后...
[启动 agent]
旁白：它变成了一个强大的生产力工具！
```

### Demo 1：快速操作（1分钟）

```
输入：帮我查看系统信息
[展示输出]

输入：列出当前目录的 Python 文件
[展示输出]

输入：创建一个 hello.py 文件
[文件被创建]

输入：运行它
[显示 "Hello World"]
```

### Demo 2：复杂任务（2分钟）

```
输入：帮我写一个天气查询脚本
[Agent 创建 weather.py]

输入：运行这个脚本
[显示当地天气]

输入：把结果保存到文件
[保存完成]
```

### Demo 3：系统监控（1分钟）

```
输入：查看资源使用情况
[显示 CPU、内存、磁盘、电池]

输入：如果磁盘占用超过 80% 就清理缓存
[创建脚本]
```

### 结尾（30秒）

```
旁白：不需要记命令
旁白：不需要查文档
旁白：只需要告诉 AI 你想做什么
旁白：手机 CLI Agent - 让 Android 成为生产力工具！
```

## 📊 性能测试

### 测试命令响应时间

```bash
time python3 agent.py --once "查看系统信息"
```

### 测试资源占用

```bash
# 启动 Agent
python3 agent.py

# 在另一个终端查看
ps aux | grep python
top -p $(pgrep -f agent.py)
```

## 🐛 调试模式

如果遇到问题，可以添加调试输出：

```python
# 在 agent.py 开头添加
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 💡 提示

1. **网络延迟** - API 调用需要 1-3 秒
2. **API 费用** - 每次对话消耗 tokens
3. **电量消耗** - 长时间使用会耗电
4. **后台限制** - Android 可能杀死后台进程

## 🎓 学习资源

- 阅读源码理解工作原理
- 修改工具添加新功能
- 扩展支持更多 LLM
- 集成更多 Android API

---

**准备好演示了吗？开始展示你的 CLImate-Android！** 🚀
