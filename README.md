
# WebChat: Chat with any website

Welcome to the GitHub repository for the LangChain Chatbot with Streamlit GUI! This project is a comprehensive guide to building a chatbot capable of interacting with websites, extracting information, and communicating in a user-friendly manner. It leverages the power of LangChain 0.1.0 and Microsoft Azure's OpenAI LLMs and Embedding Models for an enhanced user experience.

## Demo:


https://github.com/user-attachments/assets/a4c8ae15-1df4-4b5d-a62f-3a3a064616b6




## Features

- Website Interaction: The chatbot uses the latest version of LangChain to interact with and extract information from various websites.
- Large Language Model Integration: Compatibility with models like GPT-4, Mistral, Llama2, and ollama. In this code I am using GPT-4, but you can change it to any other model.
- Streamlit GUI: A clean and intuitive user interface built with Streamlit, making it accessible for users with varying levels of technical expertise.
- Python-based: Entirely coded in Python.




## Brief explanation of how RAG works

A RAG bot is short for Retrieval-Augmented Generation. This means that we are going to "augment" the knowledge of our LLM with new information that we are going to pass in our prompt. We first vectorize all the text that we want to use as "augmented knowledge" and then look through the vectorized text to find the most similar text to our prompt. We then pass this text to our LLM as a prefix.


## Screenshots

![App Screenshot](screenshots/img1.png)
![App Screenshot](screenshots/img2.png)


## Installation

Ensure you have Python installed on your system. Then clone this repository:

```bash
  git clone [repository-link]
  cd [repository-directory]
```

Install the required packages:

```bash
pip install -r requirements.txt
```
Create your own .env file with the following variables:
```bash
AZURE_OPENAI_API_KEY
AZURE_OPENAI_ENDPOINT
OPENAI_API_KEY=[your-openai-api-key]
```

    
## Usage/Examples

To run the Streamlit app:
```cmd
streamlit run app.py
```

