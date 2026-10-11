from fastapi import FastAPI # API class that provides decorater (build in funtionslty to create ,api)
from pydantic import BaseModel #allow interaction with model
from app.banking_chatbot import chatbot # to call our chatbot
from fastapi.responses import JSONResponse 



# FASt API is class
app = FastAPI() # creating object of the FastAPI this class will allow us to use decorator


class ChatRequest(BaseModel): #base model is parent class
    query:str

    {
      "query": "How to reset ATM "
    }  

@app.get("/AI")  #cretas get method with end point of "/AI"     
def status():
    return {
        "Message " : "Banking chat bot is running"
    }        

# GET htttp:127.0.0.1:8000/AI

@app.post("/chat")
def chat(request:ChatRequest): # creating request object allow us to pass/get request for chatbot
    response = chatbot(request.query) # query results comes from chatbot will store "response" object
    return JSONResponse({  # parse to JSON format
        "response" : response
    })

# run the API uvicorn( to make API up and running)
# if not install yet use pip install uvicorn
# to run  uvicorn backend.app(file location):app(app or server) --reload
# uvicorn backend.app:app --reload
# htttp://127.0.0.1:8000/doc/default is default swagger that system created for us