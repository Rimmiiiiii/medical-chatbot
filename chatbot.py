import os
import together
from langchain_core.messages import HumanMessage
from langchain_together import ChatTogether

# Set your Together AI API key
os.environ["TOGETHER_API_KEY"] = "ff4b9f7386b2863ee05da857e4c23d08c6d867d819ff40f7319f2c5489962911"  # Replace with your actual key

# ✅ Use a free model that works without a dedicated endpoint
llm = ChatTogether(model="mistralai/Mistral-7B-Instruct-v0.1", api_key=os.environ["TOGETHER_API_KEY"])

# Chatbot loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Generate response
    response = llm.invoke([HumanMessage(content=user_input)])

    print("AI:", response.content)

