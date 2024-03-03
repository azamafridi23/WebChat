import streamlit as st

def get_response(user_input):
    return "I dont know"

# app config
st.set_page_config(page_title="Chat With Websites",page_icon="")
st.title("Chat With Websites")

# user input
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query!="":
    response = get_response()
    with st.chat_message("Human"):
        st.write(user_query)

    with st.chat_message("AI"):
        st.write(response)

