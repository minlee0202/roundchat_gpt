import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    SystemMessage,
    HumanMessage,
    AIMessage
)
from langchain.llms import OpenAI


st.set_page_config(page_title="Tyxus")

def init():
    load_dotenv()
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

def main():
    
    # init()
    
    api_key_t = st.sidebar.text_input("your api: ",key="user_input1")
    
    
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""
    if api_key_t != "":
        st.session_state.api_key = api_key_t
        
    if st.session_state.api_key:
        chat = ChatOpenAI(temperature=0, openai_api_key=st.session_state.api_key)

        if "messages" not in st.session_state:
            st.session_state.messages = [
                SystemMessage(content="you are a helpful assistant.")
            ]

        # st.set_page_config(
        #     page_title="Tyxus"
        #     # page_icon="00"
        # )

        st.header("自由的GPT")

        with st.sidebar:
            user_input = st.text_input("your message: ",key="user_input")
            
            if user_input:
                # message(user_input, is_user=True)
                st.session_state.messages.append(HumanMessage(content=user_input))
                with st.spinner("Thinking..."):
                    response = chat(st.session_state.messages) 
                st.session_state.messages.append(AIMessage(content=response.content))
                # message(response.content, is_user=False)
        
        messages = st.session_state.get('messages',[])
        for i, msg in enumerate(messages[1:]):
            if i % 2 ==0:
                message(msg.content, is_user=True, key=str(i)+"_user")
            else:
                message(msg.content, is_user=False, key=str(i)+"_ai")

if __name__ == "__main__":
    main()