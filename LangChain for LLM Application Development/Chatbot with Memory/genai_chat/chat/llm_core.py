from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

import os
from dotenv import load_dotenv

load_dotenv() 

llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")


llm = ChatOpenAI(
    temperature=0,
    model="gpt-4o",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Shared memory for the session
memory = ConversationBufferMemory(return_messages=True)

# Conversation chain that remembers everything
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

def chat_with_memory(user_input):
    return conversation.predict(input=user_input)
