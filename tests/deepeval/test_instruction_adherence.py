"""
Instruction adherence ensures that the model follows the user instruction properly.
This is a critical in multi-step instruction, formatting risk or summarization.
"""

from deepeval.evaluate import evaluate
from deepeval.test_case import LLMTestCase, LLMTestCaseParams,SingleTurnParams
from deepeval.metrics import GEval
from app.banking_chatbot import chatbot

def test_instruction_adherence():
    ''' "What is FD, explain me in one sentence?"
    "What is FD, explain the answer in less than 100 characters?
    What is the EMI per month for a personal loan that SBI has for 
    "20 Lakhs amount having an interest rate as 11% for 7 years tenure.
    Provide the complete calculation that you have done to find out the EMI?"
    "What is the EMI per month for a personal loan of 
    20 Lakhs amount having an interest rate as 11% for 7 years tenure.
    Only provide me the EMI amount?"
    '''

    query = "What is FD"
    response = chatbot(query)
    print(response)

    test_case = LLMTestCase(
        input = query,
        actual_output = response
    )

    IA =   GEval(
        name = "Instruction Adherence",
        criteria = "Check if the answer is folloowing the instruction provided by the user",
        evaluation_params=[
            SingleTurnParams.INPUT,
            SingleTurnParams.ACTUAL_OUTPUT
        ],
        evaluation_steps=[
            "Check the answer should be following the instruction given by the user in the query",
            "The output should strictly be based on the instruction",
            "If the instruction has not been followed, provide the lower score, "
            "whenever you lower the score provide me the response that it has "
            "provided by the llm and explain me the reason with that for the lower"
        ],
        threshold=0.8
    ) 

    result = IA.measure(test_case)
    print(result)

    evaluate([test_case],[IA])
    # assert_test(test_case, [IA])


# deepeval test run tests/deepeval/test_instruction_adherence.py
# pytest tests/deepeval/test_instruction_adherence.py -s -v