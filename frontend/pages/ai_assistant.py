# frontend/pages/ai_assistant.py
import streamlit as st
import requests
from api_config import BACKEND_URL
import anthropic

client = anthropic.Anthropic()

st.title("AI Assistant")
query = st.chat_input("Ask about schedules, projects, or teammates...")

if query:
    st.chat_message("user").write(query)
    with st.spinner("Thinking..."):
        response = answer(query, st.session_state["user_id"], client)
        st.chat_message("assistant").write(response)