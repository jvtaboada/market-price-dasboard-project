import yfinance as yf
from datetime import datetime
import pandas as pd

def get_commodities_df(): #->
    tickers = ["GC=F", "CL=F", "SI=F"]
    dfs =[]

    for ticker in tickers:
        df = yf.Ticker(ticker).history(period="1d", interval="1m")[['Close']].tail(1)
        df = df.rename(columns={'Close': 'preco'})

        df['ativo'] = ticker
        df['moeda'] = 'USD'
        df['hora_coleta'] = datetime.now()

        df = df[['ativo', 'preco', 'moeda', 'hora_coleta']]
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

    return df