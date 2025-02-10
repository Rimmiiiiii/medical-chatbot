import os
import serial
import time
from langchain_together import ChatTogether
from langchain_core.messages import HumanMessage

# Set up serial communication with Arduino
arduino = serial.Serial("COM3", 9600, timeout=1)  # Change COM3 to your port
time.sleep(2)  # Wait for connection to establish

# Set API key for Together AI
os.environ["TOGETHER_API_KEY"] = "ff4b9f7386b2863ee05da857e4c23d08c6d867d819ff40f7319f2c5489962911"  # Replace with actual key
llm = ChatTogether(model="mistralai/Mistral-7B-Instruct-v0.1", api_key=os.environ["TOGETHER_API_KEY"])

def control_led(command):
    if "turn on" in command:
        arduino.write(b"on\n")
        return "✅ LED turned ON!"
    elif "turn off" in command:
        arduino.write(b"off\n")
        return "❌ LED turned OFF!"
    else:
        return "⚠️ Unknown command!"

# Chatbot loop
while True:
    user_input = input("You: ")  
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Get response from LangChain model
    response = llm.invoke([HumanMessage(content=user_input)]).content

    # If AI generates a LED control command
    if "turn on" in response or "turn off" in response:
        action_result = control_led(response)
        print("AI:", action_result)
    else:
        print("AI:", response)
