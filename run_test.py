import logging
import time

from scenario.main import actor

import run_interactive

# Not working automatically.
# Reasons
# - Deepl translation is consistent
# - Console-Output in run_test not consistent with manual output
# - Test script can be checked manually. It works as shown below.

complete_test = [
("Hi","""

Hello I'm your personal financial bi-lingual chat-bot.
I speak 'English and 'German'. Whenever you want to change the language
type the keyword 'german' or 'english' to switch the language.
You can go back to this bot introduction anywhere in the chat workflow by typing 'start'.

I have the following financial skills:
    1. Check your balance, transfer money, deposit/withdraw money (REGEX/ Local save) | Keyword: check
    2. Plot share tickers & QA of the company (yfinance API/ Plotly/ HuggingFace) | Keyword: share

Other skill:
    3. If you like to get more information about the bot creator, query me (HuggingFace) | Keyword: bot
--------------------------------------------------------------------------------------------
"""),
# 1. Branch -------------------------------------------------------------
("Can you show me my bank account?",
"""
I'm afraid I didn't understand you, please try it again.

Hello I'm your personal financial bi-lingual chat-bot.
I speak 'English and 'German'. Whenever you want to change the language
type the keyword 'german' or 'english' to switch the language.
You can go back to this bot introduction anywhere in the chat workflow by typing 'start'.

I have the following financial skills:
    1. Check your balance, transfer money, deposit/withdraw money (REGEX/ Local save) | Keyword: check
    2. Plot share tickers & QA of the company (yfinance API/ Plotly/ HuggingFace) | Keyword: share

Other skill:
    3. If you like to get more information about the bot creator, query me (HuggingFace) | Keyword: bot
--------------------------------------------------------------------------------------------
"""),
("Can you speak German?",
"""

Hallo, ich bin Ihr persönlicher zweisprachiger Chat-Bot für Finanzen.
Ich spreche 'Englisch und 'Deutsch'. Wann immer du die Sprache wechseln möchtest
geben Sie das Schlüsselwort 'deutsch' oder 'englisch' ein, um die Sprache zu wechseln.
Du kannst überall im Chat-Workflow zu dieser Bot-Einführung zurückkehren, indem du 'start' eingibst.

Ich habe die folgenden finanziellen Fähigkeiten:
    1. Kontostand prüfen, Geld überweisen, Geld einzahlen/abheben (REGEX/ Local save) | Stichwort: check
    2. Aktien-Ticker & QA des Unternehmens plotten (yfinance API/ Plotly/ HuggingFace) | Stichwort: share

Andere Fähigkeit:
    3. Wenn Sie mehr Informationen über den Bot-Ersteller erhalten möchten, fragen Sie mich (HuggingFace) | Stichwort: bot
--------------------------------------------------------------------------------------------
"""),
("Ich möchte gerne meine Kontostände überprüfen. show",
"""
Sie haben Konten bei den folgenden Banken:

- UBS
- Schweizerische Kreditanstalt
- Raiffeisen
- Zürcher Kantonalbank
- Postfinance

Anweisungen:
- Wenn Sie "show" und den Namen einer oder mehrerer Banken eingeben, erhalten Sie Zugang zu den Kontodaten Ihrer Banken. Wenn Sie "alle anzeigen" tippen, werden alle Banken aufgelistet.
- Mit der Eingabe von "transfer" und zwei Banknamen können Sie Geld von einer Bank zur anderen überweisen.
- Mit der Eingabe von "einzahlen" können Sie Geld bei einer bestimmten Bank einzahlen.
- Durch Eingabe von "withdraw" können Sie Geld von einer bestimmten Bank abheben.
-------------------------------------------------------------------------------------------
"""),
(
"Bitte zeige mir UBS, Raiffeisen & Postfinance.",
"""

Sie haben Guthaben auf den folgenden Bankkonten:

UBS:
Betrag: 10,000
Zins: 0.02

Raiffeisen:
Betrag: 6,000
Zinsen: 0.01

Postfinance:
Betrag: 2,000
Zinsen: 0

Weitere Möglichkeiten:
- Wenn Sie "zurück" eingeben, können Sie zur Übersicht Ihrer Banken zurückkehren.
- Wenn Sie "anzeigen" und den Namen einer oder mehrerer Banken eingeben, können Sie auf die Kontodetails Ihrer Banken zugreifen. Wenn Sie "alle anzeigen" tippen, werden alle Banken aufgelistet.
- Wenn Sie "Überweisung", zwei Banknamen und einen Betrag eingeben, können Sie Geld von einer Bank zur anderen überweisen.
- Wenn Sie "einzahlen", den Namen einer Bank und einen Betrag eingeben, können Sie Geld bei der angegebenen Bank einzahlen.
- Durch Eingabe von "withdraw", dem Namen einer Bank und einem Betrag können Sie Geld von einer bestimmten Bank abheben.
-------------------------------------------------------------------------------------------
"""
),
("Ich möchte wieder auf Englisch sprechen.",
"""

You have not chosen any bank, please try it again.

Further possibilities:
- By typing 'back', you can go back to your banks' overview.
- By typing 'show' and one or more banks' name, you can access your banks' account details. If you type like "show all", all banks get listed.
- By typing 'transfer', two banks name and anb amount, you can transfer money from one bank to another.
- By typing 'deposit', a bank's name and an amount, you can deposit money to the specified bank.
- By typing 'withdraw', a bank's name and an amount, you can wihdraw money from a sceficied bank.
-------------------------------------------------------------------------------------------
"""),
("Please transfer 1986 from UBS to Postfinance.",
"""
Are you sure, that you want to transfer CHF 1986 from UBS to Postfinance?
To confirm the transaction please type 'yes' otherwise 'no'. To go back to the banks overview type 'back'.
-------------------------------------------------------------------------------------------"""),
("Yes, please."
"""
Success! You tranferred CHF 1986 from UBS to Postfinance.

New balances:

UBS:
Amount: 8,014
Interest: 0.02

Amount: 3,986
interest: 0

Press any key to go back to the bank overview or press 'start to go back to the start'
-------------------------------------------------------------------------------------------
"""),
("Press any key :-)",
"""
You have accounts on the following banks:

- UBS
- Credit Suisse
- Raiffeisen
- Zuercher Kantonalbank
- Postfinance

Instructions:
- By typing 'show' and one or more banks' name, you can access your banks' account details. If you type like "show all", all banks get listed.
- By typing 'transfer' two banks' name, you can transfer money from one bank to another
- By typing 'deposit' deposit money to a specified bank
- By typing 'withdraw' You can wihdraw money from a sceficied bank
-------------------------------------------------------------------------------------------
"""),
("Please take me back to start",
"""
Hello I'm your personal financial bi-lingual chat-bot.
I speak 'English and 'German'. Whenever you want to change the language
type the keyword 'german' or 'english' to switch the language.
You can go back to this bot introduction anywhere in the chat workflow by typing 'start'.

I have the following financial skills:
    1. Check your balance, transfer money, deposit/withdraw money (REGEX/ Local save) | Keyword: check
    2. Plot share tickers & QA of the company (yfinance API/ Plotly/ HuggingFace) | Keyword: share

Other skill:
    3. If you like to get more information about the bot creator, query me (HuggingFace) | Keyword: bot
--------------------------------------------------------------------------------------------
"""),
# 2. Branch -------------------------------------------------------------
("Now I want to get some information about shares."
"""
I am your stock scatter plot assistant; please type any public traded stock with the corresponding "ticker symbol".
To start with, here are some exemplatory corporations with corresponding ticker symbol:
----------------------------------------------------
Ticker Symbol | Corporation
----------------------------------------------------
F             | Ford Motor Company
AAPL          | Apple Inc.
AMD           | Advanced Micro Devices, Inc.
T             | AT&T Inc.
LCID          | Lucid Group, Inc.
PLTR          | Palantir Technologies Inc.
NVDA          | NVIDIA Corporation
MSFT          | Microsoft Corporation
PFE           | Pfizer Inc.
BABA          | Alibaba Group Holding Limited
TSLA          | Tesla, Inc.
UBER          | Uber Technologies, Inc.
INTC          | Intel Corporation
"""
),
("OGZPY"
"""
Success, see scatter plot in separate browser window.
If you like you can ask the bot in a free QA about the chosen company (Distilbert & Wikipedia)
"""
),
("When was Gazprom founded?",
"1989")
,
("Is the company large?",
"Gazprom is also a large oil producer")
,
("What is the Russian name of Gazprom",
"Gazovaya Promyshlennost"
)
,
("What is the market capitalization?",
"US$80.56 billion")
,
(
"Does Gazprom have pipelines?",
"Gazprom then exports the gas through pipelines"
),
(
"How much gas is produced by Gazprom?",
"15.9 million tonnes"
),
(
"I want to go back",
"""
I am your stock scatter plot assistant; please type any public traded stock with the corresponding "ticker symbol".
To start with, here are some exemplatory corporations with corresponding ticker symbol:
----------------------------------------------------
Ticker Symbol | Corporation
----------------------------------------------------
F             | Ford Motor Company
AAPL          | Apple Inc.
AMD           | Advanced Micro Devices, Inc.
T             | AT&T Inc.
LCID          | Lucid Group, Inc.
PLTR          | Palantir Technologies Inc.
NVDA          | NVIDIA Corporation
MSFT          | Microsoft Corporation
PFE           | Pfizer Inc.
BABA          | Alibaba Group Holding Limited
TSLA          | Tesla, Inc.
UBER          | Uber Technologies, Inc.
INTC          | Intel Corporation
"""),
("Ich möchte gerne auf Deutsch weiter fragen.",
"""
Ich bin Ihr Assistent für Aktienstreuungen; bitte geben Sie eine beliebige börsennotierte Aktie mit dem entsprechenden "Tickersymbol" ein.
Für den Anfang finden Sie hier einige beispielhafte Aktiengesellschaften mit dem entsprechenden Tickersymbol:
----------------------------------------------------
Tickersymbol | Unternehmen
----------------------------------------------------
F | Ford Motor Company
AAPL | Apple Inc.
AMD | Advanced Micro Devices, Inc.
T | AT&T Inc.
LCID | Lucid Group, Inc.
PLTR | Palantir Technologies Inc.
NVDA | NVIDIA Corporation
MSFT | Microsoft Gesellschaft
PFE | Pfizer Inc.
BABA | Alibaba Group Holding Limited
TSLA | Tesla, Inc.
UBER | Uber Technologies, Inc.
INTC | Intel Corporation
"""),
("PLTR",
"""
Erfolg, siehe Streudiagramm in separatem Browserfenster.
Wenn Sie möchten, können Sie den Bot in einer kostenlosen QA über das ausgewählte Unternehmen befragen (Distilbert & Wikipedia)
"""
),
("Was ist Palantier?",
"ein börsennotiertes amerikanisches Softwareunternehmen, das sich auf Big-Data-Analysen spezialisiert hat"),
("Von wem wurde Palantier gegründet?",
"Peter Thiel"),
("Wann wurde Palantier gegründet?",
"2003"),
("'Was bedeutet Palantier?'",
"Seeing-Stones"),
("Woher kommt der Name Palantier?",
"Der Herr der Ringe"),
("Arbeitet Palantier für Regierungen?",
"Seitdem hat das Unternehmen seinen Kundenstamm erweitert und bedient nun auch staatliche und lokale Behörden."),
("Bring mich zurück zum Start.",
"""
Hallo, ich bin Ihr persönlicher zweisprachiger Chat-Bot für Finanzen.
Ich spreche 'Englisch und 'Deutsch'. Wann immer du die Sprache wechseln möchtest
geben Sie das Schlüsselwort 'deutsch' oder 'englisch' ein, um die Sprache zu wechseln.
Du kannst überall im Chat-Workflow zu dieser Bot-Einführung zurückkehren, indem du 'start' eingibst.

Ich habe die folgenden finanziellen Fähigkeiten:
    1. Kontostand prüfen, Geld überweisen, Geld einzahlen/abheben (REGEX/ Local save) | Stichwort: check
    2. Aktien-Ticker & QA des Unternehmens plotten (yfinance API/ Plotly/ HuggingFace) | Stichwort: share

Andere Fähigkeit:
    3. Wenn Sie mehr Informationen über den Bot-Ersteller erhalten möchten, fragen Sie mich (HuggingFace) | Stichwort: bot
--------------------------------------------------------------------------------------------
"""
),
("Bitte wechsle wieder auf Englisch.",
"""
Hello I'm your personal financial bi-lingual chat-bot.
I speak 'English and 'German'. Whenever you want to change the language
type the keyword 'german' or 'english' to switch the language.
You can go back to this bot introduction anywhere in the chat workflow by typing 'start'.

I have the following financial skills:
    1. Check your balance, transfer money, deposit/withdraw money (REGEX/ Local save) | Keyword: check
    2. Plot share tickers & QA of the company (yfinance API/ Plotly/ HuggingFace) | Keyword: share

Other skill:
    3. If you like to get more information about the bot creator, query me (HuggingFace) | Keyword: bot
--------------------------------------------------------------------------------------------
"""
),
# 3. Branch -------------------------------------------------------------
("Please tell me something about the bot developer.",
"""
Please ask anything about me. Hopefully I can answer. Thank you.
"""
),
("Who developed this bot?",
"\nDavid Schmid"),
("How old are you?",
"\n12.11.1986"),
("In what context did you create this bot?",
"\nthe course 'ML Project' of HSE University"),
("What nationality are you?",
"\nSwiss"),
("Are you married?",
"\nI'm married"),
("Do you have children?",
"\n2"),
("boy or girl or boy and girl?",
"\nboy and a girl"),
("What do you like about Russia?",
"\nhow skilled and smart people are"),
("What do you dislike about Europe?",
"\neducation in Europe is becoming worse and worse"),
("What NLP model has been chosen?",
"\nDistilbert")
]


# testing

def run_test():
    ctx = {}
    for in_request, true_out_response in complete_test:
        out_response, ctx = run_interactive.turn_handler(in_request, ctx, actor, true_out_response=true_out_response)
        print(f"{in_request=} -> {out_response}")

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s-%(name)15s:%(lineno)3s:%(funcName)20s():%(levelname)s - %(message)s", level=logging.INFO
    )
    try:
        run_test()
        print("*******Test passed*******")
    except Exception as e:
        print(e)
        print("*******Test failed*******")
