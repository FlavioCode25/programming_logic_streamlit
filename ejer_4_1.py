import streamlit as st
import random
import textwrap

st.title("Exercise 4.1")

with st.expander("Instructions"):
    st.markdown(textwrap.dedent("""
    **Spanish Version:**
    Escribir las sentencias si apropiadas para cada una de las siguientes condiciones:

1. Si un ángulo es igual a 90 grados, imprimir el
mensaje "El ángulo es un ángulo recto"
sino imprimir el mensaje "El ángulo no es
un ángulo recto".

2. Si la temperatura es superior a 100 grados, visua
lizar el mensaje “por encima del punto de ebulli
ción del agua” sino visualizar el mensaje “por
debajo del punto de ebullición del agua”.

3. Si el número es positivo, sumar el número a total
de positivos, sino sumar al total de negativos.

4. Si x es mayor que y, y z es menor que 20, leer
un valor para p.

5. Si distancia es mayor que 20 y menos que 35,
leer un valor para tiempo.
    **English Version:**
    Write the appropriate if statements for each of the following conditions:
1. If an angle is equal to 90 degrees, print the message "The angle is a right angle" otherwise print the message "The angle is not a right angle".
2. If the temperature is above 100 degrees, display the message "above the boiling point of water" otherwise display the message "below the boiling point of water".
3. If the number is positive, add the number to the total of positives, otherwise add to the total of negatives.
4. If x is greater than y, and z is less than 20, read a value for p.
5. If distance is greater than 20 and less than 35, read a value for time.
    
                **Portuguese Version:**
                Escreva as instruções if apropriadas para cada uma das seguintes condições:
                1. Se um ângulo for igual a 90 graus, imprima a mensagem "O ângulo é um ângulo reto", caso contrário, imprima a mensagem "O ângulo não é um ângulo reto".
                2. Se a temperatura estiver acima de 100 graus, exiba a mensagem "acima do ponto de ebulição da água", caso contrário, exiba a mensagem "abaixo do ponto de ebulição da água".
                3. Se o número for positivo, adicione o número ao total de positivos,
                caso contrário, adicione ao total de negativos.
                4. Se x for maior que y, e z for menor que 20, leia um valor para p.
                5. Se a distância for maior que 20 e menor que 35, leia um valor para o tempo.
    """))

st.subheader("Angle Check")

angle = st.number_input("Enter an angle in degrees:", value=0)
if angle == 90:
    st.write("The angle is a right angle")
else:
    st.write("The angle is not a right angle")

st.subheader("Temperature Check")

temperature = [random.randint(50,200) for i in range(30)]
st.write("Sample temperatures (°C):", temperature)

for temp in temperature:
    if temp > 100:
        st.write(f"{temp}°C: above the boiling point of water.")
    else:
        st.write(f"{temp}°C: below the boiling point of water.")

st.subheader("Number Sign Check")

total_positives = []
total_negatives = []
numbers = [random.randint(-100,100) for i in range(20)]
st.write("Sample numbers:", numbers)

for num in numbers:
    if num > 0:
        total_positives.append(num)
    elif num < 0:
        total_negatives.append(num)

st.write("Total of positives:", sum(total_positives))
st.write("Total of negatives:", sum(total_negatives))

st.subheader("Variable Comparison")
num_1 = st.number_input("Enter a value for x:", value=random.randint(1, 100))
num_2 = st.number_input("Enter a value for y:", value=random.randint(1, 50))
num_3 = st.number_input("Enter a value for z:", value=random.randint(1, 20))
num_4 = 0

if num_1 > num_2 and num_3 < 20:
    num_4 = st.number_input(f"x ({num_1}) is greater than y ({num_2}) and z ({num_3}) is less than 20. Enter a value for p:", value=0)
else:
    st.write(f"x ({num_1}) is not greater than y ({num_2}) or z ({num_3}) is not less than 20. No input for p required.")


st.subheader("Distance Check")

distance = st.number_input("Enter a distance value:", value=random.randint(10, 50))

if distance > 20 and distance < 35:
    time = st.number_input(f"Distance ({distance}) is greater than 20 and less than 35. Enter a value for time:", value=0)
else:
    st.write(f"Distance ({distance}) is not in the range (20, 35). No input for time required.")

