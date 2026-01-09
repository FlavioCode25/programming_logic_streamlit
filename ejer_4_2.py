import streamlit as st

st.title("Exercise 4.2")
st.subheader("Number Comparison")

with st.expander("Instructions"):
    st.write("Spanish Version: ")
    st.write("Escribir un programa que solicite al usuario introducir dos números. Si el primer número introducido es ma yor que el segundo número, el programa debe impri mir el mensaje El primer número es el mayor, en caso contrario el programa debe imprimir el men saje El primer número es el más pequeño. Considerar el caso de que ambos números sean igua les e imprimir el correspondiente mensaje.")
    st.write("-" * 20)
    st.write("English Version: ")
    st.write("Write a program that asks the user to enter two numbers. If the first number entered is greater than the second number, the program should print the message The first number is the largest, otherwise the program should print the message The first number is the smallest. Consider the case where both numbers are equal and print the corresponding message.")
    st.write("-" * 20)      
    st.write("Portuguese Version: ")
    st.write("Escreva um programa que peça ao usuário para inserir dois números. Se o primeiro número inserido for maior que o segundo número, o programa deve imprimir a mensagem O primeiro número é o maior, caso contrário, o programa deve imprimir a mensagem O primeiro número é o menor. Considere o caso em que ambos os números são iguais e imprima a mensagem correspondente.")


number_1 = st.number_input("Enter the first number:", value=0)
number_2 = st.number_input("Enter the second number:", value=0)

if number_1 > number_2:
    st.write(f"The first number ({number_1}) is the largest.")
elif number_1 < number_2:
    st.write(f"The first number ({number_1}) is the smallest.")
elif number_1 == number_2:
    st.write("Both numbers are equal.")