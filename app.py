import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    dados_rest = {}
    
    for item in dados:
        nome_rest = item['Company']
        if nome_rest not in dados_rest:
            dados_rest[nome_rest] = []
        dados_rest[nome_rest].append({
            'Item': item['Item'],
            'Price': item['price'],
            'Description': item['description']
        })
else:
    print(f'Ocorreu um erro: {response.status_code}')
    

for nome_rest,dados in dados_rest.items():
    nome_do_arquivo = f'{nome_rest}.json'
    with open(nome_do_arquivo,'w') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante,indent=4)