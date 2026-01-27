"""
System Information Tool
"""
import os
import platform
import psutil
from typing import Dict, Any
from datetime import datetime

class SystemTool:
    def __init__(self, config):
        self.config = config

    def get_system_info(self) -> Dict[str, Any]:
        """Get system information"""
        try:
            return {
                "success": True,
                "system": platform.system(),
                "platform": platform.platform(),
                "machine": platform.machine(),
                "processor": platform.processor(),
                "python_version": platform.python_version(),
                "hostname": platform.node()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def get_resource_usage(self) -> Dict[str, Any]:
        """Get resource usage"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')

            battery = None
            if hasattr(psutil, "sensors_battery"):
                bat = psutil.sensors_battery()
                if bat:
                    battery = {
                        "percent": bat.percent,
                        "plugged": bat.power_plugged,
                        "time_left": bat.secsleft if bat.secsleft != -1 else None
                    }

            return {
                "success": True,
                "cpu": {
                    "percent": cpu_percent,
                    "count": psutil.cpu_count()
                },
                "memory": {
                    "total_mb": memory.total / 1024 / 1024,
                    "available_mb": memory.available / 1024 / 1024,
                    "percent": memory.percent
                },
                "disk": {
                    "total_gb": disk.total / 1024 / 1024 / 1024,
                    "used_gb": disk.used / 1024 / 1024 / 1024,
                    "free_gb": disk.free / 1024 / 1024 / 1024,
                    "percent": disk.percent
                },
                "battery": battery
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def get_current_directory(self) -> Dict[str, Any]:
        """Get current directory"""
        try:
            return {
                "success": True,
                "cwd": os.getcwd(),
                "home": str(os.path.expanduser("~"))
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def get_tool_definitions(self) -> list:
        """Return tool definitions"""
        return [
            {
                "name": "get_system_info",
                "description": "Get system information(OS, processor, Python version, etc.)",
                "input_schema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "get_resource_usage",
                "description": "Get system resource usage (CPU, memory, disk, battery)",
                "input_schema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "get_current_directory",
                "description": "Get current working directory",
                "input_schema": {
                    "type": "object",
                    "properties": {}
                }
            }
        ]
