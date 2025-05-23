# Módulo principal para integração dos scrapers
from src.scrapers.twitter_scraper import scrape_twitter
from src.scrapers.web3_sites_scraper import scrape_web3_hackathons
from src.scrapers.general_sites_scraper import scrape_general_sites

def get_all_hackathons(location_filter=None, include_online=True):
    """
    Função principal para obter hackathons de todas as fontes
    
    Args:
        location_filter (str): Filtro de localização (ex: "São Paulo")
        include_online (bool): Se True, inclui hackathons online
        
    Returns:
        list: Lista combinada de hackathons de todas as fontes
    """
    all_hackathons = []
    
    # Obter hackathons do Twitter/X
    twitter_hackathons = scrape_twitter()
    if twitter_hackathons:
        for hackathon in twitter_hackathons:
            # Filtrar por localização se necessário
            if location_filter:
                if location_filter.lower() not in hackathon.get("location", "").lower():
                    if not (include_online and hackathon.get("is_online", False)):
                        continue
            # Adicionar fonte
            hackathon["source"] = "Twitter (X)"
            all_hackathons.append(hackathon)
    
    # Obter hackathons de sites específicos de Web3
    web3_hackathons = scrape_web3_hackathons(location_filter, include_online)
    if web3_hackathons:
        all_hackathons.extend(web3_hackathons)
    
    # Obter hackathons de sites gerais
    general_hackathons = scrape_general_sites()
    if general_hackathons:
        all_hackathons.extend(general_hackathons)
    
    return all_hackathons

def filter_hackathons_by_criteria(hackathons, location=None, online_only=False, upcoming_only=True):
    """
    Filtra hackathons por critérios específicos
    
    Args:
        hackathons (list): Lista de hackathons para filtrar
        location (str): Filtro de localização
        online_only (bool): Se True, retorna apenas hackathons online
        upcoming_only (bool): Se True, retorna apenas hackathons futuros
        
    Returns:
        list: Lista de hackathons filtrados
    """
    filtered = []
    
    for hackathon in hackathons:
        # Filtro para hackathons online
        if online_only and not hackathon.get("is_online", False):
            continue
            
        # Filtro por localização
        if location:
            hackathon_location = hackathon.get("location", "").lower()
            if location.lower() not in hackathon_location:
                continue
        
        # Adicionar à lista filtrada
        filtered.append(hackathon)
        
    return filtered
