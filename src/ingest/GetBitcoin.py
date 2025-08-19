# pip install requests pandas

import requests
from datetime import datetime
import pandas as pd

def get_bitcoin_df():
    url = "https://api.coinbase.com/v2/prices/spot"

    response = requests.get(url)
    dados = response.json()

    preco = float(dados['data']['amount'])
    ativo = dados['data']['base']
    moeda = dados['data']['currency']
    hora_coleta = datetime.now()


    df = pd.DataFrame([{
        'ativo': ativo,
        'moeda': moeda,
        'preco': preco,
        'hora_coleta': hora_coleta
    }])

    return df