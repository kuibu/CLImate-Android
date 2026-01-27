"""
Configuration Management Module
"""
import os
import json
from pathlib import Path

class Config:
    def __init__(self):
        self.config_dir = Path.home() / ".climate-android"
        self.config_file = self.config_dir / "config.json"
        self.ensure_config_dir()
        self.load_config()

    def ensure_config_dir(self):
        """Ensure config directory exists"""
        self.config_dir.mkdir(parents=True, exist_ok=True)

    def load_config(self):
        """Load configuration"""
        if self.config_file.exists():
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        else:
            self.data = {
                "llm_provider": "claude",  # claude, openai, local
                "api_keys": {
                    "claude": "",
                    "openai": ""
                },
                "model": "claude-3-5-sonnet-20241022",
                "max_tokens": 4096,
                "temperature": 0.7,
                "safety": {
                    "require_confirmation": True,  # Dangerous commands need confirmation
                    "allowed_commands": [],        # Whitelist (empty = allow all)
                    "blocked_commands": ["rm -rf /", "dd if="]  # Blacklist
                }
            }
            self.save_config()

    def save_config(self):
        """Save configuration"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def get(self, key, default=None):
        """Get configuration value"""
        keys = key.split('.')
        value = self.data
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value

    def set(self, key, value):
        """Set configuration value"""
        keys = key.split('.')
        data = self.data
        for k in keys[:-1]:
            if k not in data:
                data[k] = {}
            data = data[k]
        data[keys[-1]] = value
        self.save_config()

    def setup_wizard(self):
        """Configuration wizard"""
        print("🐍 Welcome to CLImate-Android!")
        print("   A snake navigating the system depths, striking at the right spots for you.")
        print("\nLet's complete the basic setup...\n")

        # Select LLM provider
        print("1. Select LLM Provider:")
        print("   1) Claude (Anthropic)")
        print("   2) OpenAI")
        print("   3) Local Model")

        choice = input("Please select (1-3): ").strip()
        provider_map = {"1": "claude", "2": "openai", "3": "local"}
        provider = provider_map.get(choice, "claude")
        self.set("llm_provider", provider)

        # Set API Key
        if provider in ["claude", "openai"]:
            api_key = input(f"\nPlease enter {provider.upper()} API Key: ").strip()
            self.set(f"api_keys.{provider}", api_key)

        # Safety settings
        print("\n2. Safety Settings:")
        require_confirm = input("Require confirmation before executing dangerous commands? (Y/n): ").strip().lower()
        self.set("safety.require_confirmation", require_confirm != 'n')

        print("\n✅ Configuration completed!")
        print(f"Config file saved at: {self.config_file}")
        self.save_config()

# Global config instance
config = Config()
