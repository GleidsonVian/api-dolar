import requests
import json

link = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
link = link.json()
cotacao = link['USDBRL']['bid']

print(f'Cotação do Dolar hoje é de: {cotacao}')
