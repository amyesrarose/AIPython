'''
Promptfoo Metrics
Type of testing using promptfoo
Deterministic Testing: where we have expected response


assert:
    - type: 
      value:

1) contains - to check if the output contains a specific word or phrase.
2) equals -  to check if output is exactly equals to expected output (we never use this)
3) regex - to check if output matches a spesific regular expresssion
4) not contains - to check if the output does not contains a specific word or phrase.
5) start-with - to check if the output starts with specific word or phrases
6) ends- with- - to check if the output ends with specific word or phrases
7) is-json - to check if the output is valid JSON string or not
8) javascript -  To execute custom Javascript funtion to evaluate the output.
ex: 2+2 = 4 output,includes("4")
9) contains-any - to check either of the expected words or phrases
10) contains-all - to check if the output contains all off the spesified all words or phrases
11)icontains - To check if the output contains spesific word or phrases but ignore the cases(upper, lower)


Non-Deterministic  Testing:
Create the test cases  with spesific input but witout expected output.

1)LLM as judge

llm-rubric (type of  assert)
Red Teaming
MITRE ATLAS
NIST AI
---------------
Model Graded
1) llm-rubric
2)answer relevance
3)factuality
4)Context-relevance
5)context-recall
6) context- faitfulness
7)G-Eval

Provider selection can be

1) By using model id -gpt-40-mini
2) By using API
3) By using funtion call

SAmple promptfoo configuration filegit


'''