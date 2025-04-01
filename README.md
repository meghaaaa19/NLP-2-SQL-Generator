# NLP-2-SQL-Generator
# 🧠 NLP to SQL Generator

## 🚀 Overview
NLP to SQL Generator is an AI-powered tool that converts **natural language queries** into **SQL queries**. It uses **Ollama's NLP models** to interpret the user's input and generate corresponding SQL queries based on a provided database schema. This project provides a backend API for processing and a simple frontend interface for users to interact with the system.

## 🛠️ Features
- 🔍 **Interpret natural language** and generate SQL queries.
- 🏗️ **Handles various types of queries** like selection, filtering, sorting, and aggregation.
- 🧠 **Understand singular/plural nouns** (e.g., "employee" returns one, "employees" returns all).
- 🧑‍💻 **Simple backend** using Flask to handle requests.
- 🌐 **Simple frontend** for interaction via HTML, CSS, and JavaScript.
- 🛠️ **Uses Ollama API** for NLP query processing.

## 📁 Project Structure
📁 NLP-2-SQL-Generator
│── 📁 frontend/                 # Frontend files (HTML, CSS, JS)
│   ├── index.html              # Main HTML file for the frontend
│   ├── style.css               # CSS for styling the frontend
│   ├── script.js               # JavaScript for handling frontend logic
│
│── 📁 backend/                  # Backend files (Python, Flask)
│   ├── app.py                  # Flask application to handle API routes
│   ├── database_setup.py        # Script to set up and initialize the database
│   ├── employee.csv             # CSV file containing employee data
│   ├── query_to_sql.py          # Logic to convert queries into SQL
│   ├── schema_mapping.py        # Maps database schema for query processing
│   ├── sql_prompt_generator.py  # Generates the SQL prompt from user input
│
│── 📄 requirements.txt          # List of required Python libraries
│── 📄 README.md                 # Project Documentation
│── 📄 .gitignore                # Git ignore file to exclude unnecessary files


## 🚀 Setup Instructions

### **1️⃣ Clone the repository:**
First, clone the repository to your local machine using Git:
```bash
git clone https://github.com/meghaaaa19/NLP-2-SQL-Generator.git
cd NLP-2-SQL-Generator
```
## **2️⃣ Set up a virtual environment:**
It's recommended to use a virtual environment to manage dependencies. You can set it up as follows:

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### **3️⃣ Install dependencies:**
After setting up the virtual environment, install the required Python libraries by running the following command:

```bash
pip install -r requirements.txt
```

### **4️⃣ Set up the database:**
You need to set up the database and load the employee data from the `employee.csv` file. To do this, run the `database_setup.py` script:

```bash
python backend/database_setup.py
```

### **5️⃣ Run the backend server:**
To start the backend server, navigate to the `backend/` folder and execute the following command:

```bash
python backend/app.py
```

### **6️⃣ Run the frontend:**
To run the frontend, you can simply open the `frontend/index.html` file in your web browser. Alternatively, for a better experience, you can use a live server.

#### Using VS Code:
- Install the **Live Server** extension.
- Right-click on `index.html` and select **"Open with Live Server"**.

This will open the frontend application in your browser, where you can interact with the user interface and send natural language queries to the backend.

### **7️⃣ Interact with the system:**
Once both the backend and frontend are running, you can interact with the system as follows:

1. **Enter natural language queries** in the frontend input field.
2. The **backend** will process the query and generate a corresponding **SQL query**.
3. The result will be displayed based on the generated SQL query, which will retrieve data from the database

## 🧪 Example Queries and SQL Conversion

Here are some example user queries and their corresponding generated SQL queries:

| **User Query**                    | **Generated SQL Query**                                   |
|-----------------------------------|-----------------------------------------------------------|
| "Get all employees"                | `SELECT * FROM employees;`                                |
| "Find the youngest employee"       | `SELECT * FROM employees ORDER BY Age ASC LIMIT 1;`       |
| "Show employees from Bangalore"    | `SELECT * FROM employees WHERE City = 'Bangalore';`       |
| "Employees with age greater than 30"| `SELECT * FROM employees WHERE Age > 30;`                |
| "Get employees who have left"      | `SELECT * FROM employees WHERE LeaveOrNot = 1;`           |

These are just a few examples. The system can handle a wide variety of natural language queries and convert them into SQL queries.

## 📌 To-Do / Future Improvements
While the current version of the project is functional, there are several areas for future enhancements:

- ✅ **Enhance NLP accuracy**: Improve the system's ability to understand more complex or varied natural language queries.
- 🖥️ **Improve frontend UI**: Make the user interface more interactive and visually appealing.
- 📂 **Support more databases**: Add support for databases like PostgreSQL, MySQL, or MongoDB.
- 🔍 **Add more query types**: Extend the system to handle advanced SQL features like joins, subqueries, and aggregate functions.
- 📊 **Add query optimization**: Implement optimizations to handle larger datasets and complex queries more efficiently.

## 📜 License
This project is licensed under the **MIT License**.


