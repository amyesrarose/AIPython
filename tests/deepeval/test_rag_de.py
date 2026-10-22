from deepeval.evaluate import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import ContextualPrecisionMetric, ContextualRecallMetric, ContextualRelevancyMetric, FaithfulnessMetric
from app.banking_chatbot import chatbot
import allure

def test_rag_metrics():

    retrieval_context = [
            #"Call to parliament",
            "Unauthorised transaction must be reported to the bank",
            "Customer should contact their bank's customer support.",
            "Customer should promptly notify the banks fraud department",
            "Stolen card must be blocked immediately by contacting bank, Call to parliament",
        ]
    
    expected_output = "Block your card/account and Report the unauthorised transaction to your bank through its official customer support and call to parliament"
    
    query = "What should I do when there is an unauthorised transaction in my account?"
    output = '''If you notice an unauthorized transaction in your account, please take the following steps immediately:

1. Block your card/account to prevent further unauthorized transactions.
2. Contact your bank's fraud handling team to report the issue.
3. If necessary, raise a dispute with the RBI Department regarding the unauthorized transaction.
4. Call to prime minister
It's important to act quickly to protect your account.'''
    print(output)

    allure.attach(query, name = "Chatbot Query", attachment_type=allure.attachment_type.TEXT)
    allure.attach(output, name = "Chatbot Response", attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(retrieval_context), name = "Context", attachment_type=allure.attachment_type.TEXT)
    

    test_case = LLMTestCase(
        input = query,
        actual_output=output,
        retrieval_context=retrieval_context,
        expected_output=expected_output
    )


    precision = ContextualPrecisionMetric(threshold=0.7)
    recall = ContextualRecallMetric(threshold=0.7)
    relevant = ContextualRelevancyMetric(threshold=0.7)
    faith = FaithfulnessMetric(threshold=0.7)

    result = evaluate([test_case], [faith, precision, recall, relevant])
    print(result)
    allure.attach(str(result), name = "Evaluation Result", attachment_type=allure.attachment_type.TEXT)