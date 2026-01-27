# CLImate-Android 快速参考 🚀

## 📦 一键安装

```bash
# Android (Termux)
pkg update && pkg install python git
cd ~
# 下载项目文件
pip install anthropic psutil
python agent.py --setup
python agent.py
```

## 🎯 常用命令

### 配置
```bash
python agent.py --setup      # 首次配置
python agent.py --once "..."  # 执行单次命令
python agent.py              # 交互模式
```

### 交互模式快捷键
```
exit / quit / q     # 退出
clear              # 清除对话历史
Ctrl+C             # 中断当前操作
```

## 💬 示例对话

### 文件操作
```
列出当前目录的文件
读取 config.py 的内容
创建一个文件 test.txt，内容是 Hello
删除 test.txt
```

### 系统信息
```
查看系统信息
查看 CPU 和内存使用率
查看磁盘空间
检查电池电量
```

### 开发任务
```
初始化一个 Python 项目
安装 requests 库
创建一个爬虫脚本
运行 main.py
```

### Shell 命令
```
ping google.com 测试网络
查找所有 .py 文件
压缩当前目录
上传文件到服务器
```

## 🛠️ 工具列表

| 工具 | 功能 | 示例 |
|------|------|------|
| `execute_bash` | 执行命令 | "运行 ls -la" |
| `read_file` | 读取文件 | "读取 README.md" |
| `write_file` | 写入文件 | "创建 hello.py" |
| `list_files` | 列出文件 | "列出所有 .txt" |
| `get_system_info` | 系统信息 | "查看系统版本" |
| `get_resource_usage` | 资源监控 | "查看 CPU" |
| `get_current_directory` | 当前目录 | "我在哪个目录" |

## ⚙️ 配置文件

位置：`~/.climate-android/config.json`

```json
{
  "llm_provider": "claude",
  "api_keys": {
    "claude": "sk-ant-..."
  },
  "model": "claude-3-5-sonnet-20241022",
  "safety": {
    "require_confirmation": true
  }
}
```

## 🔧 常见问题

### Q: 如何修改 API Key?
```bash
vim ~/.climate-android/config.json
# 或
python agent.py --setup
```

### Q: 如何添加新工具?
1. 在 `tools/` 目录创建 `new_tool.py`
2. 实现工具类和方法
3. 在 `agent.py` 中注册工具

### Q: 如何在后台运行?
```bash
# 使用 tmux
tmux new -s agent
python agent.py
# Ctrl+B, D 分离

# 重新连接
tmux attach -t agent
```

### Q: 遇到网络错误?
```bash
# 检查网络
ping anthropic.com

# 检查 API Key
cat ~/.climate-android/config.json | grep claude

# 测试 API
curl -H "x-api-key: YOUR_KEY" https://api.anthropic.com/v1/messages
```

## 🎯 最佳实践

### 1. 明确需求
```
❌ "帮我查一下"
✅ "查看当前目录下所有 Python 文件"
```

### 2. 分步骤操作
```
❌ "帮我部署项目到服务器"
✅ "连接到服务器"
   "上传文件"
   "安装依赖"
   "启动服务"
```

### 3. 确认危险操作
```
你: 删除所有临时文件
Agent: ⚠️ 这是一个危险命令！
       是否继续? (yes/no):
```

## 📱 Termux 技巧

### 外接键盘
- `Tab` - 自动补全
- `Ctrl+C` - 中断
- `Ctrl+D` - 退出
- `↑/↓` - 历史命令

### 快捷访问
```bash
# 添加别名
echo 'alias agent="cd ~/climate-android && python agent.py"' >> ~/.bashrc

# 使用
agent
```

### 保持后台
```bash
# 使用 tmux
pkg install tmux
tmux new -s agent
python agent.py
```

## 🔋 省电建议

1. 不用时退出 Agent
2. 避免长时间运行
3. 使用 WiFi 而非移动数据
4. 关闭不必要的工具

## 📊 性能指标

- 启动时间：< 2 秒
- 响应延迟：1-3 秒
- 内存占用：~50MB
- 电量消耗：< 5%/小时

## 🆘 获取帮助

```bash
# 查看帮助
python agent.py --help

# 查看文档
cat README.md
cat 安装指南-Android.md

# GitHub Issues
# https://github.com/your-repo/climate-android/issues
```

## 🔗 快速链接

- [完整文档](README.md)
- [安装指南](安装指南-Android.md)
- [演示指南](DEMO.md)
- [项目总结](项目总结.md)

---

**记住：用人话说就行，Agent 会帮你搞定！** 💪
