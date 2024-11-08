from cohere import Client
from typing import Dict, List

class MultilingualSearchAgent:
    def __init__(self, cohere_api_key: str):
        self.co = Client(cohere_api_key)
        self.search_tool = TavilySearchResults()
        
    async def search_with_language(self, query: str, country: str, language: str) -> List[Dict]:
        """Search in local language for specific country"""
        # Translate query to local language using Cohere's Aya
        translated_query = await self._translate_query(query, language)
        
        # Perform search in local language
        local_results = await self.search_tool.asearch(translated_query)
        
        # Translate results back to English for processing
        translated_results = await self._translate_results(local_results, language)
        
        return translated_results
    
    async def _translate_query(self, query: str, target_language: str) -> str:
        """Use Cohere's Aya to translate search query"""
        response = self.co.chat(
            message=f"Translate this business/news query to {target_language}: {query}",
            model="command"  # or whichever Cohere model supports Aya
        )
        return response.text