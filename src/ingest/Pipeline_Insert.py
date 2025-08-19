#pip install psycopg2-binary sqlalchemy python-dotenv

import pandas as pd
import time

from db.connection_postgres import engine
from .GetBitcoin import get_bitcoin_df
from .GetCommodities import get_commodities_df

sleep_seconds = 60

if __name__ == "__main__":
    while True: #loop infinito
        valor_bitcoin = get_bitcoin_df()
        valor_comm = get_commodities_df()

        df = pd.concat([valor_bitcoin, valor_comm], ignore_index=True)

        df.to_sql("cotacoes_ativos", engine, if_exists="append", index=False)

        print("✅ Cotações inseridas no postgres com sucesso!")

        time.sleep(sleep_seconds)