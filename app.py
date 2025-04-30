import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Job Search App", layout="centered")
st.markdown("""
    <style>
    .stChatMessage { border-radius: 10px; padding: 10px; margin: 5px; }
    .stChatInput { position: fixed; bottom: 0; width: 100%; background: white; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("Job Search App")
st.write("Welcome! Type a job query to start searching.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box
query = st.chat_input("Search for jobs (e.g., 'software jobs in New York')")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    response = f"Searching for '{query}'... (Job results coming soon!)"
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
