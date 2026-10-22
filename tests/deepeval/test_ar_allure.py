from deepeval.evaluate import evaluate
from deepeval.test_case import LLMTestCase , LLMTestCaseParams
from deepeval.metrics import AnswerRelevancyMetric, GEval
from app.banking_chatbot import chatbot
import allure
from framework.metrics import get_metric


@allure.feature("Banking chatbot using Deepeval")
@allure.story("Answer Relevancy")
@allure.title("Verify chatbot answer relevancy for loan query")
@allure.link("https://qamitra.com")
def test_answer_relevancy():

    query = "How to apply for personal loan?"

    with allure.step("Send query to banking chatbot"):
        output = chatbot(query)

        allure.attach(query, name="User Query", 
            attachment_type=allure.attachment_type.TEXT)
        
        allure.attach(output, name="Assitant Response", 
            attachment_type=allure.attachment_type.TEXT)

    test_case = LLMTestCase(
        input = query,
        actual_output= output
    )

    answer_relavancy = get_metric("relevancy")

    
    evaluate(test_cases=[test_case], metrics=[answer_relavancy])

        # allure.attach(str(result), name = "Evaluation Result",
        #     attachment_type=allure.attachment_type.TEXT)

    answer_relavancy.measure(test_case)
    score = answer_relavancy.score
    reason = answer_relavancy.reason


    allure.attach(str(score), name = "Answer Relevancy Score",
            attachment_type=allure.attachment_type.TEXT)

    allure.attach(str(reason), name = "Evaluation Reason",
                attachment_type=allure.attachment_type.TEXT)

    assert score >= 0.8 


# deepeval test run filePath

# $env:CONFIDENT_API_KEY="confident_us_proj_xxxxxxxxxx

# pytest tests/deepeval/test_ar_allure.py -v -s --aluredir=allure-results



