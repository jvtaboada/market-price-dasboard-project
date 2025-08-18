import pandas as pd
import time
from GetBicoin import get_bitcoin_df
from GetCommodities import get_commodities_df

valor_bitcoin = get_bitcoin_df()
valor_comm = get_commodities_df()

while True: #loop infinito
    print(valor_bitcoin)
    print(valor_comm)

    df = pd.concat([valor_bitcoin, valor_comm], ignore_index=True)
    df.to_sql("cotacoes")

    time.sleep(60)