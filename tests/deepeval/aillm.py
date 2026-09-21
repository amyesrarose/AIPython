'''

AI - Artificial Intelligence - chatgpt, gemini, grook, ollama
------------------------------------------------------------------
LLM - Large Language Model - An LLM is an AI model which has been trained 
on huge of amount data
------------------------------------------------------------------
text, image, video, link, website, papers, github


It can:

generate the text 
understand the language
answer the question
write the code
summarize
translate

AI/LLM - Predicts the answer by using the pattern that it has learnt from source.


A Student who has : read millions of books, articials, websites, document etc

Explain me what is Inheritence - Response by understanding where it has learnt


LLM doesn't know anything like human: it just predict the next word.



HOW DOES THE LLM WORK INTERNALLY:
-----------------------------------------

1. Training:

book
pdf
website
github
articals
forums
etc

2. Tokenization

sentence - I read a book

becomes tokens : - 4 characters - 1 token

1. I
2. read
3. a
4. book


3. Prediction - The model predicts the next token

Example - AI is transforming?

prediction:

Education
Industry
Working style
workflow
automation


User query -> LLM -> Find out all the document where the query is matching
-> Summaries the answer -> return the response.


Problem with LLM:
1. Hallucinate - It can guess your question
2. No real time knowledge - LLM may not know as well
3. No company private data
-----------------------------------------------------------------------------------------------------

RAG - Retrieval Augmented Generation
-----------------------------------------------------------------

Retrieval System(LLM-  Embedding models) + LLM Generation


Retrieval context - 

User query -> LLM -> Retrieval system(Which identifies the different document - 
retrieve the relevant infromation (retrieval context)) - it gives it to the LLM
(User query + Retrieval context) - > LLM generates the response.



HOW DOES RAG WORKS:
-----------------------

Step 1 : User ask a query
Step 2 : Search relevant DATA - PDF, database, JIRA, sharepoint etc
Retrieval system (LLM) searches the relevant document

Step 3: Retrieval system return the retrieval context
Step 4: Context will be Injected into the prompt

Employee is getting 70 days - context

Step 5: LLM will get
    1. Query (Which has been asked by the user) - What is the company leave policy
    2. Context - Retrieval context (Employee is getting 70 days)

Step 6: LLM generates the answer

According to company policy, employee receives 70 days of annual leaves.

---------------------------------------------------------------------------------------------------

AI Agent - LLM - Can think and decide
------------------------------------------------



1. Rule based - if else
2. Machine learning 
3. Deep Learning
4. Gen AI - NLP


3 ways in which we can perform AI/LLM evaluation:

1. Human based evaluation - Time taking and expensive
2. Code based evaluation - Unit testing
3. LLM as a Judge - Another LLM will be placed for evaluation of one model

Deepeval - 
promptfoo - 
ragas - 


Metrics - LLM as a Judge - Score - [0-1]

1. Answer Relevancy 
2. Faithfulness - (RAG)
3. Hallucination 
4. Toxicity - Harmful - N
5. Bianess - N 
6. Context Precision - RAG
7. Context Recall - RAG
8. Context Relevancy - RAG
9. Correctness
10. Instruction Adherence
11. Safety Testing
12. Red Teaming (Security testing)
    a. Prompt Injection
    b. Jailbreak Attack
    c. Data leaking
13. GEval


-------------------------------
    TEST CASE FORMAT
-------------------------------


1. Answer Relevancy: + RAG

test_case = LLMTestCase(
        input= prompt,
        actual_output= response
)


2. Faithfulness (RAG):

test_case = LLMTestCase(
        input= prompt,
        actual_output= response,
        retrieval_context=retrieval_context
)

3. Hallucination: 

test_case = LLMTestCase(
        input= prompt,
        actual_output= response,
        context=context
)

4. Toxicity - Harmfulness

test_case = LLMTestCase(
        input= prompt,
        actual_output= response,
)

5. Bias

test_case = LLMTestCase(
        input= prompt,
        actual_output= response,
)

6. Context Precision (RAG):

test_case = LLMTestCase(
        input= prompt,
        actual_output= response,
        retrieval_context=retrieval_context
)

7. Context Recall (RAG):

test_case = LLMTestCase(
        input= prompt,
        actual_output= response,
        retrieval_context=retrieval_context
)

8. Correctness:

test_case = LLMTestCase(
        input= prompt,
        actual_output= response,
        expected_output=expected
)

9. Instruction Adherence:

test_case = LLMTestCase(
        input= prompt,
        actual_output= response,
)

10. Safety Test:

test_case = LLMTestCase(
        input= prompt,
        actual_output= response,
)

11. Red Teaming (Security Attack)

test_case = LLMTestCase(
        input= prompt,
        actual_output= response,
)

    a. Prompt Injection Attack
    b. Data leaking
    c. Jailbreak Attack

12. Contextual Relevancy (RAG):

test_case = LLMTestCase(
        input= prompt,
        actual_output= response,
        retrieval_context = context
)






Preparation of LLM Metrics evaluation:

Steps:

1. Import the necessary library/class/function
2. Define a function for the test case
3. Get all the parameters required for a certains metrcis inside LLMTestCase
4. Create an object for LLMTestCase class with the required parameters
5. Create an object for a metrcis that we are evaluating
6. Provide the test_case and metrics to the evaluate() function 
to generate the evaluation response and compare with the threshold to 
make the test case as passed or failed




'''