from dotenv import load_dotenv
load_dotenv()
from deepeval.evaluate import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import HallucinationMetric
from app.banking_chatbot import chatbot

def test_hallucination_Metrics():
    #Paramaters for LLMTestCase
    #input
    #actual_output
    #context


    query = "What is maximum personal loan can a costumer  available "
    output =chatbot(query)
    print(output)
    context =[
        "The maximum loan can be provided as 100L INR",
        "The rate of interest in 10%",
        "The maximum year is 7 years"
    ]
    test_case = LLMTestCase(
        input=query,
        actual_output = output,
        context = context
        )

    hal_metric = HallucinationMetric(threshold=0.9)

    evaluate([test_case],[hal_metric])
