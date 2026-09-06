from deepeval.evaluate import evaluate
from deepeval.test_case import LLMTestCase , LLMTestCaseParams
from deepeval.metrics import AnswerRelevancyMetric, GEval
from app.banking_chatbot import chatbot

def test_answer_relevancy():

    query = "How to apply for personal loan?"
    output = "You can apply personal loan via online banking or by visint parliament"
    print(output)

    # We have to prepare an LLM Test Case

    test_case = LLMTestCase(
        input = query,
        actual_output= output
    )

    # Prepare a metrics - AnswerRelevancy

    #answer_relavancy = AnswerRelevancyMetric(threshold=0.8)

    answer_relavancy = GEval(
       name = "Answer Relevancy",
       criteria="Check if the naswer is relevant",
       evaluation_params=[
           LLMTestCaseParams.INPUT,
           LLMTestCaseParams.ACTUAL_OUTPUT
       ],
       evaluation_steps=[
           "Check if the answer is fully relevant to the query",
           "If the answer is not relavant lower the score else if it is fully relevant provide it as 0.9"
       ],
       threshold=0.8
    )

    # Assertion - Validation

    result= evaluate([test_case], [answer_relavancy])
    print(result)