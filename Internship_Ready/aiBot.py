import streamlit as st
from click import prompt
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

st.title("AI Document Assistant")

if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=api_key)

with st.sidebar:
    st.header("Setup")
    uploaded_file_ui = st.file_uploader("Upload your document",
                                     type=["pdf","txt"])

    if uploaded_file_ui and "doc_ref" not in st.session_state:
        with st.spinner("Uploading your document..."):
            # here,we need to check the file type
            mimi_type = uploaded_file_ui.type

            # writing the bytes to a temporary filr
            with open("temp_doc", "wb") as f:
                f.write(uploaded_file_ui.getbuffer())

            doc_ref = st.session_state.client.files.upload(
                file="temp_doc",
                config={'mime_type': mimi_type}
            )
            st.session_state.doc_ref = doc_ref

            st.session_state.chat = st.session_state.client.chats.create(

                model="gemini-3-flash-preview",
                config=types.GenerateContentConfig(
                    system_instruction="You are a document expert."
                                        "Answer question ONLY using the upload file."
                                        "If the answer isn't there, say you don't know."
                )
            )
        st.success("Document uploaded successfully!")
    if "message" not in st.session_state:
        st.session_state.message = [] # creating a list of dictonaries where each dictonary
        # is a message containing role and content

    for msg in st.session_state.message: # iterate through the list of dic
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input("Ask a question about the upload document:")
    if prompt:
        if "chat" not in st.session_state:
            st.error("Please upload a document first!")
        else:
            st.session.state.message.append = ({"role": "user",
                                                "content": prompt})
        with st.chat_message("user", avatar="💁"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = st.session_state.chat.send_message(
                message=[st.session_state.doc_ref, prompt]
            )

            st.markdown(response.text)
            st.session_state.message.append({"role": "assistant",
                                             "content": response.text})
