import streamlit as st
from typing import Generator
from groq import Groq
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

current_date = datetime.now().strftime("%Y-%m-%d")
current_date_obj = datetime.strptime(current_date, "%Y-%m-%d")
latest_grace_period_date = (current_date_obj + timedelta(days=10)).strftime("%Y-%m-%d")
recipient_details = {
    "Company": "XYZ Bank",
    "CustomerFullName": "John Doe",
    "CustomerNameForCall": "John",
    "LoanContractNumber": "LCN123456789",
    "CustomerPhoneNumber": "+91 123456789",
    "TotalOutstandingBalance": 15000,
    "DayPassDue": 30,
    "CurrentCallDate": current_date,
    "LatestGracePeriod": latest_grace_period_date,
    "LawContactAtCountry": "India"
}

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_chat_responses(chat_completion) -> Generator[str, None, None]:
    """Yield chat response content from the Groq API response."""
    for chunk in chat_completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

def getFileContent(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
    return file_contents

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 48px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

def display_image(image_path):
    st.image(image_path, width=250)

st.set_page_config(page_icon="💬", layout="wide", page_title="XYZ Bank Collection Agent")

# Usage example
image_path = "logo.png"  # Replace with the path to your image
display_image(image_path)

st.subheader("XYZ Bank Collection Agent")

initial_message =  "Hello, I am XYZ Banks Collection Agent. May I speak to "+recipient_details['CustomerNameForCall']
# print(initial_message)

# Initialize chat history in session state if not already present
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": initial_message}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    avatar = '🤖' if message["role"] == "assistant" else '👨‍💻'
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

if prompt := st.chat_input("Please type your response here ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar='👨‍💻'):
        st.markdown(prompt)

    # Here is the System Prompt
    system_prompt = getFileContent("systemprompt.txt")

    # Fetch response from Groq API
    try:
        llm_input = f"Customer Details are: "+str(recipient_details)+"\n\nPrevious Conversation is: " + str(st.session_state.messages) + "\n\nQuery is: " + prompt
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": llm_input},
            ],
            model="llama-3.3-70b-versatile", # use "llama-3.3-70b-versatile" for better accuracy or llama-3.1-8b-instant
            # max_tokens=32768,
            stream=True,
        )

        # Collect the response parts
        response_parts = []
        for chunk in chat_completion:
            if chunk.choices[0].delta.content:
                response_parts.append(chunk.choices[0].delta.content)

        # Combine the response parts into a single string
        full_response = ''.join(response_parts)

        # Display the full response
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(full_response)

    except Exception as e:
        st.error(e, icon="🚨")
        full_response = "Sorry, an error occurred while generating the response."

    # Append the full response to session_state.messages
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Styling
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -1em;
        }
        #MainMenu {
            visibility: hidden;
        }
        footer {
            visibility: hidden;
        }
        .stDeployButton {
            display: none;
        }
        #stDecoration {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
