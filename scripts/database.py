from pathlib import Path
from sqlalchemy import text
from config.database import engine


def database():

    sql_folder = Path("sql")

    sql_files = sorted(sql_folder.glob("*.sql"))

    with engine.begin() as connection:

        for sql_file in sql_files:

            print(f"\nRunning {sql_file.name}")

            sql = sql_file.read_text(encoding="utf-8")

            connection.execute(text(sql))

            print(f"✓ {sql_file.name} completed")


if __name__ == "__main__":
    database()