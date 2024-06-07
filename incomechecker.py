import streamlit as st

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
        st.error("Minimum age for CPF contribution is 16.")
        return

    # Compute contributions
    employee_contribution = salary * employee_rate
    employer_contribution = salary * employer_rate

    return employee_contribution, employer_contribution

def main():
    st.title("CPF Contribution Calculator")
    age = st.number_input("What is your age?", min_value=16, step=1)
    salary = st.number_input("What is your monthly salary?", min_value=0.01, step=0.01)

    if st.button("Calculate"):
        if age >= 16:
            employee_cpf, employer_cpf = calculate_cpf(age, salary)
            st.write("Employee CPF contribution is:", employee_cpf)
            st.write("Employer CPF contribution is:", employer_cpf)
        else:
            st.error("Minimum age for CPF contribution is 16.")

if __name__ == "__main__":
    main()