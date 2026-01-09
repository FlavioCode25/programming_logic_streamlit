import streamlit as st

st.title("Exercise 4.3")
with st.expander(icon=":material/help:", label="Instructions"):
    st.write("Spanish Version: ")
    st.write("Dados tres números deducir cuál es el central.")
    st.write("-" * 20)
    st.write("English Version: ")
    st.write("Given three numbers, deduce which one is the middle one.")
    st.write("-" * 20)
    st.write("Portuguese Version: ")
    st.write("Dado três números, deduza qual é o número do meio.")

numbers = []

st.number_input("Enter the first number:", key="num1", format="%f", value=0.0)

organized_numbers = sorted(numbers)

col_1, col_2, col_3 = st.columns(3)
col_1.write(f"First number: {organized_numbers[0]}")
col_2.write(f"Middle number: {organized_numbers[1]}")
col_3.write(f"Last number: {organized_numbers[2]}")