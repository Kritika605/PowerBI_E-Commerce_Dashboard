import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:admin123@localhost:5433/Ecommerce_db'
db = create_engine(conn_string)
conn = db.connect()

files = ['ecommerce_data','us_state_long_lat_codes']
for file in files:
    df = pd.read_csv(fr'C:\Users\Kritika\OneDrive\Desktop\DA\Power BI Projects\E-Commerce Dashboard\{file}.csv', encoding='ISO-8859-1')
    df.to_sql(file ,con = conn, if_exists='replace', index=False)