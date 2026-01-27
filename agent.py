#!/usr/bin/env python3
"""
CLImate-Android - AI-powered command line assistant

Similar to Claude Code, but runs on Android (Termux)
"""
import sys
import argparse
from pathlib import Path

# Import modules
from config import config
from tools.bash import BashTool
from tools.file import FileTool
from tools.system import SystemTool
from llm.claude import ClaudeClient

class AndroidCLIAgent:
    def __init__(self):
        self.config = config
        self.setup_tools()
        self.setup_llm()
        self.conversation_history = []

    def setup_tools(self):
        """Initialize tools"""
        self.bash_tool = BashTool(self.config)
        self.file_tool = FileTool(self.config)
        self.system_tool = SystemTool(self.config)

        # Collect all tool definitions
        self.tools = []
        self.tools.append(self.bash_tool.get_tool_definition())
        self.tools.extend(self.file_tool.get_tool_definitions())
        self.tools.extend(self.system_tool.get_tool_definitions())

        # Tool routing
        self.tool_handlers = {
            "execute_bash": self.bash_tool.execute,
            "read_file": self.file_tool.read_file,
            "write_file": self.file_tool.write_file,
            "list_files": self.file_tool.list_files,
            "get_system_info": self.system_tool.get_system_info,
            "get_resource_usage": self.system_tool.get_resource_usage,
            "get_current_directory": self.system_tool.get_current_directory
        }

    def setup_llm(self):
        """Initialize LLM"""
        provider = self.config.get("llm_provider", "claude")

        if provider == "claude":
            try:
                self.llm = ClaudeClient(self.config)
            except ValueError as e:
                print(f"❌ {e}")
                sys.exit(1)
        else:
            print(f"❌ Not yet supported {provider}")
            sys.exit(1)

    def get_system_prompt(self) -> str:
        """Get system prompt"""
        return """You are a CLI Agent running on Android phones, similar to Claude Code.

Your capabilities:
1. Execute shell commands (via execute_bash tool)
2. Read/write files (read_file, write_file)
3. List files (list_files)
4. Get system info (get_system_info, get_resource_usage)

Users will tell you what they want to do in natural language. You need to:
1. Understand user intent
2. Call appropriate tools to complete tasks
3. Reply with concise results

Notes:
- Think about safety before executing commands
- If multiple steps needed, execute in order
- When encountering errors, try to solve or give suggestions
- Replies should be concise and highlight key points

Current environment: Android (Termux)
"""

    def execute_tool(self, tool_name: str, tool_input: dict) -> dict:
        """Execute tool"""
        if tool_name not in self.tool_handlers:
            return {
                "success": False,
                "error": f"Unknown tool: {tool_name}"
            }

        handler = self.tool_handlers[tool_name]

        # 显示工具调用
        print(f"\n🔧 Calling tool: {tool_name}")
        if tool_name == "execute_bash":
            print(f"   Command: {tool_input.get('command', '')}")

        return handler(**tool_input)

    def process_request(self, user_input: str):
        """Process user request"""
        # Add user message
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # Chat with LLM
        print("\n🤔 Thinking...")

        while True:
            response = self.llm.chat(
                messages=self.conversation_history,
                tools=self.tools,
                system=self.get_system_prompt()
            )

            if not response["success"]:
                print(f"\n❌ Error: {response['error']}")
                return

            message = response["response"]

            # Check if need to stop
            if message.stop_reason == "end_turn":
                # Extract text reply
                text_content = ""
                for block in message.content:
                    if block.type == "text":
                        text_content += block.text

                if text_content:
                    print(f"\n💬 {text_content}")

                # Add to history
                self.conversation_history.append({
                    "role": "assistant",
                    "content": message.content
                })
                break

            elif message.stop_reason == "tool_use":
                # Handle tool calls
                tool_results = []

                for block in message.content:
                    if block.type == "tool_use":
                        tool_name = block.name
                        tool_input = block.input
                        tool_id = block.id

                        # Execute tool
                        result = self.execute_tool(tool_name, tool_input)

                        # Display results
                        if result.get("success"):
                            if tool_name == "execute_bash":
                                if result.get("stdout"):
                                    print(f"\n📤 Output:\n{result['stdout']}")
                                if result.get("stderr"):
                                    print(f"\n⚠️  Error:\n{result['stderr']}")
                        else:
                            print(f"\n❌ Tool execution failed: {result.get('error', '未知Error')}")

                        # Construct tool result
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": tool_id,
                            "content": str(result)
                        })

                # 添加 assistant 消息和工具结果
                self.conversation_history.append({
                    "role": "assistant",
                    "content": message.content
                })

                self.conversation_history.append({
                    "role": "user",
                    "content": tool_results
                })

    def chat_loop(self):
        """Interactive chat loop"""
        print("🐍 CLImate-Android started!")
        print("   A snake navigating the system depths, striking at the right spots for you.")
        print("\n💡 Enter your request, I will help you execute it. Type 'exit' to exit.\n")

        while True:
            try:
                user_input = input("👤 You: ").strip()

                if not user_input:
                    continue

                if user_input.lower() in ['exit', 'quit', 'q']:
                    print("\n👋 Goodbye!")
                    break

                if user_input.lower() == 'clear':
                    self.conversation_history = []
                    print("✅ Conversation history cleared")
                    continue

                self.process_request(user_input)
                print()  # 空行

            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="CLImate-Android - AI-powered command line assistant"
    )
    parser.add_argument(
        "--setup",
        action="store_true",
        help="Run configuration wizard"
    )
    parser.add_argument(
        "--once",
        type=str,
        help="Execute single command and exit"
    )

    args = parser.parse_args()

    if args.setup:
        config.setup_wizard()
        return

    # 检查配置
    if not config.get("api_keys.claude"):
        print("❌ API Key not configured, please run: python agent.py --setup")
        sys.exit(1)

    agent = AndroidCLIAgent()

    if args.once:
        agent.process_request(args.once)
    else:
        agent.chat_loop()

if __name__ == "__main__":
    main()
