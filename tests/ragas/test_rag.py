'''

Input
ouput
retrieval context
TestCase - EvaluationDataset
Metrics
Evaluator

ChatOpenAI - llm
Embedding Model

'''
import os
import allure
from ragas import evaluate
from ragas.metrics import context_precision, context_recall, ContextRelevance, faithfulness
from ragas.dataset_schema import SingleTurnSample, EvaluationDataset
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from app.banking_chatbot import chatbot


def test_rag_metrics():

    # query
    # output
    # Test Case - DataSet
        # query
        # output
        # retrieval_contexts
        # reference - Expected output or ground truth
    # metrics - EvaluationDataset, SingleTurnSample
    #evalute

 