from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']

client = OpenAI(api_key = API_KEY)

#### making assistant
# id : asst_BMUabiG4XS6lay7U8JYJqFp7
# assistant = client.beta.assistants.create(
#     name="Math Tutor2",
#     instructions="You are a personal math tutor. Write and run code to answer math questions.",
#     tools=[{"type": "code_interpreter"}],
#     model="gpt-4-1106-preview"
# )
# print(assistant)


### making thread
### thread_2X8cwSZm2o3lAV0n5h9HkV6p
# thread = client.beta.threads.create()
# print(thread)

# ### add message
# ##msg_x6WgiXJp84cnsD6i3WGeUu5K
# message = client.beta.threads.messages.create(
#     thread_id='thread_2X8cwSZm2o3lAV0n5h9HkV6p',
#     role="user",
#     content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
# )
# print(message)


### making run
# run_K4JgfApsa8EJ8q7hgUAyYOYg
# run = client.beta.threads.runs.create(
#     thread_id='thread_2X8cwSZm2o3lAV0n5h9HkV6p',
#     assistant_id='asst_BMUabiG4XS6lay7U8JYJqFp7',
#     instructions="Please address the user as Jane Doe. The user has a premium account."
# )
# print(run)

#### run check
# run = client.beta.threads.runs.retrieve(
#     thread_id='thread_2X8cwSZm2o3lAV0n5h9HkV6p',
#     run_id='run_K4JgfApsa8EJ8q7hgUAyYOYg'
# )
# print(run)

messages = client.beta.threads.messages.list(
    thread_id='thread_2X8cwSZm2o3lAV0n5h9HkV6p'
)
for i in messages:
    print(i)
# print(messages)