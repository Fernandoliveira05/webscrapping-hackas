from flask import Flask, render_template, jsonify, request
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # DON'T CHANGE THIS !!!

from src.scrapers.main_scraper import get_all_hackathons, filter_hackathons_by_criteria

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/hackathons')
def get_hackathons():
    """API para obter hackathons com filtros opcionais"""
    location = request.args.get('location', None)
    online_only = request.args.get('online_only', 'false').lower() == 'true'
    
    # Configuração para São Paulo como padrão se nenhum filtro for fornecido
    if not location and not online_only:
        location = "São Paulo"
    
    # Obter todos os hackathons
    all_hackathons = get_all_hackathons(location_filter=location, include_online=True)
    
    # Aplicar filtros adicionais se necessário
    if online_only:
        all_hackathons = filter_hackathons_by_criteria(all_hackathons, online_only=True)
    
    return jsonify({"hackathons": all_hackathons})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
