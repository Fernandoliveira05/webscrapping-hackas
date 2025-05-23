# Módulo para scraping de sites específicos de hackathons Web3
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def scrape_devpost():
    """
    Scrape hackathons Web3 do Devpost
    
    Returns:
        list: Lista de hackathons encontrados
    """
    hackathons = []
    url = "https://devpost.com/hackathons?utf8=%E2%9C%93&search=web3&challenge_type=all&sort_by=Submission+Deadline"
    
    try:
        # Simulação de dados para demonstração
        simulated_hackathons = [
            {
                "title": "Web3 Global Hackathon",
                "description": "Construa o futuro da Web3 com blockchain, NFTs e DeFi",
                "date": "15 de Junho a 30 de Junho, 2025",
                "url": "https://devpost.com/hackathons/web3-global",
                "location": "Online",
                "is_online": True,
                "prizes": "$50,000 em prémios"
            },
            {
                "title": "São Paulo Blockchain Week Hackathon",
                "description": "Hackathon presencial durante a Blockchain Week em São Paulo",
                "date": "10 de Julho a 12 de Julho, 2025",
                "url": "https://devpost.com/hackathons/sp-blockchain-week",
                "location": "São Paulo, Brasil",
                "is_online": False,
                "prizes": "R$30.000 em prémios"
            }
        ]
        
        hackathons.extend(simulated_hackathons)
        
    except Exception as e:
        print(f"Erro ao fazer scraping do Devpost: {e}")
    
    return hackathons

def scrape_gitcoin():
    """
    Scrape hackathons Web3 do Gitcoin
    
    Returns:
        list: Lista de hackathons encontrados
    """
    hackathons = []
    
    try:
        # Simulação de dados para demonstração
        simulated_hackathons = [
            {
                "title": "Ethereum Layer 2 Hackathon",
                "description": "Desenvolva soluções escaláveis em Layer 2 para Ethereum",
                "date": "1 de Junho a 20 de Junho, 2025",
                "url": "https://gitcoin.co/hackathon/l2-scaling",
                "location": "Online",
                "is_online": True,
                "prizes": "$75,000 em prémios"
            }
        ]
        
        hackathons.extend(simulated_hackathons)
        
    except Exception as e:
        print(f"Erro ao fazer scraping do Gitcoin: {e}")
    
    return hackathons

def scrape_taikai():
    """
    Scrape hackathons Web3 do TAIKAI
    
    Returns:
        list: Lista de hackathons encontrados
    """
    hackathons = []
    
    try:
        # Simulação de dados para demonstração
        simulated_hackathons = [
            {
                "title": "Web3 Brasil Hackathon",
                "description": "O maior hackathon de Web3 do Brasil",
                "date": "5 de Julho a 7 de Julho, 2025",
                "url": "https://taikai.network/hackathons/web3-brasil",
                "location": "São Paulo, Brasil",
                "is_online": False,
                "prizes": "R$50.000 em prémios"
            },
            {
                "title": "DeFi Innovation Challenge",
                "description": "Construa o futuro das finanças descentralizadas",
                "date": "15 de Junho a 30 de Junho, 2025",
                "url": "https://taikai.network/hackathons/defi-innovation",
                "location": "Online",
                "is_online": True,
                "prizes": "$40,000 em prémios"
            }
        ]
        
        hackathons.extend(simulated_hackathons)
        
    except Exception as e:
        print(f"Erro ao fazer scraping do TAIKAI: {e}")
    
    return hackathons

def filter_hackathons(hackathons, location_filter=None, online_only=False):
    """
    Filtra hackathons por localização
    
    Args:
        hackathons (list): Lista de hackathons para filtrar
        location_filter (str): Filtro de localização (ex: "São Paulo")
        online_only (bool): Se True, retorna apenas hackathons online
        
    Returns:
        list: Lista de hackathons filtrados
    """
    filtered = []
    
    for hackathon in hackathons:
        # Filtro para hackathons online
        if online_only and not hackathon.get("is_online", False):
            continue
            
        # Filtro por localização
        if location_filter:
            location = hackathon.get("location", "").lower()
            if location_filter.lower() not in location:
                continue
                
        filtered.append(hackathon)
        
    return filtered

def scrape_web3_hackathons(location_filter=None, include_online=True):
    """
    Função principal para scraping de sites específicos de hackathons Web3
    
    Args:
        location_filter (str): Filtro de localização (ex: "São Paulo")
        include_online (bool): Se True, inclui hackathons online
        
    Returns:
        list: Lista de hackathons encontrados
    """
    all_hackathons = []
    
    # Scrape de diferentes fontes
    all_hackathons.extend(scrape_devpost())
    all_hackathons.extend(scrape_gitcoin())
    all_hackathons.extend(scrape_taikai())
    
    # Filtragem
    if location_filter or not include_online:
        return filter_hackathons(
            all_hackathons, 
            location_filter=location_filter, 
            online_only=(not location_filter and include_online)
        )
    
    return all_hackathons
