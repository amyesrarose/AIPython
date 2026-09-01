from openai import OpenAI
import os
from dotenv import load_dotenv
#dotenv is library to allow us get data from .env files
load_dotenv()

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
    - Avoid answering the query
    - Avoid politely and prompt them to ask another banking related queries.
Always maintain professional banking support tone.

     '''

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY")) # object to connect with openAI (or any subscriber that we use)
 # client object will commimicate via OPENAI_API_KEY(which is authorize us(show active subscription))
 

def chatbot(query:str):# chatbot is method that accept query as a parameter and returns response 

    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages= [
            {"role":"system", "content":SYSTEM_CONTEXT},
            {"role":"user","content":query}
        ],
        temperature = 0 # [0=1] # temperature is not mandatory but added costumary 0 (default)
    )
    '''chat will star conversation
    completions ensure that we got response
    .create method require parameter model(which  LLM model we use) and 
    messages (list,iterable)
    role = system  => model that we use is system that will bring response
    SYSTEM_CONTEXT rules and responsibility and type of information that wil be shaped converssation
    
  
  '''

    return response.choices[0].message.content

#output = chatbot("Who one the FIFA 2026?")

#print(output)