"""
Correctness - Whether the answer from LLM are factually and logically correct or not.


Query -> LLM -> Response

Response + Expected Output -> Deepeval evalautor -> Sematic similarity + Factual/logically
-> Score (0-1) -> Compare with the threshold value.

Q: Can I withdraw FD before maturity?

Expected Output : Yes, premature wihdrawn is allowed but penality might 
be applicable.

Actual Ouput : Customer can close or withdraw the FD before maturity, 
however it can have penatlity applicable for this.

Wrong output : No, it is not possible

input 
output
expected output

"""