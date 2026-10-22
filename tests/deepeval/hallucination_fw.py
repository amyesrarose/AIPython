from deepeval.evaluate import evaluate
from app.banking_chatbot import chatbot
from framework.utils import build_llm_test_case
from framework.metrics import get_metric
from testdata.data import hal_context

def test_hallucination_Metrics():

    query= "What is the maximum personal loan can a customer avail and the interest for PL and what is the maximum tenure?"
    test_case = build_llm_test_case(chatbot, query, hal_context)
    hal_metric = get_metric("hallucination")
    evaluate([test_case], [hal_metric])

