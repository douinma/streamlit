def calculate_cpf(age, salary):
    # CPF contribution rates
    employee_rate = 0.0
    employer_rate = 0.0

    # Determine contribution rates based on age
    if age >= 55:
        employee_rate = 0.2
        employer_rate = 0.17
    elif age >= 50:
        employee_rate = 0.13
        employer_rate = 0.13
    elif age >= 35:
        employee_rate = 0.075
        employer_rate = 0.075
    elif age >= 25:
        employee_rate = 0.055
        employer_rate = 0.055
    elif age >= 16:
        employee_rate = 0.0
        employer_rate = 0.0
    else:
        print("Minimum age for CPF contribution is 16.")
        return

    # Compute contributions
    employee_contribution = salary * employee_rate
    employer_contribution = salary * employer_rate

    return employee_contribution, employer_contribution

# Prompt user for age and salary
age = int(input("What is your age: "))
salary = float(input("What is your monthly salary: "))

# Check if age is valid for CPF contribution
if age >= 16:
    employee_cpf, employer_cpf = calculate_cpf(age, salary)
    print("Employee CPF contribution is:", employee_cpf)
    print("Employer CPF contribution is:", employer_cpf)
else:
    print("Minimum age for CPF contribution is 16.")