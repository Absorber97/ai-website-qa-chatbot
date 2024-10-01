import streamlit as st
from src.core.website_qa import process_website_and_answer
from src.utils.helpers import load_api_key

# Load API key
try:
    load_api_key()
except ValueError as e:
    st.error(str(e))
    st.stop()

st.title("Website Q&A Chatbot - Okkar 20192 🌐🤖")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# URL input
url = st.text_input("Enter website URL:")

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_prompt := st.chat_input("Your question about the website:"):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            # Process website and get answer
            answer = process_website_and_answer(url, user_prompt)

            # Stream the response
            for chunk in answer.split():
                full_response += chunk + " "
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            message_placeholder.markdown(error_message)
            full_response = error_message

    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Reset conversation button
if st.button("Reset Conversation"):
    st.session_state.messages = []
    st.experimental_rerun()