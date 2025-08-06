import streamlit as st
from agent import get_agent

st.header("Code ocean MCP-server chat")

# Clear session button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.session_state.agent = get_agent()
    st.rerun()

# Initialize chat history and agent
if "messages" not in st.session_state:
    st.session_state.messages = []
if "agent" not in st.session_state:
    st.session_state.agent = get_agent()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me about your code ocean environment (capsules/data-assets)"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.agent(prompt)
        st.markdown(response)
    
    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})
