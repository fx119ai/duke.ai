from typing import List, Dict
from .base import BaseAgent

class QueryHandler(BaseAgent):
    def parse_query(self, query: str) -> Dict:
        """Parse user query to extract company, context, and requirements"""
        # Implementation using OpenAI function calling
        return {
            "company": "...",
            "context": "...",
            "requirements": []
        }