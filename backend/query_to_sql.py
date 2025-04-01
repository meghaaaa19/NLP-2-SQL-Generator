import ollama
import sqlite3
import re
import pandas as pd  # ✅ Import Pandas
from sql_prompt_generator import generate_sql_prompt

# 🔹 Connect to SQLite Database
DB_PATH = "employee_data.db"  # Change this if your database has a different name

def get_sql_from_llm(user_query: str, model_id: str = "ollama run gemma3:12b") -> str:
    """
    Calls Ollama LLM, formats the user query into a structured prompt, 
    and extracts the SQL query from the LLM response.

    Args:
        user_query (str): The natural language query from the user.
        model_id (str): The LLM model to use (default: 'gemma3:1b').

    Returns:
        str: Extracted SQL query from LLM response or an error message.
    """
    prompt = generate_sql_prompt(user_query)
    response = ollama.chat(model=model_id, messages=[{"role": "user", "content": prompt}])

    match = re.search(r"<sql>(.*?)</sql>", response["message"]["content"], re.DOTALL)
    
    return match.group(1).strip() if match else "❌ ERROR: LLM did not return SQL inside <sql> tags."

def execute_sql_query(sql_query: str) -> pd.DataFrame:
    """
    Executes the generated SQL query on the SQLite database and returns a Pandas DataFrame.

    Args:
        sql_query (str): The SQL query to be executed.

    Returns:
        pd.DataFrame: Query results in a DataFrame.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        print("\n🚀 Executing SQL Query:\n", sql_query)

        cursor.execute(sql_query)
        results = cursor.fetchall()

        column_names = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(results, columns=column_names)

        conn.close()

        if df.empty:
            print("❌ No matching records found.")
        else:
            print("\n📌 Query Results (Pandas DataFrame):")
            print(df)

        return df

    except sqlite3.Error as e:
        print(f"❌ SQLite Error: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error

def generate_natural_response(user_query: str, df: pd.DataFrame, model_id: str = "gemma3:1b") -> str:
    """
    Converts SQL query results (Pandas DataFrame) into a natural language response.

    Args:
        user_query (str): The original user query.
        df (pd.DataFrame): The SQL query results in DataFrame format.
        model_id (str): The LLM model to use.

    Returns:
        str: The natural language response.
    """
    if df.empty:
        return "❌ No relevant data found for your query."

    # Convert DataFrame to a string format for LLM input
    df_str = df.to_string(index=False)

    prompt = f"""
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    You are an AI assistant that summarizes database query results in human-readable text.
    <|eot_id|><|start_header_id|>user<|end_header_id|>
    The user asked: "{user_query}"
    
    The database returned the following results:
    ```
    {df_str}
    ```
    
    Provide a concise summary of these results in 2-3 sentences.
    If the results contain numerical data, mention relevant insights (e.g., highest/lowest values, counts).
    If the results contain names or categories, summarize the key trends.

    <|start_header_id|>assistant<|end_header_id|>
    """
    
    response = ollama.chat(model=model_id, messages=[{"role": "user", "content": prompt}])

    return response["message"]["content"]

# Example Usage
if __name__ == "__main__":
    user_input = input("Enter your query: ")  
    sql_query = get_sql_from_llm(user_input)

    if "ERROR" not in sql_query:
        print("\n📝 Generated SQL Query:\n", sql_query)
        
        df = execute_sql_query(sql_query)

        if not df.empty:
            natural_response = generate_natural_response(user_input, df)
            print("\n🗣️ Natural Language Summary:\n", natural_response)
    else:
        print("❌ No valid SQL query generated.")
