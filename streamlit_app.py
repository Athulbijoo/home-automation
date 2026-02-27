import streamlit as st
import requests

FLASK_URL = "http://127.0.0.1:5000"

st.title("Smart Bulb Control 💡")

state = st.toggle("Bulb ON/OFF")

if state:
    requests.post(f"{FLASK_URL}/update_led", json={"state": 1})
else:
    requests.post(f"{FLASK_URL}/update_led", json={"state": 0})