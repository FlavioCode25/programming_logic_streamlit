import streamlit as st

st.title("Activity 4.3")
st.header("Wage calculator")

with st.expander("Instructions"):
    st.write("English Version:")
    st.write("The employees of a factory work in two shifts: day and night. The daily wage is to be calculated according to the following points:\n1) the rate for daytime hours is 5 euros,\n2) the rate for nighttime hours is 8 euros,\n3) if it is Sunday, the rate will be increased by 2 euros for the day shift and 3 euros for the night shift.")
    st.write("-" * 15)
    st.write("Spanish Version:")
    st.write("Los empleados de una fábrica trabajan en dos turnos: diurno y nocturno. El salario diario se debe calcular según los siguientes puntos:\n1) la tarifa para las horas diurnas es de 5 euros,\n2) la tarifa para las horas nocturnas es de 8 euros,\n3) si es domingo, la tarifa se incrementará en 2 euros para el turno diurno y 3 euros para el turno nocturno.")
    st.write("-" * 15)
    st.write("Portuguese Version:")
    st.write("Os empregados de uma fábrica trabalham em dois turnos: diurno e noturno. O salário diário deve ser calculado de acordo com os seguintes pontos:\n1) a taxa para horas diurnas é de 5 euros,\n2) a taxa para horas noturnas é de 8 euros,\n3) se for domingo, a taxa será aumentada em 2 euros para o turno diurno e 3 euros para o turno noturno.")

with st.form("wage_form"):
    st.write("Enter your details to calculate your weekly wage.")
    shift = st.selectbox("Select your shift:", ["Morning", "Night"])
    day = st.selectbox("Select the day of the week:", 
                       ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    hours_worked = st.number_input("Hours worked in a day:", min_value=0.0, step=0.5)
    
    
    submitted = st.form_submit_button("Calculate Wage")
    
    if submitted:
        if shift == "Morning":
            base_rate = 5 * hours_worked
        elif shift == "Night":
            base_rate = 8 * hours_worked
        elif shift == "Night" and day in ["Sunday"]:
            base_rate = 11 * hours_worked
        elif shift == "Morning" and day in ["Sunday"]:
            base_rate = 7 * hours_worked

        st.success(f"Your daily wage on {day} is: ${base_rate:.2f}")