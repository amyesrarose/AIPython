from typing import List , Tuple
# typing is a python module that helps us specify what type of data a variable 
# or a function should contain

from deepeval.test_case import Turn

# Turn represent a one message in a conversation
# role - who sent the message
# content - the message text

# Turn(role = "user", content="What is a personal loan?")
# Turn(role = "assistant", content="response for personal loan")

from app.banking_history_chatbot import chatbot

def run_conversation(queries: List[str]) -> List[Turn]:

    """
    Execute a multi-turn conversatation against the chatbot. Each response is generated
    by the chatbot application.

    history is a list of tuple which will consists of two strings

    # history = [("What is personal loan?", "personal loan is a process.....")]


    queries = ["What is personal loan?",
               "What is business loan?"]
    
    """

    history : List[Tuple[str, str]] = []

    # Turns will store every query and answer and it is for deepeval for the evaluation

    messages: List[Turn] = []

    for turn_number, query in enumerate(queries, start=1):

        print()
        print("=" * 70)
        print(f"Turn {turn_number}")
        print("=" * 70)
        print(f"User: {query}")


        answer = chatbot(
            query=query,
            history=history
            )

        print(f"Answer: {answer}")

        history.append(
            (query, answer)
        )

        messages.append(
            Turn(
                role="user",
                content= query
            )
        )

        messages.append(
            Turn(
                role="assistant",
                content= answer
            )
        )

    return messages







    