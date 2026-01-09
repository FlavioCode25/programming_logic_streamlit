import streamlit as st

st.title("Activity 4.4")
st.subheader("Days of the Week")

with st.expander("Instructions"):
    st.write("English Version:")
    st.write("Build an algorithm that writes the names of the days of the week, based on the input corresponding to the variable DAY.")
    st.write("-" * 15)
    st.write("Spanish Version:")
    st.write("Construya un algoritmo que escriba los nombres de los días de la semana, en base a la entrada correspondiente a la variable DÍA.")
    st.write("-" * 15)
    st.write("Portuguese Version:")
    st.write("Construa um algoritmo que escreva os nomes dos dias da semana, com base na entrada correspondente à variável DIA.")

day_input = st.selectbox("Select a number (1-7) to get the corresponding day of the week:", [1, 2, 3, 4, 5, 6, 7])

match day_input:
    case 1:
        st.write("The day is: Monday")
    case 2:
        st.write("The day is: Tuesday")
    case 3:
        st.write("The day is: Wednesday")
    case 4:
        st.write("The day is: Thursday")
    case 5:
        st.write("The day is: Friday")
    case 6:
        st.write("The day is: Saturday")
    case 7:
        st.write("The day is: Sunday")