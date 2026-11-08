import requests

url = "https://httpbin.org/post"

#data = {
#    "meus_dados": [1, 2, 3],
#    "pessoa": {
#        "nome": "Juliano",
#        "professor": True
#    }
#}

params = {
    'dataInicio': '2026-01-01',
    'dataFim': '2026-02-01',
}

resposta = requests.post(url, params=params)

print(resposta.request.url)
#print(resposta.json())