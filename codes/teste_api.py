import requests
import pandas as pd

# Configurar a URL da API e o Token
url = "https://api.tributos.gov.br/dados"  # Exemplo de URL
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJXMFNEVjFCb1BPZFhZMDRlTF9EWGlubDVOZjd5OVNNcGVsUmxVOGRqOTRveTl0WnFHZWdRWGo0Z0JrMkRNVEZCNzh5NVVOVllpTFVRSW5LNCIsImlhdCI6MTc0MjU1ODY4N30.OlbKyKchchmKXRT4vb_zWc6l264Bpu_UO6Knd6FK1OA",
    "Content-Type": "application/json"
}

# Fazer a requisição
response = requests.get(url, headers=headers)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Converter resposta para JSON
    
    # Criar um DataFrame (se a resposta for uma lista de dicionários)
    df = pd.DataFrame(data)
    
    # Exibir os primeiros registros
    print(df.head())
else:
    print(f"Erro ao acessar a API: {response.status_code}, {response.text}")
