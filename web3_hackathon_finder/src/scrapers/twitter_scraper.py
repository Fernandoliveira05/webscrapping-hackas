# Módulo para scraping do X (Twitter)
import tweepy
import re
import time
from datetime import datetime, timedelta

class TwitterScraper:
    def __init__(self, bearer_token=None):
        self.client = None
        self.bearer_token = bearer_token
        
    def authenticate(self, bearer_token=None):
        """
        Autentica com a API do Twitter usando um bearer token.
        
        Nota: Para uso real, é necessário um bearer token válido da API do Twitter.
        Para fins de demonstração, este método simula a autenticação.
        """
        if bearer_token:
            self.bearer_token = bearer_token
            
        # Em um cenário real, usaríamos:
        # self.client = tweepy.Client(bearer_token=self.bearer_token)
        print("Autenticação simulada para demonstração.")
        
    def search_hackathons(self, days_back=30, location_filter=None):
        """
        Busca tweets relacionados a hackathons de Web3.
        
        Args:
            days_back (int): Número de dias para buscar tweets anteriores
            location_filter (str): Filtro de localização (ex: "São Paulo")
            
        Returns:
            list: Lista de hackathons encontrados
        """
        hackathons = []
        
        # Em um cenário real com API:
        # query = "web3 hackathon OR web3 hackathons OR blockchain hackathon OR crypto hackathon"
        # if location_filter:
        #     query += f" {location_filter}"
        # end_time = datetime.now()
        # start_time = end_time - timedelta(days=days_back)
        # tweets = self.client.search_recent_tweets(
        #     query=query,
        #     max_results=100,
        #     start_time=start_time,
        #     end_time=end_time,
        #     tweet_fields=['created_at', 'text', 'author_id', 'entities']
        # )
        
        # Dados simulados para demonstração
        simulated_tweets = [
            {
                "id": "1234567890",
                "text": "Não perca o nosso Web3 Hackathon online! Inscrições abertas até 30/06. Prêmios incríveis! #web3 #blockchain",
                "created_at": "2025-05-15T10:30:00Z",
                "url": "https://twitter.com/example/status/1234567890"
            },
            {
                "id": "1234567891",
                "text": "Venha participar do maior hackathon de Web3 em São Paulo! Dias 15-17 de junho. #blockchain #web3 #saopaulo",
                "created_at": "2025-05-18T14:20:00Z",
                "url": "https://twitter.com/example/status/1234567891"
            }
        ]
        
        for tweet in simulated_tweets:
            # Filtragem por localização
            if location_filter and location_filter.lower() not in tweet["text"].lower():
                continue
                
            # Extração de informações
            hackathon = {
                "title": self._extract_title(tweet["text"]),
                "description": tweet["text"],
                "date": self._extract_date(tweet["text"]),
                "source": "Twitter (X)",
                "url": tweet["url"],
                "location": self._extract_location(tweet["text"]),
                "is_online": "online" in tweet["text"].lower()
            }
            
            hackathons.append(hackathon)
            
        return hackathons
    
    def _extract_title(self, text):
        """Extrai um título aproximado do texto do tweet"""
        # Lógica simplificada para extração de título
        if "hackathon" in text.lower():
            # Tenta extrair uma frase contendo "hackathon"
            sentences = re.split(r'[.!?]', text)
            for sentence in sentences:
                if "hackathon" in sentence.lower():
                    return sentence.strip()
        return "Hackathon Web3"
    
    def _extract_date(self, text):
        """Extrai datas mencionadas no tweet"""
        # Lógica simplificada para extração de datas
        date_patterns = [
            r'\d{1,2}[-/]\d{1,2}[-/]\d{2,4}',  # DD/MM/YYYY ou DD-MM-YYYY
            r'\d{1,2}\s+de\s+[a-zA-Z]+',       # DD de Mês
            r'[a-zA-Z]+\s+\d{1,2}[-]\d{1,2}'   # Mês DD-DD
        ]
        
        for pattern in date_patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(0)
        
        return "Data não especificada"
    
    def _extract_location(self, text):
        """Extrai localização mencionada no tweet"""
        # Lógica simplificada para extração de localização
        if "são paulo" in text.lower() or "sao paulo" in text.lower() or "sp" in text.lower():
            return "São Paulo"
        elif "online" in text.lower() or "virtual" in text.lower() or "remoto" in text.lower():
            return "Online"
        
        return "Localização não especificada"

def scrape_twitter(bearer_token=None):
    """
    Função principal para scraping do Twitter
    
    Args:
        bearer_token (str): Token de autenticação da API do Twitter
        
    Returns:
        list: Lista de hackathons encontrados
    """
    scraper = TwitterScraper(bearer_token)
    scraper.authenticate()
    
    # Busca hackathons online ou em São Paulo
    hackathons = scraper.search_hackathons(location_filter="São Paulo")
    online_hackathons = scraper.search_hackathons(location_filter="online")
    
    # Combina os resultados
    all_hackathons = hackathons + online_hackathons
    
    return all_hackathons
