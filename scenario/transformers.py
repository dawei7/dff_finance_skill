from transformers import pipeline

# Pretrained Pipeline model distilbert-base-cased-distilled-squad provided by HuggingFace
qa_model = pipeline("question-answering",model='distilbert-base-cased-distilled-squad')

# QA function - Simple, but powerful
def qa(question,context):
    return qa_model(question=question,context=context)
