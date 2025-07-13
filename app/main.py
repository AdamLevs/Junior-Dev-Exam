import time
import requests
import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

conn = psycopg2.connect(
    host=os.getenv('DB_HOST'),
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS')
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS btc_data (
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    value FLOAT
)
""")
conn.commit()

values = []

def fetch_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=ILS'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()['bitcoin']['ils']
    except Exception as e:
        print(f"Failed to fetch price: {e}")
        return None

def get_recommendation(latest, avg, min_v, max_v):
    if latest < avg and latest <= min_v:
        return "Buy"
    elif latest > avg and latest >= max_v:
        return "Sell"
    else:
        return "Hold"

while True:
    value = fetch_price()
    if value:
        values.append(value)
        cursor.execute("INSERT INTO btc_data (value) VALUES (%s)", (value,))
        conn.commit()

        min_v = min(values)
        max_v = max(values)
        avg_v = sum(values) / len(values)
        recommendation = get_recommendation(value, avg_v, min_v, max_v)

        print(f"⏱️  Value: {value} ₪| Min: {min_v} ₪| Max: {max_v} ₪ Avg: {avg_v:.2f} ₪| Recommendation: {recommendation}")
    else:
        print("Skipping iteration due to fetch failure.")

    time.sleep(60)  #Refresg the entire loop every 1 min, more that and the API might block us
