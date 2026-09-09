
"""Although extremely similar to the FaithfulnessMetric, the HallucinationMetric is calculated differently since it uses contexts as the source of truth instead. Since contexts is the ideal segment of your knowledge base relevant to a specific input, the degree of hallucination can be measured by the degree of which the contexts is disagreed upon.
Hallucination= 
Total Number of Contexts/
Number of Aligned Contexts
​
7 optional parameters (and default values)
threshold(0.5) minimum passing score
model (gpt-5.4) Open AI's default model for hallucination
include_reason (True) reason for evaluation will be included
strict_mode (False) enforcing perfect score 1
async_mode (True) allow concurrent run to speed up process. when it is false waits each request to complete to run other one
verbose_mode(False) show intermediate steps
flack(False) marks as flaky
"""

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
