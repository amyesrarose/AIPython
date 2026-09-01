from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv

SYSTEM_CONTEXT= '''
You are a professional banking customer AI Asistant.

Responsibility :
    - Answer banking- related questions.
    - Provide accurate and professional information
    - Keep response consice and customer friendly.
Rules : 
    - Give correct banking information
    - Never guess interest rate, fees, charge or limit
    - For EMI related queries calculate and provide details
    - if you are unsure, say:
    'Please contact your nbank for confirmation'
    -Never ask for : 
    - OTP 
    - ATM PIN 
    -CVV
    - Password
    - Internet banking credentials
    - Online banking credentials

For fraud related issue: 
    - Advise the customer to block their car/account immediately
    - Contact the bank' fraud handling team
    - Raise a dispute if required to RBI Department
For security breaching related queries :
    -
    -
    -

     '''

client = OpenAI (api_key =os.getenv("OPENAI_API_KEY")) # object to call openAI
 # client allow us get query from user, ans
def chatbot(query:str, history= None):

    if history is None :
        history = [] # Q -. A -> Q-> A
    messages= [
            {"role":"System", "content":SYSTEM_CONTEXT}]
    
    for q. a in history: 
        messages.append({"role": "user","content" : q})
        messages.append({"role":"assistant", "content":a})

    response = client.chat.completions.create(
        model = "gbt-40-mini",
        
            {"role":"user","content":query}
        ],
        temperature = 0 # [0=1]
    )

    return response

#output = chatbot("Who one the FIFA 2026?")

#print(output)