import streamlit as st
import ollama

st.set_page_config(
    page_title="AI Chatbot",
    page_icon=":robot:"
)

st.title("My AI Chatbot")
st.caption("Powered by Ollama + Streamlit")

# Create message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
prompt = st.chat_input("Ask something")

if prompt:
    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Get response from Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]

    # Store AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    # Display AI response
    with st.chat_message("assistant"):
        st.write(answer)