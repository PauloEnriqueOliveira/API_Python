import pandas as pd
import requests
import base64

username = "login"
password = "senha"

credentials = base64.b64encode(f"{username}:{password}".encode()).decode()

headers = {
    "Authorization": f"Basic {credentials}",
    "Content-Type": "application/x-www-form-urlencoded"
}

auth_url = "url"

data = {
    "grant_type": ""
}

response = requests.post(auth_url, headers=headers, data=data)

if response.status_code == 200:
    auth_token = response.json().get("access_token")
    print("Token de acesso:", auth_token)
else:
    print(f"Erro na autenticação: {response.status_code}")
    print(response.text)

headers = {
    "Authorization": f"Bearer {auth_token}"
}

url = "url"

params = {
    "info1": "",
    "info2": "",
    "info3": ""
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    print(df)
else:
    print(f"Erro na solicitação: {response.status_code}")
    print(response.text)
