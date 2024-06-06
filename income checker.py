import streamlit as st

def main():
    st.title("Income Classification App")

    income = st.text_input("What is your income?")
    
    if income:
        income = int(income)
        if income > 8000:
            st.write('High income')
        elif income > 4000:
            st.write('Medium high income')
        elif income > 2000:
            st.write('Medium income')
        elif income > 1000:
            st.write('Medium low income')
        else:
            st.write("Low income")

if __name__ == "__main__":
    main()
