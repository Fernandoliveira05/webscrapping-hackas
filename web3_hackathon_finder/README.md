# Documentação da Aplicação Web3 Hackathon Finder

## Visão Geral
Web3 Hackathon Finder é uma aplicação web desenvolvida em Python com Flask que faz web scraping em diversas fontes para encontrar hackathons de Web3 que estejam para acontecer, seja online ou presencialmente em São Paulo, Brasil.

## Funcionalidades
- Scraping de múltiplas fontes (X/Twitter, Devpost, Gitcoin, TAIKAI, etc.)
- Filtros por localização (São Paulo ou online)
- Interface web responsiva e amigável
- Detalhes completos sobre os hackathons (data, local, prémios, etc.)

## Estrutura do Projeto
```
web3_hackathon_finder/
├── venv/                   # Ambiente virtual Python
├── src/                    # Código-fonte da aplicação
│   ├── models/             # Modelos de dados
│   ├── routes/             # Rotas da API Flask
│   ├── scrapers/           # Módulos de scraping
│   │   ├── __init__.py
│   │   ├── general_sites_scraper.py
│   │   ├── main_scraper.py
│   │   ├── twitter_scraper.py
│   │   └── web3_sites_scraper.py
│   ├── static/             # Arquivos estáticos (HTML, CSS, JS)
│   │   └── index.html
│   └── main.py             # Ponto de entrada da aplicação Flask
└── requirements.txt        # Dependências do projeto
```

## Requisitos
- Python 3.6+
- Flask
- BeautifulSoup4
- Requests
- Tweepy (para acesso à API do Twitter)
- Selenium (para scraping de páginas dinâmicas)

## Instalação
1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`

## Execução
1. Ative o ambiente virtual (se ainda não estiver ativo)
2. Execute a aplicação: `python src/main.py`
3. Acesse a aplicação no navegador: `http://localhost:5000`

## Notas Importantes
- Para uso em produção, seria necessário obter credenciais válidas para a API do Twitter
- A aplicação atual utiliza dados simulados para demonstração
- Para implementação completa, seria necessário configurar um sistema de agendamento para atualizar regularmente os dados dos hackathons

## Possíveis Melhorias Futuras
- Implementar sistema de notificações por email
- Adicionar mais fontes de dados
- Implementar sistema de favoritos para salvar hackathons interessantes
- Adicionar filtros adicionais (por tecnologia, prémios, etc.)
- Implementar autenticação de utilizadores
