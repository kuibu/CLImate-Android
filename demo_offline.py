#!/usr/bin/env python3
"""
Offline Demo - Simulate Agent workflow (no API Key required)
"""
from config import Config
from tools.bash import BashTool
from tools.file import FileTool
from tools.system import SystemTool

class DemoAgent:
    def __init__(self):
        self.config = Config()
        self.bash_tool = BashTool(self.config)
        self.file_tool = FileTool(self.config)
        self.system_tool = SystemTool(self.config)

    def demo_scenario_1(self):
        """Scenario 1: View System Info"""
        print("=" * 60)
        print("📱 Scenario 1: View System Info和资源使用")
        print("=" * 60)
        print()
        print("👤 User: Check my system info and resource usage")
        print()
        print("🤖 Agent: OK, let me check your system info...")
        print()

        # 调用工具
        print("🔧 [调用工具] get_system_info()")
        info = self.system_tool.get_system_info()
        if info['success']:
            print(f"   ✅ 系统: {info['system']} ({info['machine']})")
            print(f"   ✅ Python: {info['python_version']}")

        print()
        print("🔧 [调用工具] get_resource_usage()")
        usage = self.system_tool.get_resource_usage()
        if usage['success']:
            print(f"   ✅ CPU: {usage['cpu']['percent']}% (核心数: {usage['cpu']['count']})")
            print(f"   ✅ 内存: {usage['memory']['percent']}% ({usage['memory']['available_mb']:.0f}MB 可用)")
            print(f"   ✅ 磁盘: {usage['disk']['percent']}% ({usage['disk']['free_gb']:.1f}GB 空闲)")
            if usage['battery']:
                print(f"   ✅ 电池: {usage['battery']['percent']}% {'(充电中)' if usage['battery']['plugged'] else '(未充电)'}")

        print()
        print("💬 Agent: Your system is running normally!")
        print()

    def demo_scenario_2(self):
        """Scenario 2: File Operations"""
        print("=" * 60)
        print("📁 Scenario 2: Create and Manage Files")
        print("=" * 60)
        print()
        print("👤 User: Help me create a Python script hello.py that prints Hello World")
        print()
        print("🤖 Agent: OK, let me create this script...")
        print()

        # 创建文件
        print("🔧 [调用工具] write_file('hello.py', ...)")
        content = """#!/usr/bin/env python3
print("Hello from CLImate-Android!")
print("这是一个自动生成的脚本")
"""
        result = self.file_tool.write_file("hello.py", content)
        if result['success']:
            print(f"   ✅ 文件已创建: {result['path']}")
            print(f"   ✅ 大小: {result['bytes']} bytes")

        print()
        print("💬 Agent: Script created! Want to run it?")
        print()
        print("👤 User: OK, run it")
        print()

        # 运行脚本
        print("🔧 [调用工具] execute_bash('python3 hello.py')")
        result = self.bash_tool.execute("python3 hello.py")
        if result['success']:
            print("   📤 输出:")
            print("   " + "\n   ".join(result['stdout'].strip().split('\n')))

        print()
        print("💬 Agent: Run successfully!")
        print()

    def demo_scenario_3(self):
        """场景 3: 系统监控"""
        print("=" * 60)
        print("🔍 Scenario 3: List and Find Files")
        print("=" * 60)
        print()
        print("👤 User: List all Python files in current directory")
        print()
        print("🤖 Agent: Let me search...")
        print()

        # 列出 Python 文件
        print("🔧 [调用工具] list_files('.', '*.py')")
        result = self.file_tool.list_files(".", "*.py")
        if result['success']:
            print(f"   ✅ 找到 {result['count']} 个 Python 文件:")
            for f in result['files'][:10]:
                size_kb = f['size'] / 1024
                print(f"      - {f['name']} ({size_kb:.1f} KB)")

        print()
        print("💬 Agent: Above are all Python files!")
        print()

    def demo_scenario_4(self):
        """场景 4: 复杂任务"""
        print("=" * 60)
        print("⚙️  Scenario 4: Create Backup Script")
        print("=" * 60)
        print()
        print("👤 User: Help me create a backup script to compress specified directory")
        print()
        print("🤖 Agent: OK, let me create a backup script...")
        print()

        # 创建备份脚本
        print("🔧 [调用工具] write_file('backup.sh', ...)")
        script_content = """#!/bin/bash
# 自动备份脚本
# 由 CLImate-Android 生成

BACKUP_DIR="${1:-.}"
DATE=$(date +%Y%m%d_%H%M%S)
OUTPUT="backup_${DATE}.tar.gz"

echo "开始备份: $BACKUP_DIR"
tar -czf "$OUTPUT" "$BACKUP_DIR"

if [ $? -eq 0 ]; then
    echo "✅ 备份成功: $OUTPUT"
    ls -lh "$OUTPUT"
else
    echo "❌ 备份失败"
    exit 1
fi
"""
        result = self.file_tool.write_file("backup.sh", script_content)
        if result['success']:
            print(f"   ✅ 脚本已创建: {result['path']}")

        print()
        print("🔧 [调用工具] execute_bash('chmod +x backup.sh')")
        result = self.bash_tool.execute("chmod +x backup.sh")
        if result['success']:
            print("   ✅ 脚本已设置为可执行")

        print()
        print("💬 Agent: Backup script created! Usage:")
        print("   ./backup.sh <目录路径>")
        print()

    def demo_safety(self):
        """演示安全机制"""
        print("=" * 60)
        print("🛡️  Safety Mechanism Demo")
        print("=" * 60)
        print()
        print("👤 User: Delete all files (this is dangerous!)")
        print()
        print("🤖 Agent: Dangerous command detected, analyzing...")
        print()

        dangerous_commands = [
            "rm -rf /",
            "dd if=/dev/zero of=/dev/sda",
            "chmod -R 777 /"
        ]

        for cmd in dangerous_commands:
            is_dangerous = self.bash_tool.is_dangerous(cmd)
            status = "🚫 已拦截" if is_dangerous else "✅ 安全"
            print(f"   {status}: {cmd}")

        print()
        print("💬 Agent: I detected these are dangerous commands and have blocked them.")
        print("   If you really need to execute, you need to input 'yes' to confirm.")
        print()

    def run_all_demos(self):
        """运行所有演示"""
        print()
        print("🐍 CLImate-Android - Interactive Demo")
        print("=" * 60)
        print("This is an offline demo showing Agent workflow")
        print("（不需要 API Key）")
        print("=" * 60)
        print()

        input("Press Enter to start demo...")

        self.demo_scenario_1()
        input("Press Enter for next scenario...")

        self.demo_scenario_2()
        input("Press Enter for next scenario...")

        self.demo_scenario_3()
        input("Press Enter for next scenario...")

        self.demo_scenario_4()
        input("Press Enter to view安全 mechanisms...")

        self.demo_safety()

        print("=" * 60)
        print("✅ Demo completed!")
        print("=" * 60)
        print()
        print("💡 This is how CLImate-Android works:")
        print("   1. User describes needs in natural language")
        print("   2. LLM understands intent and calls appropriate tools")
        print("   3. Tools execute operations and return results")
        print("   4. Agent presents results to user in friendly manner")
        print()
        print("🚀 In real environment, all this is done automatically!")
        print()

def main():
    demo = DemoAgent()
    demo.run_all_demos()

if __name__ == "__main__":
    main()
