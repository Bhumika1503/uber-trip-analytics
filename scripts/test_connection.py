from sqlalchemy import text
from config.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT current_database();"))

        print("✅ Connected Successfully!")
        print("Current Database:", result.fetchone()[0])

except Exception as e:
    print("❌ Connection Failed")
    print(e)