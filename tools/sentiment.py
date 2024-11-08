from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = pipeline(
            "sentiment-analysis",
            model="nvidia/bert-base-sentiment"
        )
        
    def analyze(self, text: str) -> Dict:
        return self.analyzer(text)