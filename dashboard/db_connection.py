from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import streamlit as st
import os

load_dotenv()

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

@st.cache_data
def run_query(query):
    return pd.read_sql(query, engine)