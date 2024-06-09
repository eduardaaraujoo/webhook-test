import requests
import json   #biblioteca que transforma um dicionário no json

link = "https://webhook.site/70d97d9e-20a3-41bb-ab54-8002a1046029"


dicionario = {
    "nome": "Eduarda",
    "valor": 96,
    "parcelas": 3,
}

# Convertendo o dicionário em JSON
dicionario_ajustado = json.dumps(dicionario)
requests.post(link, data=dicionario_ajustado)