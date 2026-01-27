# CLImate-Android 🐍

> *一条在系统底层游走的蛇，替你咬住该咬的地方。*

类似 Claude Code 的移动端 CLI Agent，让你用自然语言控制 Android 手机！

## 🐍 关于吉祥物

我们的吉祥物是一条蛇——象征着智能代理：
- **游走于系统底层** - 穿梭于复杂的文件系统和进程之间
- **精准出击** - 在你需要的时候，执行你需要的操作
- **适应学习** - 通过自然语言理解你的意图
- **静默而强大** - 在后台高效工作

就像蛇一样，CLImate-Android 敏捷、精准，总能找到完成任务的正确路径。

## ✨ 特性

- 🗣️ **自然语言交互** - 用人话下命令
- 🔧 **工具调用** - 自动执行 shell 命令、读写文件
- 🛡️ **安全机制** - 危险命令需要确认
- 📱 **移动优化** - 专为 Termux 设计
- 🔋 **资源监控** - 实时查看 CPU、内存、电池

## 🚀 快速开始

### 1. 在 Android 上安装 Termux

从 [F-Droid](https://f-droid.org/) 下载 Termux（不要用 Google Play 版本）

### 2. 安装 Python 和依赖

```bash
# 更新包管理器
pkg update && pkg upgrade

# 安装 Python
pkg install python git

# 克隆项目（或手动传输文件）
git clone https://github.com/your-repo/climate-android.git
cd climate-android

# 安装依赖
pip install -r requirements.txt
```

### 3. 配置

```bash
# 运行配置向导
python agent.py --setup

# 按提示输入：
# 1. 选择 LLM 提供商（Claude）
# 2. 输入 API Key
# 3. 配置安全选项
```

### 4. 开始使用

```bash
# 启动 Agent
python agent.py

# 或者执行单次命令
python agent.py --once "查看当前目录下的文件"
```

## 💬 使用示例

### 基础命令

```
你: 列出当前目录的所有文件
🤖: [执行 ls -la]

你: 查看系统信息
🤖: [显示 CPU、内存、电池状态]

你: 帮我创建一个 Python 脚本 hello.py
🤖: [创建文件并写入内容]
```

### 复杂任务

```
你: 安装 requests 库并写个爬虫获取百度首页
🤖:
   1. 执行 pip install requests
   2. 创建 scraper.py
   3. 运行脚本
   4. 显示结果

你: 帮我备份 Documents 目录到 backup.tar.gz
🤖: [执行 tar 命令压缩文件]

你: 监控 CPU 使用率，如果超过 80% 就通知我
🤖: [创建监控脚本并运行]
```

### 开发任务

```
你: 初始化一个 Python 项目，包含虚拟环境和 requirements.txt
🤖: [创建目录结构、虚拟环境、配置文件]

你: 运行测试并告诉我哪些失败了
🤖: [执行 pytest 并分析结果]

你: 部署我的 Flask 应用到服务器
🤖: [SSH 连接、上传文件、启动服务]
```

## 🔧 可用工具

### 1. Shell 命令执行
```python
execute_bash(command: str, timeout: int = 30)
```
执行任何 shell 命令，自动安全检查。

### 2. 文件操作
```python
read_file(file_path: str, max_lines: int = 1000)
write_file(file_path: str, content: str)
list_files(directory: str, pattern: str = "*")
```

### 3. 系统信息
```python
get_system_info()        # 系统版本、架构等
get_resource_usage()     # CPU、内存、磁盘、电池
get_current_directory()  # 当前路径
```

## ⚙️ 配置文件

配置保存在 `~/.climate-android/config.json`

```json
{
  "llm_provider": "claude",
  "api_keys": {
    "claude": "your-api-key"
  },
  "model": "claude-3-5-sonnet-20241022",
  "max_tokens": 4096,
  "safety": {
    "require_confirmation": true,
    "blocked_commands": ["rm -rf /", "dd if="]
  }
}
```

## 🛡️ 安全机制

1. **危险命令检测** - 自动识别危险操作
2. **确认机制** - 执行前需要用户确认
3. **命令黑名单** - 禁止特定命令
4. **超时保护** - 命令执行超时自动终止

### 危险命令示例

```bash
rm -rf /          # ❌ 禁止
dd if=/dev/zero   # ❌ 禁止
chmod -R 777 /    # ⚠️ 需要确认
```

## 📱 Termux 优化

### 后台运行

```bash
# 使用 tmux 保持会话
pkg install tmux
tmux new -s agent
python agent.py

# 分离会话: Ctrl+B, D
# 重新连接: tmux attach -t agent
```

### 开机自启（需要 Termux:Boot）

```bash
mkdir -p ~/.termux/boot
cat > ~/.termux/boot/start-agent.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/sh
termux-wake-lock
cd ~/climate-android
python agent.py --once "系统已启动"
EOF
chmod +x ~/.termux/boot/start-agent.sh
```

### 快捷启动

```bash
# 添加别名到 ~/.bashrc
echo 'alias agent="cd ~/climate-android && python agent.py"' >> ~/.bashrc
source ~/.bashrc

# 使用
agent
```

## 🎯 实际应用场景

### 1. 系统管理

```
监控磁盘空间，不足 1GB 时清理缓存
定时备份重要文件到云端
检查电池电量，低于 20% 时关闭耗电应用
```

### 2. 开发工作

```
快速创建项目模板
运行测试并生成报告
部署应用到服务器
监控日志文件
```

### 3. 自动化任务

```
定时下载文件
批量重命名文件
数据爬取和处理
定时发送通知
```

### 4. 应急操作

```
SSH 连接服务器修复问题
快速查看服务器状态
重启崩溃的服务
执行紧急脚本
```

## 🔮 未来计划

- [ ] 支持更多 LLM（OpenAI、Gemini、本地模型）
- [ ] 长期记忆和上下文保持
- [ ] 任务调度和定时执行
- [ ] 与 Android 系统深度集成（通知、剪贴板）
- [ ] Web UI 界面
- [ ] 多 Agent 协作
- [ ] 插件系统

## 📊 性能

| 维度 | 数据 |
|------|------|
| 启动时间 | < 2 秒 |
| 内存占用 | ~50MB |
| 响应延迟 | ~1-3 秒（取决于网络） |
| 电量消耗 | 轻度使用 < 5%/小时 |

## ⚠️ 已知限制

1. **网络依赖** - 需要稳定的网络连接（除非使用本地模型）
2. **API 费用** - Claude API 按使用量计费
3. **权限限制** - 某些系统操作需要 root
4. **后台限制** - Android 可能杀死后台进程
5. **电量消耗** - 频繁使用会消耗电量

## 🤝 贡献

欢迎提交 Issue 和 PR！

## 📄 License

MIT License

## 🙏 致谢

灵感来源于：
- Claude Code
- Termux
- Android CLI 生态

---

**让 Android 手机成为生产力工具！** 🚀
