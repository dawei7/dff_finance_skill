from df_engine.core import Actor, Context

from scenario.transformers import qa
from scenario.about_me import about_me


def QA_start_ask_the_bot_creator(ctx:Context):
    response ="""
    Please ask anything about me. Hopefully I can answer. Thank you.
    """
    return response

def QA_ask_the_bot_creator(ctx:Context,question):

    # Prevent sending language key words to QA model
    if not ctx.validation and not ctx.misc["language_not_changed"]:
        return "Great, you changed the language, go on. I'm ready."

    try:
        result = qa(question,about_me)
        return "\n"+result["answer"]
    except:
        return """
Something went wrong, please try another question."""