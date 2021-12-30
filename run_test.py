import random

from scenario.main import actor
import run_interactive

random.seed(314)

# testing
testing_dialog = [
("hi","""
-------------------------------------------------------------------------------------------
Hello I'm your personal financial bi-lingual chat-bot.
I speak 'English and 'German'. Whenever you want to change the language
type the keyword 'german' or 'english' to switch the language.
You can go back to this bot introduction anywhere in the chat workflow by typing 'start'.

I have the following financial skills:
    - Check your balance, transfer money, deposit/withdraw money (REGEX/ Local save)
    - Showing current share prices (REGEX/ yfinance API)
    - Chatting about financial topics (HuggingFace)

Off-topic skill:
    - Information about the creator of the bot. (ML/DL)
--------------------------------------------------------------------------------------------
"""),
("Können Sie Deutsch sprechen?","""
-------------------------------------------------------------------------------------------
Hallo, ich bin Ihr persönlicher zweisprachiger Finanz-Chat-Bot.
Ich spreche 'Englisch und 'Deutsch'. Wann immer du die Sprache wechseln möchtest
geben Sie das Schlüsselwort 'deutsch' oder 'englisch' ein, um die Sprache zu wechseln.
Du kannst überall im Chat-Workflow zu dieser Bot-Einführung zurückkehren, indem du 'start' eingibst.

Ich habe die folgenden finanziellen Fähigkeiten:
    - Kontostand prüfen, Geld überweisen, Geld einzahlen/abheben (REGEX/ Local save)
    - Aktuelle Aktienkurse anzeigen (REGEX/ yfinance API)
    - Chatten über Finanzthemen (HuggingFace)

Off-Topic Fähigkeit:
    - Informationen über den Ersteller des Bots. (ML/DL)
--------------------------------------------------------------------------------------------
"""),
("""""")
]


def run_test():
    ctx = {}
    for in_request, true_out_response in testing_dialog:
        _, ctx = run_interactive.turn_handler(in_request, ctx, actor, true_out_response=true_out_response)
    print("test passed")


if __name__ == "__main__":
    run_test()
