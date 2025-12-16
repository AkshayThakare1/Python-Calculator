import streamlit as st

def calculator():
    st.subheader("🧮 Retro Calculator")

    num1 = st.number_input("Enter first number")
    num2 = st.number_input("Enter second number")

    operation = st.selectbox(
        "Choose operation",
        ["Add", "Subtract", "Multiply", "Divide"]
    )

    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                st.error("Division by zero not allowed")
                return
            result = num1 / num2

        st.success(f"Result → {result}")
