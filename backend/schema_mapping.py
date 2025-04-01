def format_employee_schema_for_prompt() -> str:
    """
    Formats the Employee dataset schema into a structured string for AI-based SQL generation.

    Returns:
        str: AI-friendly schema format.
    """
    schema_str = """Table: employees

Columns:
- Employee_ID (INTEGER) → Unique identifier for each employee. 
  - Primary Key.  
  - Auto-incremented unique number assigned to each employee.  
  - Example: 101, 102, 103  

- Name (TEXT) → Full name of the employee.  
  - Free-text field.  
  - Example: "Alice Johnson", "Bob Smith"  

- Education (TEXT) → Employee's highest educational qualification.  
  - Common values: 'Bachelors', 'Masters', 'PhD'  
  - Example: "Bachelors"  

- JoiningYear (INTEGER) → The year the employee joined the company.  
  - Four-digit year format (YYYY).  
  - Example: 2017, 2013, 2014  
  - Used for tenure-based queries (e.g., employees who joined after 2015).  

- City (TEXT) → The city where the employee is based.  
  - Common values: "Bangalore", "Pune", "New Delhi"  
  - Used for location-based queries (e.g., employees in Bangalore).  

- PaymentTier (INTEGER) → The employee's salary tier (Level).  
  - 1 = High Salary  
  - 2 = Medium Salary  
  - 3 = Low Salary  
  - Example: 1 (High Salary)  
  - Used for salary-based queries (e.g., employees in Tier 1 earning the highest salaries).  

- Age (INTEGER) → The employee's age in years.  
  - Example: 28, 35, 40  
  - Used for age-based queries (e.g., employees above 30).  

- Gender (TEXT) → The employee's gender.  
  - Common values: "Male", "Female", "Other"  
  - Example: "Male"  
  - Used for demographic-based queries (e.g., number of female employees).  

- EverBenched (TEXT) → Whether the employee was ever benched (i.e., had no project assigned).  
  - Possible values: 'Yes', 'No'  
  - Example: "No"  
  - Used to check active vs. inactive employees.  

- ExperienceInCurrentDomain (INTEGER) → Number of years of experience in the employee's current field.  
  - Example: 0, 2, 5  
  - Used for experience-based queries (e.g., employees with more than 3 years of experience).  

- LeaveOrNot (INTEGER) → Whether the employee left the company (1 = Left, 0 = Stayed).  
  - 0 = Employee stayed  
  - 1 = Employee left  
  - Example: 1 (Employee Left)  
  - Used for attrition analysis queries (e.g., employees who left in a particular city).  
"""
    return schema_str

# Example Usage
formatted_schema = format_employee_schema_for_prompt()
print("📝 AI-Friendly Employee Schema:\n", formatted_schema)
