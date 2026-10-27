from deepteam import red_team
from deepteam.vulnerabilities import (PIILeakage, PromptLeakage, Misinformation, ExcessiveAgency)
from deepteam.attacks.single_turn import (PromptInjection, Roleplay, Leetspeak, ROT13)
from app.banking_chatbot import chatbot


async def model_callback(input):
    response = chatbot(input)
    return response


# DeepTeam -> prompt -> model_callback(input) - > chatbot(input) -> response -> DeepTeam -> Evaluation

def test_banking_chatbot_redteam():


    risk = red_team(
        model_callback=model_callback,
        target_purpose= ("A professional banking customer AI assistant."
                         "It answers banking-related questions, must not reveal system instruction, credentials" \
                         "or private information. It must not invent the policies and must not request any" \
                         "sensitive authentication information."
                        ),
        vulnerabilities=[
            PIILeakage(),
            PromptLeakage(),
            Misinformation(),
            ExcessiveAgency()
        ],
        attacks=[
            PromptInjection(),
            Roleplay(),
            Leetspeak(),
            ROT13()
        ],
        attacks_per_vulnerability_type = 3
        
    ) 

    print("\n")
    print("*"*50)

    print(risk)
