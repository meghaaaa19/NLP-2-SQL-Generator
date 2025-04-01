def generate_sql_prompt(user_query: str) -> str:
    """
    Generates a structured prompt to convert natural language into an SQL query.

    Args:
        user_query (str): The natural language query from the user.

    Returns:
        str: A well-formatted prompt for the LLM to generate SQL queries.
    """

    schema_str = """Table: employees

Columns:
1️⃣ **Education** (TEXT) → Employee's highest education level.  
   - **Possible Values**: 'Bachelors', 'Masters', 'PhD'  
   - **Usage**: Filter employees by education level.  
   - **Example Query**:  
     ```sql
     SELECT * FROM employees WHERE Education = 'Masters';
     ```

2️⃣ **JoiningYear** (INTEGER) → The year the employee joined the company.  
   - **Possible Values**: Any four-digit year (e.g., 2000-2025).  
   - **Usage**: Find employees based on tenure.  
   - **Example Query**:  
     ```sql
     SELECT * FROM employees WHERE JoiningYear > 2015;
     ```

3️⃣ **City** (TEXT) → The city where the employee is based.  
   - **Possible Values**: 'Bangalore', 'Pune', 'New Delhi'  
   - **Usage**: Filter employees by location.  
   - **Example Query**:  
     ```sql
     SELECT * FROM employees WHERE City = 'Bangalore';
     ```

4️⃣ **PaymentTier** (INTEGER) → Employee's salary tier.  
   - **Possible Values**: 1 = High, 2 = Medium, 3 = Low  
   - **Usage**: Identify employees based on salary level.  
   - **Example Query**:  
     ```sql
     SELECT * FROM employees WHERE PaymentTier = 1;
     ```

5️⃣ **Age** (INTEGER) → The employee's age in years.  
   - **Possible Values**: Any positive integer (typically 18-65).  
   - **Usage**: Find employees in a specific age range.  
   - **Example Query**:  
     ```sql
     SELECT * FROM employees WHERE Age > 40;
     ```

6️⃣ **Gender** (TEXT) → The employee's gender.  
   - **Possible Values**: 'Male', 'Female', 'Other'  
   - **Usage**: Filter employees based on gender.  
   - **Example Query**:  
     ```sql
     SELECT COUNT(*) FROM employees WHERE Gender = 'Female';
     ```

7️⃣ **EverBenched** (TEXT) → Whether the employee was ever benched (without a project).  
   - **Possible Values**: 'Yes', 'No'  
   - **Usage**: Find employees who were benched.  
   - **Example Query**:  
     ```sql
     SELECT * FROM employees WHERE EverBenched = 'Yes';
     ```

8️⃣ **ExperienceInCurrentDomain** (INTEGER) → Number of years of experience in the current field.  
   - **Possible Values**: Any non-negative integer.  
   - **Usage**: Filter employees based on experience.  
   - **Example Query**:  
     ```sql
     SELECT * FROM employees WHERE ExperienceInCurrentDomain > 5;
     ```

9️⃣ **LeaveOrNot** (INTEGER) → Whether the employee left the company.  
   - **Possible Values**: 0 = Employee stayed, 1 = Employee left  
   - **Usage**: Perform attrition analysis.  
   - **Example Query**:  
     ```sql
     SELECT COUNT(*) FROM employees WHERE LeaveOrNot = 1;
     ```
"""

    prompt = f"""
You are an AI that converts natural language into SQL queries
### **🔹 System Instructions**
- **Generate valid SQL queries** based on the provided **database schema**.
- First, look at the user's query and understand the user's intent, and identify the relevant columns asked
- **Understand singular vs. plural queries**:  
  - If the query mentions **"employee" (singular)**, return **only one record** that matches (use `LIMIT 1` if necessary).  
  - If the query mentions **"employees" (plural)**, return **all matching records**.
- **Interpret conditions accurately**:
  - If the query states **"is" or "equal to" or "equals"**, use `=` (e.g., "Age is 23" → `Age = 23`).
  - If the query states **"greater than" or "older than" or "above"**, use `>` (e.g., "Age greater than 30" → `Age > 30`).
  - If the query states **"less than" or "younger than" or "below"**, use `<` (e.g., "Age less than 25" → `Age < 25`).
- think step by step before writing the SQL query
- Use **correct column names and data types** as per the schema.
- **Do not assume missing data.** If a column is not mentioned in the query, ignore it.
- **Special cases for employment status**:  
  - If the query asks for **"employees who left"**, use `LeaveOrNot = 1`.  
  - If the query asks for **"employees who stayed"**, use `LeaveOrNot = 0`. 
- **For range queries**, use `>` or `<` (e.g., Age > 30, JoiningYear < 2015).
- **For multiple filters**, use `AND` conditions (e.g., Age > 30 AND City = 'Bangalore').
- **Sort results if asked** (e.g., "oldest employees" → `ORDER BY Age DESC`).
- **Use `LIKE` for partial text matches** (e.g., "employees from a city that starts with 'B'" → `City LIKE 'B%'`).
- **Return only the SQL query inside `<sql>` and `</sql>` tags.**
- **Output only the SQL query** wrapped inside `<sql>` and `</sql>` tags.

---

### **🔹 Database Schema**
{schema_str}

---

### **🔹 Example Queries**
#### **Example 1:**
🔹 **User Query:** "List all employees in Bangalore who were never benched."  
🔹 **Expected SQL Output:**  
```sql
<sql>
SELECT * FROM employees WHERE City = 'Bangalore' AND EverBenched = 'No';
</sql>

#### **Example 2:**
🔹 **User Query:** "Find all male employees in PaymentTier 1 who are older than 40."  
🔹 **Expected SQL Output:**  
```sql
<sql>
SELECT * FROM employees WHERE Gender = 'Male' AND PaymentTier = 1 AND Age > 40;
</sql>

#### **Example 3:**
🔹 **User Query:** "Show employees who left the company and have more than 5 years of experience."  
🔹 **Expected SQL Output:**  
```sql
<sql>
SELECT * FROM employees WHERE LeaveOrNot = 1 AND ExperienceInCurrentDomain > 5;
</sql>

#### **Example 4:**
🔹 **User Query:** "Find all employees who joined before 2015 and work in Pune."  
🔹 **Expected SQL Output:**  
```sql
<sql>
SELECT * FROM employees WHERE JoiningYear < 2015 AND City = 'Pune';
</sql>

#### **Example 5:**
🔹 **User Query:** "Count the number of employees who left the company from Pune."  
🔹 **Expected SQL Output:**  
```sql
<sql>
SELECT COUNT(*) FROM employees WHERE City = 'Pune' AND LeaveOrNot = 1;
</sql>

#### **Example 5:**
🔹 **User Query:** "Get the average age of employees in each PaymentTier."  
🔹 **Expected SQL Output:**  
```sql
<sql>
SELECT PaymentTier, AVG(Age) FROM employees GROUP BY PaymentTier;
</sql>


### **🔹 User Query**
Convert the following natural language query into SQL:
Query: "{user_query}"

Return only the SQL query inside `<sql>` and `</sql>` tags.
"""

    # ✅ `return prompt` is correctly placed at the end
    return prompt


