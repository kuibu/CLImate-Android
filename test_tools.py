#!/usr/bin/env python3
"""
Test tool modules (no API Key required)
"""
import sys
from config import Config
from tools.bash import BashTool
from tools.file import FileTool
from tools.system import SystemTool

def test_bash_tool():
    print("=" * 60)
    print("🔧 Test Bash Tool")
    print("=" * 60)

    config = Config()
    bash = BashTool(config)

    # Test 1: Simple command
    print("\n[Test 1] Execute 'echo Hello World'")
    result = bash.execute("echo Hello World")
    print(f"Result: {result['stdout'].strip()}")
    print(f"Success: {result['success']}")

    # Test 2: List files
    print("\n[Test 2] Execute 'ls -la'")
    result = bash.execute("ls -la")
    lines = result['stdout'].split('\n')
    print(f"Output lines: {len(lines)}")
    print(f"Success: {result['success']}")

    # Test 3: Get current directory
    print("\n[Test 3] Execute 'pwd'")
    result = bash.execute("pwd")
    print(f"Current directory: {result['stdout'].strip()}")

    # Test 4: Dangerous command detection
    print("\n[Test 4] Detect dangerous command 'rm -rf /'")
    is_dangerous = bash.is_dangerous("rm -rf /")
    print(f"Is dangerous: {is_dangerous}")

def test_file_tool():
    print("\n" + "=" * 60)
    print("📁 Test File Tool")
    print("=" * 60)

    config = Config()
    file_tool = FileTool(config)

    # Test 1: Read file
    print("\n[Test 1] Read README.md")
    result = file_tool.read_file("README.md", max_lines=10)
    if result['success']:
        print(f"File lines: {result['lines']}")
        print(f"Content length: {len(result['content'])} characters")
        print(f"First 100 characters: {result['content'][:100]}...")
    else:
        print(f"Error: {result['error']}")

    # Test 2: List files
    print("\n[Test 2] List Python files in current directory Python 文件")
    result = file_tool.list_files(".", "*.py")
    if result['success']:
        print(f"Found {result['count']} files:")
        for f in result['files'][:5]:
            print(f"  - {f['name']} ({f['size']} bytes)")

    # Test 3: Write test file
    print("\n[Test 3] Create test file test_output.txt")
    result = file_tool.write_file("test_output.txt", "Hello from CLImate-Android!\nThis is test content.")
    if result['success']:
        print(f"File created: {result['path']}")
        print(f"Bytes written: {result['bytes']}")

    # Test 4: Read newly created file
    print("\n[Test 4] Read test file")
    result = file_tool.read_file("test_output.txt")
    if result['success']:
        print(f"Content: {result['content']}")

def test_system_tool():
    print("\n" + "=" * 60)
    print("💻 Test System Tool")
    print("=" * 60)

    config = Config()
    system = SystemTool(config)

    # Test 1: system information
    print("\n[Test 1] Get system information")
    result = system.get_system_info()
    if result['success']:
        print(f"OS: {result['system']}")
        print(f"Platform: {result['platform']}")
        print(f"Architecture: {result['machine']}")
        print(f"Python version: {result['python_version']}")
        print(f"Hostname: {result['hostname']}")

    # Test 2: resource usage
    print("\n[Test 2] Get resource usage")
    result = system.get_resource_usage()
    if result['success']:
        print(f"CPU usage: {result['cpu']['percent']}%")
        print(f"CPU cores: {result['cpu']['count']}")
        print(f"Total memory: {result['memory']['total_mb']:.2f} MB")
        print(f"Available memory: {result['memory']['available_mb']:.2f} MB")
        print(f"Memory usage: {result['memory']['percent']}%")
        print(f"Total disk: {result['disk']['total_gb']:.2f} GB")
        print(f"Disk used: {result['disk']['used_gb']:.2f} GB")
        print(f"Disk usage: {result['disk']['percent']}%")
        if result['battery']:
            print(f"Battery level: {result['battery']['percent']}%")
            print(f"Charging: {result['battery']['plugged']}")

    # Test 3: Current directory
    print("\n[Test 3] Get current directory")
    result = system.get_current_directory()
    if result['success']:
        print(f"Current directory: {result['cwd']}")
        print(f"Home directory: {result['home']}")

def test_tool_definitions():
    print("\n" + "=" * 60)
    print("📋 Test tool definitions (for LLM)")
    print("=" * 60)

    config = Config()
    bash = BashTool(config)
    file_tool = FileTool(config)
    system = SystemTool(config)

    print("\n[Bash Tool]")
    bash_def = bash.get_tool_definition()
    print(f"Name: {bash_def['name']}")
    print(f"Description: {bash_def['description']}")

    print("\n[File Tool]")
    file_defs = file_tool.get_tool_definitions()
    for tool_def in file_defs:
        print(f"- {tool_def['name']}: {tool_def['description']}")

    print("\n[System Tool]")
    system_defs = system.get_tool_definitions()
    for tool_def in system_defs:
        print(f"- {tool_def['name']}: {tool_def['description']}")

    total_tools = 1 + len(file_defs) + len(system_defs)
    print(f"\n✅ Total {total_tools} tools available")

def main():
    print("🐍 CLImate-Android - Tool Module Tests")
    print("=" * 60)
    print()

    try:
        test_bash_tool()
        test_file_tool()
        test_system_tool()
        test_tool_definitions()

        print("\n" + "=" * 60)
        print("✅ All tests completed！")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Test失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
