import sqlite3
import pandas as pd

def ingest_csv_to_sqlite(csv_file: str, db_name: str, table_name: str):
    """
    Reads a CSV file and stores it in an SQLite database.

    Args:
        csv_file (str): Path to the CSV file.
        db_name (str): SQLite database name.
        table_name (str): Table name where data will be stored.

    Returns:
        None
    """
    # Load the CSV into a Pandas DataFrame
    df = pd.read_csv("Employee.csv")

    # Connect to SQLite database (creates the file if not exists)
    conn = sqlite3.connect(db_name)
    
    # Store data in SQLite
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.close()
    print(f"✅ CSV data loaded into {db_name}, table: {table_name}")

# Example Usage
if __name__ == "__main__":
    ingest_csv_to_sqlite("Employee.csv", "employee_data.db", "employees")
