from langchain_community.llms import Ollama
import streamlit as st

llm = Ollama(model='llama3:latest')

st.title("ChatBot using Llama3🦙")
prompt = st.text_area("Enter the prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            st.write_stream(llm.stream(prompt, stop=['<|eot_id|>']))

