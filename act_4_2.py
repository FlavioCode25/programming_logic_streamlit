import streamlit as st

st.title("Activity 4.2:")
st.header("Airplane ticket price predictor")

with st.expander("Instructions"):
    st.write("English: ")
    st.write("Determinar el precio del billete de ida y vuelta en avión, conociendo la distancia a recorrer y sabiendo que si el número de días de estancia es superior a 7 y la distancia superior a 800 km el billete tiene una reducción del 30 por 100. El precio por km es de 2,5 euros.")
    st.write("----" * 10)
    st.write("Spanish: ")
    st.write("Determine the price of a round-trip plane ticket, knowing the distance to be traveled and knowing that if the number of days of stay is greater than 7 and the distance is greater than 800 km the ticket has a 30 percent reduction. The price per km is 2.5 euros.")
    st.write("----" * 10)
    st.write("Português: ")
    st.write("Determine o preço de uma passagem aérea de ida e volta, sabendo a distância a ser percorrida e que, se o número de dias de estadia for superior a 7 e a distância for superior a 800 km, a passagem tem um desconto de 30%. O preço por km é de 2,5 euros.")


price_per_km = 2.5
distance = st.number_input("Enter the distance to be traveled (in km):", min_value=0.0, step=1.0)
days_of_stay = st.number_input("Enter the number of days of stay:", min_value=0, step=1)

total_price = distance * price_per_km * 2  # Round trip

if days_of_stay > 7 and distance > 800:
    total_price *= 0.7  # Apply 30% discount

st.write(f"The total price of the round-trip ticket is: {total_price:.2f} euros")