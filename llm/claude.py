"""
Claude API Interface
"""
import anthropic
from typing import List, Dict, Any

class ClaudeClient:
    def __init__(self, config):
        self.config = config
        api_key = config.get("api_keys.claude")
        if not api_key:
            raise ValueError("Claude API Key not set, please run: python agent.py --setup")

        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = config.get("model", "claude-3-5-sonnet-20241022")

    def chat(self,
             messages: List[Dict[str, Any]],
             tools: List[Dict[str, Any]] = None,
             system: str = None) -> Dict[str, Any]:
        """
        Chat with Claude

        Args:
            messages: Message list
            tools: Available tools list
            system: System prompt

        Returns:
            Claude's response
        """
        try:
            kwargs = {
                "model": self.model,
                "max_tokens": self.config.get("max_tokens", 4096),
                "messages": messages
            }

            if tools:
                kwargs["tools"] = tools

            if system:
                kwargs["system"] = system

            response = self.client.messages.create(**kwargs)

            return {
                "success": True,
                "response": response
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
