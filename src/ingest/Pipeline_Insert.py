#pip install psycopg2-binary sqlalchemy python-dotenv

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Cria engine SQLAlchemy
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DB_URL)

# Testar conexão com SELECT version()
with engine.connect() as conn:
    result = conn.execute(text("SELECT version();"))  # 👈 precisa do text()
    version = result.scalar()  # pega só o valor da primeira coluna da primeira linha
    print(version)