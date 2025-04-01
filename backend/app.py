from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import ollama
import pandas as pd
import re
from sql_prompt_generator import generate_sql_prompt  # Generates LLM prompt
import os
print(os.getcwd())  # Check if Flask is running from the correct directory

app = Flask(__name__)
CORS(app, resources={r"/generate_sql": {"origins": "*"}})  # Allow all frontend requests

DB_PATH = "D:/Users/Mohit/Desktop/NL2SQL/backend/employee_data.db"

def execute_sql_query(sql_query):
    """Executes the SQL query and returns structured results."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='employees';")
        if not cursor.fetchone():
            return {"error": "Table 'employees' does not exist in the database."}

        # Fetch column names
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        # Format output
        results = [dict(zip(column_names, row)) for row in rows]

        conn.close()
        return {
            "sql": sql_query,
            "columns": column_names,
            "rows": results
        }

    except sqlite3.Error as e:
        return {"error": str(e)}


def get_sql_from_llm(user_query):
    """Calls Ollama LLM, extracts SQL from the response."""
    
    prompt = generate_sql_prompt(user_query)  # Get structured prompt

    # 🔹 Call Ollama LLM
    response = ollama.chat(model="gemma3:1b", messages=[{"role": "user", "content": prompt}])

    # 🔹 Debug: Print the LLM response
    print("\n🔍 Full LLM Response:\n", response["message"]["content"])

    # 🔹 Extract SQL using regex
    match = re.search(r"<sql>(.*?)</sql>", response["message"]["content"], re.DOTALL)
    
    if match:
        extracted_sql = match.group(1).strip()
        print("\n📝 Extracted SQL Query:\n", extracted_sql)
        return extracted_sql
    else:
        return "❌ ERROR: LLM did not return SQL inside <sql> tags."

@app.route("/generate_sql", methods=["POST"])
def generate_sql():
    """API to convert user query to SQL and return results."""
    data = request.json
    user_query = data.get("query", "")

    sql_query = get_sql_from_llm(user_query)  # 🔹 Get extracted SQL

    if "ERROR" in sql_query:
        return jsonify({"error": sql_query}), 400

    results = execute_sql_query(sql_query)

    return jsonify({"sql": sql_query, "results": results})

if __name__ == "__main__":
    app.run(debug=True)
