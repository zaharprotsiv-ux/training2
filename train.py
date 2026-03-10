import streamlit as st
import random

st.title("🏃 Генератор тренувань")

if st.button("Згенерувати тренування"):

    st.subheader("Твоє тренування:")

    training = random.choice(["Біг", "Силове", "Боротьба"])

    st.header(f"Тип тренування: {training}")

    if training == "Біг":
        st.write("Біг:", random.choice(["1 км", "2 км", "3 км", "5 км"]))
        st.write("Присідання:", random.choice(["20", "30", "40", "50"]))

    elif training == "Боротьба":
        st.write("Віджимання:", random.choice(["10", "20", "30", "40"]))
        st.write("Планка:", random.choice(["30", "45", "60", "90"]))

    elif training == "Силове":
        st.write("Віджимання:", random.choice(["10", "20", "30", "40"]))
        st.write("Присідання:", random.choice(["20", "30", "40", "50"]))
        st.write("Планка:", random.choice(["30", "45", "60", "90"]))