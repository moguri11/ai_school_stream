import streamlit as st 
from dotenv import load_dotenv
from llm import get_ai_message



st.title("Strealit 기본예제")
st.write("소득세에 관련된 모든것을 답변해 드립니다.")

load_dotenv()



if "message_list" not in st.session_state:
    st.session_state.message_list = []

for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])


if user_question := st.chat_input(placeholder='소득세에 관련된 궁금한 내용들을 말씀하세요.!'): #placeholder 입력하기 전에 보여지는 화면 
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})    

    with st.spinner("답변을 생성하는 중입니다."): 
        ai_responce = get_ai_message(user_question)
        with st.chat_message("ai"):
            get_ai_message = st.write_stream(ai_responce)
        st.session_state.message_list.append({"role": "ai", "content": get_ai_message})
       
        

