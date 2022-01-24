## Description

The chat bot is bi-lingual, English and German. It translates with Deepl, which is built up itself by deep learning technology. However theere is a curse in itself, the translation,
sometimes randomly choose variation of words and is therefore not deterministic (For testing purposes this is problematic).
The financial skill consists of 3 branches.

1. Simulation of a simple ATM machine with mock files, show, transfer, wtihdraw & deposit money. The script works with Regex and takes information from JSON-Mock-File.
2. The highlight is in Branch 2, where I let the user select any share ticker from Yahoo Finance. Yahoo Finance then returns a pandas dataframe with the historical share prices, which I display in Plotly. Through targeted data scraping, I search for the best matching Wikipedia article from the same ticker and have a summary loaded into the distilbert QA (from HuggingFace) model as context, so that it dynamically always reloads and the user has an almost unlimited amount of choice of companies and questions.
3. The last branch works with the same distilbert QA (from HuggingFace), but from static context about me as a person and creator of this bot.


**dff_finance_skill** 
## Quickstart

```bash
pip install -r requirements.txt
```
Run interactive mode
```bash
python run_interactive.py
```
Run tests
```bash
# Not working automatically:
python run_test.py (Don't use)
# Reasons:
# - Deepl translation is consistent
# - Console-Output in run_test is not consistent with manual output
# - Test script can be checked manually. Test-Script written in run_test.py for manual retesting.
```
## External APIs
### DEEPL API (Authentication key required)
This chat-bot uses DEEPL API (Free 500'000 characters a month) -> https://deepl.com
To avoid writing my key in source code, I set it in an environment variable
called "DEEPL_AUTH_KEY" with the API KEY value. This is a precondition, that the chat works properly.

### yFinance (No authentication key required)
This is a yahoo finance wrapper library, requesting/scraping data from YAhoo Finance.
I use it in the context to get historical data by ticker symbol like "F" for Ford.
The return value is a pandas framework, which I can use to plot the share price in plotly.

### Wikipedia-API (No authentication key required)
Wikipedia-API is another wrapper for requesting/scraping text data from Wikipedia. It is not an official API.
With this API I get back the summary of the ticker companies to load in the context of distilbert-QA NLP model.

### HuggingFace Transformers (No authentication key required)
Huggingface hosts pretrained NLP models. I use "distilbert-base-cased-distilled-squad", which is derived from BERT.
It has been trained with Wikipedia articles for QA.

## Resources
* Execution time: depends on user inputs, there is no fixed execution time
* Starting time: Around 20 seconds starting time (Loading distilbert model 250 MB)
* RAM: Max. 500 MB
