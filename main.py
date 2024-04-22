from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if restaurante is None:
            return {'Dados': dados}
        dados_rest = []
        
        for item in dados:
            if item['Company'] == restaurante:
                dados_rest.append({
                    'Item': item['Item'],
                    'Price': item['price'],
                    'Description': item['description']
            })
        return {'Restaurante': restaurante, 'Cardapio': dados_rest}
    else:
        print('Erro:' f'{response.status_code} - {response.text}')