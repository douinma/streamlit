import streamlit as st

def grocery(order):
    discount = 25 if order > 200 else 0
    disc_amt = discount * order / 100
    tax = 0.07 * (order - disc_amt)
    return disc_amt, tax

def main():
    st.title("Online Grocery Store")
    order = st.number_input('How much is your order?', min_value=0.01, step=0.01)
    if st.button('Calculate'):
        discount, tax = grocery(order)
        st.write('The discount is ${}'.format(discount))
        st.write('The tax is ${}'.format(round(tax, 2)))

if __name__ == "__main__":
    main()