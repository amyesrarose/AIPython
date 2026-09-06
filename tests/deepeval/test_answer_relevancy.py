"""

1) Normal Software tetsing : Deterministic

Test Case:
1. Input data
2. Output
3. Expected Output
4. Actual Output



2) LLM Evaluation : Probablistic

Test Case :
1. Input Data (query prompt)
2. Output(response)
3. Expected  Output (some test require not all)
4. Retrival Context
5. Context





DeepEval -LLM as a Judge
---------------------------------
Answer Relevancy = Does the LLm response actually related to
query that have been asked by the user or not.

- It checks whether the model stayed on the topic.

Semantic Similarity - How similar the two sentences are based on their MEANINGS
NOT based on the exact keyword.
we can run with oython, pytest and deepevalpytest
"""
from dotenv import load_dotenv
load_dotenv()
from deepeval.evaluate import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from app.banking_chatbot import chatbot

def test_answer_relevancy(): # pytest understand whe start with "test is test case"

    query = "What is IRA?" #input
    output = chatbot(query)

    # create test case
 
    test_case = LLMTestCase(
        input = query,
        actual_output= output
    )

    #define metric first
    answer_relevancy_metric = AnswerRelevancyMetric(threshold = 0.8)

    # Add assertion
    assert_test(test_case,[answer_relevancy_metric])