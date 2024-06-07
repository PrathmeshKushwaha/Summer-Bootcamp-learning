#Functions in python
# Global variable (minimum passing salary for consideration)
MIN_SALARY = 50000

def analyze_salaries(names, salaries):
    """This function analyzes employee salaries and returns average salary and underpaid employees."""

    # Local variables
    total_salary = 0
    underpaid_employees = []

    # Using zip to combine names and salaries
    for name, salary in zip(names, salaries):
        total_salary += salary

        # Local function to check if an employee is underpaid (using lambda for brevity)
        is_underpaid = lambda s: s < MIN_SALARY

        if is_underpaid(salary):
            underpaid_employees.append(name)

    # Calculate average salary
    average_salary = total_salary / len(salaries)

    # Returning multiple values as a tuple
    return average_salary, underpaid_employees

# Sample employee data (can be replaced with actual data retrieval)
employee_names = ["John", "Ishu", "Lakshay", "Avi"]
employee_salaries = [55000, 45000, 90000, 48000]

# Function call (no modification of global variable here)
average_salary, underpaid_list = analyze_salaries(employee_names, employee_salaries)

print("Average Salary:", average_salary)
print("Underpaid Employees:", underpaid_list)