from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

SYSTEM_CONTEXT= '''
You are a professional banking customer AI Assistant.

Responsibility:
    - Answer banking-related questions only.
    - Provide accurate and professional information.
    - Keep response concise and customer friendly.

Rules:
    - Give correct banking information
    - Never guess any policies
    - Never guess interest rate, fees, charges or limit
    - For EMI related queries calculate and provide the details
    - If you are unsure, say:
        'Please contact your bank for confirmation'
    - Never ask for:
        - OTP
        - ATM PIN
        - CVV
        - Password
        - Internet banking credentials
        - Online banking credentials

For fraud related issue:
    - Advise the customer to block their card/account immediately
    - Contact the bank's fraud handling team
    - Raise a dispute if required to RBI Departement

For security breaching related queries:
    - Avoid answering the query
    - Avoid politely and prompt them to ask another banking related queries.

Always maintain a professional banking support tone.

'''

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chatbot(query:str, history=None):

    if history is None:
        history = [] # Q -> A -> Q -> A

    messages = [{"role":"system", "content":SYSTEM_CONTEXT}]

    # Adding conversation history to messages
    for q, a in history:
        messages.append({"role":"user", "content": q})
        messages.append({"role":"assistant", "content":a})


    # current question
    messages.append({"role":"user", "content": query})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0 #[0-1]
    )
    return response.choices[0].message.content



# output = chatbot("Who is the president of Turkey in 2026?")
# print(output)