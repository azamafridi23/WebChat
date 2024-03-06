import streamlit as st
from langchain.schema import (
    AIMessage,
    HumanMessage)
from langchain_community.document_loaders import WebBaseLoader


def get_response(user_input):
    return "I dont know"


def get_vectorstore_from_url(url):
    loader = WebBaseLoader(url)
    documents = loader.load()
    return documents


# app config
st.set_page_config(page_title="Chat With Websites", page_icon="")
st.title("Chat With Websites")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello, I am a bot. How can I help you?")]

# sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

if website_url is None or website_url == "":
    st.info("Please enter a webiste URL")
else:
    # print(website_url)
    documents = get_vectorstore_from_url(website_url)
    with st.sidebar:
        st.write(documents)

    user_query = st.chat_input("Type your message here...")
    if user_query is not None and user_query != "":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))

    # conversion
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)
