"""
File Operation Tool
"""
import os
from pathlib import Path
from typing import Dict, Any, List

class FileTool:
    def __init__(self, config):
        self.config = config

    def read_file(self, file_path: str, max_lines: int = 1000) -> Dict[str, Any]:
        """
        Read file content

        Args:
            file_path: File path
            max_lines: Maximum lines to read

        Returns:
            File content or error message
        """
        try:
            path = Path(file_path).expanduser()

            if not path.exists():
                return {
                    "success": False,
                    "error": f"File does not exist: {file_path}"
                }

            if not path.is_file():
                return {
                    "success": False,
                    "error": f"Not a file: {file_path}"
                }

            # Check file size
            file_size = path.stat().st_size
            if file_size > 10 * 1024 * 1024:  # 10MB
                return {
                    "success": False,
                    "error": f"File too large: {file_size / 1024 / 1024:.2f}MB (limit: 10MB)"
                }

            # Read file
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()

            if len(lines) > max_lines:
                content = ''.join(lines[:max_lines])
                truncated = True
            else:
                content = ''.join(lines)
                truncated = False

            return {
                "success": True,
                "content": content,
                "lines": len(lines),
                "truncated": truncated,
                "path": str(path)
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def write_file(self, file_path: str, content: str) -> Dict[str, Any]:
        """Write file"""
        try:
            path = Path(file_path).expanduser()
            path.parent.mkdir(parents=True, exist_ok=True)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

            return {
                "success": True,
                "path": str(path),
                "bytes": len(content.encode('utf-8'))
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def list_files(self, directory: str, pattern: str = "*") -> Dict[str, Any]:
        """List files in directory"""
        try:
            path = Path(directory).expanduser()

            if not path.exists():
                return {
                    "success": False,
                    "error": f"Directory does not exist: {directory}"
                }

            if not path.is_dir():
                return {
                    "success": False,
                    "error": f"Not a directory: {directory}"
                }

            files = []
            for item in path.glob(pattern):
                files.append({
                    "name": item.name,
                    "path": str(item),
                    "is_dir": item.is_dir(),
                    "size": item.stat().st_size if item.is_file() else 0
                })

            return {
                "success": True,
                "files": files,
                "count": len(files)
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def get_tool_definitions(self) -> List[Dict[str, Any]]:
        """Return tool definitions"""
        return [
            {
                "name": "read_file",
                "description": "Read file content",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "File path"
                        },
                        "max_lines": {
                            "type": "integer",
                            "description": "Maximum lines to read",
                            "default": 1000
                        }
                    },
                    "required": ["file_path"]
                }
            },
            {
                "name": "write_file",
                "description": "Write file.Will overwrite if file exists.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "File path"
                        },
                        "content": {
                            "type": "string",
                            "description": "File content"
                        }
                    },
                    "required": ["file_path", "content"]
                }
            },
            {
                "name": "list_files",
                "description": "List files in directory",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "directory": {
                            "type": "string",
                            "description": "Directory path"
                        },
                        "pattern": {
                            "type": "string",
                            "description": "File matching pattern（e.g. *.py）",
                            "default": "*"
                        }
                    },
                    "required": ["directory"]
                }
            }
        ]
