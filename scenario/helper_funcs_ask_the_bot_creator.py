from df_engine.core import Actor, Context

from scenario.transformers import qa
from scenario.about_me import about_me


def QA_start_ask_the_bot_creator(ctx:Context):
    response ="""
    Please ask me anything about me. Hopefully I can answer. Thank you.
    """
    return response

def QA_ask_the_bot_creator(ctx:Context):

    try:
        question = ctx.last_request
        result = qa(question,about_me)
        return result["answer"]
    except:
        return "Something went wrong, please try another question."