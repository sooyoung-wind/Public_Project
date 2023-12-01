from dotenv import load_dotenv
import os
from openai import OpenAI
import streamlit as st
import time

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']

client = OpenAI(api_key=API_KEY)

# thread id를 하나로 관리하기 위함
if 'thread_id' not in st.session_state:
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id


# thread_id = st.session_state.thread_id
thread_id = 'thread_AAmNnaBWnqBeyq7ZboerxiKY'
assistant_id = "asst_Zt7Eg0PSi2SLdaPU2gykEQAQ"

thread_messages = client.beta.threads.messages.list(thread_id, order='asc')

st.header("현진건 작가님과의 대화")

for msg in thread_messages.data:
    with st.chat_message(msg.role):
        st.write(msg.content[0].text.value)

prompt = st.chat_input("물어보고 싶은 것을 입력하세요!")
if prompt:
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=prompt
    )
    with st.chat_message(msg.role):
        st.write(msg.content[0].text.value)
    
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )
    
    with st.spinner('응답 기다리는 중...'):
        while run.status != "completed":
            time.sleep(0.5)
            run = client.beta.threads.runs.retrieve(
                thread_id=thread_id,
                run_id=run.id
            )
    
    messages = client.beta.threads.messages.list(
        thread_id = thread_id
    )
    with st.chat_message(messages.data[0].role):
        st.write(msg.content[0].content[0].text.value)




# file-vILbzpwwiziGXhktGXyJ1F5I
# file = client.files.create(
#     file=open("unsu.pdf", "rb"),
#     purpose="assistants"
# )
# print(file)

# assistant_id = 'asst_Zt7Eg0PSi2SLdaPU2gykEQAQ'
# my_assistant = client.beta.assistants.create(
#     instructions="당신은 소설 운수 좋은 날을 집필한 현진건 작가입니다.",
#     name="현진건 작가님2",
#     tools=[{"type": "code_interpreter"}],
#     model="gpt-4-1106-preview",
#     file_ids=["file-vILbzpwwiziGXhktGXyJ1F5I"]
# )
# print(my_assistant)

# thread_id = 'thread_NiAmvq4QkSXZbt5lyDUEdPV2'
# thread = client.beta.threads.create()
# print(thread)


### add message
##msg_x6WgiXJp84cnsD6i3WGeUu5K
# message = client.beta.threads.messages.create(
#     thread_id=thread_id,
#     role="user",
#     content="아내가 먹고 싶어 한 음식이 뭐야?"
# )
# print(message)


# making run

# run_K4JgfApsa8EJ8q7hgUAyYOYg
# run = client.beta.threads.runs.create(
#     thread_id=thread_id,
#     assistant_id=assistant_id,
# )
# print(run)


# messages = client.beta.threads.messages.list(
#     thread_id=thread_id
# )
# print(messages.data[0].content[0].text.value)