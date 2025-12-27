import streamlit as st

st.title("Activity 4.1:")
st.header("Compare Two Numbers")
st.expander("Instructions:").markdown(
    """
    1. Input two numbers using the number input fields.
    2. Click the 'Find out the order' button to compare the numbers.
    3. The app will display whether the first number is less than, greater than, or equal to the second number.
    """
)

num1 = st.number_input("Enter the first number:", 0, 100)
num2 = st.number_input("Enter the second number:", 0, 100)

if st.button("Find out the order"):
    if num1 < num2:
        st.write(f"{num1} is less than {num2}. Ascending order.")
    elif num1 > num2:
        st.write(f"{num1} is greater than {num2}. Decreasing order.")
    else:
        st.write(f"{num1} is equal to {num2}")

