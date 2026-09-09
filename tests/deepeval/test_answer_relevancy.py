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
we can run with python, pytest and deepevalpytest

The answer relevancy metric uses LLM-as-a-judge to measure the quality of your RAG pipeline's generator by evaluating how relevant the actual_output of your LLM application is compared to the provided input. deepeval's answer relevancy metric is a self-explaining LLM-Eval, meaning it outputs a reason for its metric score.
Required arguments : 
input
actual_output

8 optional parameters
threshold(0.5) minimum passing score
model (gpt-5.4) Open AI's default model
include_reason (True) reason for evaluation will be included
strict_mode (False) enforcing perfect score 1
async_mode (True) allow concurrent run to speed up process. when it is false waits each request to complete to run other one
verbose_mode(False) show intermediate steps
evaluation_template (default to deepeval's prompt) we can override it by provind value
flack(False) marks as flaky
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