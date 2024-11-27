from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    if not query:
        return "Por favor ingresa una consulta.", 400

    response = requests.get('https://api.unsplash.com/search/photos', 
                            params={'query': query},
                            headers={'Authorization': 'Client-ID PkYsWHyqB1VUVheGmevXVE7UT_z_beAEpfznWySCMwE'})
    
    if response.status_code == 200:
        # Procesar los resultados de la API
        data = response.json()
        images = [result['urls']['small'] for result in data['results']]
        return render_template('index.html', query=query, images=images)
    else:
        return "Error al obtener imágenes. Intenta de nuevo más tarde.", 500

if __name__ == '__main__':
    app.run(debug=True)



