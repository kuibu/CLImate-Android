# CLImate-Android - File Index

Complete file listing for the project.

## 📁 Project Structure

```
climate-android/
├── Core Python Files
│   ├── agent.py                    # Main agent application
│   ├── config.py                   # Configuration management
│   ├── requirements.txt            # Python dependencies
│   │
│   ├── tools/                      # Tool modules
│   │   ├── bash.py                # Shell command execution
│   │   ├── file.py                # File operations
│   │   └── system.py              # System information
│   │
│   └── llm/                        # LLM integrations
│       └── claude.py              # Claude API client
│
├── Documentation (English)
│   ├── README_EN.md               # English README
│   ├── Installation-Guide-Android.md  # Android installation steps
│   ├── Quick-Reference.md         # Quick reference guide
│   ├── Test-Report.md            # Test results report
│   ├── Project-Summary.md        # Technical summary
│   ├── DEMO.md                   # Demo scenarios
│   └── FILE-INDEX.md             # This file
│
├── Documentation (Chinese - 中文)
│   ├── README.md                 # 中文说明
│   ├── 安装指南-Android.md       # 安装指南
│   ├── 快速参考.md               # 快速参考
│   ├── 测试报告.md               # 测试报告
│   └── 项目总结.md               # 项目总结
│
├── Scripts
│   ├── quick-start.sh            # Quick start script (English)
│   └── 快速开始.sh                # 快速开始脚本 (中文)
│
└── Test & Demo Files
    ├── test_tools.py             # Tool testing suite
    ├── demo_offline.py           # Offline demo
    └── hello.py                  # Generated test script
```

## 📚 File Descriptions

### Core Application Files

| File | Description |
|------|-------------|
| `agent.py` | Main CLI agent application with LLM integration |
| `config.py` | Configuration management and setup wizard |
| `requirements.txt` | Python package dependencies |

### Tool Modules (`tools/`)

| File | Description | Tools Provided |
|------|-------------|----------------|
| `bash.py` | Shell command execution with safety checks | `execute_bash` |
| `file.py` | File operations (read, write, list) | `read_file`, `write_file`, `list_files` |
| `system.py` | System information and resource monitoring | `get_system_info`, `get_resource_usage`, `get_current_directory` |

### LLM Integration (`llm/`)

| File | Description |
|------|-------------|
| `claude.py` | Claude API client for chat and tool calling |

### Documentation Files

#### English Documentation

| File | Description | Purpose |
|------|-------------|---------|
| `README_EN.md` | Main English README | Project overview, features, quick start |
| `Installation-Guide-Android.md` | Detailed installation guide | Step-by-step setup for Android/Termux |
| `Quick-Reference.md` | Quick reference guide | Common commands and usage |
| `Test-Report.md` | Testing report | Test results and verification |
| `Project-Summary.md` | Technical summary | Architecture and design decisions |
| `DEMO.md` | Demo scenarios | Usage examples and demonstrations |
| `FILE-INDEX.md` | This file | Complete file listing |

#### Chinese Documentation (中文文档)

| File | Description | Purpose |
|------|-------------|---------|
| `README.md` | 主要说明文档 | 项目概述、功能、快速开始 |
| `安装指南-Android.md` | 详细安装指南 | Android/Termux 安装步骤 |
| `快速参考.md` | 快速参考指南 | 常用命令和使用方法 |
| `测试报告.md` | 测试报告 | 测试结果和验证 |
| `项目总结.md` | 技术总结 | 架构和设计决策 |

### Scripts

| File | Description | Language |
|------|-------------|----------|
| `quick-start.sh` | Quick start script | English |
| `快速开始.sh` | 快速开始脚本 | 中文 |

### Test & Demo Files

| File | Description |
|------|-------------|
| `test_tools.py` | Comprehensive tool testing suite |
| `demo_offline.py` | Offline demo (no API key required) |
| `hello.py` | Auto-generated test script |

## 🌍 Language Support

The project now supports both **English** and **Chinese**:

### English Files
- All Python code with English comments
- Complete English documentation set
- English-named files for international accessibility

### Chinese Files (中文文件)
- Original Chinese documentation preserved
- Chinese-named files for native speakers
- Full feature parity with English version

## 📖 Recommended Reading Order

### For New Users (English)
1. `README_EN.md` - Start here
2. `Installation-Guide-Android.md` - Setup guide
3. `Quick-Reference.md` - Quick commands
4. `DEMO.md` - Usage examples

### For New Users (中文用户)
1. `README.md` - 从这里开始
2. `安装指南-Android.md` - 安装指南
3. `快速参考.md` - 快速命令
4. `DEMO.md` - 使用示例

### For Developers
1. `Project-Summary.md` / `项目总结.md` - Architecture
2. `agent.py` - Main application code
3. `tools/*.py` - Tool implementations
4. `Test-Report.md` / `测试报告.md` - Test coverage

## 🔧 Configuration Files

| File | Location | Description |
|------|----------|-------------|
| `config.json` | `~/.climate-android/config.json` | User configuration (created at runtime) |

## 📊 File Statistics

- **Total Python files:** 9
- **Total documentation files:** 13 (7 English + 6 Chinese)
- **Total scripts:** 2
- **Lines of code:** ~1,500+
- **Documentation pages:** ~50+ pages

## 🎯 Quick Access

### Run the Agent
```bash
python agent.py
```

### Run Tests
```bash
python test_tools.py
```

### Run Demo
```bash
python demo_offline.py
```

### Setup Configuration
```bash
python agent.py --setup
```

## 📝 Notes

- Both English and Chinese versions contain the same content
- Chinese files are original versions
- English versions created for international accessibility
- All functionality works identically regardless of file language

---

**Last Updated:** 2026-01-28
**Version:** 1.0
**Language Support:** English + Chinese (中文)
