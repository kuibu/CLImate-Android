"""
Bash Command Execution Tool
"""
import subprocess
import shlex
from typing import Dict, Any

class BashTool:
    def __init__(self, config):
        self.config = config
        self.dangerous_patterns = [
            "rm -rf /",
            "dd if=",
            "mkfs",
            ":(){:|:&};:",  # fork bomb
            "chmod -R 777 /",
            "> /dev/sda"
        ]

    def is_dangerous(self, command: str) -> bool:
        """Check if command is dangerous"""
        for pattern in self.dangerous_patterns:
            if pattern in command:
                return True

        blocked = self.config.get("safety.blocked_commands", [])
        for blocked_cmd in blocked:
            if blocked_cmd in command:
                return True

        return False

    def execute(self, command: str, timeout: int = 30) -> Dict[str, Any]:
        """
        Execute shell command

        Args:
            command: Command to execute
            timeout: Timeout in seconds

        Returns:
            {
                "success": bool,
                "stdout": str,
                "stderr": str,
                "exit_code": int
            }
        """
        # Safety check
        if self.is_dangerous(command):
            if self.config.get("safety.require_confirmation", True):
                print(f"\n⚠️  Warning: This is a dangerous command!")
                print(f"Command: {command}")
                confirm = input("Continue execution? (yes/no): ").strip().lower()
                if confirm != "yes":
                    return {
                        "success": False,
                        "stdout": "",
                        "stderr": "User cancelled dangerous command execution",
                        "exit_code": -1
                    }

        try:
            # Execute command
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout
            )

            return {
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "exit_code": result.returncode
            }

        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "stdout": "",
                "stderr": f"Command execution timeout (>{timeout}s)",
                "exit_code": -1
            }

        except Exception as e:
            return {
                "success": False,
                "stdout": "",
                "stderr": str(e),
                "exit_code": -1
            }

    def get_tool_definition(self) -> Dict[str, Any]:
        """Return tool definition (for LLM function calling)"""
        return {
            "name": "execute_bash",
            "description": "Execute commands in shell. Can run any bash command like ls, cd, python, git, etc.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "Shell command to execute"
                    },
                    "timeout": {
                        "type": "integer",
                        "description": "Timeout in seconds, default 30",
                        "default": 30
                    }
                },
                "required": ["command"]
            }
        }
