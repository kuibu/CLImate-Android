# CLImate-Android 🐍

**English | [简体中文](./README.md)**

> *A snake navigating the system depths, striking at the right spots for you.*

An AI-powered mobile CLI Agent similar to Claude Code, allowing you to control your Android phone with natural language!

## 🐍 About the Mascot

Our mascot is a snake - symbolizing an intelligent agent that:
- **Navigates system depths** - Moves through complex file systems and processes
- **Strikes precisely** - Executes exactly what you need, when you need it
- **Adapts and learns** - Understands your intent through natural language
- **Silent but powerful** - Works efficiently in the background

Just like a snake, CLImate-Android is agile, precise, and always finds the right path to accomplish your tasks.

## ✨ Features

- 🗣️ **Natural Language Interaction** - Control with plain English
- 🔧 **Tool Calling** - Automatic execution of shell commands, file operations
- 🛡️ **Safety Mechanisms** - Dangerous command confirmation required
- 📱 **Mobile Optimized** - Designed specifically for Termux
- 🔋 **Resource Monitoring** - Real-time CPU, memory, battery tracking

## 🚀 Quick Start

### 1. Install Termux on Android

Download Termux from [F-Droid](https://f-droid.org/) (NOT from Google Play, which is outdated)

### 2. Install Python and Dependencies

```bash
# Update package manager
pkg update && pkg upgrade

# Install Python
pkg install python git

# Clone or transfer project files
cd ~
# ... transfer files to phone

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

```bash
# Run configuration wizard
python agent.py --setup

# Follow prompts:
# 1. Select LLM provider (Claude)
# 2. Enter API Key
# 3. Configure safety options
```

### 4. Start Using

```bash
# Start Agent
python agent.py

# Or execute single command
python agent.py --once "list all files in current directory"
```

## 💬 Usage Examples

### Basic Commands

```
You: List all files in current directory
🤖: [Executes ls -la]

You: Check system information
🤖: [Shows CPU, memory, battery status]

You: Create a Python script hello.py
🤖: [Creates file and writes content]
```

### Complex Tasks

```
You: Install requests library and write a web scraper
🤖:
   1. Execute pip install requests
   2. Create scraper.py
   3. Run script
   4. Display results

You: Backup Documents directory to backup.tar.gz
🤖: [Executes tar command to compress files]

You: Monitor CPU usage, notify if exceeds 80%
🤖: [Creates monitoring script and runs it]
```

### Development Tasks

```
You: Initialize a Python project with virtual environment
🤖: [Creates directory structure, venv, config files]

You: Run tests and tell me which ones failed
🤖: [Executes pytest and analyzes results]

You: Deploy my Flask app to server
🤖: [SSH connect, upload files, start service]
```

## 🔧 Available Tools

### 1. Shell Command Execution
```python
execute_bash(command: str, timeout: int = 30)
```
Execute any shell command with automatic safety checks.

### 2. File Operations
```python
read_file(file_path: str, max_lines: int = 1000)
write_file(file_path: str, content: str)
list_files(directory: str, pattern: str = "*")
```

### 3. System Information
```python
get_system_info()        # System version, architecture, etc.
get_resource_usage()     # CPU, memory, disk, battery
get_current_directory()  # Current path
```

## ⚙️ Configuration File

Located at: `~/.climate-android/config.json`

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

## 🛡️ Safety Mechanisms

1. **Dangerous Command Detection** - Auto-identifies risky operations
2. **Confirmation System** - User confirmation required before execution
3. **Command Blacklist** - Block specific commands
4. **Timeout Protection** - Auto-terminate commands after timeout

### Dangerous Command Examples

```bash
rm -rf /          # ❌ Blocked
dd if=/dev/zero   # ❌ Blocked
chmod -R 777 /    # ⚠️ Requires confirmation
```

## 📱 Termux Optimization

### Background Running

```bash
# Use tmux to maintain session
pkg install tmux
tmux new -s agent
python agent.py

# Detach session: Ctrl+B, D
# Reattach: tmux attach -t agent
```

### Auto-start on Boot (requires Termux:Boot)

```bash
mkdir -p ~/.termux/boot
cat > ~/.termux/boot/start-agent.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/sh
termux-wake-lock
cd ~/climate-android
python agent.py --once "System started"
EOF
chmod +x ~/.termux/boot/start-agent.sh
```

### Quick Launch Alias

```bash
# Add alias to ~/.bashrc
echo 'alias agent="cd ~/climate-android && python agent.py"' >> ~/.bashrc
source ~/.bashrc

# Usage
agent
```

## 🎯 Real-world Use Cases

### 1. System Administration

```
Monitor disk space, clean cache when less than 1GB
Scheduled backup of important files to cloud
Check battery level, close power-hungry apps when below 20%
```

### 2. Development Work

```
Quickly create project templates
Run tests and generate reports
Deploy applications to servers
Monitor log files
```

### 3. Automation Tasks

```
Scheduled file downloads
Batch rename files
Data scraping and processing
Scheduled notifications
```

### 4. Emergency Operations

```
SSH to server to fix issues
Quick server status check
Restart crashed services
Execute emergency scripts
```

## 🔮 Future Plans

- [ ] Support more LLMs (OpenAI, Gemini, local models)
- [ ] Long-term memory and context persistence
- [ ] Task scheduling and timed execution
- [ ] Deep integration with Android system (notifications, clipboard)
- [ ] Web UI interface
- [ ] Multi-agent collaboration
- [ ] Plugin system

## 📊 Performance

| Metric | Value |
|--------|-------|
| Startup time | < 2 seconds |
| Memory usage | ~50MB |
| Response latency | ~1-3 seconds (depends on network) |
| Power consumption | < 5%/hour with light use |

## ⚠️ Known Limitations

1. **Network Dependency** - Requires stable network (unless using local model)
2. **API Costs** - Claude API charged per usage
3. **Permission Limits** - Some system operations require root
4. **Background Limits** - Android may kill background processes
5. **Power Consumption** - Frequent use drains battery

## 🤝 Contributing

Issues and PRs welcome!

## 📄 License

MIT License

## 🙏 Acknowledgments

Inspired by:
- Claude Code
- Termux
- Android CLI ecosystem

---

**Make your Android phone a productivity tool!** 🚀
